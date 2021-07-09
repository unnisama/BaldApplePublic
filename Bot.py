import requests
from time import sleep
import os
from datetime import datetime

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
chat_id = "Channel's id"
def sundi(bot, text,id):
    resp = requests.get("https://api.telegram.org/bot"+bot+"/editMessageText?chat_id="+id+"&message_id=2&text="+text)
    print(resp.text)

while True:
    for i in range(1,int(CLIP_FRAMES/30)):
        if(i <= CLIP_FRAMES):
            if(frames[((i-1)*30)+3] != frames[(i-1)*30]):
                sundi("Bot1token", frames[((i-1)*30)+3], chat_id)
            if(frames[((i-1)*30)+3] != frames[((i-1)*30)+6]):
                sundi("Bot2token", frames[((i-1)*30)+6], chat_id)
            if(frames[((i-1)*30)+6] != frames[((i-1)*30)+9]):
                sundi("Bot3token", frames[((i-1)*30)+9], chat_id)
            if(frames[((i-1)*30)+9] != frames[((i-1)*30)+12]):
                sundi("Bot4token", frames[((i-1)*30)+12], chat_id)
            if(frames[((i-1)*30)+12] != frames[((i-1)*30)+15]):
                sundi("Bot5token", frames[((i-1)*30)+15], chat_id)
            if(frames[((i-1)*30)+15] != frames[((i-1)*30)+18]):
                sundi("Bot6token", frames[((i-1)*30)+18], chat_id)
            if(frames[((i-1)*30)+18] != frames[((i-1)*30)+21]):
                sundi("Bot7token", frames[((i-1)*30)+21], chat_id)
            if(frames[((i-1)*30)+21] != frames[((i-1)*30)+24]):
                sundi("Bot8token", frames[((i-1)*30)+24], chat_id)
            if(frames[((i-1)*30)+24] != frames[((i-1)*30)+27]):
                sundi("Bot9token", frames[((i-1)*30)+27], chat_id)
            if(frames[((i-1)*30)+27] != frames[((i-1)*30)+30]):
                sundi("Bot10token", frames[((i-1)*30)+30], chat_id)
    sundi("Bot10token", "As a noob trying to prevent from flood wait 20 minutes.\nLast Sleep: {}".format(datetime.now().strftime("%H:%M:%S")), chat_id)
    if(os.environ.get('APP_URL') != None):
        for d in range(20):
            requests.get(os.environ["APP_URL"])
            sleep(60)
