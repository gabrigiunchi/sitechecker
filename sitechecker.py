import multitimer
import urllib.request
import sys
from datetime import datetime
from playsound import playsound
import re
import argparse

argumentsParser = argparse.ArgumentParser()
argumentsParser.add_argument("-url")
argumentsParser.add_argument("-frequency")
argumentsParser.add_argument("-clean")
argumentsParser.add_argument("-playOnStart")

htmlTagRegex = re.compile(r"<.+?>")
commentRegex = re.compile(r"<!--.*!?-->")
song = "aaaaaaaaaaaaa.mp3"
previous = "marunn che bello sto programma"
url = "https://www.bag.admin.ch/bag/it/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/empfehlungen-fuer-reisende/quarantaene-einreisende.html#1204858541"
removeTagsAndComments = True
frequency=60

args = args=argumentsParser.parse_args()

if args.url is not None:
    url = args.url

if args.clean is not None:
    removeTagsAndComments = args.clean.lower() == "true"

if args.frequency is not None:
    frequency = int(args.frequency)

if args.playOnStart is not None and args.playOnStart.lower() == "false":
    print("\nI am very dissapointed in you. You had the opportunity to listen to the voice of God and you did not take it. Shame.\n")
    previous = ""

print(f"url: {url}")
print(f"frequency: {frequency}s")
print(f"remove html tags and comments: {removeTagsAndComments}\n")

def check():
    global previous
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        if removeTagsAndComments:
            html = htmlTagRegex.sub("", html)
            html = commentRegex.sub("", html)
        if previous != html and previous != "":
            print(f"SITE HAS CHANGED ({datetime.now()})")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
            playsound(song)
        previous = html

t1 = multitimer.MultiTimer(frequency, check)
t1.start()

s = ""
while s.lower() != "stop":
    try:
        s = input("Enter stop to stop (duh)\n\n")
    except KeyboardInterrupt:
        s = "stop"
    if s == "play":
        playsound(song)

t1.stop()