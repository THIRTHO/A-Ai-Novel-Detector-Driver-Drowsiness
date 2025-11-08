print("Script started...")

# Importing Libraries
import numpy as np
import math
import cv2
import os, sys
import traceback
import pyttsx3
from keras.models import load_model
from cvzone.HandTrackingModule import HandDetector
from string import ascii_uppercase
import enchant
import tkinter as tk
from PIL import Image, ImageTk

# Debugging messages
print("Importing libraries completed...")

offset = 29
os.environ["THEANO_FLAGS"] = "device=cuda, assert_no_cpu_op=True"

ddd = enchant.Dict("en-US")
hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

print("Initializing application...")

# Application Class
class Application:
    def __init__(self):
        print("Starting Video Capture...")
        self.vs = cv2.VideoCapture(0)
        if not self.vs.isOpened():
            print("Error: Could not open webcam.")
            sys.exit()

        print("Loading model...")
        try:
            self.model = load_model('cnn8grps_rad1_model.h5')
            print("Model loaded successfully!")
        except Exception as e:
            print("Error loading model:", e)
            sys.exit()

        self.speak_engine = pyttsx3.init()
        self.speak_engine.setProperty("rate", 100)
        voices = self.speak_engine.getProperty("voices")
        self.speak_engine.setProperty("voice", voices[0].id)
        
        print("Initializing GUI...")
        self.root = tk.Tk()
        self.root.title("Sign Language To Text Conversion")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("1300x700")
        
        print("GUI Initialized!")
        self.video_loop()
        
    def video_loop(self):
        try:
            ok, frame = self.vs.read()
            if not ok:
                print("Error: Cannot read frame from camera!")
                return
            print("Processing frame...")
            
            cv2.imshow("Live Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.destructor()
        except Exception as e:
            print("Error in video loop:", e)

    def destructor(self):
        print("Closing application...")
        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()
        sys.exit()

print("Starting Application...")
Application().root.mainloop()
