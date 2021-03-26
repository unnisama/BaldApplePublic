import requests
from time import sleep
import os

def cleanl(listi):
    listi = [s for s in listi if s != ""]
    return listi

CLIP_FRAMES = 6571
framesf = open('frameo.txt', 'r')
framesf = framesf.read().split("\n\n")
frames = []
for d in framesf:
    foa = ""
    d = cleanl(d.split("\n"))
    for r in d:
        for c in cleanl(r.split("-")):
            foa += chr(int(c)+10240)
        foa += "\n"
    frames.append(foa)
chat_id = "-1001162248544"
def sundi(bot, text,id):
    resp = requests.get("https://api.telegram.org/bot"+bot+"/editMessageText?chat_id="+id+"&message_id=2&text="+text)
    print(resp.text)

while True:
    for i in range(1,int(CLIP_FRAMES/30)):
        if(i <= CLIP_FRAMES):
            if(frames[((i-1)*30)+3] != frames[(i-1)*30]):
                sundi("1620657190:AAGToNV9CgIs-FSQBqxmVp73Xjba8_4bPw0", frames[((i-1)*30)+3], chat_id)
            if(frames[((i-1)*30)+3] != frames[((i-1)*30)+6]):
                sundi("1638300673:AAFxcLYYcp3I5oHQxP1ytFOQaRqmj9BGWTY", frames[((i-1)*30)+6], chat_id)
            if(frames[((i-1)*30)+6] != frames[((i-1)*30)+9]):
                sundi("1687997175:AAESD8lLNRuE6H3Cnc-OsN5mZjgEqZ--Po8", frames[((i-1)*30)+9], chat_id)
            if(frames[((i-1)*30)+9] != frames[((i-1)*30)+12]):
                sundi("1615551265:AAFlkghi-CHXi47h1rG57yiOM1Da1fnPSLM", frames[((i-1)*30)+12], chat_id)
            if(frames[((i-1)*30)+12] != frames[((i-1)*30)+15]):
                sundi("1230499014:AAFoAAj3b5vBwi6RXF30mCYfIARrAandsvE", frames[((i-1)*30)+15], chat_id)
            if(frames[((i-1)*30)+15] != frames[((i-1)*30)+18]):
                sundi("1641211579:AAHrnchL3fZHzo3Sg3hfYetZx-IhkbbYA70", frames[((i-1)*30)+18], chat_id)
            if(frames[((i-1)*30)+18] != frames[((i-1)*30)+21]):
                sundi("1325328143:AAE1f4Nnfvd2BPCvseOjpFBfOD59-U8UYKQ", frames[((i-1)*30)+21], chat_id)
            if(frames[((i-1)*30)+21] != frames[((i-1)*30)+24]):
                sundi("1682741696:AAHaNuE9SczYiFNg05F4nestmy1Sa8QXOeo", frames[((i-1)*30)+24], chat_id)
            if(frames[((i-1)*30)+24] != frames[((i-1)*30)+27]):
                sundi("1688755576:AAFOqrDDR2VB-bWrg4ZbYV8inRgI-9FG9J0", frames[((i-1)*30)+27], chat_id)
            if(frames[((i-1)*30)+27] != frames[((i-1)*30)+30]):
                sundi("1792748042:AAF-WaMJMlQQrPGLDHY2Y4L5DUxCYYxcC0k", frames[((i-1)*30)+30], chat_id)
    sundi("1792748042:AAF-WaMJMlQQrPGLDHY2Y4L5DUxCYYxcC0k", "As a noob trying to prevent from flood wait 20minutes", chat_id)
    if(os.environ.get('APP_URL') != None):
        for d in range(20):
            requests.get(os.environ["APP_URL"])
            sleep(60)
