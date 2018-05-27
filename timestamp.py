#!/usr/bin/python
# coding=utf8

import time


def now():
    return {"timestamp": str(time.time()).split('.')[0], "timestr": time.strftime('%Y-%m-%d %H:%M:%S')}

if __name__ == '__main__':
    print now()