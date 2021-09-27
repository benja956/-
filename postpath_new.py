# -*- coding:utf-8 -*-
import linecache
import os
import random
import re

actress_path = "E:\\EEE/"
txt = actress_path + "path.txt"
sent_txt = actress_path + "sent.txt"


def choice_actress(path):
    # 定义一个列表，用来存储结果
    actress_list = []
    # 判断路径是否存在
    if os.path.exists(path):
        # 获取该目录下的所有文件或文件夹目录
        files = os.listdir(path)
        for file in files:
            # 得到该文件下所有目录的路径
            m = os.path.join(path, file)
            # 判断该路径下是否是文件夹
            if os.path.isdir(m):
                h = os.path.split(m)
                actress_list.append((h[1]))
        image_path = actress_path + random.choice(actress_list) + "/"
        return image_path


# 随机获取文本行以得到图片路径
def random_path(s):
    count = len(open(s, 'rU', encoding='UTF-8').readlines())
    random_num = random.randrange(1, count)
    random_line = linecache.getline(s, random_num)
    random_image_path = random_line
    # 从文本中获取随机行即为获取随机图片路径
    return random_image_path


# 从女优文件夹读取照片
def walk(image_path):
    data = open(txt, "w+", encoding='UTF-8')
    for root, dirs, files in os.walk(image_path):
        for file in files:
            path_str = os.path.join(root, file)
            print(path_str, file=data)
    data.close()


# 读取txt目录文件删除以txt为后缀的行
def del_txt():
    lineList = []
    matchPattern = re.compile(r'txt')
    file = open(txt, 'r', encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        elif matchPattern.search(line):
            pass
        else:
            lineList.append(line)
    file.close()

    file = open(txt, 'w', encoding='UTF-8')
    for i in lineList:
        file.write(i)
    file.close()


# 封装上述步骤 并 验证是否已经发送过该图片 返回为发送的图片路径
def post_image():
    image_path = choice_actress(actress_path)
    walk(image_path)
    del_txt()
    get = random_path(txt)
    sent = open(sent_txt, "r", encoding="utf-8").read()
    while get in sent:
        walk(image_path)
        del_txt()
        get = random_path(txt)
    return get


# 获取对于该图片的文本描述
def get_description():
    image = post_image()
    get = image.strip("\n")[::-1].split("/", 1)[1][::-1] + "/"
    description_path = get + "description.txt"
    post_txt = open(description_path, "r", encoding="utf-8").read()
    return post_txt, image


# 写入该图片路径到已发送图片库
def write_get(get):
    sent = open(sent_txt, "r", encoding="utf-8").read()
    new_sent = get + sent
    sd = open(sent_txt, "w", encoding="utf-8")
    sd.write(new_sent)
    sd.close()


def main():
    text, image = get_description()
    return image, text