#coding:utf-8
#author:heloowird

from __future__ import print_function
import sys
import os
from time import time

from pypinyin import pinyin, lazy_pinyin, Style

# improve pinyin acc
from pypinyin_dict.phrase_pinyin_data import cc_cedict
cc_cedict.load()
from pypinyin_dict.pinyin_data import kxhc1983
kxhc1983.load()

import jieba
from tqdm import tqdm


def word2pinyin(words):
    pinyins = pinyin(words, style=Style.NORMAL)
    return [ele[0] for ele in pinyins]


def text2pinyin(line):
    words = list(jieba.cut(line))
    pinyins = []
    for word in words:
        pinyins.extend(word2pinyin(word))
    return (list(line), pinyins, words)


def line2pinyin(line):
    ans = []
    line = line.strip('\r\n')
    texts = line.split('\t')
    for text in texts:
        text = text.replace(' ', '').strip('\r\t ')  
        hanzis, pinyins, words = text2pinyin(text)
        ans.append('{}\t{}\t{}'.format(' '.join(hanzis), ' '.join(pinyins), ' '.join(words)))

    return ans

def process(input_fn, output_fn):
    lines = []
    with open(input_fn, 'r') as f:
        lines = f.readlines()

    with open(output_fn, 'w') as f:
        for line in tqdm(lines):
            texts = line2pinyin(line)
            for ele in texts:
                f.write('{}\n'.format(ele))


def multiple_process(fn, cpu_num=3):
    from multiprocessing import Pool
    with open(fn, 'r') as f:
        lines = f.readlines()

        with Pool(cpu_num) as p:
            p.map(line2pinyin, lines)


def main():
    corpus_dir = sys.argv[1]
    pinyin_seg_dir = sys.argv[2]
    for fn in os.listdir(corpus_dir):
        ab_fn = os.path.join(corpus_dir, fn)
        if not os.path.isfile(ab_fn):
            continue
        sys.stderr.write('start processing {}\n'.format(ab_fn))
        process(ab_fn, '{}/{}'.format(pinyin_seg_dir, fn))
        sys.stderr.write('end processing {}\n'.format(ab_fn))


if __name__ == "__main__":
    main()

