import argparse


def parse_prepro():

    parser = argparse.ArgumentParser(description = 'preprocessing options for speech emotion recognition')

    parser.add_argument(
        '-f', 
        '--feature', 
        type = str, 
        default = 'o',
        choices = ['o', 'l'],
        dest = 'feature', 
        help = "The method for features extracting: use 'o' to use opensmile or use 'l' to use librosa.")

    parser.add_argument(
        '-s', 
        '--feature-set', 
        type = str, 
        default = 'IS10_paraling',
        dest = 'feature_set', 
        help = "Which IS (09, 10, 11, 12, 13) Featureset")

    parser.add_argument(
        '-i', 
        '--input-path', 
        type = str, 
        default = '/content/opensmile-train/',
        dest = 'in_path', 
        help = "Folder of .wav files")

    parser.add_argument(
        '-o', 
        '--out-path', 
        type = str, 
        default = 'out/',
        dest = 'out_path', 
        help = "Where to output extracted features for preprocessing")

    args = parser.parse_args()
    return args


def parse_train():

    parser = argparse.ArgumentParser(description = 'Speech Emotion Recognition')

    # svm / mlp / lstm
    parser.add_argument(
        '-mt', 
        '--model_type', 
        type = str, 
        default = 'lstm',
        choices = ['lstm', 'dense'],
        dest = 'model_type', 
        help = "The type of model (svm, mlp or lstm).")

    parser.add_argument(
        '-mn', 
        '--model_name', 
        type = str, 
        default = 'default',
        dest = 'model_name', 
        help = "The name of saved model file.")
    
    parser.add_argument(
        '-f', 
        '--feature', 
        type = str, 
        default = 'o',
        choices = ['o', 'l'],
        dest = 'feature', 
        help = "The method for features extracting: 'o' for opensmile, 'l' for librosa.")

    parser.add_argument(
        '-s', 
        '--feature-set', 
        type = str, 
        default = 'IS10_paraling',
        dest = 'feature_set', 
        help = "Which IS (09, 10, 11, 12, 13) Featureset")

    parser.add_argument(
        '-i', 
        '--input-path', 
        type = str, 
        default = 'in/',
        dest = 'input_path', 
        help = "Location of preprocessed features")

    args = parser.parse_args()
    return args


def parse_pred():

    parser = argparse.ArgumentParser(description = 'Speech Emotion Recognition')

    # svm / mlp / lstm
    parser.add_argument(
        '-mt', 
        '--model_type', 
        type = str, 
        default = 'lstm',
        choices = ['lstm', 'dense'],
        dest = 'model_type', 
        help = "The type of model (svm, mlp or lstm).")

    parser.add_argument(
        '-mn', 
        '--model_name', 
        type = str, 
        default = 'default',
        dest = 'model_name', 
        help = "The name of saved (h5) model file.")

    parser.add_argument(
        '-f', 
        '--feature', 
        type = str, 
        default = 'o',
        choices = ['o', 'l'],
        dest = 'feature', 
        help = "The method for features extracting: 'o' for opensmile, 'l' for librosa.")

    parser.add_argument(
        '-a', 
        '--audio', 
        type = str, 
        default = 'default.wav',
        dest = 'audio', 
        help = "The path of audio which you want to predict.")

    parser.add_argument(
        '-i', 
        '--in-path', 
        type = str, 
        default = 'in/',
        dest = 'in_path', 
        help = "Where to load the dang model")

    parser.add_argument(
        '-o', 
        '--out-path',
        type = str, 
        default = 'nobody-gives-a-shit/',
        dest = 'out_path', 
        help = "Where to write intermediate features. Find way to put this in temp folder")

    parser.add_argument(
        '-s', 
        '--feature-set', 
        type = str, 
        default = 'IS10_paraling',
        dest = 'feature_set', 
        help = "Which IS (09, 10, 11, 12, 13) Featureset")

    args = parser.parse_args()
    return args