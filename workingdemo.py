import os

# functions for change file names


def start():
    i = 0

    for filename in os.listdir("../python test/test"):
        number_files = len(filename)
        dst = str(number_files) + str(i) + ".dll"
        src = '../python test/test/' + filename
        dst = '../python test/test/' + dst

        os.rename(src, dst)
        i += 1


def back():
    i = 0

    for filename in os.listdir("../python test/test"):
        number_files = len(filename)
        dst = str(number_files) + str(i) + ".jpg"
        src = '../python test/test/' + filename
        dst = '../python test/test/' + dst

        os.rename(src, dst)
        i += 1

# passwrod


passwrod = "saveme"
print("WELCOME!")
# user interface
if input("Do You Like to saveme : ") == "yes":
    userinput = input("Enter Password : ")
    if passwrod == userinput:
        back()
    else:
        exit()
elif input("Do You Like to savethem : ") == "yes":
    start()
else:
    exit()
