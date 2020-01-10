from requests import post
from sys import argv

if len(argv) < 2:
  print('You must provide your api key')
  exit()
  
api_key = argv[1]
endpoint = 'http://api.thealtening.com/v1/generate?token=%s' % api_key
response = post(endpoint)

print(response.text)
