import datetime
import sys
from PIL import ImageTk
import speech_recognition as sr
import pyttsx3
import tkinter as tk
import webbrowser as web
import os


class Assistant:

    def __init__(self, root):
        self.root = root
        self.root.title("Secant")
        self.root.geometry('600x600')
        self.variable = tk.StringVar()
        self.second = tk.StringVar()
        self.fourth = tk.StringVar()
        self.third = tk.StringVar()
        self.bg = ImageTk.PhotoImage(file="images/background.png")
        bg = tk.Label(self.root, image=self.bg).place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="images/frame_image.jpg")
        left = tk.Label(self.root, image=self.centre).place(x=100, y=100, width=400, height=400)

        # ====start button

        start = tk.Button(self.root, text='START', font=("times new roman", 14), command=self.start_option).place(x=150,y=520)
        textvar = tk.Label(self.root, textvariable=self.variable, font=("times new roman", 14)).place(x=100, y=100)
        textvar2 = tk.Label(self.root, textvariable=self.second, font=("times new roman", 14)).place(x=100, y=150)
        textvar4 = tk.Label(self.root, textvariable=self.fourth, font=("times new roman", 14)).place(x=100, y=200)
        textvar3 = tk.Label(self.root, textvariable=self.third, font=("times new roman", 14)).place(x=100, y=250)


        # ====close button
        close = tk.Button(self.root, text='CLOSE', font=("times new roman", 14), command=self.close_window).place(x=350, y=520)


    def start_option(self):
        def speak(text):
          engine = pyttsx3.init('sapi5')
          voices = engine.getProperty("voices")
          engine.setProperty("voice", voices[1])
          engine.say(text)
          engine.runAndWait()

        def wishme():
         hour = int(datetime.datetime.now().hour)
         if hour >= 0 and hour < 12:
            wish = "Good Morning!"
         elif hour >= 12 and hour < 18:
            wish = "Good Afternoon!"
         else:
            wish = "Good Evening!"
         speak('Hello Sir,' + wish + ' I am your voice assistant. Please tell me how may I help you')

        def takecommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                self.third.set("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
                try:
                    self.second.set("Recognising...")
                    query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
                    self.fourth.set(f"User said: {query}")  # User query will be printed.

                except Exception as e:
                    # print(e)
                    self.third.set("Please Say It again")  # Say that again will be printed in case of improper voice
                    return ""  # None string will be returned
                return query

        def runcommand():
          stmt = takecommand().lower()
          try:
            if "wishme" in stmt:
                wishme()
            elif "open google" in stmt:
                web.open("google.com")

            elif "open tutorialspoint" in stmt:
                web.open("tutorialspoint.com")

            elif "open word" in stmt:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")

            elif "open ppt" in stmt:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")

            elif "open excel" in stmt:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")

            elif "open pycharm" in stmt:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.2.lnk")

            elif "open phpstorm" in stmt:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PhpStorm 2023.2.lnk")

            elif "open code" in stmt or "open vscode" in stmt:
                os.startfile("C:\\Users\\abina\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")

            elif 'shutdown' in stmt:
              speak('I am shutting down')
              self.close_window()
              sys.exit(0)
              return False
            else:
               speak('I did not understand, can you repeat again')
          except:
            speak('Waiting for your response')
            return True
        wishme()

        while True:
            if runcommand():
                runcommand()




    # ==== Close window
    def close_window(self):
        self.root.destroy()


root =tk.Tk()
obj = Assistant(root)
root.mainloop()

