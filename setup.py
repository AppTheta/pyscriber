#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages
import os
import re

basepath = os.path.dirname(__file__)
readme_rst = os.path.join(basepath, "README.rst")
requirements_txt = os.path.join(basepath, "requirements.txt")

with open(readme_rst) as readme:
    long_description = readme.read()

with open(requirements_txt) as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]


def get_version(filename):
    with open(filename) as r:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", r.read()))
        return metadata['version']


args = dict(
    name='scriber',
    version=get_version("scriber/__init__.py"),
    author='Josh Braegger',
    author_email='rckclmbr@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={'scriber': ['data/ca-certificates.crt',]},
    url='https://github.com/scriber/scriber.py',
    license='Apache 2.0',
    description='Python client API for scriber.io',
    long_description=long_description,
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Monitoring',
    ],
    data_files=(
        ('', ["LICENSE.txt", ]),
    ),
    zip_safe=False,
    install_requires=install_requires,
)

setup(**args)
