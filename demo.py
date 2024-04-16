import requests
from caslogin import login

resp_proxy = requests.get("http://v2.api.juliangip.com/company/postpay/getips?num=1&pt=1&result_type=json&trade_no=6941024556910948&sign=3178f51630758c114eca195ad347fabf")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}
proxies = {
    "http": resp_proxy.json()["data"]["proxy_list"][0]
}
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
