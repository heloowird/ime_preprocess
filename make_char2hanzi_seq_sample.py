#coding:utf-8
#author:heloowird

from __future__ import print_function
import sys
import os
from collections import defaultdict


def load_dict(fn):
    token_dict = defaultdict(str)
    with open(fn, 'r') as f:
        for line in f:
            i, ele, cnt = line.strip('\r\n').split('\t')
            token_dict[ele] = i
    return token_dict


def process(input_fn, hanzi_dict, pinyin_dict, train_sample_fn):
    with open(train_sample_fn, 'w') as wf:
        with open(input_fn, 'r') as rf:
            for line in rf:
                hanzis, pinyins, words = line.strip('\r\n').split('\t')
                hanzi_index = [hanzi_dict[ele] if ele in hanzi_dict else hanzi_dict['UNK'] for ele in hanzis.split(' ')]
                pinyin_index = [pinyin_dict[ele] if ele in pinyin_dict else pinyin_dict['UNK'] for ele in pinyins.replace(' ', '')]
                wf.write('{}\t{}\n'.format(' '.join(pinyin_index), ' '.join(hanzi_index)))


def main():
    pinyin_seg_dir = sys.argv[1]
    hz_dict_fn = sys.argv[2]
    py_dict_fn = sys.argv[3]
    train_seq_dir = sys.argv[4]

    hanzi_dict = load_dict(hz_dict_fn)
    pinyin_dict = load_dict(py_dict_fn)

    for fn in os.listdir(pinyin_seg_dir):
        ab_fn = os.path.join(pinyin_seg_dir, fn)
        if not os.path.isfile(ab_fn):
            continue
        sys.stderr.write('start processing {}\n'.format(ab_fn))
        train_sample_fn = '{}/{}_{}'.format(train_seq_dir, fn.split('.')[0], 'train_sample')
        process(ab_fn, hanzi_dict, pinyin_dict, train_sample_fn)
        sys.stderr.write('end processing {}\n'.format(ab_fn))


if __name__ == "__main__":
    main()

