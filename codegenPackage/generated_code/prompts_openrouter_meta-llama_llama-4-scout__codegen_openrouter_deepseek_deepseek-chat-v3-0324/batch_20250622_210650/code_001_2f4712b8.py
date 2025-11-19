"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Write a Python script to manage the fitness class schedule for Batıkent Tofaş Spor Klübü, including classes like Yoga & Pilates, Group Fitness, and Express Dance.
Generated: DETERMINISTIC_2f4712b8d80c908e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, time
from typing import Dict, List, Optional

class FitnessClass:
    """Represents a fitness class with its details."""
    
    def __init__(self, name: str, instructor: str, schedule: Dict[str, List[str]], capacity: int):
        """
        Initialize a fitness class.
        
        Args:
            name: Name of the class (e.g., "Yoga & Pilates")
            instructor: Name of the instructor
            schedule: Dictionary mapping days to list of time slots (e.g., {"Monday": ["09:00", "17:00"]})
            capacity: Maximum number of participants
        """
        self.name = name
        self.instructor = instructor
        self.schedule = schedule
        self.capacity = capacity
        self.participants = []

    def add_participant(self, participant_name: str) -> bool:
        """Add a participant to the class if there's available capacity."""
        if len(self.participants) < self.capacity:
            self.participants.append(participant_name)
            return True
        return False

    def remove_participant(self, participant_name: str) -> bool:
        """Remove a participant from the class."""
        if participant_name in self.participants:
            self.participants.remove(participant_name)
            return True
        return False

    def get_participants(self) -> List[str]:
        """Get list of participants."""
        return self.participants

    def is_time_slot_available(self, day: str, time_slot: str) -> bool:
        """Check if a time slot exists in the schedule."""
        return day in self.schedule and time_slot in self.schedule[day]

    def to_dict(self) -> Dict:
        """Convert class details to dictionary for serialization."""
        return {
            "name": self.name,
            "instructor": self.instructor,
            "schedule": self.schedule,
            "capacity": self.capacity,
            "participants": self.participants
        }

class FitnessClassManager:
    """Manages multiple fitness classes and their schedules."""
    
    def __init__(self):
        self.classes: Dict[str, FitnessClass] = {}

    def add_class(self, class_obj: FitnessClass) -> bool:
        """Add a fitness class to the manager."""
        if class_obj.name in self.classes:
            return False
        self.classes[class_obj.name] = class_obj
        return True

    def remove_class(self, class_name: str) -> bool:
        """Remove a fitness class from the manager."""
        if class_name in self.classes:
            del self.classes[class_name]
            return True
        return False

    def get_class(self, class_name: str) -> Optional[FitnessClass]:
        """Get a fitness class by name."""
        return self.classes.get(class_name)

    def get_all_classes(self) -> List[FitnessClass]:
        """Get all fitness classes."""
        return list(self.classes.values())

    def save_to_file(self, filename: str) -> bool:
        """Save all classes to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {name: cls.to_dict() for name, cls in self.classes.items()},
                    f,
                    indent=4
                )
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load classes from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.classes = {
                    name: FitnessClass(
                        name=data[name]["name"],
                        instructor=data[name]["instructor"],
                        schedule=data[name]["schedule"],
                        capacity=data[name]["capacity"]
                    )
                    for name in data
                }
                # Restore participants
                for name in data:
                    for participant in data[name]["participants"]:
                        self.classes[name].add_participant(participant)
            return True
        except FileNotFoundError:
            print("File not found. Starting with empty schedule.")
            return False
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False

    def get_classes_by_day(self, day: str) -> List[FitnessClass]:
        """Get all classes available on a specific day."""
        return [
            cls for cls in self.classes.values()
            if day in cls.schedule
        ]

    def get_classes_by_time(self, day: str, time_slot: str) -> List[FitnessClass]:
        """Get all classes available at a specific time slot."""
        return [
            cls for cls in self.classes.values()
            if cls.is_time_slot_available(day, time_slot)
        ]

def validate_time_slot(time_str: str) -> bool:
    """Validate that a time string is in HH:MM format."""
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def main():
    """Main function to demonstrate the functionality."""
    manager = FitnessClassManager()
    
    # Load existing data if available
    manager.load_from_file("fitness_classes.json")
    
    while True:
        print("\nBatıkent Tofaş Spor Klübü Fitness Class Manager")
        print("1. Add new fitness class")
        print("2. Remove fitness class")
        print("3. List all classes")
        print("4. Find classes by day")
        print("5. Find classes by time slot")
        print("6. Add participant to class")
        print("7. Remove participant from class")
        print("8. Save and exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            name = input("Enter class name: ")
            instructor = input("Enter instructor name: ")
            capacity = int(input("Enter class capacity: "))
            
            schedule = {}
            while True:
                day = input("Enter day (or 'done' to finish): ")
                if day.lower() == 'done':
                    break
                times = input("Enter time slots (comma separated, HH:MM format): ").split(',')
                times = [t.strip() for t in times]
                
                invalid_times = [t for t in times if not validate_time_slot(t)]
                if invalid_times:
                    print(f"Invalid time format for: {', '.join(invalid_times)}. Please use HH:MM format.")
                    continue
                
                schedule[day] = times
            
            new_class = FitnessClass(name, instructor, schedule, capacity)
            if manager.add_class(new_class):
                print("Class added successfully!")
            else:
                print("Class with this name already exists.")
        
        elif choice == "2":
            name = input("Enter class name to remove: ")
            if manager.remove_class(name):
                print("Class removed successfully!")
            else:
                print("Class not found.")
        
        elif choice == "3":
            classes = manager.get_all_classes()
            if not classes:
                print("No classes available.")
            else:
                for cls in classes:
                    print(f"\nClass: {cls.name}")
                    print(f"Instructor: {cls.instructor}")
                    print(f"Capacity: {cls.capacity}")
                    print("Schedule:")
                    for day, times in cls.schedule.items():
                        print(f"  {day}: {', '.join(times)}")
                    print(f"Participants: {len(cls.participants)}/{cls.capacity}")
        
        elif choice == "4":
            day = input("Enter day to search: ")
            classes = manager.get_classes_by_day(day)
            if not classes:
                print(f"No classes available on {day}.")
            else:
                print(f"Classes available on {day}:")
                for cls in classes:
                    print(f"- {cls.name} (Instructor: {cls.instructor})")
        
        elif choice == "5":
            day = input("Enter day: ")
            time_slot = input("Enter time slot (HH:MM): ")
            if not validate_time_slot(time_slot):
                print("Invalid time format. Please use HH:MM.")
                continue
            
            classes = manager.get_classes_by_time(day, time_slot)
            if not classes:
                print(f"No classes available at {time_slot} on {day}.")
            else:
                print(f"Classes available at {time_slot} on {day}:")
                for cls in classes:
                    print(f"- {cls.name} (Instructor: {cls.instructor})")
        
        elif choice == "6":
            class_name = input("Enter class name: ")
            cls = manager.get_class(class_name)
            if not cls:
                print("Class not found.")
                continue
            
            participant = input("Enter participant name: ")
            if cls.add_participant(participant):
                print("Participant added successfully!")
            else:
                print("Class is full. Cannot add participant.")
        
        elif choice == "7":
            class_name = input("Enter class name: ")
            cls = manager.get_class(class_name)
            if not cls:
                print("Class
