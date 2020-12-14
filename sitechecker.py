import multitimer
import urllib.request
import sys
from datetime import datetime
from playsound import playsound
import re

htmlTagRegex = re.compile(r"<.+?>")
commentRegex = re.compile(r"<!--.*!-->")
song = "aaaaaaaaaaaaa.mp3"
previous = "marunn che bello sto programma"
url = "https://www.bag.admin.ch/bag/it/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/empfehlungen-fuer-reisende/quarantaene-einreisende.html#1204858541"

if (len(sys.argv) > 1):
    url = sys.argv[1]

print(f"url: {url}")

def check():
    global previous
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        html = htmlTagRegex.sub("", html)
        html = commentRegex.sub("", html)
        if (previous != html and previous != ""):
            print(f"SITE HAS CHANGED ({datetime.now()})")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            playsound(song)
        previous = html

t1 = multitimer.MultiTimer(10, check)
t1.start()

s = ""
while s.lower() != "stop":
    try:
        s = input("Enter stop to stop (duh)\n")
    except KeyboardInterrupt:
        s = "stop"
    if (s == "play"):
        playsound(song)

t1.stop()