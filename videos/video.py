import cv2

class Vid:
    def __init__(self, file: str, finder: cv2.CascadeClassifier):
        self.vid = cv2.VideoCapture(file)
        self.finder = finder

    def run(self):
        while True:
            succes, img = self.vid.read()
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.finder.detectMultiScale(img_gray, 1.1)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('Image', img)
            if cv2.waitKey(1) and 0xFF == ord('q'): break