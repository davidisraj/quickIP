#!/usr/bin/python

"""
quickly obtains external IP address and prints to CLI
"""

import requests
import re

#print working message
print("\nWorking...\n")

#get data from web
data = requests.get('https://ipv4.wtfismyip.com')

#extract IPv4
ipv4 = re.findall(r'([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})', data.text)

#
print("Your External IP is: " + ipv4[0])
print(" ")

input("Press Enter to exit.")
