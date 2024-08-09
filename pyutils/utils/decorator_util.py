# -*- encoding: utf-8 -*-
'''
@文件        :decorator.py
@说明        :装饰器工具集合
@时间        :2024/02/22 21:16:39
@作者        :Karthrand
@版本        :1.0
'''
import os
import sys
import functools
from datetime import datetime


def exception_with_time(func):
    """
    装饰器, Exception抛出异常时增加时间
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time_message = f"{e} (Occurred at: {now})"
            raise type(e)(time_message).with_traceback(e.__traceback__)
    return wrapper


