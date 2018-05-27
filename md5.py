#!/usr/bin/python
# coding=utf8

import hashlib


class MD5:

    md5 = hashlib.md5()

    @staticmethod
    def md5(str_value):
        MD5.md5.update(str_value)
        return MD5.md5.hexdigest()

if __name__ == '__main__':
    print MD5.md5('123456')