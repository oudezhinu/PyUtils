# -*- encoding: utf-8 -*-
'''
@文件        :nwetwork_util.py
@说明        :网络相关工具类
@时间        :2023/12/04 17:03:36
@作者        :Karthrand
@版本        :1.0
'''
import os
import yaml
from loguru import logger as log
from typing import Dict, Any
import platform

def write_file(data, file_path, mode='w'):
    with open(file_path, mode) as f:
        f.write(data)

def config_domain(ip, domain):
    domain_conversion = "{} {}".format(ip, domain)
    system = platform.system().lower()
    log.info("当前系统为:{}".format(system))
    
    if system == "windows":
        p = r"C:\Windows\System32\drivers\etc\hosts"
    elif system == "linux":
        p = "/etc/hosts"
    else:
        raise Exception("未知系统:{}".format(system))

    try:
        with open(p, mode="r") as f:
            lines = f.readlines()
    except Exception as e:
        log.error("读取文件失败: {}".format(str(e)))
        return
    
    updated_lines = []
    domain_found = False
    
    for line in lines:
        if line.strip() and not line.startswith("#"):
            parts = line.split()
            if len(parts) >= 2 and parts[1] == domain:
                updated_lines.append(domain_conversion + "\n")
                domain_found = True
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    if not domain_found:
        updated_lines.append(domain_conversion + "\n")
    
    try:
        write_file(''.join(updated_lines), p, mode="w")
        log.info("写入:{}  to {} 成功".format(domain_conversion, p))
    except Exception as e:
        log.error("写入文件失败: {}".format(str(e)))

# Example usage
if __name__ == "__main__":
    config_domain("192.168.1.1", "example.com")
