import urllib.request
import urllib.error
import urllib
import codecs
import socket
from  bs4 import BeautifulSoup
import gzip
import zlib
import random
#from scrapy.spiders import Spider
import json
from lxml import etree
import re
import pandas as pd
import pymysql
#from sqlalchemy import create_engine
import time
import datetime
import http.cookiejar
import requests

#读取代理ip
my_proxy = []
with open('proxy_ip.txt','rt') as proxy_file:
    temp_data = proxy_file.readlines()
    for data_lines in temp_data:
        my_proxy.append(data_lines.strip())


# In[3]:

province_address = [
"https://www.haodf.com/yiyuan/beijing/list.htm",
"https://www.haodf.com/yiyuan/shanghai/list.htm",
"https://www.haodf.com/yiyuan/guangdong/list.htm",
"https://www.haodf.com/yiyuan/guangxi/list.htm",
"https://www.haodf.com/yiyuan/jiangsu/list.htm",
"https://www.haodf.com/yiyuan/zhejiang/list.htm",
"https://www.haodf.com/yiyuan/anhui/list.htm",
"https://www.haodf.com/yiyuan/jiangxi/list.htm",
"https://www.haodf.com/yiyuan/fujian/list.htm",
"https://www.haodf.com/yiyuan/shandong/list.htm",
"https://www.haodf.com/yiyuan/sx/list.htm",
"https://www.haodf.com/yiyuan/hebei/list.htm",
"https://www.haodf.com/yiyuan/henan/list.htm",
"https://www.haodf.com/yiyuan/tianjin/list.htm",
"https://www.haodf.com/yiyuan/liaoning/list.htm",
"https://www.haodf.com/yiyuan/heilongjiang/list.htm",
"https://www.haodf.com/yiyuan/jilin/list.htm",
"https://www.haodf.com/yiyuan/hubei/list.htm",
"https://www.haodf.com/yiyuan/hunan/list.htm",
"https://www.haodf.com/yiyuan/sichuan/list.htm",
"https://www.haodf.com/yiyuan/chongqing/list.htm",
"https://www.haodf.com/yiyuan/shanxi/list.htm",
"https://www.haodf.com/yiyuan/gansu/list.htm",
"https://www.haodf.com/yiyuan/yunnan/list.htm",
"https://www.haodf.com/yiyuan/xinjiang/list.htm",
"https://www.haodf.com/yiyuan/neimenggu/list.htm",
"https://www.haodf.com/yiyuan/hainan/list.htm",
"https://www.haodf.com/yiyuan/guizhou/list.htm",
"https://www.haodf.com/yiyuan/qinghai/list.htm",
"https://www.haodf.com/yiyuan/ningxia/list.htm",
"https://www.haodf.com/yiyuan/xizang/list.htm"]

#爬虫编写
def url_request(page_url,my_proxy):
    my_UA = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    ]
    my_referrs = [
                'https://www.google.com/',
                'https://cn.bing.com/',
                'https://www.baidu.com/',
                'https://www.sogou.com/',
                'https://www.haodf.com/yiyuan/beijing/list.htm'
    ]
    UA_rand = random.choice(my_UA)
    referrer_rand = random.choice(my_referrs)
    decode_type='gbk'
    proxy_rand = {'http': random.choice(my_proxy)}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
