#!/usr/bin/env python3
#Baznx Theos Forum

import requests
print("""
\033[1;35m
  ------------------------------------------
     |      Theos Forum-Baznx     |
     |     theosforum.org    |
     |                                 |
     |          Baznx and Frazy     |
     |       YouTube Baznx Frazy         |
  ------------------------------------------                                                 
""")                                                                    
                                                                    



website = input("Site adresini gir: \033[1;39m")
print ("")

def main(website):
	url = "https://api.indoxploit.or.id/domain/{}".format(website)
	data = requests.get(url).json()
	ambil_data = data['data']['subdomains']
	for i in ambil_data:
		print(i)

if __name__ == '__main__':
	main(website)
