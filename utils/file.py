# -*- encoding: utf-8 -*-
'''
@文件        :file.py
@说明        :文件及文件夹相关操作
@时间        :2023/12/04 17:03:36
@作者        :Karthrand
@版本        :1.0
'''
import os
import yaml
from loguru import logger as log
from typing import Dict, Any

def read_file_content(file_path, encoding='utf-8', file_exception=True):
    """
    读取文件内容 

    参数:
        - file_path (str):              文件路径
        - encoding (str, 可选):         编码方式, 默认值: 'utf-8'.
        - file_exception (bool, 可选):  文件不存在时是否报错, 默认值: True.

    Raises:
        FileNotFoundError:              文件不存在时抛出异常.

    返回:
        - file_content (str):           文件内容
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        if file_exception:
            raise FileNotFoundError(f'文件不存在: {file_path}')
        else:
            log.warning(f'文件不存在: {file_path}')
            return None
    
    # 读取内容
    with open(file=file_path, mode='r', encoding=encoding) as file:
        file_content = file.read()
    return file_content

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

def 更新yaml配置文件(config_file, update_data):

    # 读取现有的YAML文件
    with open(config_file, 'r') as file:
        config_data = yaml.safe_load(file) or {}

    # 使用深度更新,更新数据
    deep_update(config_data, update_data)

    # 将更新后的数据写回YAML文件
    with open(config_file, 'w') as file:
        yaml.dump(config_data, file, default_style=False)

    log.info("yaml更新完毕")
