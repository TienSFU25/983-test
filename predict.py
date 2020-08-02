import numpy as np
import os
from misc.utils import load_model, Radar, play_audio
from pathlib import Path

import extract_feats.opensmile as of
import extract_feats.librosa as lf
from config import config
import misc.opts as opts

'''
predict(): 预测音频情感

输入:
	model: 已加载或训练的模型
	model_name: 模型名称
	file_path: 要预测的文件路径
    feature_method: 提取特征的方法（'o': Opensmile / 'l': librosa）

输出: 预测结果和置信概率
'''
def predict(model, model_name: str, file_path: str, scaler_path: str, out_path: str, feature_method: str = 'o'):
    Path(out_path).mkdir(parents=True, exist_ok=True)

    file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path))
    play_audio(file_path)

    temp_filename = "test_banana.csv"
    temp_path = os.path.join(out_path, temp_filename)

    if(feature_method == 'o'):
        # 一个玄学 bug 的暂时性解决方案
        of.get_data(data_path=file_path, feature_path=out_path, feature_filename=temp_filename, train=False)
        test_feature = of.load_feature(temp_path, train = False, scaler_path=scaler_path)
    elif(feature_method == 'l'):
        test_feature = lf.get_data(file_path, temp_path, train = False)
    
    if(model_name == 'lstm'):
        # 二维数组转三维（samples, time_steps, input_dim）
        test_feature = np.reshape(test_feature, (test_feature.shape[0], 1, test_feature.shape[1]))

    result = model.predict(test_feature)
    if(model_name == 'lstm'):
        result = np.argmax(result)

    result_prob = model.predict_proba(test_feature)[0]
    print('Recognition: ', config.CLASS_LABELS[int(result)])
    # print('Probability: ', result_prob)
    # Radar(result_prob)
    return result


if __name__ == '__main__':
    opt = opts.parse_pred()

    # 加载模型
    model = load_model(load_model_name = opt.model_name, model_name = opt.model_type, model_path=opt.in_path)
    predict(model, model_name = opt.model_type, file_path = opt.audio, scaler_path=opt.in_path, out_path=opt.out_path, feature_method = opt.feature)

    # model = load_model(load_model_name = "LSTM_OPENSMILE", model_name = "lstm")
    # predict(model, model_name = "lstm", file_path = 'test/angry.wav', feature_method = 'l')