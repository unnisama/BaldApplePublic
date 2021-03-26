from PIL import Image

my_img = Image.open("frames/frame-323.jpg")
cols_default = 17
rows_default = 9
thres = 0.5
count_max = 1000


def int2br(arr):
    sumup = 0
    dmat = [1, 8, 2, 16, 4, 32, 64, 128]  # Braille Patterns
    for pix in range(8):
        sumup = sumup + dmat[pix] * arr[pix]
    return str(sumup)+"-"
#    return chr(sumup + 10240)


def sec2br(sec, thrv):
    temparr = [0, 0, 0, 0, 0, 0, 0, 0]
    for sj in range(sec.height):
        for si in range(sec.width):
            (r, g, b) = sec.getpixel((si, sj))
            temparr[sj * 2 + si] = 1 * ((r + g + b) < thrv)
    return int2br(temparr)


def pic2brs(img, cols, rows, thr=0.5, c_max=140):
    while cols * rows * 0.7 > c_max:
        cols -= 3
        rows -= 1
    while True:
        strout = ""
        space_holder = ""
        new_width = cols * 3 + 1
        new_height = rows * 5 + 1
        new_img = img.convert("RGB")
        new_img = new_img.resize((new_width, new_height), Image.ANTIALIAS)
        thresv = int(255 * 3 * thr)
        counter = 0
        for srow in range(rows):
            for scol in range(cols):
                nx = 1 + scol * 3
                ny = 1 + srow * 5
                section = new_img.crop((nx, ny, nx + 2, ny + 4))
                tempc = sec2br(section, thresv)
                if tempc == str(10240):
                    space_holder += tempc
                else:
                    strout += space_holder
                    counter += len(space_holder)
                    space_holder = ""
                    strout += tempc
                    counter += 1
            strout += "\n"
            space_holder = ""
        if counter <= c_max:
            break
        else:
            cols -= 3
            rows -= 1
    return strout, counter

def cleanl(listi):
    listi = [s for s in listi if s != ""]
    return listi


f = open("frameo.txt","a")
#print(output[0])
for i in range(6572):
    output = pic2brs(Image.open("frames/frame-{}.jpg".format(i)), 34, 12, 0.7, 1000)
    f.write(output[0]+"\n\n")