#         'Cookie': '__jsluid=c1ac5b5309c82ad82bffeba120fdfd2a; g=78915_1530610642808; \
#                    UM_distinctid=1645f80f00cf2c-01d41c7a19b803-5e442e19-100200-1645f80f00e639; _ga=GA1.2.1253019111.1530610643; \
#                    _gid=GA1.2.1154013751.1530610643; BAIDU_SSP_lcr=https://www.google.com/; g=HDF.133.5b3b5eef12940; \
#                    CNZZDATA1256706712=659526392-1530609423-https%253A%252F%252Fcn.bing.com%252F%7C1530681552; _gat=1; \
#                    Hm_lvt_dfa5478034171cc641b1639b2a5b717d=1530621510,1530681338,1530686518,1530686524; \
#                    Hm_lpvt_dfa5478034171cc641b1639b2a5b717d=1530686524',
        'DNT': '1',
        'Host': 'www.haodf.com',
        'Referer': referrer_rand,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': UA_rand
          }
    cookies = http.cookiejar.CookieJar()
    cookies_handler = urllib.request.HTTPCookieProcessor(cookies)
    # 代理IP信息为字典格式，key为“http”，value为“代理ip：端口”
    timeout = 4
    # 设置socket超时
    socket.setdefaulttimeout(timeout)
    try:
        response = urllib.request.Request(page_url,headers = headers)
        # 使用ProxyHandler方法生成处理器对象
        proxy_handler = urllib.request.ProxyHandler(proxy_rand)
        # 创建代理IP的opener实例
        opener = urllib.request.build_opener(proxy_handler)
        opener.add_handler(cookies_handler)
        # 打开信息
        try:
            html = opener.open(response)
            print(html.getcode())
        except:
            time.sleep(1+random.randint(0,3))
            resulttxt = url_request(page_url,my_proxy)
            return resulttxt
        result = html.read()
        try:
            resulttxt = zlib.decompress(result, 16+zlib.MAX_WBITS).decode(decode_type,'ignore')
        except:
            time.sleep(1+random.randint(0,3))
            resulttxt = url_request(page_url,my_proxy)
            return resulttxt
    except urllib.error.URLError as e:
        if hasattr(e, "reason"):
            print("错误原因："+ str(e.reason))
            time.sleep(1+random.randint(0,3))
            resulttxt = url_request(page_url,my_proxy)
            return resulttxt
    except urllib.error.HTTPError as e:
        if hasattr(e, "code"):
            print("错误状态码："+ str(e.reason))
            time.sleep(1+random.randint(0,3))
            resulttxt = url_request(page_url,my_proxy)
            return resulttxt
    except socket.timeout:
        print("请求超时")
        time.sleep(3+random.randint(0,3))
        resulttxt = url_request(page_url,my_proxy)
        return resulttxt
    else:
#         print("请求通过")
        return resulttxt

