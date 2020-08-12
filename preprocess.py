'''
提取数据集中音频的特征并保存
'''

import extract_feats.opensmile as of
import extract_feats.librosa as lf
from config import config
from pathlib import Path
import misc.opts as opts
import os

if __name__ == '__main__':
    opt = opts.parse_prepro()
    feat_method = opt.feature
    in_path = opt.in_path
    out_path = opt.out_path

    Path(opt.out_path).mkdir(parents=True, exist_ok=True)

    if(feat_method == 'o'):
        of.get_data(in_path, out_path, config.PREPROCESS_OPENSMILE_FILENAME, feature_set=opt.feature_set, train = True)

    elif(feat_method == 'l'):
        lf.get_data(in_path, out_path, config.PREPROCESS_OPENSMILE_FILENAME, train = True)