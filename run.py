"""
将命令写入py文件，启动爬虫时直接运行run.py即可
"""
from scrapy import cmdline
cmdline.execute("scrapy crawl attkSpider".split())
