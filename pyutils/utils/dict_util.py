# -*- encoding: utf-8 -*-
'''
@文件        :dict_util.py
@说明        :字典相关操作
@时间        :2023/12/04 17:03:36
@作者        :Karthrand
@版本        :1.0
'''
import os
from typing import Dict, Any

def deep_update(source: Dict[Any, Any], updates: Dict[Any, Any]):
    """递归地更新字典，保留嵌套字典的原始键"""
    if not isinstance(source, dict):
        # 如果 source 不是字典类型，则返回一个新的空字典
        source = {}
    for key, value in updates.items():
        if isinstance(value, dict) and value:
            # 如果更新的值是非空字典，递归更新
            node = source.setdefault(key, {}) # 如果 key 不存在，则初始化为 {}
            source[key] = deep_update(node, value) # 递归更新
        else:
            # 如果更新的值不是字典或者是空字典，则直接赋值
            source[key] = value
    return source