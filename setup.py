#!/usr/bin/env python

"""Download HMP data files."""

from os.path import dirname

setup_args = {}

try:
    from setuptools import setup
    # Dependencies for easy_install:
    setup_args.update(
        install_requires=[
            'pandas >= 0.20.2',
            'numpy >= 1.13.3',
            'wget >= 3.0',
        ])
except ImportError:
    from distutils.core import setup


DIR = (dirname(__file__) or '.') + '/'


setup_args.update(
    name='hmp_download',
    version='0.1',
    description=__doc__,
    author='Daniel Ian McSkimming',
    author_email='dim@buffalo.edu',
    url='http://github.com/dmcskim/hmp_download',
    scripts=[
        DIR + 'hmp_download.py',
    ])

setup(**setup_args)

