import multitimer
import urllib.request
import sys
from playsound import playsound

previous = "marunn che bello sto programma"

url = "https://www.bag.admin.ch/bag/it/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/empfehlungen-fuer-reisende/quarantaene-einreisende.html#1204858541"
if (len(sys.argv) > 1):
    url = sys.argv[1]

print(f"Url: {url}")

def check():
    global previous
    with urllib.request.urlopen(url) as response:
        html = response.read()
        if (previous != html and previous != ""):
            print("SITE HAS CHANGED")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            playsound("aaaaaaaaaaaaa.mp3")
        previous = html

t1 = multitimer.MultiTimer(10, check)
t1.start()

s = ""
while s.lower() != "stop":
    s = input("Enter stop to stop (duh)\n")
    if (s == "play"):
        playsound("aaaaaaaaaaaaa.mp3")
t1.stop()