#!/usr/bin/python3

import subprocess
import requests
import json
import sys
import re

def rxg_get(path):
	full_path = base_url + path + "/index.json?api_key=" + api_key
	response = json.loads(requests.get(full_path).text)
	return response

def get_ssh_keys():
	response = rxg_get('/ssh_keypairs')
	return response

if len(sys.argv) != 3:
	print('\n\n   PLEASE USE THE FOLLOWING FORMAT:')
	print('     pikeymgr.py fully.qualified.domain.name api_key\n\n')
	quit()

fqdn = sys.argv[1]
api_key = sys.argv[2]
base_url = 'https://' + fqdn + '/admin/scaffolds'
current_keys = []

current_key_pair_data = get_ssh_keys()

#make a backup of the authorized_keys that exist currently
subprocess.run('mv /home/pi /home/pi.bak', shell=True)

for i in current_key_pair_data:
	current_keys.append(i["public_key"])

keyfile = open("/home/pi/.ssh/authorized_keys", "a")

for i in current_keys:
	#subprocess.run("echo " + i + " >> /Users/nkarrick/.ssh/authorized_keys")
	keyfile.write(i + "\n")

keyfile.close()