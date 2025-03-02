import logging
import sys
import time

# 创建一个logger对象
logger = logging.getLogger('life')
logger.setLevel(logging.DEBUG) # 设置日志级别为DEBUG，以便输出所有级别的日志

# 创建一个控制台处理器，并设置级别为DEBUG
console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('log'+ time.strftime('[%Y-%m-%d %H:%M:%S]'))
file_handler.setLevel(logging.DEBUG)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将控制台处理器添加到logger对象
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 输出日志信息
def debug(msg):
    logger.debug(msg)
def info(msg):
    logger.info(msg)
def warning(msg):
    logger.warning(msg)
def error(msg):
    logger.error(msg)
def critical(msg):
    logger.critical(msg)