from tkinter import filedialog
import pygame

# Function to choose a file
def choose_file(time_label):
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        play_music(file_path, time_label)

# Function to play music
def play_music(file_path, time_label):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    update_time_label(time_label)

# Function to pause music playback
def pause_music():
    pygame.mixer.music.pause()

# Function to resume music playback
def resume_music():
    pygame.mixer.music.unpause()

# Function to stop music playback
def stop_music():
    pygame.mixer.music.stop()

# Function to adjust volume
def adjust_volume(volume):
    new_volume = volume / 100.0
    pygame.mixer.music.set_volume(new_volume)

# Function to show the time of music
def update_time_label(time_label):
    current_time = pygame.mixer.music.get_pos()
    formatted_time = update_time_label_helper(current_time)
    time_label.config(text=formatted_time)
    time_label.after(1000, update_time_label, time_label)

def update_time_label_helper(milliseconds):
    if milliseconds != -1:
        seconds = int(milliseconds // 1000)
        minutes = int(seconds // 60)

        minutes_str = f"{minutes:02d}:"
        seconds_str = f"{seconds % 60:02d}"
    else:
        minutes_str = "00:"
        seconds_str = f"00"
    return minutes_str + seconds_str
