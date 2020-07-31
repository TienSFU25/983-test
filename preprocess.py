'''
提取数据集中音频的特征并保存
'''

import extract_feats.opensmile as of
import extract_feats.librosa as lf
from config import config
import misc.opts as opts

if __name__ == '__main__':
    opt = opts.parse_prepro()
    feat_method = opt.feature
    data_path = opt.data_path
    out_path = opt.out_path
    
    if(feat_method == 'o'):
        of.get_data(data_path, out_path, config.PREPROCESS_OPENSMILE_FILENAME, train = True)

    elif(feat_method == 'l'):
        lf.get_data(data_path, config.TRAIN_FEATURE_PATH_LIBROSA, train = True)