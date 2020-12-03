import requests
import os

#填入你的账号密码
user = ""
password = ""
print("登录账号: {}".format(user))
print("登录密码: {}".format(password))

#GET请求取重定向地址
geturl = "http://1.1.1.1/"
http_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
try:
    over = requests.get(geturl,headers=http_headers,allow_redirects=False)
except BaseException as err:
    print("--------错误--------")
    print(str(err))
    os.system("pause")
    exit()
location = over.headers["Location"]
#print(over.headers)
if location == "https://1.1.1.1/":
    print("已登录过")
    os.system("pause")
    exit()
else:
    print("重定向到{}".format(location))

#POST提交校园网登录表单
url = "http://223.99.141.139:9090/web/connect"
data = {
    "web-auth-user": user,
    "web-auth-password": password,
    "redirect-url": location
}
header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "219",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "BIGipServersc-ltm-xywpt-portal3-pool=135926188.33315.0000",
    "Host": "223.99.141.139:9090",
    "Origin": "http://223.99.141.139:9090",
    "Referer": location,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
res = requests.post(url,data,headers=header).status_code
print("回应代码{}".format(res))

if res == 200:
    print("登录成功")
else:
    print("登录失败,请检查账号密码是否正确")

os.system("pause")