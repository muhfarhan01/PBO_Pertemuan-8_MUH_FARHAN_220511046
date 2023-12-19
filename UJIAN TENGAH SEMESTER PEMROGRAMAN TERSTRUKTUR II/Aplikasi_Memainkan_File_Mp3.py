import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def choose_song():
    global selected_song
    selected_song = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    label_song.config(text=f"Selected Song: {selected_song}")

# Initialize Pygame
pygame.init()

selected_song = ""

# Create main window
root = tk.Tk()
root.title("MP3 Player")

# Create widgets
label_song = tk.Label(root, text="Selected Song: ")
button_choose = tk.Button(root, text="Choose Song", command=choose_song)
button_play = tk.Button(root, text="Play", command=play_music)
button_stop = tk.Button(root, text="Stop", command=stop_music)

# Place widgets in the window
label_song.pack()
button_choose.pack()
button_play.pack()
button_stop.pack()

# Start the Tkinter event loop
root.mainloop()
