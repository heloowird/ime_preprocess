#coding:utf-8
#author:heloowird

from __future__ import print_function
import sys
import os
from collections import defaultdict


def write_dict(unsorted_dict, fn, need_special=True):
    with open(fn, 'w') as f:
        skip_cnt = 0
        if need_special:
            f.write('{}\t{}\t{}\n'.format(0, 'PAD', -1))
            f.write('{}\t{}\t{}\n'.format(1, 'SEP', -1))
            f.write('{}\t{}\t{}\n'.format(2, 'BOS', -1))
            f.write('{}\t{}\t{}\n'.format(3, 'EOS', -1))
            f.write('{}\t{}\t{}\n'.format(4, 'MASK', -1))
            f.write('{}\t{}\t{}\n'.format(5, 'UNK', -1))
            skip_cnt = 6
        for i, ele in enumerate(sorted(unsorted_dict.items(), key=lambda x:x[1], reverse=True)):
            f.write('{}\t{}\t{}\n'.format(i+skip_cnt, ele[0], ele[1]))


def load_dict(fn):
    token_dict = defaultdict(int)
    with open(fn, 'r') as f:
        for line in f:
            _, ele, cnt = line.strip('\r\n').split('\t')
            token_dict[ele] = int(cnt)
    return token_dict


def process(input_dir, hz_dict_fn, py_dict_fn):
    hanzi_dict = defaultdict(int)
    pinyin_dict = defaultdict(int)

    fns = os.listdir(input_dir)
    for fn in fns:
        ab_fn = os.path.join(input_dir, fn)
        sys.stderr.write('start processing {}\n'.format(ab_fn))
        if not os.path.isfile(ab_fn):
            continue
        token_dict = load_dict(ab_fn)
        if ab_fn.endswith('hz_dict.txt'):
            hanzi_dict.update(token_dict)
        elif ab_fn.endswith('py_dict.txt'):
            pinyin_dict.update(token_dict)
        sys.stderr.write('end processing {}\n'.format(ab_fn))

    write_dict(hanzi_dict, hz_dict_fn, True)
    write_dict(pinyin_dict, py_dict_fn, True)


def main():
    dict_dir = sys.argv[1]
    hz_dict_fn = '{}/{}'.format(dict_dir, 'hz_dict_tot.txt')
    py_dict_fn = '{}/{}'.format(dict_dir, 'py_dict_tot.txt')
    process(dict_dir, hz_dict_fn, py_dict_fn)


if __name__ == "__main__":
    main()

