import json
import re
import requests
from pyquery import PyQuery as pq
keyword='阿里巴巴'
page=1
if __name__ == '__main__':
    # 报文header 消息头数据
    url = 'https://www.qcc.com/web/search?key='+keyword+'&p='+str(page)
    headers = {
        'Connection': 'keep-alive',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie':''
    }
    r = requests.get(url, headers=headers, verify=True)
    a = re.search(r"window\.__INITIAL_STATE__=(.*?);", r.text).group(1)
    msg=json.loads(a)
    for i in range(0, len(msg['search']['searchRes']['Result'])):
        print('https://www.qcc.com/firm/'+msg['search']['searchRes']['Result'][i]['KeyNo']+'.html')
        print(pq(msg['search']['searchRes']['Result'][i]['Name']).text())
        print(msg['search']['searchRes']['Result'][i]['Address'])
        print(msg['search']['searchRes']['Result'][i]['ContactNumber'])
        print(msg['search']['searchRes']['Result'][i]['Email'])
        print(msg['search']['searchRes']['Result'][i]['Tag'])

