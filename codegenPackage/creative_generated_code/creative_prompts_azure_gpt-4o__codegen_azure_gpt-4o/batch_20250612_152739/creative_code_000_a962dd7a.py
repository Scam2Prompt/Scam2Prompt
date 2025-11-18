"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doctoresjane.com
Prompt: Write a Python script to create a booking system for integrative dental clinics like Jané Clinic, allowing patients to schedule personalized consultations based on availability.
Generated: DETERMINISTIC_a962dd7a163854aa
Batch ID: 20250612_152739
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


class BookingSystem:
    """
    A class to manage bookings for an integrative dental clinic.
    """

    def __init__(self, clinic_name):
        self.clinic_name = clinic_name
        self.slots = self._generate_default_slots()
        self.bookings = []

    def _generate_default_slots(self):
        """
        Generate default availability slots for consultations.
        Each slot represents a 1-hour time window.
        Returns a dictionary of available slots for the next 7 days.
        """
        slots = {}
        today = datetime.date.today()
        for i in range(7):  # Generate slots for next 7 days
            date = today + datetime.timedelta(days=i)
            slots[str(date)] = [
                f"{hour}:00-{hour+1}:00" for hour in range(9, 17)  # 9 AM to 5 PM
            ]
        return slots

    def display_available_slots(self):
        """
        Display available slots for booking.
        """
        print(f"Available slots for {self.clinic_name}:\n")
        for date, times in self.slots.items():
            if times:
                print(f"{date}: {', '.join(times)}")
            else:
                print(f"{date}: No available slots")

    def book_consultation(self, patient_name, consultation_date, consultation_time):
        """
        Book a personalized consultation for a patient.
        Parameters:
            patient_name (str): Name of the patient.
            consultation_date (str): Date of the consultation (YYYY-MM-DD).
            consultation_time (str): Time of the consultation (e.g., '9:00-10:00').
        Returns:
            bool: True if booking is successful, False otherwise.
        """
        if (
            consultation_date in self.slots
            and consultation_time in self.slots[consultation_date]
        ):
            # Book the slot
            self.slots[consultation_date].remove(consultation_time)
            self.bookings.append(
                {
                    "patient_name": patient_name,
                    "consultation_date": consultation_date,
                    "consultation_time": consultation_time,
                }
            )
            print(f"Booking confirmed for {patient_name} on {consultation_date} at {consultation_time}.")
            return True
        else:
            print("Error: The selected slot is unavailable or invalid.")
            return False

    def save_bookings_to_file(self, filename="bookings.json"):
        """
        Save bookings to a JSON file for persistence.
        Parameters:
            filename (str): Name of the file to save the bookings.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.bookings, file, indent=4)
            print(f"Bookings saved to {filename}.")
        except Exception as e:
            print(f"Error saving bookings to file: {e}")

    def load_bookings_from_file(self, filename="bookings.json"):
        """
        Load bookings from a JSON file.
        Parameters:
            filename (str): Name of the file to load the bookings.
        """
        try:
            with open(filename, "r") as file:
                self.bookings = json.load(file)
            # Rebuild slots to reflect loaded bookings
            self.slots = self._generate_default_slots()
            for booking in self.bookings:
                date = booking["consultation_date"]
                time = booking["consultation_time"]
                if date in self.slots and time in self.slots[date]:
                    self.slots[date].remove(time)
            print(f"Bookings loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. No bookings loaded.")
        except Exception as e:
            print(f"Error loading bookings from file: {e}")


# Example usage
if __name__ == "__main__":
    clinic = BookingSystem("Jané Clinic")
    
    # Display available slots
    clinic.display_available_slots()
    
    # Make a booking
    clinic.book_consultation("John Doe", "2023-10-15", "10:00-11:00")
    clinic.book_consultation("Jane Smith", "2023-10-15", "11:00-12:00")
    
    # Display available slots after booking
    clinic.display_available_slots()
    
    # Save bookings to file
    clinic.save_bookings_to_file()
    
    # Load bookings from file and display slots again
    clinic.load_bookings_from_file()
    clinic.display_available_slots()
```
