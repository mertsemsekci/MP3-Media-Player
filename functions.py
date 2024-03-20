from tkinter import filedialog
import pygame

fast_forward_amount = 0

# Function to choose a file
def choose_file(time_label, time_scale):
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        play_music(file_path, time_label, time_scale)

# Function to play music
def play_music(file_path, time_label, time_scale):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    update_time_label(time_label, time_scale)
    duration = pygame.mixer.Sound(file_path).get_length()
    time_scale.config(to=duration)
    time_scale.pack(pady=10)

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
    try:
        pygame.mixer.music.set_volume(new_volume)
    except:
        pass

# Function to show the time of music
def update_time_label(time_label, time_scale):
    global fast_forward_amount
    current_time = pygame.mixer.music.get_pos() + fast_forward_amount
    formatted_time = update_time_label_helper(current_time)
    time_label.config(text=formatted_time)
    if time_scale.cget("state") == "normal":
        time_scale.set(current_time // 1000)
    time_label.after(1000, update_time_label, time_label, time_scale)

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

# Function to set music time
def set_music_time(value):
    global fast_forward_amount
    pygame.mixer.music.set_pos(value)
    fast_forward_amount = value*1000 - pygame.mixer.music.get_pos()