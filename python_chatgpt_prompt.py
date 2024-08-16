from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import re
import pathlib
import datetime
import os


# 设置Edge浏览器选项
edge_options = Options()
edge_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# 指定Edge WebDriver的路径
webdriver_path = "D:\\Downloads\\edgedriver_win64\\msedgedriver.exe"

# 创建Edge浏览器实例
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# 命令行执行 msedge.exe --remote-debugging-port=9222 --user-data-dir="D:\python\seleniumEdge"

try:
    # 打开ChatGPT网页
    driver.get("https://chat.openai.com/")
    
    # 等待页面加载
    time.sleep(5)
    
    
    content_temp = "Give your custom prompt here"
    inputElements=driver.find_elements(By.TAG_NAME, "textarea")
    inputElements[0].send_keys(content_temp)
    time.sleep(2)
    inputElements[0].send_keys(Keys.ENTER)
    time.sleep(60)

    # 获得网页的所有内容

    outputElements=driver.find_elements(By.CLASS_NAME, r"markdown.prose.w-full.break-words.dark\:prose-invert.light")
    results = []
    for element in outputElements:
        results.append(element.text)
        # print(results)
        timenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        with open(f"output{timenow}.txt", 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result + '\n')


finally:
    # 关闭浏览器
    driver.quit()
