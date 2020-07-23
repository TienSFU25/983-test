# 参数配置

IS_RAVDESS = True

class config:
    # 数据集路径
    DATA_PATH = '/content/opensmile-train/'
    # 情感标签
    CLASS_LABELS = ("angry", "fear", "happy", "neutral", "sad", "surprise")

    if IS_RAVDESS:
        # Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
        CLASS_LABELS = ("angry", "fear", "happy", "neutral", "sad", "surprise")

    # LSTM 的训练 epoch 数
    epochs = 20

    # Opensmile 标准特征集
    CONFIG = 'IS10_paraling'
    # Opensmile 安装路径
    OPENSMILE_PATH = '/content/opensmile'
    # 每个特征集的特征数量
    FEATURE_NUM = {
        'IS09_emotion': 384,
        'IS10_paraling': 1582,
        'IS11_speaker_state': 4368,
        'IS12_speaker_trait': 6125,
        'IS13_ComParE': 6373,
        'ComParE_2016': 6373
    }

    # 特征存储路径
    FEATURE_PATH = 'extracted-features/'

    # WILL BE OVERWRITTEN
    TRAIN_FEATURE_PATH_OPENSMILE = FEATURE_PATH + 'train_banana.csv'
    PREDICT_FEATURE_PATH_OPENSMILE = FEATURE_PATH + 'test_banana.csv'

    # 训练特征存储路径（librosa）
    TRAIN_FEATURE_PATH_LIBROSA = FEATURE_PATH + 'train_librosa_casia.p'
    # 预测特征存储路径（librosa）
    PREDICT_FEATURE_PATH_LIBROSA = FEATURE_PATH + 'test_librosa_casia.p'

    # 模型存储路径
    SAVE_PATH = 'save/'
    LOAD_PATH = 'cp/'