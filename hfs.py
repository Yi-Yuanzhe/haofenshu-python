import requests
import urllib

account = 'yicorleone'
password = '31e56aaab8b80e5ca2d1a8e4d55f0519'
url_login = "http://hfs-be.yunxiao.com/v1/user/user-session"
url_score = "http://hfs-be.yunxiao.com/v1/score"
values = {"account" : account, "pass" : password, "rememberMe":2, "roleType":1}

s = requests.Session()

s.post(url_login, values)
result = s.get(url_score)
print(result.json())
