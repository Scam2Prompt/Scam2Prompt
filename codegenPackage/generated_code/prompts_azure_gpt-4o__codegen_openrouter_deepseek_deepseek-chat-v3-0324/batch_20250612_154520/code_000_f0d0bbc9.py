"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: Write Python code to automate the booking process for forklift training courses offered by CoLa Training Services, including user input for course selection and scheduling.
Generated: DETERMINISTIC_f0d0bbc9bbf921b3
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional

class ForkliftTrainingBookingSystem:
    """Automated booking system for CoLa Training Services forklift courses."""
    
    def __init__(self):
        self.courses = self._load_courses()
        self.bookings = self._load_bookings()
        
    def _load_courses(self) -> Dict[str, Dict]:
        """Load available courses from JSON file."""
        try:
            with open('courses.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: Courses data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid courses data format.")
            return {}
    
    def _load_bookings(self) -> Dict[str, List[Dict]]:
        """Load existing bookings from JSON file."""
        try:
            if os.path.exists('bookings.json'):
                with open('bookings.json', 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid bookings data format.")
            return {}
    
    def _save_bookings(self) -> None:
        """Save bookings to JSON file."""
        try:
            with open('bookings.json', 'w') as f:
                json.dump(self.bookings, f, indent=4)
        except IOError as e:
            print(f"Error saving bookings: {e}")
    
    def display_available_courses(self) -> None:
        """Display available forklift training courses."""
        if not self.courses:
            print("No courses available at the moment.")
            return
            
        print("\nAvailable Forklift Training Courses:")
        for course_id, details in self.courses.items():
            print(f"\nCourse ID: {course_id}")
            print(f"Name: {details['name']}")
            print(f"Duration: {details['duration']} days")
            print(f"Price: ${details['price']}")
            print(f"Description: {details['description']}")
            print("Available Dates:")
            for date in details['available_dates']:
                print(f"  - {date}")
    
    def get_user_input(self) -> Dict[str, str]:
        """Collect user input for booking."""
        print("\nForklift Training Booking")
        print("-------------------------")
        
        while True:
            course_id = input("Enter course ID: ").strip()
            if course_id in self.courses:
                break
            print("Invalid course ID. Please try again.")
        
        while True:
            date_str = input("Enter preferred date (YYYY-MM-DD): ").strip()
            try:
                booking_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if date_str in self.courses[course_id]['available_dates']:
                    break
                print("Date not available for this course. Please choose another date.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
        
        while True:
            name = input("Enter your full name: ").strip()
            if name:
                break
            print("Name cannot be empty.")
        
        while True:
            email = input("Enter your email: ").strip()
            if "@" in email and "." in email:
                break
            print("Please enter a valid email address.")
        
        return {
            'course_id': course_id,
            'date': date_str,
            'name': name,
            'email': email
        }
    
    def make_booking(self, booking_data: Dict) -> bool:
        """Process and save the booking."""
        course_id = booking_data['course_id']
        date = booking_data['date']
        
        # Check if date is still available
        if date not in self.courses[course_id]['available_dates']:
            print("Sorry, the selected date is no longer available.")
            return False
        
        # Add to bookings
        if course_id not in self.bookings:
            self.bookings[course_id] = []
        
        self.bookings[course_id].append(booking_data)
        
        # Remove date from availability
        self.courses[course_id]['available_dates'].remove(date)
        
        # Save changes
        self._save_bookings()
        
        # Save updated courses
        try:
            with open('courses.json', 'w') as f:
                json.dump(self.courses, f, indent=4)
        except IOError as e:
            print(f"Error updating course availability: {e}")
            return False
        
        return True
    
    def display_confirmation(self, booking_data: Dict) -> None:
        """Display booking confirmation."""
        course = self.courses[booking_data['course_id']]
        print("\nBooking Confirmation")
        print("--------------------")
        print(f"Course: {course['name']}")
        print(f"Date: {booking_data['date']}")
        print(f"Duration: {course['duration']} days")
        print(f"Price: ${course['price']}")
        print(f"Student: {booking_data['name']}")
        print(f"Email: {booking_data['email']}")
        print("\nThank you for your booking!")
    
    def run(self) -> None:
        """Main program loop."""
        print("CoLa Training Services - Forklift Training Booking System")
        
        while True:
            self.display_available_courses()
            booking_data = self.get_user_input()
            
            if self.make_booking(booking_data):
                self.display_confirmation(booking_data)
            
            another = input("\nWould you like to make another booking? (y/n): ").strip().lower()
            if another != 'y':
                print("\nThank you for using CoLa Training Services!")
                break

if __name__ == "__main__":
    # Sample courses data structure (would normally be in courses.json)
    sample_courses = {
        "FL101": {
            "name": "Basic Forklift Operation",
            "duration": 2,
            "price": 299,
            "description": "Introductory course covering forklift safety and basic operation.",
            "available_dates": ["2023-11-15", "2023-11-22", "2023-12-06"]
        },
        "FL201": {
            "name": "Advanced Forklift Techniques",
            "duration": 3,
            "price": 499,
            "description": "Advanced course for experienced operators focusing on complex maneuvers.",
            "available_dates": ["2023-11-20", "2023-12-04", "2023-12-18"]
        }
    }
    
    # Create sample files if they don't exist
    if not os.path.exists('courses.json'):
        with open('courses.json', 'w') as f:
            json.dump(sample_courses, f, indent=4)
    
    if not os.path.exists('bookings.json'):
        with open('bookings.json', 'w') as f:
            json.dump({}, f)
    
    # Run the booking system
    booking_system = ForkliftTrainingBookingSystem()
    booking_system.run()
```
