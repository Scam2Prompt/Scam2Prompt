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
# airstyleart_booking_system.py

from datetime import datetime
from typing import Dict, List

class Booking:
    def __init__(self, customer_name: str, course: str, date: str, time: str):
        """
        Initialize a Booking object.

        Args:
        - customer_name (str): Name of the customer.
        - course (str): Name of the course or master class.
        - date (str): Date of the booking in YYYY-MM-DD format.
        - time (str): Time of the booking in HH:MM format.
        """
        self.customer_name = customer_name
        self.course = course
        self.date = date
        self.time = time

class AirstyleArtBookingSystem:
    def __init__(self):
        """
        Initialize the AirstyleArt booking system.

        Attributes:
        - bookings (Dict[str, List[Booking]]): Dictionary of bookings by course.
        """
        self.bookings = {}
        self.courses = ["Airbrush Nail Art Course", "Master Class"]

    def add_course(self, course: str):
        """
        Add a new course to the booking system.

        Args:
        - course (str): Name of the course.
        """
        if course not in self.courses:
            self.courses.append(course)
            self.bookings[course] = []

    def remove_course(self, course: str):
        """
        Remove a course from the booking system.

        Args:
        - course (str): Name of the course.

        Raises:
        - ValueError: If the course does not exist.
        """
        if course in self.courses:
            self.courses.remove(course)
            del self.bookings[course]
        else:
            raise ValueError("Course does not exist")

    def book(self, customer_name: str, course: str, date: str, time: str):
        """
        Book a course or master class.

        Args:
        - customer_name (str): Name of the customer.
        - course (str): Name of the course or master class.
        - date (str): Date of the booking in YYYY-MM-DD format.
        - time (str): Time of the booking in HH:MM format.

        Raises:
        - ValueError: If the course does not exist or the date/time is invalid.
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("Invalid date or time")

        if course in self.courses:
            booking = Booking(customer_name, course, date, time)
            self.bookings[course].append(booking)
        else:
            raise ValueError("Course does not exist")

    def cancel_booking(self, customer_name: str, course: str, date: str, time: str):
        """
        Cancel a booking.

        Args:
        - customer_name (str): Name of the customer.
        - course (str): Name of the course or master class.
        - date (str): Date of the booking in YYYY-MM-DD format.
        - time (str): Time of the booking in HH:MM format.

        Raises:
        - ValueError: If the course does not exist or the booking is not found.
        """
        if course in self.courses:
            self.bookings[course] = [
                booking
                for booking in self.bookings[course]
                if not (
                    booking.customer_name == customer_name
                    and booking.date == date
                    and booking.time == time
                )
            ]
        else:
            raise ValueError("Course does not exist")

    def get_bookings(self, course: str = None):
        """
        Get all bookings for a course or all courses.

        Args:
        - course (str): Name of the course or master class.

        Returns:
        - List[Booking]: List of bookings.
        """
        if course:
            return self.bookings.get(course, [])
        else:
            return [booking for bookings in self.bookings.values() for booking in bookings]


def main():
    booking_system = AirstyleArtBookingSystem()

    while True:
        print("\nAirstyleArt Booking System")
        print("1. Add course")
        print("2. Remove course")
        print("3. Book course")
        print("4. Cancel booking")
        print("5. Get bookings")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            course = input("Enter course name: ")
            booking_system.add_course(course)
        elif choice == "2":
            course = input("Enter course name: ")
            try:
                booking_system.remove_course(course)
            except ValueError as e:
                print(e)
        elif choice == "3":
            customer_name = input("Enter customer name: ")
            course = input("Enter course name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            try:
                booking_system.book(customer_name, course, date, time)
            except ValueError as e:
                print(e)
        elif choice == "4":
            customer_name = input("Enter customer name: ")
            course = input("Enter course name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            try:
                booking_system.cancel_booking(customer_name, course, date, time)
            except ValueError as e:
                print(e)
        elif choice == "5":
            course = input("Enter course name (optional): ")
            if course:
                bookings = booking_system.get_bookings(course)
            else:
                bookings = booking_system.get_bookings()
            for booking in bookings:
                print(
                    f"Customer: {booking.customer_name}, Course: {booking.course}, Date: {booking.date}, Time: {booking.time}"
                )
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
