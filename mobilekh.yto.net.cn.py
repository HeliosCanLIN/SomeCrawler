import requests
from Crypto.Cipher  import AES
import base64
key = ''#偏移量
vi = ''#密钥
phone= #手机号
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
def AES_Encrypt(key,vi,data):# 密钥（key）, 密斯偏移量（iv） CBC模式加密
    data = pad(data)# 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    encodestrs = base64.b64encode(encryptedbytes)# 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    enctext = encodestrs.decode('utf8')# 对byte字符串按utf-8进行解码
    return enctext
if __name__ == '__main__':
    phone=
    pushdata = '{"userCode":"","phone":"'+str(phone)+'","pageNo":1,"pageSize":20}'
    OrderUrl = 'http://mobilekh.yto.net.cn/steward/app/traceCode/getOrderInfo'
    headers = {
        'Host': 'mobilekh.yto.net.cn',
        'Connection': 'keep-alive',
        'Content-Length': '146',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'http://mobilekh.yto.net.cn',
        'Referer': 'http://mobilekh.yto.net.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'JSESSIONID=65EC93290DB711BE75C057B4D9139E8B'
    }
    Orderdata = '{"encryptText":"'+AES_Encrypt(key,vi,pushdata)+'"}'
    r = requests.post(OrderUrl, headers=headers, data=Orderdata, verify=True)
    for i in range(0,len(r.json()['rows'])):
        print(r.json()['rows'][i]['trackingNumber'],end=' ')
        print(r.json()['rows'][i]['phone'],end=' ')
        print(r.json()['rows'][i]['receiveName'],end=' ')
        print(r.json()['rows'][i]['address'],end=' ')
        print(r.json()['rows'][i]['status'],end=' ')
        print(r.json()['rows'][i]['orderTimeStr'],end=' ')
        print(r.json()['rows'][i]['orderTime'])
        trackingNumber=r.json()['rows'][i]['trackingNumber']
        traceUrl = 'http://mobilekh.yto.net.cn/steward/app/traceCode/getTraceInfo'
        traceData = '{"encryptText":"'+AES_Encrypt(key,vi,'{"trackingNumber":"'+trackingNumber+'"}')+'"}'
        traceDetail = requests.post(traceUrl, headers=headers, data=traceData, verify=True)
        for j in range(0, len(traceDetail.json()['data']['listTrace'])):
            print(str(traceDetail.json()['data']['listTrace'][j]['processInfo'])+str(traceDetail.json()['data']['listTrace'][j]['upload_Time']))
        print("---------------------------------------------------------------------------------------")