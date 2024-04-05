# -*- encoding: utf-8 -*-
'''
@文件        :file.py
@说明        :文件及文件夹相关操作
@时间        :2023/12/04 17:03:36
@作者        :Karthrand
@版本        :1.0
'''
import os
from loguru import logger as log
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
