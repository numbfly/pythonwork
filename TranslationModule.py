## 用于将英文模块翻译成中文，提高学习速度
##  初期只翻译在txt文件中，后续将调用gui
##

import os, time
import requests
from urllib.error import URLError,ContentTooShortError,HTTPError
from bs4 import BeautifulSoup

class TranslationModule(object):

    def module(module_name):
        import module_name         ## import 待翻译模块
        module_list = dir(module_name)  ## 查看该模块目录
        module_length = len(module_list)
        print(f"正在翻译 {module_name}模块，它有 {module_length}个功能。")
        for mothod in module_list:     ##  处理该目录功能
            translationmethod = translate(method)
            print(f"{module_name}.{method}----（{translationmethod}）\n")
            print(help(f"{module_name}.{mothod}"))
            time.sleep(0.5)   ## 设置延迟0.5s

## 翻译目录中的方法
    def translate(method, num_retries = 2):
        url = f"https://translate.google.cn/?tl=ar#view=home&op=translate&sl=en&tl=zh-CN&text={method}"
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.36"
        headers = {'User_Agent': user_agent}
        try:
            resq = requests.get(url, headers = headers, timeout = 10)
            html = resq.text
        except (URLError, HTTPError, ContentTooShortError) as e:
            print ("下载错误原因： ", e.reason)
            html = None
            if num_retries > 0 :
                if hasattr(e, "code") and 500 <= e.code <= 600 :
                    return translate(method, num_retries - 1)

        soup = BeautifulSoup(html, 'lxml')
        translationmean = soup.find_all('span', class_="tlid-translation translation")


## 设置存储路径
    def savefile_path():
        path = os.getcwd()  ### os.getcwd()输出当前工作路径
        print("当前文件路径是：", path)
        choice = input("是否需要修改路径（是/否）：")
        ## python3 是以Unicode编码的
        ## ord（）可以将单个字符串取整数编码
        ## chr（）可以将整数编码转换成字符
        while int(ord(choice)) != int(ord('是')) and int(ord(choice)) != int(ord('否')):

            print('输入错误，请重新输入是或者否')
            choice = input("是否需要修改路径（是/否）：")
        if int(ord(choice)) == int(ord('是')):
            path = input("请输入新路径：")
            os.chdir(path)
        else:
            pass


## 保存文件
    def save_file(module_name):
        with open (f"{module_name}模块翻译.txt", "a+") as f:
            f.write(module(module_name))

##
if __name__ == '__main__':
    module_name = input("需要翻译的模块是： ")
    firststep = TranslationModule.module(module_name)
    secondstep = TranslationModule.savefile_path()
    laststep = TranslationModule.save_file(module_name)
