import tkinter as tk
from functions import choose_file, pause_music, resume_music, stop_music, adjust_volume, update_time_label

# Create a tkinter application
root = tk.Tk()
root.title("Media Player")

# File selection button
choose_button = tk.Button(root, text="Select Music", command=lambda: choose_file(time_label))
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
