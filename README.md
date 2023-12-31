# HustCASLogin
`华中科技大学统一身份认证登录接口`

## 快速开始
```
# demo.py
from caslogin import login

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}
username="Uyyyyxxxxx"
password="xxxxxxxxxx"

resp_login,session=login(
    url_cas="http://pass.hust.edu.cn/cas/login?service=http://register.hust.edu.cn/caslogin",
    headers=headers,
    username=username,
    password=password,
)
print(resp_login.status_code)
print(resp_login.url)

```


**1kuzus**
