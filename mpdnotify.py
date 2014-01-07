#!/usr/bin/python
import mpd
import subprocess
import datetime
import time

def sendmessage(title, message):
    subprocess.Popen(['notify-send', title, message, '-i', '/home/damonj/bin/note.png'])
    return


client = mpd.MPDClient(use_unicode=True)
client.connect("localhost", 6600)

current = ""

while True:
	if client.idle('player') != "":
		d = client.currentsong()
		if d['title'] != current:
			sendmessage( d['artist'],d['title'] +"\n"+ d['album'] +"\n"+ str(datetime.timedelta(seconds=int(d['time']))) )
			current = d['title']
