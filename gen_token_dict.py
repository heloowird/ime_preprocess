#coding:utf-8
#author:heloowird

from __future__ import print_function
import sys
import os
from collections import defaultdict


def write_dict(unsorted_dict, fn, need_special=False):
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


def process(input_fn, hz_dict_fn, py_dict_fn):
    hanzi_dict = defaultdict(int)
    pinyin_dict = defaultdict(int)

    error_line_cnt = 0
    with open(input_fn, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\r\n')
            info = line.split('\t')
            if len(info) != 3:
                error_linecnt += 1        
                print(line)
            hanzis, pinyins, words = info
            for hz in hanzis.split(' '):
                if hz.isprintable():hanzi_dict[hz] += 1
            for py in pinyins.split(' '):
                for e in py:
                    if e.isprintable():pinyin_dict[e] += 1
    
    write_dict(hanzi_dict, hz_dict_fn)
    write_dict(pinyin_dict, py_dict_fn)
    print('error lines: {}'.format(error_line_cnt))


def main():
    corpus_dir = sys.argv[1]
    dict_dir = sys.argv[2]
    for fn in os.listdir(corpus_dir):
        ab_fn = os.path.join(corpus_dir, fn)
        if not os.path.isfile(ab_fn):
            continue
        hz_dict_fn = '{}/{}_{}'.format(dict_dir, fn.split('.')[0], 'hz_dict.txt')
        py_dict_fn = '{}/{}_{}'.format(dict_dir, fn.split('.')[0], 'py_dict.txt')
        sys.stderr.write('start processing {}\n'.format(ab_fn))
        process(ab_fn, hz_dict_fn, py_dict_fn)
        sys.stderr.write('end processing {}\n'.format(ab_fn))


if __name__ == "__main__":
    main()

