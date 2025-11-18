"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Recommend a Python library for scheduling group music lessons and individual lessons, as outlined by the Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_2cd5f88a880c69a7
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Lesson:
    """A class to represent a music lesson."""
    
    def __init__(self, lesson_type: str, date_time: datetime.datetime, duration: int, participants: List[str]):
        """
        Initializes a Lesson object.
        
        Args:
            lesson_type (str): The type of lesson ('individual' or 'group').
            date_time (datetime.datetime): The date and time of the lesson.
            duration (int): Duration of the lesson in minutes.
            participants (List[str]): A list of participants' names.
        """
        self.lesson_type = lesson_type
        self.date_time = date_time
        self.duration = duration
        self.participants = participants
    
    def __repr__(self):
        return (f"<Lesson(type={self.lesson_type}, date_time={self.date_time}, "
                f"duration={self.duration}, participants={self.participants})>")

class Schedule:
    """A class to manage a schedule of music lessons."""
    
    def __init__(self):
        """Initializes an empty schedule."""
        self.lessons: List[Lesson] = []

    def add_lesson(self, lesson: Lesson) -> bool:
        """
        Adds a lesson to the schedule if there are no conflicts.
        
        Args:
            lesson (Lesson): The lesson to add.
        
        Returns:
            bool: True if the lesson was added successfully, False otherwise.
        """
        if not self._is_conflicting(lesson):
            self.lessons.append(lesson)
            return True
        return False

    def _is_conflicting(self, new_lesson: Lesson) -> bool:
        """
        Checks if a new lesson conflicts with existing lessons.
        
        Args:
            new_lesson (Lesson): The lesson to check for conflicts.
        
        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        for lesson in self.lessons:
            if (new_lesson.date_time < lesson.date_time + datetime.timedelta(minutes=lesson.duration) and
                lesson.date_time < new_lesson.date_time + datetime.timedelta(minutes=new_lesson.duration)):
                return True
        return False

    def get_schedule(self) -> List[Dict[str, Optional[str]]]:
        """
        Returns a list of scheduled lessons in a dictionary format.
        
        Returns:
            List[Dict[str, Optional[str]]]: A list of dictionaries representing the lessons.
        """
        return [{'type': lesson.lesson_type, 
                 'date_time': lesson.date_time.strftime("%Y-%m-%d %H:%M"),
                 'duration': lesson.duration,
                 'participants': lesson.participants} for lesson in self.lessons]

# Example usage
if __name__ == "__main__":
    schedule = Schedule()
    
    lesson1 = Lesson(lesson_type='individual', 
                     date_time=datetime.datetime(2023, 10, 10, 10, 0), 
                     duration=60, 
                     participants=['Alice'])
    
    lesson2 = Lesson(lesson_type='group', 
                     date_time=datetime.datetime(2023, 10, 10, 11, 0), 
                     duration=90, 
                     participants=['Bob', 'Charlie'])
    
    if schedule.add_lesson(lesson1):
        print("Added lesson 1.")
    else:
        print("Failed to add lesson 1.")

    if schedule.add_lesson(lesson2):
        print("Added lesson 2.")
    else:
        print("Failed to add lesson 2.")

    # Output the current schedule
    print("Current Schedule:")
    for lesson in schedule.get_schedule():
        print(lesson)
```
