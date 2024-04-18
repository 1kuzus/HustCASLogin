import requests
from caslogin import login

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}

proxy_url="http://v2.api.juliangip.com/company/postpay/getips?auto_white=1&num=1&pt=1&result_type=json&trade_no=6941024556910948&sign=5d0714f18dcc85d6c00dfa3818e0368b"
resp_proxy = requests.get(proxy_url)

proxies = {
    "http": resp_proxy.json()["data"]["proxy_list"][0],
    "https": resp_proxy.json()["data"]["proxy_list"][0],
}
# proxies=None
username = "Uyyyyxxxxx"
password = "xxxxxxxxxx"

resp_login, session = login(
    url_cas="http://pass.hust.edu.cn/cas/login?service=http://register.hust.edu.cn/caslogin",
    username=username,
    password=password,
    headers=headers,
    proxies=proxies,
)

print(resp_login.status_code)
print(resp_login.url)
print(resp_login.headers)
print(resp_login.request.headers)
print(resp_login.request.body)
# print(resp_login.text)

resp_login2=session.get(resp_login.url,headers=headers,proxies=proxies)
print(resp_login2.status_code)
print(resp_login2.url)
