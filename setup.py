#!/usr/bin/env python
import os
from fdfs_client import __version__
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

f = open(os.path.join(os.path.dirname(__file__), 'README.md'),"r",encoding="utf-8" )
long_description = f.read()
f.close()

sdict = {
    'name' : 'easyPyFdfs',
    'version' : __version__,
    'description' : 'Python3 and Python2 client for Fastdfs',
    'long_description_content_type': 'text/markdown',
    'long_description' : long_description,
    'author' : 'renoyuan',
    'author_email' : 'renoyuan@foxmail.com',
    'url':'http://github.com/renoyuan/easyPyFdfs',
    'keywords':['Fastdfs', 'Distribute File System'],
    'license' : 'GPLV3',
    'packages' : ['fdfs_client']
    #'ext_modules' : [Extension('fdfs_client.sendfile',
    #                         sources = ['fdfs_client/sendfilemodule.c'])],
}


setup(**sdict)

