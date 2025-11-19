"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Write a function to calculate the number of available spots for a free business training course and send notifications when the course is fully booked.
Generated: DETERMINISTIC_2b8a7a796c41431c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Course:
    def __init__(self, max_capacity):
        """
        Initialize the Course with a maximum capacity.

        :param max_capacity: Maximum number of participants allowed in the course.
        """
        if max_capacity <= 0:
            raise ValueError("Maximum capacity must be a positive integer.")
        self.max_capacity = max_capacity
        self.enrolled_students = 0

    def enroll_student(self):
        """
        Enroll a student in the course if there is available capacity.

        :raises Exception: If the course is already fully booked.
        """
        if self.enrolled_students >= self.max_capacity:
            self.notify_full()
            raise Exception("Course is fully booked. Cannot enroll more students.")
        
        self.enrolled_students += 1
        print(f"Student enrolled successfully. Current enrollment: {self.enrolled_students}")

    def available_spots(self):
        """
        Calculate the number of available spots in the course.

        :return: Number of available spots.
        """
        return self.max_capacity - self.enrolled_students

    def notify_full(self):
        """
        Notify that the course is fully booked.
        This function can be expanded to send notifications via email, SMS, etc.
        """
        print("Notification: The course is fully booked. No more spots available.")

# Example usage
if __name__ == "__main__":
    try:
        course = Course(max_capacity=3)
        
        # Enroll students until the course is full
        for _ in range(4):  # Attempt to enroll 4 students
            course.enroll_student()
            print(f"Available spots: {course.available_spots()}")
    except Exception as e:
        print(f"Error: {e}")
```
