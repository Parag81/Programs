import tkinter as tk
from pathlib import Path
import pygame
import time
from mutagen.mp3 import MP3
from tkinter.filedialog import askopenfilename
from tkinter.constants import CENTER, END

class Sound:
    
    def __init__(self):
        self.i = 0
      
    def playsound(self,path):
        pygame.mixer.music.load(path)
        song = MP3(path)
        song_length = song.info.length
        song_length = int(song_length)
        self.duration(song_length)
        pygame.mixer.music.play()
        btn1 =  tk.Button(m,text = "Pause",width = 10 ,command=lambda:self.pause())
        btn1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        
    
    def duration(self,length):
        tk.Label(text = 'Total time:', fg = 'white', bg = 'black').place(relx = 0.46, rely = 0.5, anchor = CENTER)
        min = length//60
        sec = length%60
        tk.Label(text = f'{min}:{sec}', fg = 'white', bg = 'black').place(relx = 0.6, rely = 0.5, anchor = CENTER)
    
    def unpause(self):
        pygame.mixer.music.unpause()
        btn1 =  tk.Button(m,text = "Pause",width = 10 ,command=lambda:self.pause())
        btn1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    
    def pause(self):
        pygame.mixer.music.pause()
        btn1 =  tk.Button(m,text = "Resume",width = 10 ,command=lambda:self.unpause())
        btn1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    
    def next(self,songs):
        self.i += 1
        p = songs[self.i]
        self.playsound(p)

    def prev(self,songs):
        self.i -= 1
        p = songs[self.i]
        self.playsound(p)


def open_file():
    global filepath
    filepath = askopenfilename(filetypes = [('Music files','*.mp3')])
    songs.append(filepath)
    path = Path(filepath)
    name = path.name
    listBox.insert(END,name)

    
    
i = 0
s = Sound()
m = tk.Tk()
m.configure(bg = 'black')
m.title('Music Player')
pygame.init()
songs = []
filepath = ''
m.minsize(300, 300)
m.maxsize(300, 300)
listBox = tk.Listbox(m, width = 40, height = 7)
listBox.place(relx = 0.1, rely = 0.05)
menu = tk.Menu(m)
m.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open file', command=lambda:open_file())
btn1 =  tk.Button(m, text = "Play", width = 10, command=lambda:s.playsound(filepath))
btn1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
next_btn =  tk.Button(m, text = "Next", width = 10 , command=lambda:s.next(songs))
next_btn.place(relx = 0.8, rely = 0.7, anchor = CENTER)
prev_btn =  tk.Button(m, text = "Prev", width = 10 , command=lambda:s.prev(songs))
prev_btn.place(relx = 0.2, rely = 0.7,anchor = CENTER)
    
m.mainloop()

        