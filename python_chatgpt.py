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

def count_files_with_pattern(directory, pattern):
    # Initialize count
    count = 0
    # Iterate over all files in the directory
    for file_name in os.listdir(directory):
        # If the file name contains the pattern, increment the count
        if pattern in file_name:
            count += 1
    return count

# os.system("msedge.exe --remote-debugging-port=9222 --user-data-dir=\"D:\\python\\seleniumEdge\"")
# time.sleep(10)
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

# 命令行执行 msedge.exe --remote-debugging-port=9222 --user-data-dir="D:\python\seleniumEdge"

try:
    # 打开ChatGPT网页
    driver.get("https://chat.openai.com/")
    
    # 等待页面加载
    time.sleep(5)
    
    file_path = pathlib.Path("test20240816094139.txt")
    # 获取当前文件夹里的修改时间最新的txt文件
    file_splitname=file_path.stem+"_part"
    dictionary="."
    num=count_files_with_pattern(dictionary, file_splitname)
    
    for i in range(num):
        with open(f"{file_path.stem}_part{i+1}.txt", 'r', encoding='utf-8') as file:
            content_temp = file.read()
            inputElements=driver.find_elements(By.TAG_NAME, "textarea")
            inputElements[0].send_keys(content_temp)
            time.sleep(2)
            inputElements[0].send_keys(Keys.ENTER)
            time.sleep(60)

    # 获得网页的所有内容

    # outputElements=driver.find_elements(By.CLASS_NAME, r"markdown.prose.w-full.break-words.dark\:prose-invert.light")
    # results = []
    # for element in outputElements:
    #     results.append(element.text)
    #     # print(results)
    #     timenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    #     with open(f"output{timenow}.txt", 'w', encoding='utf-8') as f:
    #         for result in results:
    #             f.write(result + '\n')


finally:
    # 关闭浏览器
    driver.quit()
