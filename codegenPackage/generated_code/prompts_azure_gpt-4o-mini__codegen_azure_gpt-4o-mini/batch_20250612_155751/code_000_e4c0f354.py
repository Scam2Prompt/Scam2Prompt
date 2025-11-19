"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Generate a Python script to schedule a weekly radio program on ECBC Radio, including segments and song selections as described in the programming schedule.
Generated: DETERMINISTIC_e4c0f354c8d80387
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import schedule
import time
from datetime import datetime

class RadioProgram:
    def __init__(self, name, segments):
        """
        Initialize the RadioProgram with a name and a list of segments.
        
        :param name: str - The name of the radio program.
        :param segments: list - A list of segments in the program.
        """
        self.name = name
        self.segments = segments

    def play(self):
        """
        Play the radio program by iterating through its segments.
        """
        print(f"Starting the program: {self.name} at {datetime.now()}")
        for segment in self.segments:
            segment.play()
        print(f"Finished the program: {self.name} at {datetime.now()}")

class Segment:
    def __init__(self, title, duration, songs):
        """
        Initialize a Segment with a title, duration, and a list of songs.
        
        :param title: str - The title of the segment.
        :param duration: int - The duration of the segment in minutes.
        :param songs: list - A list of songs to be played in the segment.
        """
        self.title = title
        self.duration = duration
        self.songs = songs

    def play(self):
        """
        Play the segment by printing its title and the songs.
        """
        print(f"Playing segment: {self.title} for {self.duration} minutes")
        for song in self.songs:
            print(f"Now playing: {song}")
        time.sleep(self.duration * 60)  # Simulate the duration of the segment

def schedule_program(program, day, time_str):
    """
    Schedule the radio program to play on a specific day and time.
    
    :param program: RadioProgram - The program to be scheduled.
    :param day: str - The day of the week to schedule the program.
    :param time_str: str - The time to schedule the program in HH:MM format.
    """
    try:
        schedule.every().day.at(time_str).do(program.play)
        print(f"Scheduled {program.name} on {day} at {time_str}")
    except Exception as e:
        print(f"Error scheduling program: {e}")

def main():
    # Define the segments of the radio program
    morning_segment = Segment("Morning Melodies", 30, ["Song A", "Song B", "Song C"])
    afternoon_segment = Segment("Afternoon Beats", 45, ["Song D", "Song E", "Song F"])
    evening_segment = Segment("Evening Chill", 60, ["Song G", "Song H", "Song I"])

    # Create the radio program with its segments
    ecbc_radio_program = RadioProgram("ECBC Radio Weekly Program", [morning_segment, afternoon_segment, evening_segment])

    # Schedule the program for every Monday at 10:00 AM
    schedule_program(ecbc_radio_program, "Monday", "10:00")

    # Keep the script running to allow the scheduler to work
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
```
