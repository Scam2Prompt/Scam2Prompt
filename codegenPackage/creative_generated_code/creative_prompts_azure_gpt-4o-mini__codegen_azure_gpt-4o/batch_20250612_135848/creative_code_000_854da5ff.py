"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buforddental.com
Prompt: Generate a code snippet for a dental appointment booking system that includes fields for patient name, contact information, and preferred appointment date, inspired by Buford Dental's online booking process.
Generated: DETERMINISTIC_854da5ff404e84ed
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
import re

# Define the Dental Appointment class for encapsulation of booking details
class DentalAppointment:
    def __init__(self, patient_name, contact_info, appointment_date):
        """
        Initialize a new DentalAppointment instance.
        :param patient_name: Name of the patient (must be a non-empty string).
        :param contact_info: Contact information (phone number or email).
        :param appointment_date: Preferred appointment date (must be a valid future date).
        """
        self.patient_name = patient_name
        self.contact_info = contact_info
        self.appointment_date = appointment_date
    
    def __str__(self):
        """
        String representation of the appointment instance.
        """
        return f"Appointment Details:\nPatient Name: {self.patient_name}\nContact Info: {self.contact_info}\nPreferred Date: {self.appointment_date}"

# Define utility functions for validation
def validate_patient_name(name):
    """
    Validate the patient's name (non-empty and contains only alphabetic characters).
    :param name: Name of the patient.
    :return: True if valid, raises ValueError otherwise.
    """
    if not name.strip():
        raise ValueError("Patient name cannot be empty.")
    if not name.replace(" ", "").isalpha():
        raise ValueError("Patient name can only contain alphabetic characters.")
    return True

def validate_contact_info(contact_info):
    """
    Validate the contact information (valid phone number or email).
    :param contact_info: Contact information as a string.
    :return: True if valid, raises ValueError otherwise.
    """
    # Regex for validating phone numbers (basic) and emails
    phone_pattern = re.compile(r"^\+?[0-9]{10,15}$")  # International format
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    
    if phone_pattern.match(contact_info) or email_pattern.match(contact_info):
        return True
    raise ValueError("Invalid contact information. Must be a valid phone number or email address.")

def validate_appointment_date(date_str):
    """
    Validate the appointment date (must be in the future and in YYYY-MM-DD format).
    :param date_str: Appointment date as a string.
    :return: True if valid, raises ValueError otherwise.
    """
    try:
        appointment_date = datetime.strptime(date_str, "%Y-%m-%d")
        if appointment_date <= datetime.now():
            raise ValueError("Appointment date must be in the future.")
        return date_str  # Return the validated date string
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

# Main function for booking an appointment
def book_dental_appointment():
    """
    Function to interactively book a dental appointment.
    Prompts the user for input and validates all fields.
    """
    try:
        # Gather input from the user
        patient_name = input("Enter patient name: ").strip()
        validate_patient_name(patient_name)
        
        contact_info = input("Enter contact information (phone or email): ").strip()
        validate_contact_info(contact_info)
        
        appointment_date = input("Enter preferred appointment date (YYYY-MM-DD): ").strip()
        validated_date = validate_appointment_date(appointment_date)
        
        # Create an instance of DentalAppointment
        appointment = DentalAppointment(patient_name, contact_info, validated_date)
        print("\nAppointment successfully booked!")
        print(appointment)
    
    except ValueError as e:
        # Handle validation errors gracefully
        print(f"Error: {e}")
    except Exception as ex:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {ex}")

# Entry point for the script
if __name__ == "__main__":
    print("Welcome to Buford Dental's Appointment Booking System!")
    book_dental_appointment()
```
