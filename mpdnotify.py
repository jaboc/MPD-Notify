#!/usr/bin/python
import mpd
import subprocess
import datetime

def sendmessage(title, message):
    subprocess.Popen(['notify-send', title, message, '-i', '/home/damonj/bin/note.png'])
    return


client = mpd.MPDClient(use_unicode=True)
client.connect("localhost", 6600)


while True:
	if client.idle('player') != "":
		d = client.currentsong()
		sendmessage( d['artist'],d['title'] +"\n"+ d['album'] +"\n"+ str(datetime.timedelta(seconds=int(d['time']))) )

