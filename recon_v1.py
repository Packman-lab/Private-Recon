#Date : 21 Nov 2021
#Creator : Packman-lab
#Lang : Python
#Status : Beta

from pynput.keyboard import Key, Listener
import os
import socket
import requests
import hashlib
import argparse
import json
import logging
import time
import nmap
import sys



print("\nRecon is a Web Reconnaissance framework written in Python3.")
print("This can gather data from the Internet about the websites.")


while True :

	print("\n\nOptions : \n")

	print("1. Keylogger")
	print("2. Web Fingerprinting ")
	print("3. Port Scan")
	print("4. MD5 Cracker")
	print("5. Subdomain finder")
	print("6. Exit")

	i=input("\n\nChoice : ")

	if i=='1':

		print("Starting Keylogger", end="")
		sys.stdout.flush()
		message=" ...." 
		for i in message:
		   print(i+"",end="")
		   sys.stdout.flush()
		   time.sleep(0.5)

		print("\nRunning....")

		logdir = ""
		logging.basicConfig(filename=(logdir+"klog.txt"),level=logging.DEBUG,format="%(asctime)s: %(message)s")

		def pressing_key(Key):
			try:
				logging.info(str(Key))
			except AttributeError:
				print("A special key {0} has been pressed.".format(key))
		def releasing_key(key):
			if key == Key.esc:
				return False
		print("\nStarted listening...\n")
		print("\nPress 'Esc' to stop it ..")
		with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
			listener.join()

	elif i=='2':
		global url
		url = input("Enter the url : ")
		Req=requests.get("https://"+url)
		print("Collecting headers info", end="")
		sys.stdout.flush()
		message=" ...." 
		for i in message:
		   print(i+"",end="")
		   sys.stdout.flush()
		   time.sleep(0.8)
		print("\n\n",Req.headers)

		GetHost = socket.gethostbyname(url)
		print("\nIP address of "+url+" is: "+ GetHost + "\n")


		Info=requests.get("https://ipinfo.io/"+GetHost+"/json")
		Resp=json.loads(Info.text)
		print("Gathering Location info", end="")
		sys.stdout.flush()
		message=" ...." 
		for i in message:
		   print(i+"",end="")
		   sys.stdout.flush()
		   time.sleep(0.5)
		print("\n\nLocation: "+Resp["loc"])
		print("Region: "+Resp["region"])
		print("City: "+Resp["city"])
		print("Country: "+Resp["country"])

	elif i=='3':

		global Ip
		print("\nEnter 1 for Url based Port Scanning [By DEFAULT]")
		print("Enter 2 for Ip  based Port Scanning ")
		mode=input("\n\nEnter Mode : ")
		if mode == '1':
			url = input("Enter the url : ")
			Ip = socket.gethostbyname(url)
			target = str(Ip)
		elif mode == '2':
			Ip = input("Enter the IP addr :")
			target = str(Ip)
		else :
			url = input("Enter the url : ")
			Ip = socket.gethostbyname(url)
			target = str(Ip)

		print("\n\nNote: This is a quick Scan Tool. For Detailed deep scan Please use nmap.")

		ports = []

		n = int(input("Enter the number of ports to Scan (MUST BE SMALL) : "))

		print("\nEnter the port numbers. For Example 21,22,80,443..etc\n")

		for i in range(0, n):
		    ele = int(input())

		    ports.append(ele)

		scan = nmap.PortScanner()

		print("\nScanning",target, end="")
		sys.stdout.flush()
		message=" ...."
		for i in message:
		   print(i+"",end="")
		   sys.stdout.flush()
		   time.sleep(0.5)
		print("\n")
		for port in ports:
		    portscan = scan.scan(target,str(port))
		    print("Port",port," is ",portscan['scan'][target]['tcp'][port]['state'])

		print("\nHost",target," is ",portscan['scan'][target]['status']['state'])

	elif i=='4':
		
		hash_md5 = input("Enter the MD5 Hash : ")
		wordlist = input("Enter the wordlist Path : ")

		print("\n[+] Cracking", end="")
		sys.stdout.flush()
		message=" ...."
		for i in message:
		   print(i+"",end="")
		   sys.stdout.flush()
		   time.sleep(0.5)
		print("\n")
		start = time.time()
		hash_cracked = ""
		with open(wordlist, "r") as file:
			for line in file:
				line = line.strip()
				if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest() == hash_md5:
					hash_cracked = line
					print("\n[+] MD5-hash has been successfully cracked.\nThe Key is %s." %line)
					break
					# end = time.time()
					# print ("[*] Time: %s seconds" % round((end - start), 2))
		if hash_cracked == "" :
			
			print("\n[+] Failed to crack the hash. \n\nTry using a bigger/different dictionary.")
			
		end = time.time()
		print("[*] Time: %s seconds" % round((end - start), 2))
	elif i =='5':
		url=input("Enter url : ")
		a=input(" Proceed to find Subdomains ? (Y/N) : ")
		if(a=='Y' or a=='y'):
			domain=""
			domain=input("\nEnter the Path of your Subdomains list [Press Enter to use Default] : ")
			print("\n Finding Subdomains from given txt :")
			print("------------------------------------------------------------------\n")
			if domain=="":
				sub_list = open("subdomains-1000.txt").read()
			else:
				sub_list = open(domain).read()
				
			subs = sub_list.splitlines()

			for sub in subs:
			    url_to_check = f"https://{sub}.{url}"

			    try:
			        requests.get(url_to_check)

			    except requests.ConnectionError:
			        pass

			    else:
			        print("Valid domain: ",url_to_check)
		elif(a=='N' or a == 'n'):
			print("Process Completed \n")
		else:
			print("Enter a Valid Input \n")

	elif i=='6':
		exit()

	else:
		pass


