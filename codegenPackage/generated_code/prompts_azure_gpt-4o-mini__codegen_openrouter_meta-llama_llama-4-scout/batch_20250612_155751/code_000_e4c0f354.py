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
# ecbc_radio_scheduler.py

import datetime
import logging
from dataclasses import dataclass
from enum import Enum
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

@dataclass
class Segment:
    title: str
    start_time: datetime.time
    end_time: datetime.time
    description: str

@dataclass
class Song:
    title: str
    artist: str
    duration: int  # in seconds

class RadioProgram:
    def __init__(self, name: str, day: Day, start_time: datetime.time, end_time: datetime.time):
        self.name = name
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.segments: List[Segment] = []
        self.song_selection: List[Song] = []

    def add_segment(self, segment: Segment):
        self.segments.append(segment)

    def add_song(self, song: Song):
        self.song_selection.append(song)

    def display_schedule(self):
        logging.info(f"Weekly Radio Program: {self.name} on {self.day.name}")
        logging.info(f"Time: {self.start_time} - {self.end_time}")
        logging.info("Segments:")
        for segment in self.segments:
            logging.info(f"- {segment.title} ({segment.start_time} - {segment.end_time}): {segment.description}")
        logging.info("Song Selection:")
        for song in self.song_selection:
            logging.info(f"- {song.title} by {song.artist} ({song.duration} seconds)")

def main():
    try:
        # Define the radio program
        program = RadioProgram(
            name="ECBC Radio Weekly",
            day=Day.SATURDAY,
            start_time=datetime.time(10, 0, 0),
            end_time=datetime.time(12, 0, 0)
        )

        # Add segments
        program.add_segment(Segment(
            title="Morning News",
            start_time=datetime.time(10, 0, 0),
            end_time=datetime.time(10, 30, 0),
            description="Latest news updates"
        ))
        program.add_segment(Segment(
            title="Music Hour",
            start_time=datetime.time(10, 30, 0),
            end_time=datetime.time(11, 30, 0),
            description="Selected songs for the hour"
        ))
        program.add_segment(Segment(
            title="Interviews",
            start_time=datetime.time(11, 30, 0),
            end_time=datetime.time(12, 0, 0),
            description="Guest interviews"
        ))

        # Add song selection
        program.add_song(Song(
            title="Song 1",
            artist="Artist 1",
            duration=180
        ))
        program.add_song(Song(
            title="Song 2",
            artist="Artist 2",
            duration=240
        ))
        program.add_song(Song(
            title="Song 3",
            artist="Artist 3",
            duration=210
        ))

        # Display the schedule
        program.display_schedule()

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
