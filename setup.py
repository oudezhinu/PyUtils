# -*- encoding: utf-8 -*-
'''
@文件        :setup.py
@说明        :Python打包脚本
@时间        :2024/04/05 11:19:48
@作者        :Karthrand
@版本        :1.0
'''
from setuptools import setup, find_packages

setup(
    name="pyutils",
    version="20240523",
    packages=find_packages(exclude=["test"]),
    url="http://nas.karthrand.cn:8181/oudezhinu/pyutils.git",
    author="Karthrand",
    include_package_data=True
)
