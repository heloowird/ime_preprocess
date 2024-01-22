#coding:utf-8
#author:heloowird

from __future__ import print_function
import sys
import os
import random


def process(input_fn, train_sample_fn, test_sample_fn):
    train_lst = []
    test_lst = []
    with open(input_fn, 'r') as rf:
        for line in rf:
            line = line.strip('\r\n')
            if random.random() < 0.01:
                test_lst.append(line)
            else:
                train_lst.append(line)

    with open(train_sample_fn, 'a') as wf:
        for line in train_lst:
            wf.write('{}\n'.format(line))

    with open(test_sample_fn, 'a') as wf:
        for line in test_lst:
            wf.write('{}\n'.format(line))


def main():
    sample_dir = sys.argv[1]
    train_sample_fn = '{}/{}'.format(sample_dir, 'train_seq_tot.txt')
    test_sample_fn = '{}/{}'.format(sample_dir, 'test_seq_tot.txt')

    files = os.listdir(sample_dir)
    for fn in files:
        ab_fn = os.path.join(sample_dir, fn)
        if not os.path.isfile(ab_fn):
            continue
        sys.stderr.write('start processing {}\n'.format(ab_fn))
        process(ab_fn, train_sample_fn, test_sample_fn)
        sys.stderr.write('end processing {}\n'.format(ab_fn))


if __name__ == "__main__":
    main()

