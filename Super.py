import time
import datetime
import requests
import json

''' 
Super约课专用，输出周一至周五时间戳
by Poison
'''


# 发送约课报文
def postAppointment(date):
    # ss_data = "cli_v=3.4.7&coachId=6&personalTrainerCardId=0&phone=15298666541&sess=1e7d06aLLLHTs3RPNozDShlXRHstpw6TzEfOzT%2BYWqUIbQ%2BS&sys_c=sys_c&sys_m=iPhone&sys_p=i&sys_v=14.2&dayFromTime=" + training_day
    stm_data = "cli_v=3.4.7&coachId=6&personalTrainerCardId=0&phone=15905230866&sess=64baEbPzK%2Be1UENjiNmo7HRniwCPUFRgbGlCdQk1adBtH2OI&sys_c=sys_c&sys_m=iPhone&sys_p=i&sys_v=14.2&dayFromTime=" + date
    url = "https://app.fitoneapp.com/app/club/coache/book"
    headers = {
        'method': 'POST',
        'scheme': 'https',
        'path': '/app/club/coache/book',
        'authority': 'app.fitoneapp.com',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B176 FitOne/1.5',
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9, zh-HK;q=0.8',
        'cookie': 'fitone_sess=cedd9O8BYakUpPF4T02hNjqDtseWLPHkSWt29PZwX7TW8nQ',
        'content-type': 'application/x-www-form-urlencoded',
        'content-length': '186'
    }
    req = requests.post(url, data=stm_data, headers=headers)
    data = json.loads(req.text)

    print(req.status_code)
    # print(req.text)
    print(data)


# 将%Y-%m-%d %H:%M:%S格式的日期转换为时间戳
def formatTimestamp(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    timestamp = str(int(time.mktime(date.timetuple())))
    return timestamp


# 根据不同人来发送约课报文
def postReservation(date, data):
    data = data + date
    url = "https://app.fitoneapp.com/app/club/coache/book"
    headers = {
        'method': 'POST',
        'scheme': 'https',
        'path': '/app/club/coache/book',
        'authority': 'app.fitoneapp.com',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B176 FitOne/1.5',
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9, zh-HK;q=0.8',
        'cookie': 'fitone_sess=cedd9O8BYakUpPF4T02hNjqDtseWLPHkSWt29PZwX7TW8nQ',
        'content-type': 'application/x-www-form-urlencoded',
        'content-length': '186'
    }
    req = requests.post(url, data=data, headers=headers)
    data = json.loads(req.text)
    # print(req.status_code)
    # print(req.text)
    print(data["message"])


# 预约课程，固定为中午12点
def reservation(date):
    date = date + " 12:00:00"
    postAppointment(formatTimestamp(date))


# 预约日期以及包含该日期之后n天，stm ss轮流约
def reservations(date, days):
    date = date + " 12:00:00"
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    for i in range(0, days):
        print(date, end='')
        if i % 2 == 0:
            data = "cli_v=3.4.7&coachId=6&personalTrainerCardId=0&phone=15298666541&sess=1e7d06aLLLHTs3RPNozDShlXRHstpw6TzEfOzT%2BYWqUIbQ%2BS&sys_c=sys_c&sys_m=iPhone&sys_p=i&sys_v=14.2&dayFromTime="
            print("\t预约ss\t", end='')
        else:
            data = "cli_v=3.4.7&coachId=6&personalTrainerCardId=0&phone=15905230866&sess=64baEbPzK%2Be1UENjiNmo7HRniwCPUFRgbGlCdQk1adBtH2OI&sys_c=sys_c&sys_m=iPhone&sys_p=i&sys_v=14.2&dayFromTime="
            print("\t预约stm\t", end='')
        postReservation(str(int(time.mktime(date.timetuple()))), data)
        delta = datetime.timedelta(days=1)
        date = date + delta


# 从起始日开始5天，一般为周一
if __name__ == '__main__':
    # 从起始日期开始，预约几天
    reservations("2021-07-05", 5)
