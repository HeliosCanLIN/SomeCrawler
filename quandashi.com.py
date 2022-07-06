import requests
page=0
num=0
keyword='小米'
if __name__ == '__main__':
    # 报文header 消息头数据
    url = 'https://so.quandashi.com/search/search/search-list'
    headers = {
        'Host': 'so.quandashi.com',
        'Connection': 'keep-alive',
        'Content-Length': '377',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://so.quandashi.com',
        'Referer': 'https://so.quandashi.com/index/search',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie':''
    }
    data = {'key':keyword,
            'searchKey':'',
            #'param':'2',
            'page': '0',
            'pageSize': '100000',
            }
    r = requests.post(url, headers=headers, data=data, verify=True)
    print(r.json())
    totalPage=r.json()['data']['pages']
    while page < totalPage:
        for i in range(0, len(r.json()['data']['items'])):
            print(r.json()['data']['items'][i]['tmName'])
            print(r.json()['data']['items'][i]['statusZh'])
            print(r.json()['data']['items'][i]['intCls'])
            print(r.json()['data']['items'][i]['address'])
            print(r.json()['data']['items'][i]['agency'])
            print(r.json()['data']['items'][i]['applicantCn'])
            num+=1
        page+=1
        data = {'key': keyword,
                'searchKey': '',
                # 'param':'2',
                'page': str(page),
                'pageSize': '100000',
                }
        r = requests.post(url, headers=headers, data=data, verify=True)
print("总共"+str(totalPage)+"页，共"+str(num)+"条记录")