def get_hospital(link, f):
    hospital_net = url_request(link, my_proxy)
    rha = link[31:-4]


    #医院名
    x1 = hospital_net.find('<h1 class="hospital-name">')
    x2 = hospital_net.find('</h1>')
    title = hospital_net[x1+26:x2]
    hospital_net = hospital_net[x2:]

    #头衔
    label = ''
    while True:
        x3 = hospital_net.find('<span class="hospital-label-item">')
        x4 = hospital_net.find('</span>')
        if len(hospital_net[x3+34:x4]) > 8:
            break
        label = label + hospital_net[x3+34:x4] + ','
        hospital_net = hospital_net[x4+1:]
    #print(hospital_net)
    if not label:
        label = 'null'

    #评价
    if '<span class="h-i-label mr10">' in hospital_net:
        x5 = hospital_net.find('<span class="h-i-label mr10">')
        x6 = x5 + hospital_net[x5 + 1:].find('<span class="h-i-label mr10">')

        text1 = hospital_net[x5 + 50:x6]
        t1 = text1.find('第')
        t2 = text1.find('名')
        city = text1[t1 + 1:t2]
        if '全国' in text1:
            text1 = text1[t2 + 5:]
            t3 = text1.find('第')
            t4 = text1.find('名')
            country = text1[t3 + 1:t4]
        else:
            country = 'null'
        hospital_net = hospital_net[x6+10:]

        x7 = hospital_net.find('<span class="h-i-label mr10">')
        text2 = hospital_net[:x7]
        t5 = text2.find('<span class="h-i-orange">')
        t6 = text2.find('次')
        visitor = text2[t5 + 26:t6]
        if '万' in visitor:
            visitor = visitor[:-2] + '0000'

        text2 = text2[t6 + 1:]
        t7 = text2.find('<span class="h-i-orange">')
        t8 = text2.find('位')
        online = text2[t7 + 25:t8]

        hospital_net = hospital_net[x7+2:]

        t9 = hospital_net.find('<span class="h-i-orange">')
        t10 = hospital_net.find('</span></span>')

        positive = hospital_net[t9 + 25:t10]
        hospital_net = hospital_net[t10 + 10:]
        t11 = hospital_net.find('<span class="h-i-orange mr10">')
        t12 = hospital_net.find('</span><span class="h-i-label">')
        negative = hospital_net[t11 + 31:t12]

        hospital_net = hospital_net[t12 + 20:]

        t13 = hospital_net.find('<span class="h-i-orange">')
        t14 = hospital_net.find('%</span>')

        overall = hospital_net[t13 + 25:t14] + '%'

    else:
        x5 = hospital_net.find('<span class="hp-i-label">')
        x6 = x5 + hospital_net[x5 + 1:].find('<span class="hp-i-label">')

        text1 = hospital_net[x5 + 50:x6]
        t1 = text1.find('第')
        t2 = text1.find('名')
        city = text1[t1 + 1:t2]
        if '全国' in text1:
            text1 = text1[t2 + 5:]
            t3 = text1.find('第')
            t4 = text1.find('名')
            country = text1[t3 + 1:t4]
        else:
            country = 'null'
        hospital_net = hospital_net[x6 + 10:]
        x7 = hospital_net.find('累计访问量')
        text2 = hospital_net[x7:]
        t5 = text2.find('<span class="hp-i-orange">')
        t6 = text2.find('次')
        visitor = text2[t5 + 26:t6]
        if '万' in visitor:
            visitor = visitor[:-2] + '0000'

        text2 = text2[t6 + 1:]
        t7 = text2.find('<span class="hp-i-orange">')
        t8 = text2.find('位')
        online = text2[t7 + 26:t8]

        x8 = hospital_net.find('两年内评价')
        hospital_net = hospital_net[x8 + 2:]

        t9 = hospital_net.find('<span class="hp-i-orange mr16">')
        t10 = t9 + hospital_net[t9:].find('</span>')

        positive = hospital_net[t9 + 31:t10]

        hospital_net = hospital_net[t10 + 10:]

        t11 = hospital_net.find('<span class="hp-i-orange">')
        t12 = t11 + hospital_net[t11:].find('</span>')
        negative = hospital_net[t11 + 27:t12]

        hospital_net = hospital_net[t12 + 20:]

        t13 = hospital_net.find('<span class="hp-i-orange">')
        t14 = hospital_net.find('%</span>')

        overall = hospital_net[t13 + 26:t14] + '%'

    t15 = hospital_net.find('<span class="m-h-title-grey">')
    hospital_net = hospital_net[t15:]
    t16 = hospital_net.find('科室')
    t17 = hospital_net.find('个')
    t18 = hospital_net.find('大夫')
    t19 = hospital_net.find('人')
    keshi_num = hospital_net[t16 + 3:t17 - 1]
    doctor_num = hospital_net[t18 + 3:t19 - 1]

    f.write(rha + '\t' + title + '\t' + label + '\t' + city + '\t' + country + '\t' + visitor + '\t' + online + '\t' + positive + '\t' + negative + '\t' + overall + '\t' + keshi_num + '\t' + doctor_num + '\t' + link + '\n')
    print(title, label, '市内排名：' + city, '全国排名：'+country, '累计访问量：'+visitor, '在线服务患者：'+online, '好评：'+positive, '差评：'+negative, '患者满意度：'+overall)
    #while True:


if __name__ == "__main__":
    f = codecs.open('wuhan.txt', 'w')
    #get_hospital('https://www.haodf.com/hospital/DE4r0Fy0C9LuGRgNgmyuD0lf3o2p0zvkj.htm', f)

    x = ["https://www.haodf.com/yiyuan/hubei/list.htm"]
    #获得各省各医院的网址
    for each in x:
        province_net = url_request(each, my_proxy) #获取html
        count = 0
        #print(province_net)
        hospital_net = []

        while True:
            x1 = province_net.find('<a href="/hospital/')
            x2 = x1 + province_net[x1:].find('" target="_blank"')
            if len(province_net[x1:x2]) < 2:
                break
            hospital_net.append('https://www.haodf.com' + province_net[x1+9:x2])
            count += 1
            province_net = province_net[x2:]

        print(count)

        for each in hospital_net:
            get_hospital(each, f)


        break
