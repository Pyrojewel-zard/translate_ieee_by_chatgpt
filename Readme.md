解析ieee网页，并利用chatgpt翻译，然后在chatgpt网页里可以手动复制出来，相对而言翻译的精度比其他软件要高

由于网络环境和cookie问题，所以略显麻烦，懒得进一步优化了
1. 首次运行时，先执行os_open.py文件，在这个文件执行后，会自动打开浏览器，然后登录，然后再执行html_deal.py文件
2. 在html_deal.py中，替换ieee的网址，然后运行(需要身份验证过，正常能够访问ieee里的内容)
3. 在html_deal会在当前目录下生成一个含时间戳信息的txt文件以及拆分后的parttxt文件，在python_chatgpt.py中，替换成这个含时间戳信息的txt文件，然后执行即可（需要能访问chatgpt官网环境，同时已登录）

采用的是selenium模块，同时，创建了"D:\\python\\seleniumEdge\"这个文件夹，存放了浏览器打开的cookie信息等等。因此登录的操作只需要在初次执行的时候进行一次即可。
