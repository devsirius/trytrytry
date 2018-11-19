import urllib,urllib2,json

def send_message():
    url = "http://127.0.0.1:5000/openqq/send_group_message"
    textmod = {"name":"双子星测试通知","content":"111晴朗"}
    data = urllib.urlencode(textmod)
    req = urllib2.Request(url=url,data=data)
    res = urllib2.urlopen(req)
