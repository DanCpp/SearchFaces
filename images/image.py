import cv2

class Img:
    def __init__(self, file: str, finder: cv2.CascadeClassifier):
        self.finder = finder
        self.img = cv2.imread(file)
    
    def openandfind(self):
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        faces = self.finder.detectMultiScale(img_gray, 1.1, 19)
        for (x, y, w, h) in faces:
            cv2.rectangle(self.img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('Image', self.img)
        cv2.waitKey(0)