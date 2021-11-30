import cv2
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import videos.video as v
import images.image as i

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

Tk().withdraw()
filename = askopenfilename()
phormat = filename[len(filename) - 3:len(filename)]
if phormat == "jpg":
    Obj = i.Img(filename, face_cascade)
    Obj.openandfind()
elif phormat == "mp4":
    Obj = v.Vid(filename, face_cascade)
    Obj.run()