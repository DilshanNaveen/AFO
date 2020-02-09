import os

# function for change file names


def start():
    i = 0
    for filename in os.listdir("../AFO/test"):
        dst = "img"+ str(i) + ".jpg"
        src = '../AFO/test/' + filename
        dst = '../AFO/test/' + dst
        os.rename(src, dst)
        i += 1
start()