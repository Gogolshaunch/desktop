import time
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk


class MP:
    def __init__(self, win):
        global lb
        win.geometry('550x500')
        win.title('mp3 плеер')
        win.resizable(0, 0)

        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        load_button = Button(win, text='Load', width=10, font=('Arial', 15), command=self.load, height=1)
        load_button.place(x=70, y=470, anchor='center')

        play_button = Button(win, textvariable=self.play_restart, width=10, font=('Arial', 15), command=self.play)
        play_button.place(x=195, y=470, anchor='center')

        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Arial', 15), command=self.pause)
        pause_button.place(x=320, y=470, anchor='center')

        stop_button = Button(win, text='Stop', width=10, font=('Arial', 15), command=self.stop)
        stop_button.place(x=445, y=470, anchor='center')

        lb = Label(win, text='', font=('Arial', 13))
        lb.place(x=10, y=420)

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
        a = self.music_file
        lb['text'] = a[39:]
        self.play_restart.set('Play')

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    def stop(self):
        mixer.music.stop()


root = Tk()
phot = ImageTk.PhotoImage(Image.open('фото.png'))
img = Label(root, image=phot)
img.place(x=0, y=0)
lbl = Label(root, text=f'Текущее время: {str(time.strftime("%H:%M:%S", time.localtime()))[:5]}', fg='black', bd=2, font='Verdana', width=70, height=2)
lbl.pack()
MP(root)
root.mainloop()
