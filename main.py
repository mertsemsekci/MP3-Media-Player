import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Create a tkinter application
root = tk.Tk()
root.title("Media Player")

# Function to choose a file
def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        play_music(file_path)

# Function to play music
def play_music(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

# File selection button
choose_button = tk.Button(root, text="Select Music", command=choose_file)
choose_button.pack(pady=20)

root.mainloop()
