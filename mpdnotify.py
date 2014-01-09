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

currentTrack 	= ""
currentState 	= "badger"
previousState 	= "ferret"

while True:
	if client.idle('player') != "" :
		d = client.currentsong()
		noted = "false"
		
		
	if client.status()['state'] == "pause":
		previousState = currentState
		currentState = client.status()['state']
		print ("Previous : " + previousState)
		print ("Current  : " + currentState)
		
	if client.status()['state'] == "play" :
		try:
			artist = d['artist']
			title  = d['title']
			album  = d['album']
			time   = d['time']
		except KeyError:
			artist = ""
			title  = ""
			album  = ""
			time   = ""
		
		if d['title'] != currentTrack and noted == "false":		
			sendmessage( artist , title +"\n"+ album +"\n"+ str(datetime.timedelta(seconds=int(time))) )
			currentTrack = title
			previousState = currentState
			currentState = client.status()['state']
			noted = "true"
		else:
			if d['title'] == currentTrack and currentState != previousState:
				sendmessage( artist , title +"\n"+ album +"\n"+ str(datetime.timedelta(seconds=int(time))) )
				currentTrack = title
				previousState = currentState
				currentState = client.status()['state']
				noted = "true"

