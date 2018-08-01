import os
import sys
from scrapy.cmdline import execute

#__file__当前文件
print(os.path.abspath(__file__))#输出当前文件路径
print(os.path.dirname(__file__))#输出当前文件父路径
sys.path.append(os.path.dirname(__file__))
execute(['scrapy','crawl','jingdong'])