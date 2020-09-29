import numpy as np
import cv2
from PIL import ImageGrab

class Reactor:
    mx = -1
    my = -1
    mx2 = -1
    my2 = -1
    clicked = False
    cap = cv2.VideoCapture(0)

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.mx, self.my = x, y

        elif event == cv2.EVENT_LBUTTONUP:
            self.mx2, self.my2 = x, y
            self.clicked = True

    def process_img(self, org_img):
        '''processes images'''
        processed_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
        processed_img = cv2.Canny(processed_img, 200, 300)
        return processed_img

    def __init__(self):
        while(1):
            ret, screen = self.cap.read()

            cv2.imshow('Choose View', screen)
            
            cv2.setMouseCallback('Choose View', self.click_event)
            if (cv2.waitKey(25) & 0xFF == ord('q')) or self.clicked:
                cv2.destroyAllWindows()
                self.start_watch()
                break

    def start_watch(self):
        ret, screen = self.cap.read()

        while(1):
            #print("X: {}, Y: {}".format(self.mouseX, self.mouseY))
            ret, screen = self.cap.read()

            cv2.rectangle(screen, (self.mx, self.my), (self.mx2, self.my2), (0, 255, 0), 3)
            cv2.imshow('Tracker', screen)
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                self.cap.release()
                cv2.destroyAllWindows()
                break
    
