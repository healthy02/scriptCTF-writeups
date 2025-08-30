# Web - Renderer
The `app.py` wants us to upload an image file to it and then it gives you a preview of what you have uploaded.

However the real vulnerability of the system is in the way that it stores cookies.

When we upload the image it calls the `/developer` for the first time, it sees that the `secret_cookie.txt` is empty and updates it with a random value, thus creating a new secret.

```py
secret_resp = s.get(f"{BASE}/static/uploads/secrets/secret_cookie.txt")
secret = secret_resp.text.strip()
```

It returns `"You are not a developer!"` but now we have a secret, which is saved in the public static library, so we can just download the secret.


We set the value of the `developer_secret_cookie` as the secret, and now we access the `/developer` again.

```py
s.cookies.set('developer_secret_cookie', secret, domain='play.scriptsorcerers.xyz')
```
This returns the value of the flag.

```py
final_resp = s.get(f"{BASE}/developer")
```


`scriptCTF{my_c00k135_4r3_n0t_s4f3!}`