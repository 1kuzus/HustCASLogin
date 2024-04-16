from lxml import etree
from .ocr import ocr
from .encrypt import encrypt
import requests

def login(url_cas, username, password, headers, proxies):
    url_captcha = "https://pass.hust.edu.cn/cas/code"
    url_public_key = "https://pass.hust.edu.cn/cas/rsa"
    with requests.Session() as session:
        # get请求统一身份认证页，获取表单隐藏域的值
        resp_get_url_cas = session.get(url=url_cas, headers=headers, proxies=proxies)
        tree = etree.HTML(resp_get_url_cas.text)
        lt = tree.xpath("//input[@name='lt']/@value")[0]
        execution = tree.xpath("//input[@name='execution']/@value")[0]
        eventId = tree.xpath("//input[@name='_eventId']/@value")[0]

        # 请求验证码
        code_gif_bin = session.get(url=url_captcha, headers=headers, proxies=proxies).content
        code = ocr(code_gif_bin=code_gif_bin)

        public_key = requests.post(url=url_public_key, headers=headers, proxies=proxies).json()['publicKey']
        ul, pl = encrypt(username=username, password=password, public_key=public_key)
        data = {
            "rsa": "",
            "ul": ul,
            "pl": pl,
            "code": code,
            "phoneCode": "",
            "lt": lt,
            "execution": execution,
            "_eventId": eventId,
        }

        return session.post(url=url_cas, headers=headers, data=data, proxies=proxies), session
