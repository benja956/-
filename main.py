import postpath_new
import requests

actress_path = "E:\\EEE/"
access_token = '2.00Nne1MHZt3nrC59aa3c4cc7qib48E'
url = "https://api.weibo.com/2/statuses/share.json"


def main():
    # 获取图片绝对路径和描述
    image, status = postpath_new.main()
    postpath_new.write_get(image)
    pic = image.replace("\n", "")
    text = status + "http://weibo.ccxg.cc"
    print(pic, text)
    # 构建POST参数
    params = {
        "access_token": access_token,
        "status": text
    }
    # 构建二进制multipart/form-data编码的参数
    files = {
        "pic": open(pic, "rb")
    }
    # POST请求，发表文字微博
    res = requests.post(url, data=params, files=files)
    print(res.text)
    print(res.text, file=open(actress_path + "log.txt", "a+", encoding='UTF-8'))


if __name__ == '__main__':
    main()
