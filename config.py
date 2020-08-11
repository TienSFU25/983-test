# 参数配置

class config:
    # 情感标签
    # CLASS_LABELS = ("angry", "fear", "happy", "neutral", "sad", "surprise")

    # CLASS_LABELS = ("neutral", "calm", "happy", "sad", "angry", "fear", "disgust", "surprise")
    CLASS_LABELS = ("low-arousal", "positive-high-arousal", "negative-high-arousal")

    # LSTM 的训练 epoch 数
    epochs = 20

    # Opensmile 标准特征集
    # CONFIG = 'IS10_paraling'
    # CONFIG = 'IS09_emotion'

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

    PREPROCESS_OPENSMILE_FILENAME = 'preprocess.csv'
