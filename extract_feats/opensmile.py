import os
import csv
import sys
import time
import pandas as pd
import pdb

from sklearn.preprocessing import StandardScaler
from typing import Tuple
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

from config import config


'''
_get_feature_opensmile(): Opensmile 提取一个音频的特征

输入:
    file_path: 音频路径

输出：
    该音频的特征向量
'''

def _get_feature_opensmile(filepath: str, out_path: str, feature_set: str):
    # Opensmile 命令
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    feature_dir = os.path.join(BASE_DIR, out_path, 'single_feature.csv')

    cmd = 'cd ' + config.OPENSMILE_PATH + ' && ./SMILExtract -C config/' + feature_set + '.conf -I "' + filepath + '" -O ' + feature_dir
    print("Opensmile cmd: ", cmd)
    os.system(cmd)
    
    reader = csv.reader(open(feature_dir, 'r'))
    rows = [row for row in reader]
    last_line = rows[-1]
    return last_line[1: config.FEATURE_NUM[feature_set] + 1]


'''
load_feature(): 从 .csv 文件中加载特征数据

输入:
    feature_path: 特征文件路径
    train: 是否为训练数据

输出:
    训练数据、测试数据和对应的标签
'''

def load_feature(feature_path: str, train: bool, scaler_path: str, feature_set: str):
    # 加载特征数据
    df = pd.read_csv(feature_path)
    features = [str(i) for i in range(1, config.FEATURE_NUM[feature_set] + 1)]

    X = df.loc[:,features].values
    Y = df.loc[:,'label'].values

    if train == True:
        # 标准化数据 
        scaler = StandardScaler().fit(X)
        # 保存标准化模型
        joblib.dump(scaler, os.path.join(scaler_path, 'SCALER_OPENSMILE.m'))
        X = scaler.transform(X)

        # 划分训练集和测试集
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
        return x_train, x_test, y_train, y_test
    else:
        # 标准化数据
        # 加载标准化模型
        scaler = joblib.load(os.path.join(scaler_path, 'SCALER_OPENSMILE.m'))
        X = scaler.transform(X)
        return X

def load_from_csv(feature_path: str, scaler_path: str = '', feature_set: str = 'IS10_paraling'):
    df = pd.read_csv(feature_path)
    features = [str(i) for i in range(1, config.FEATURE_NUM[feature_set] + 1)]

    X = df.loc[:,features].values
    Y = df.loc[:,'label'].values

    if scaler_path != '':
        scaler = joblib.load(os.path.join(scaler_path, 'SCALER_OPENSMILE.m'))
        X = scaler.transform(X)

    return (X, Y)

'''
get_data(): 
    提取所有音频的特征: 遍历所有文件夹, 读取每个文件夹中的音频, 提取每个音频的特征，把所有特征保存在 feature_path 中

输入:
    data_path: 数据集文件夹路径
    feature_path: 保存特征的路径
    train: 是否为训练数据

输出:
    train = True: 训练数据、测试数据特征和对应的标签
    train = False: 预测数据特征
'''

# Opensmile 提取特征
# data path is location of .wav file, feature path is directory, filename is "X.csv"
def get_data(data_path: str, feature_path: str, feature_filename: str, train: bool, feature_set: str):
    feature_file = os.path.join(feature_path, feature_filename)
    writer = csv.writer(open(feature_file, 'w'))
    first_row = ['label']
    for i in range(1, config.FEATURE_NUM[feature_set] + 1):
        first_row.append(str(i))
    writer.writerow(first_row)

    writer = csv.writer(open(feature_file, 'a+'))
    print('Opensmile extracting...')

    if train == True:
        cur_dir = os.getcwd()
        sys.stderr.write('Curdir: %s\n' % cur_dir)
        os.chdir(data_path)
        # 遍历文件夹
        for i, directory in enumerate(config.CLASS_LABELS):
            sys.stderr.write("Started reading folder %s\n" % directory)
            # pdb.set_trace()
            os.chdir(directory)

            # label_name = directory
            label = config.CLASS_LABELS.index(directory)

            # 读取该文件夹下的音频
            for filename in os.listdir('.'):
                if not filename.endswith('wav'):
                    continue
                filepath = os.getcwd() + '/' + filename
                
                # 提取该音频的特征
                feature_vector = _get_feature_opensmile(filepath, feature_path, feature_set)
                feature_vector.insert(0, label)
                # 把每个音频的特征整理到一个 csv 文件中
                writer.writerow(feature_vector)

            sys.stderr.write("Ended reading folder %s\n" % directory)
            os.chdir('..')
        os.chdir(cur_dir)
    
    else:
        feature_vector = _get_feature_opensmile(data_path, feature_path, feature_set)
        feature_vector.insert(0, '-1')
        writer.writerow(feature_vector)

    print('Opensmile extract done.')

    # 一个玄学 bug 的暂时性解决方案
    # 这里无法直接加载除了 IS10_paraling 以外的其他特征集的预测数据特征，非常玄学
    if(train == True):
        return load_feature(feature_file, train = train, scaler_path=feature_path)