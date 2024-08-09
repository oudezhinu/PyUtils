import datetime 
import time
import re
import pytz

def check_log_time(logs, **kwargs):
    """
    校验各种日志中时间与当前时间误差
    
    参数:
        - log (_type_):        必选，日志信息
        - **kwargs:            可选，容忍的时间误差, 默认为1分钟,支持timedelta的参数
                                如minutes=1、seconds=1、days=1、hours=1等
    """
    if not kwargs:
        # 如果没有传入额外参数，则给kwargs一个默认值：1分钟
        kwargs = {'minutes': 1}

    # 从kwargs中提取值，并创建timedelta对象
    #time_tolerance = timedelta(**{k: v for k, v in kwargs.items() if k in timedelta.__dict__})
    time_tolerance = datetime.timedelta(**{k: int(v) for k, v in kwargs.items() if k in ['days', 'seconds', 'microseconds', 'milliseconds', 'minutes', 'hours', 'weeks']})

    # 正则匹配日志中的时间
    match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', logs)
    if match is None:
        print("日志中无时间信息，跳过")
        return
    
    log_time_str = match.group()
    # 将日志中的时间字符串转换为 datetime 对象，并设置为UTC时间
    log_time = datetime.datetime.strptime(log_time_str, "%Y-%m-%d %H:%M:%S")
    
    # 将日志时间转换为东八区时间
    log_time_utc8 = pytz.timezone('Asia/Shanghai').localize(log_time)
    
    # 获取当前时间，并将其转换为UTC时间
    now_utc = datetime.datetime.now(pytz.utc)
    # 将当前时间转换为东八区时间
    now_utc8 = now_utc.astimezone(pytz.timezone('Asia/Shanghai'))

    # 计算时间差的绝对值
    abs_time_difference = abs(now_utc8 - log_time_utc8)
    
    # 时间差大于容忍时间，抛出异常
    if abs_time_difference > time_tolerance:
        raise ValueError(f"日志时间：{log_time_utc8}，当前时间{now_utc8}，误差时间: {abs_time_difference} 超出时间误差容忍范围: {time_tolerance}")
    else:
        print(f"日志时间：{log_time_utc8}，当前时间{now_utc8}，误差时间: {abs_time_difference} 在时间误差容忍范围: {time_tolerance}")
if __name__ == '__main__':
    check_log_time("2024-05-10 11:14:50  sdasdasdsad")