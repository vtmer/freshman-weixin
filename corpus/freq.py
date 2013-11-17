#coding: utf-8

import os
from collections import Counter
import jieba

from utils import list_raw_files, parse


SPECIAL_DICT = os.path.abspath('./special.dict')
with open(os.path.abspath('./stopwords.txt')) as f:
    STOP_WORDS = [i.decode('utf-8').strip() for i in f.readlines()]
RAW = os.path.abspath('./raw')
DEST = os.path.abspath('./corpus-freq.dict')


jieba.load_userdict(SPECIAL_DICT)


def concat():
    content = []
    for name in list_raw_files(RAW):
        with open(name) as f:
            content.append(parse(f.read())['content'])
    return '\n'.join(content)


def cut(raw):
    return jieba.cut(raw)


def clean(raw):
    def judge(item):
        cleaned = item.strip()
        return cleaned not in STOP_WORDS and cleaned

    return filter(judge, raw)


def count(raw):
    ret = Counter([i.strip() for i in raw]).items()
    ret.sort(cmp=lambda a, b: b[1] - a[1])
    return ret


def main():
    with open(DEST, 'w') as f:
        for k, v in count(clean(cut(concat()))):
            f.write('%s %d\n' % (k.encode('utf-8'), v))


if __name__ == '__main__':
    main()
