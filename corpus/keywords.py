#coding: utf-8

import os
import jieba
import jieba.analyse

from utils import list_raw_files, parse


SPECIAL_DICT = os.path.abspath('./special.dict')
CORPUS_FREQ_DICT = os.path.abspath('./corpus-freq.dict')
RAW = os.path.abspath('./raw')
TOP_K = 10
DEST = os.path.abspath('./keywords')


jieba.load_userdict(CORPUS_FREQ_DICT)
jieba.load_userdict(SPECIAL_DICT)


def extract(post, top_k=None):
    top_k = top_k or TOP_K
    return list(set(jieba.analyse.extract_tags(post['title']) +
                    jieba.analyse.extract_tags(post['content'])))


def main():
    for files in list_raw_files(RAW):
        with open(files) as f:
            post = parse(f.read())
            with open(os.path.join(DEST, os.path.basename(files)), 'w') as d:
                d.write('\n'.join(extract(post)).encode('utf-8'))


if __name__ == '__main__':
    main()
