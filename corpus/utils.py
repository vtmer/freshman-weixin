#coding: utf-8

import os


def list_raw_files(raw_parent):
    taken = []
    for name, dirs, files in os.walk(raw_parent):
        for i in files:
            taken.append(os.path.join(name, i))
    return taken


def parse(raw):
    r = raw.split('---------')
    return {
        'title': r[0].decode('utf-8').strip(),
        'content': ''.join(r[1:]).decode('utf-8').strip()
    }
