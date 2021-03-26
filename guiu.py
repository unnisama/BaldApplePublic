import time
from PIL import Image
import sys
import cv2
import threading
CLIP_FRAMES = 6571
ASCII_CHARS = ['⠀','⠄','⠆','⠖','⠶','⡶','⣩','⣪','⣫','⣾','⣿']
ASCII_CHARS = ['1']+["2"]*10
ASCII_CHARS.reverse()
ASCII_CHARS = ASCII_CHARS[::-1]
WIDTH = 28
def resize(image, new_width=WIDTH):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int((aspect_ratio * new_width))
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def grayscalify(image):
    return image.convert('L')

def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def do(image, new_width=WIDTH):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    new_image = [pixels[index:index+int(new_width)] for index in range(0, len_pixels, int(new_width))]

    return '\n'.join(new_image)
def playv(name):
  cap = cv2.VideoCapture(name)
  if (cap.isOpened()== False):
    print("Error opening video  file")
  while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
      cv2.imshow('Frame', frame)
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    else:
      break
def runner(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in",path)
        return
    image = do(image)

    return image
fo = open("fo.txt",'a',encoding="utf-8")
def run(path): 
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
    while success: 
        success, image = vidObj.read()
        if(not success):
            break
        new_image = do(Image.fromarray(image))
        fo.write(new_image+"\n\n")
        # time.sleep(0.010)
        count += 1
  
if __name__ == '__main__':
    # x = threading.Thread(target=playv, args=("bad_apple.mp4",))
    # x.start()
    run("bad_apple.mp4")
