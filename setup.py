#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'flumelogger',
    version = '0.1',
    description = 'Flume logging handler for sending log events to Flume',
    author = 'Lars Sjostrom',
    author_email = 'lars@radicore.se',
    url = 'http://github.com/lsjostro/flumehandler',
    packages = find_packages(),
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'thrift',
    ],
)