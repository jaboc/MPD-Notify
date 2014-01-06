#!/usr/bin/python
import mpd
import subprocess
import shlex
import datetime

def sendmessage(title, message):
	#args = shlex.split(args)
	#print ( args )
    subprocess.Popen(['notify-send', title, message, '-i', '/home/damonj/bin/note.png'])
    #subprocess.Popen(['notify-send', "Hello", "boo"])
    return


client = mpd.MPDClient(use_unicode=True)
client.connect("localhost", 6600)

print (client.currentsong())
print (client.stats())
print (client.status())

x = 1
while True:
	if client.idle('player') != "":
		print ("")
		print ("")
		d = client.currentsong()
		print ( d )
		print ( d['album'] )
		
		sendmessage( d['artist'],d['title'] +"\n"+ d['album'] +"\n"+ str(datetime.timedelta(seconds=int(d['time']))) )

#notify-send -i "path/to/icon.png" "Title (bold)" "Text Line1 \nText Line2 \nText Line3"
