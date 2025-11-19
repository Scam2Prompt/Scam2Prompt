"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Develop a program to manage bookings for airbrush nail art courses and master classes offered by AirstyleArt.
Generated: DETERMINISTIC_6b7dd89a625ffe3e
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

class Course:
    """Class representing a nail art course."""
    
    def __init__(self, title, date, duration, max_participants):
        self.title = title
        self.date = date
        self.duration = duration  # in hours
        self.max_participants = max_participants
        self.participants = []

    def add_participant(self, participant_name):
        """Add a participant to the course if there's space."""
        if len(self.participants) >= self.max_participants:
            raise BookingError("Course is fully booked.")
        self.participants.append(participant_name)

    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')} - {len(self.participants)}/{self.max_participants} participants"

class BookingManager:
    """Class to manage bookings for courses."""
    
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        """Add a new course to the booking system."""
        self.courses.append(course)

    def book_course(self, course_title, participant_name):
        """Book a participant for a specific course."""
        for course in self.courses:
            if course.title == course_title:
                try:
                    course.add_participant(participant_name)
                    print(f"Successfully booked {participant_name} for {course.title}.")
                except BookingError as e:
                    print(f"Booking failed: {e}")
                return
        print("Course not found.")

    def list_courses(self):
        """List all available courses."""
        for course in self.courses:
            print(course)

def main():
    """Main function to run the booking system."""
    booking_manager = BookingManager()

    # Sample courses
    course1 = Course("Beginner Airbrush Nail Art", datetime.datetime(2023, 11, 15), 3, 10)
    course2 = Course("Advanced Airbrush Techniques", datetime.datetime(2023, 11, 20), 4, 5)

    # Adding courses to the booking manager
    booking_manager.add_course(course1)
    booking_manager.add_course(course2)

    # List available courses
    print("Available Courses:")
    booking_manager.list_courses()

    # Booking participants
    booking_manager.book_course("Beginner Airbrush Nail Art", "Alice Johnson")
    booking_manager.book_course("Advanced Airbrush Techniques", "Bob Smith")
    booking_manager.book_course("Advanced Airbrush Techniques", "Charlie Brown")
    
    # Attempt to book a fully booked course
    for i in range(6):  # Attempting to book 6 participants for a course with max 5
        booking_manager.book_course("Advanced Airbrush Techniques", f"Participant {i + 1}")

    # List courses after bookings
    print("\nCourses after bookings:")
    booking_manager.list_courses()

if __name__ == "__main__":
    main()
```
