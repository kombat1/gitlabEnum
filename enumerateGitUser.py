#!/bin/python3

import time
import requests
import pprint


for i in range(0,0x5f5e0ff):
	time.sleep(0x0001)
	code = requests.get("https://gitlab.com/api/v4/users/"+str(i))
	if code.status_code == 200:
		#print(code.url)
		data = code.json()
		#pprint.pprint(data)
		if "web_url" in data:
			print(data['web_url'])
		if "name" in data:
			print("Name:",data['name'])
		if "avatar_url" in data:
			print("[mail box] md5 Hash:",data["avatar_url"].split('/')[4][:32])
			print("="*50)
			print('\n')
	else:
		pass

