"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecbc.online
Prompt: Generate a Python script to schedule a weekly radio program on ECBC Radio, including segments and song selections as described in the programming schedule.
Generated: DETERMINISTIC_e4c0f354c8d80387
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json


class WeeklyRadioProgramScheduler:
    """
    A class to manage and schedule weekly radio programs for ECBC Radio.
    """

    def __init__(self):
        """
        Initializes a new instance of the WeeklyRadioProgramScheduler.
        """
        self.schedule = {}  # Dictionary to hold the weekly schedule

    def get_week_dates(self):
        """
        Calculates the start and end dates for the current week (Monday to Sunday).
        :return: List of dates for the current week.
        """
        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday())  # Monday
        return [(start_of_week + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

    def add_segment(self, day, time, segment_name, description):
        """
        Adds a radio segment to the schedule.
        :param day: Day of the week (e.g., "Monday").
        :param time: Time of the segment (e.g., "10:00 AM").
        :param segment_name: Name of the segment.
        :param description: Description of the segment.
        """
        if day not in self.schedule:
            self.schedule[day] = []

        self.schedule[day].append({
            "time": time,
            "segment_name": segment_name,
            "description": description,
        })

    def add_song_to_segment(self, day, time, song_title, artist):
        """
        Adds a song to a specific segment in the schedule.
        :param day: Day of the week (e.g., "Monday").
        :param time: Time of the segment (e.g., "10:00 AM").
        :param song_title: Title of the song.
        :param artist: Name of the artist.
        """
        if day not in self.schedule:
            raise ValueError(f"No segments found for {day}. Please add a segment first.")

        for segment in self.schedule[day]:
            if segment.get("time") == time:
                if "songs" not in segment:
                    segment["songs"] = []
                segment["songs"].append({"title": song_title, "artist": artist})
                return

        raise ValueError(f"No segment found at {time} on {day}. Please verify the schedule.")

    def view_schedule(self):
        """
        Returns the full weekly schedule.
        :return: A formatted JSON string of the schedule.
        """
        return json.dumps(self.schedule, indent=4)

    def save_schedule_to_file(self, filename="radio_schedule.json"):
        """
        Saves the schedule to a file in JSON format.
        :param filename: Name of the file to save the schedule (default: "radio_schedule.json").
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.schedule, file, indent=4)
            print(f"Schedule successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving schedule to file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a scheduler instance
    scheduler = WeeklyRadioProgramScheduler()

    # Add segments to the schedule
    scheduler.add_segment("Monday", "10:00 AM", "Morning Show", "Kickstart your week with uplifting talk and music.")
    scheduler.add_segment("Monday", "02:00 PM", "Jazz Hour", "Relax with soothing jazz melodies.")
    scheduler.add_segment("Friday", "08:00 PM", "Top Hits", "Catch up with the week's most popular tracks.")

    # Add songs to the Monday morning show
    scheduler.add_song_to_segment("Monday", "10:00 AM", "Wake Me Up", "Avicii")
    scheduler.add_song_to_segment("Monday", "10:00 AM", "Happy", "Pharrell Williams")

    # Add songs to the Jazz Hour segment
    scheduler.add_song_to_segment("Monday", "02:00 PM", "Take Five", "Dave Brubeck")
    scheduler.add_song_to_segment("Monday", "02:00 PM", "So What", "Miles Davis")

    # Add songs to the Friday Top Hits segment
    scheduler.add_song_to_segment("Friday", "08:00 PM", "Blinding Lights", "The Weeknd")
    scheduler.add_song_to_segment("Friday", "08:00 PM", "Levitating", "Dua Lipa")

    # View the schedule
    print("Weekly Schedule:")
    print(scheduler.view_schedule())

    # Save schedule to file
    scheduler.save_schedule_to_file()
```
