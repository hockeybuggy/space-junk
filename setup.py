#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = "0.0.1"

setup(
    name='va-space-junk',
    version=__version__,
    author='Vantage Analytics',
    description='Style enforcement tools',
    author_email='dev@vantageanalytics.com',
    url='https://github.com/vantageanalytics/space-junk',
    packages=find_packages(),
    include_package_data=True,
    data_files=[('.', ('requirements.txt',))],
    install_requires=open('requirements.txt').readlines(),
    license='MIT - 2016 Vantage Analytics',
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False
)
