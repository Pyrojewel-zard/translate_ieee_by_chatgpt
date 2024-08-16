import datetime
from selenium import webdriver  # 导入网页控制器
import selenium.webdriver.edge.options  # 导入Edge的选项控制器
from msedge.selenium_tools import Edge, EdgeOptions  # 导入Edge的功能
from selenium.webdriver.common.by import By  # 用于定位class元素
from selenium.webdriver.support.ui import WebDriverWait  # 等待
from selenium.webdriver.support import expected_conditions as EC  # 执行条件

from bs4 import BeautifulSoup
import pyperclip
import re
import pathlib
#import datetime  # 用来计算程序运行时间，测试完就隐藏起来了

#st = datetime.datetime.now()  # 获取程序运行的起始时间

def GetUrl(sourceurl):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True  # 初始化Edge
    edge_options.headless = False  # 非静默运行，网页显示
 
    # 公司电脑，没权限在python安装目录里存放webdriver，就自己建立个文件夹存放，所以在调用的时候，要引用到那个存放目录
    driver = Edge(executable_path="D:\\Downloads\\edgedriver_win64\\msedgedriver.exe", options=edge_options)
    
    driver.get(sourceurl)
    
    try:
        # 等待页面完全加载
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body"))  # 等待页面body元素加载完成
        )
        
        # 获取页面内容
        page_content = driver.page_source
        return page_content
    
    finally:
        driver.quit()
        # pass


import re

import re
from pathlib import Path

def split_text_by_words_preserve_newlines(file_path, words_per_chunk=800):
    # 读取输入文件的所有内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式将内容分割为单词，同时保留换行符
    words_with_newlines = re.split(r'(\s+)', content)

    # 初始化变量
    chunks = []
    current_chunk = []
    current_word_count = 0

    # 迭代单词并将它们累积到块中
    for element in words_with_newlines:
        # 如果元素是一个单词（而不仅仅是空白）
        if re.match(r'\S+', element):
            current_word_count += 1
        current_chunk.append(element)

        # 当达到指定的单词数且句子结束时，添加到块列表中
        if current_word_count >= words_per_chunk:
            # 检查最后一个元素是否是句子结束符号
            if re.search(r'[.!?]', element):
                chunks.append(''.join(current_chunk))
                current_chunk = []
                current_word_count = 0

    # 如果最后的块存在，则添加到列表中
    if current_chunk:
        chunks.append(''.join(current_chunk))

    # 将每个块保存到一个单独的.txt文件中
    for idx, chunk in enumerate(chunks):
        chunk_file_path = Path(f"{file_path.stem}_part{idx+1}.txt")
        with open(chunk_file_path, 'w', encoding='utf-8') as chunk_file:
            content = chunk + "<br>翻译成中文，同时公式输出在$$……$$中，行内字符输出在$……$中，标题及小标题用#来区分"
            chunk_file.write(content)

    return len(chunks)  # 返回创建的块的数量



if __name__ == '__main__':
    
    sourceurl="https://ieeexplore.ieee.org/document/6022011"
    html_content = GetUrl(sourceurl)
    print(html_content)

    # 连续的<\p><p>替换成两个换行符</p>\n\n<p>
    with open("test.txt", 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 写入到文件test.txt里
    timenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    txtname='test'+timenow+'.txt'
    # ed = datetime.datetime.now()  # 获取程序结束时间
    # print((ed - st).seconds) 

   # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # 保留换行符
    for br in soup.find_all('br'):
        br.replace_with('\n')

    # 保留段落格式
    for p in soup.find_all('p'):
        p.insert_after('<br>')
        p.replace_with('<br>  ' + p.get_text())

    # 保留标题格式
    for i in range(1, 7):
        for heading in soup.find_all(f'h{i}'):
            heading.insert_before(f"{'#' * i} ")
            heading.insert_after('<br>')

    # Extract the body content
    body_content = soup.find('body')
    # Get text from the body content
    body_text = body_content.get_text() if body_content else "No body content found"

    # print(body_text[:2000])  # Display the first 500 characters of the body text to get an idea of the content

    # 匹配文本'Abstract'，并获取其后的文本内容
    content_txt = body_text[body_text.find('Contents'):]

    # 去掉起始的Contents
    content_txt = content_txt[8:]

    # 替换View Source为空
    content_txt=content_txt.replace('View Source','')
    #正则表达式匹配([^\n])\n([^\n])，并去掉换行符
    content_txt = re.sub(r'([^\n])\n([^\n])', r'\1\2', content_txt)
    content_txt = re.sub(r'([^\n])\n([^\n])', r'\1\2', content_txt)
    # 多次匹配\n\n，替换成\n,直到没有\n\n
    while '\n\n' in content_txt:
        content_txt = content_txt.replace('\n\n', '\n')
    
    #匹配末尾文本"Authors Figures References Citations Keywords"，并去掉其及其之后的文本
    content_txt = content_txt[:content_txt.find('AuthorsFiguresReferencesCitationsKeywords')]
    #遍历每一行，去掉行首空格
    content_txt = '\n'.join([line.lstrip() for line in content_txt.split('\n')])
    content_txt = re.sub(r'Show All\n', r'', content_txt)
    # 去掉开头的空行

    content_txt = re.sub(r'\n',r'<br>',content_txt)
    content_txt = content_txt.lstrip()
    # 输出到剪贴板

    with open(txtname, 'w', encoding='utf-8') as f:
        f.write(content_txt)

    path = pathlib.Path(txtname)
    split_text_by_words_preserve_newlines(path, 800)
    