# -*- coding: utf8 -*-

import requests, os
from bs4 import BeautifulSoup
 
cookie = os.environ.get('cookie_dnf_bbs')

def pjCheckin(*args):
    try:
        msg = ""
        SCKEY = os.environ.get('SCKEY')
        s = requests.Session()
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip, deflate, br',
            'Cookie': cookie,
            'ContentType':'text/html;charset=gbk'
        }
        s.get('https://dnf.gamebbs.qq.com/plugin.php?id=k_misign:sign', headers=headers)
        a = s.get('https://dnf.gamebbs.qq.com/plugin.php?id=k_misign:sign&operation=qiandao&formhash=91f427c6&format=empty', headers=headers)
        b = BeautifulSoup(a.text,'html.parser')
        c = b.find('div',id='messagetext').find('p').text

        if ""  in c:
            if SCKEY:
                scurl = f"https://sc.ftqq.com/{SCKEY}.send"
                data = {
                        "text" : "DNF论坛  Cookie过期",
                        "desp" : c
                        }
                requests.post(scurl, data=data)
            print("cookie_dnf_bbs失效，需重新获取")
            msg += "cookie_dnf_bbs失效，需重新获取"
        elif "恭喜"  in c:
            print("论坛签到成功")
            msg += "论坛签到成功"
        else:
            print(c)
    except:
        print(b)
        print("签到出错")
        msg += "签到出错"
    return msg
        

if __name__ == "__main__":
    if cookie:
        print("----------DNF论坛开始尝试签到----------")
        pjCheckin()
        print("----------DNF论坛签到执行完毕----------")
