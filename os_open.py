import os
import time
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium import webdriver

os.popen("msedge.exe --remote-debugging-port=9222 --user-data-dir=\"D:\\python\\seleniumEdge\"")
time.sleep(2)
# 设置Edge浏览器选项
edge_options = Options()
edge_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# 指定Edge WebDriver的路径
webdriver_path = "D:\\Downloads\\edgedriver_win64\\msedgedriver.exe"

# 创建Edge浏览器实例
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)
sourceurl="https://ieeexplore.ieee.org/document/6022011"
driver.get(sourceurl)
