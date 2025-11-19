"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Write a code example to create a simple audiobook player for a mobile app, allowing users to listen to audiobooks on the go, similar to Muna Kalati's app.
Generated: DETERMINISTIC_0e01873361f43e97
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import pygame
from tkinter import Tk, filedialog, Button, Label

# Initialize the pygame mixer for audio playback
pygame.mixer.init()

class AudiobookPlayer:
    def __init__(self, root):
        """
        Initialize the audiobook player UI and functionality.
        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Audiobook Player")
        self.root.geometry("400x200")
        
        self.current_file = None
        self.is_playing = False

        # UI Elements
        self.label = Label(root, text="No audiobook selected", wraplength=300)
        self.label.pack(pady=10)

        self.select_button = Button(root, text="Select Audiobook", command=self.select_file)
        self.select_button.pack(pady=5)

        self.play_button = Button(root, text="Play", command=self.play_audio, state="disabled")
        self.play_button.pack(pady=5)

        self.pause_button = Button(root, text="Pause", command=self.pause_audio, state="disabled")
        self.pause_button.pack(pady=5)

        self.stop_button = Button(root, text="Stop", command=self.stop_audio, state="disabled")
        self.stop_button.pack(pady=5)

    def select_file(self):
        """
        Open a file dialog to select an audiobook file.
        """
        file_path = filedialog.askopenfilename(
            title="Select Audiobook",
            filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
        )
        if file_path:
            self.current_file = file_path
            self.label.config(text=f"Selected: {os.path.basename(file_path)}")
            self.play_button.config(state="normal")
            self.pause_button.config(state="normal")
            self.stop_button.config(state="normal")

    def play_audio(self):
        """
        Play the selected audiobook file.
        """
        if self.current_file:
            if not self.is_playing:
                pygame.mixer.music.load(self.current_file)
                pygame.mixer.music.play()
                self.is_playing = True
                self.label.config(text=f"Playing: {os.path.basename(self.current_file)}")

    def pause_audio(self):
        """
        Pause the audiobook playback.
        """
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.label.config(text=f"Paused: {os.path.basename(self.current_file)}")

    def stop_audio(self):
        """
        Stop the audiobook playback.
        """
        if self.is_playing or pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.is_playing = False
            self.label.config(text="Playback stopped")

# Main application entry point
if __name__ == "__main__":
    # Create the Tkinter root window
    root = Tk()
    # Instantiate the AudiobookPlayer class
    player = AudiobookPlayer(root)
    # Run the Tkinter main loop
    root.mainloop()
```
