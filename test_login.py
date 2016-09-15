import urllib
import urllib2
import sys
import cookielib
import json

type = sys.getfilesystemencoding()

filename = 'cookie.txt'
account = ''
password = ''

values = {"account" : account, "pass" : password, "rememberMe":2, "roleType":1}
url = "http://hfs-be.yunxiao.com/v1/user/user-session"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

headers = {'User-Agent':user_agent}
data = urllib.urlencode(values)

cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

request = urllib2.Request(url, data, headers)
resp = opener.open(request)
cookie.save(ignore_discard=True, ignore_expires=True)

loginUrl = 'http://hfs-be.yunxiao.com/v1/score'
result = opener.open(loginUrl)
resp = result.read().decode('UTF-8').encode(type)
#print result.read().decode('UTF-8').encode(type)
print resp
