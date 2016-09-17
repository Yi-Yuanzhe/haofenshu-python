import requests
import urllib
import EncPwd
import json

#account = 'yicorleone'
#password = '31e56aaab8b80e5ca2d1a8e4d55f0519'
url_login = "http://hfs-be.yunxiao.com/v1/user/user-session"
url_score = "http://hfs-be.yunxiao.com/v1/score"


s = requests.Session()

def login():
    account = input('请输入用户名:')
    password = input('请输入密码:')
    pwd_md5 = EncPwd.md5(password)
    values = {"account" : account, "pass" : pwd_md5, "rememberMe":2, "roleType":1}
    resp = s.post(url_login, values).text
    result = json.loads(resp)
    print('\n')
    print('信息: ' + result['msg'])
    print('学生Id: ' + result['data']['studentId'])
    print('学生姓名: ' + result['data']['studentName'])

def getScore():
    resp = s.get(url_score)
    result = json.loads(resp.text)
    print('\n')
    print('信息：' + result['msg'])
    print('近期考试: ' + result['data'][0]['name'])
    print('全级人数: ' + str(result['data'][0]['gradeStudentNum']))
    print('班级人数: ' + str(result['data'][0]['classStudentNum']))
    print('班级人数: ' + str(result['data'][0]['classStudentNum']))
    print('\n')
    print('=====考试情况=====' + '\n')
    print('全科成绩: ' + str(result['data'][0]['details'][0]['score']))
    print('你的成绩: ' + str(result['data'][0]['details'][0]['realScore']))
    print('班级平均分: ' + str(result['data'][0]['details'][0]['classAvg']))
    print('班级排名: ' + str(result['data'][0]['details'][0]['classRank']))
    print('全级平均分: ' + str(result['data'][0]['details'][0]['gradeAvg']))
    print('全级排名: ' + str(result['data'][0]['details'][0]['gradeRank']))

if __name__ == '__main__':
    login()
    getScore()
