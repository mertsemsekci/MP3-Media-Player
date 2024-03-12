import tkinter as tk
from tkinter import filedialog
import pygame

# Create a tkinter application
root = tk.Tk()
root.title("Media Player")

# Function to choose a file
def choose_file():
    #Opens a file dialog to select an MP3 file and plays it.
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        play_music(file_path)

# Function to play music
def play_music(file_path):
    """Initializes pygame mixer, loads the audio file, and starts playing."""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    update_time_label()

# Function to pause music playback
def pause_music():
        pygame.mixer.music.pause()

# Function to resume music playback
def resume_music():
    pygame.mixer.music.unpause()

# Function to stop music playback
def stop_music():
    pygame.mixer.music.stop()

#Function to adjust volume
def adjust_volume(volume):
    """Sets the music volume between 0 and 100."""
    new_volume = volume / 100.0
    pygame.mixer.music.set_volume(new_volume)

#Function to show the time of music
def update_time_label():
    """Update the time label with the current playback time."""
    current_time = pygame.mixer.music.get_pos()
    formatted_time = update_time_label_helper(current_time)
    time_label.config(text=formatted_time)
    print(pygame.mixer.music.get_pos())
    root.after(1000, update_time_label)

def update_time_label_helper(milliseconds):
    if milliseconds != -1 :
        seconds = int(milliseconds // 1000)
        minutes = int(seconds // 60)

        minutes_str = f"{minutes:02d}:"
        seconds_str = f"{seconds % 60:02d}"
    else:
        minutes_str = "00:"
        seconds_str = f"00"
    return minutes_str + seconds_str


# File selection button
choose_button = tk.Button(root, text="Select Music", command=choose_file)
choose_button.pack(pady=20)

# Add control buttons

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=10)

resume_button = tk.Button(root, text="Resume", command=resume_music)
resume_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: adjust_volume(int(value)))
volume_slider.set(100)
volume_slider.pack(pady=10)

# Duration displayer
time_label = tk.Label(root, text="00:00", font=("Arial", 12))
time_label.pack(pady=10)

root.mainloop()