import execjs
import re
import os

def encrypt(username, password, public_key):
    root_dir = os.path.dirname(__file__)
    with open(os.path.join(root_dir, "encrypt.js"), "r") as js_file:
        jscode = js_file.read()
    jscode = re.sub(r"setPublicKey\('(.*?)'\)", f"setPublicKey('{public_key}')", jscode)
    encrypt_js = execjs.compile(jscode)
    ul = encrypt_js.call("strEnc", username)
    pl = encrypt_js.call("strEnc", password)
    return ul, pl
