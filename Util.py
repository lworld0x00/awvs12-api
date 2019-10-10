#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/10/10
# @Author  : tudouya (chenfengwei@jd.com)
# @Editor  : xrayl (1world0x00@gmail.com)
# @Version : 1.0.0

from os.path import dirname, join

ROOT_DIR = dirname(dirname(__file__))


def get_file_path(*path):

    return join(ROOT_DIR, *path)


