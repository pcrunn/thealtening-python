import requests
x = "http://api.thealtening.com/v1/generate?token=%enter-api-key-here%"
r = requests.post(x)
print(r.text)
