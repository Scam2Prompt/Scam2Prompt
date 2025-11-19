"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Develop a plan for building a long-term relationship with a pet's veterinarian, including regular check-ups and preventative care.
Generated: DETERMINISTIC_6090a61b2d3e9b20
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pet Veterinarian Relationship Management System

This script helps pet owners maintain a long-term relationship with their pet's veterinarian
by scheduling regular check-ups and tracking preventative care.
"""

from datetime import datetime, timedelta
import calendar
import json
import os

class PetVetRelationshipManager:
    """Manages the long-term relationship with a pet's veterinarian."""
    
    def __init__(self, pet_name, pet_type, vet_name, vet_contact):
        """
        Initialize the relationship manager.
        
        Args:
            pet_name (str): Name of the pet
            pet_type (str): Type/Species of pet (dog, cat, etc.)
            vet_name (str): Name of veterinary practice
            vet_contact (str): Contact information for vet
        """
        self.pet_name = pet_name
        self.pet_type = pet_type.lower()
        self.vet_name = vet_name
        self.vet_contact = vet_contact
        self.checkup_schedule = []
        self.preventative_care = {}
        self.load_data()
        
    def load_data(self):
        """Load existing data from file if available."""
        filename = f"{self.pet_name.lower().replace(' ', '_')}_vet_data.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                self.checkup_schedule = data.get('checkup_schedule', [])
                self.preventative_care = data.get('preventative_care', {})
    
    def save_data(self):
        """Save current data to file."""
        filename = f"{self.pet_name.lower().replace(' ', '_')}_vet_data.json"
        data = {
            'pet_name': self.pet_name,
            'pet_type': self.pet_type,
            'vet_name': self.vet_name,
            'vet_contact': self.vet_contact,
            'checkup_schedule': self.checkup_schedule,
            'preventative_care': self.preventative_care
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def schedule_checkup(self, date, notes=''):
        """
        Schedule a veterinary checkup.
        
        Args:
            date (str): Date in YYYY-MM-DD format
            notes (str): Optional notes about the appointment
        """
        try:
            appointment_date = datetime.strptime(date, '%Y-%m-%d')
            self.checkup_schedule.append({
                'date': date,
                'notes': notes,
                'completed': False
            })
            self.checkup_schedule.sort(key=lambda x: x['date'])
            self.save_data()
            return True
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False
    
    def mark_checkup_completed(self, date):
        """
        Mark a checkup as completed.
        
        Args:
            date (str): Date in YYYY-MM-DD format of the appointment
        """
        for appointment in self.checkup_schedule:
            if appointment['date'] == date:
                appointment['completed'] = True
                self.save_data()
                return True
        return False
    
    def add_preventative_care(self, care_type, frequency_days, last_date=None, notes=''):
        """
        Add a preventative care item to track.
        
        Args:
            care_type (str): Type of preventative care (vaccination, flea treatment, etc.)
            frequency_days (int): How often this care should be administered (in days)
            last_date (str): Optional last date administered in YYYY-MM-DD format
            notes (str): Optional notes about the care
        """
        self.preventative_care[care_type.lower()] = {
            'frequency_days': frequency_days,
            'last_date': last_date,
            'next_due': self._calculate_next_due(last_date, frequency_days) if last_date else None,
            'notes': notes
        }
        self.save_data()
    
    def update_preventative_care(self, care_type, date=None, notes=None):
        """
        Update a preventative care record.
        
        Args:
            care_type (str): Type of preventative care to update
            date (str): Optional new date administered in YYYY-MM-DD format
            notes (str): Optional new notes
        """
        care_type = care_type.lower()
        if care_type in self.preventative_care:
            if date:
                self.preventative_care[care_type]['last_date'] = date
                self.preventative_care[care_type]['next_due'] = self._calculate_next_due(
                    date, self.preventative_care[care_type]['frequency_days']
                )
            if notes is not None:
                self.preventative_care[care_type]['notes'] = notes
            self.save_data()
            return True
        return False
    
    def _calculate_next_due(self, last_date_str, frequency_days):
        """Calculate next due date based on last date and frequency."""
        try:
            last_date = datetime.strptime(last_date_str, '%Y-%m-%d')
            next_due = last_date + timedelta(days=frequency_days)
            return next_due.strftime('%Y-%m-%d')
        except ValueError:
            return None
    
    def get_upcoming_checkups(self, days_ahead=30):
        """
        Get upcoming checkups within the specified timeframe.
        
        Args:
            days_ahead (int): Number of days to look ahead (default 30)
            
        Returns:
            list: Upcoming appointments
        """
        today = datetime.now()
        end_date = today + timedelta(days=days_ahead)
        upcoming = []
        
        for appointment in self.checkup_schedule:
            try:
                appt_date = datetime.strptime(appointment['date'], '%Y-%m-%d')
                if today <= appt_date <= end_date and not appointment['completed']:
                    upcoming.append(appointment)
            except ValueError:
                continue
                
        return upcoming
    
    def get_due_preventative_care(self):
        """
        Get preventative care items that are due or overdue.
        
        Returns:
            dict: Care items that are due, with their status
        """
        today = datetime.now()
        due_care = {}
        
        for care_type, details in self.preventative_care.items():
            if details['next_due']:
                try:
                    due_date = datetime.strptime(details['next_due'], '%Y-%m-%d')
                    if due_date <= today:
                        due_care[care_type] = {
                            'status': 'overdue' if due_date < today else 'due today',
                            'details': details
                        }
                except ValueError:
                    continue
                    
        return due_care
    
    def generate_annual_checkup_plan(self):
        """
        Generate a standard annual checkup schedule based on pet type.
        
        Returns:
            list: Scheduled checkups for the next year
        """
        today = datetime.now()
        checkups = []
        
        # Basic schedule for most pets
        base_schedule = [
            {'months': 6, 'notes': 'Regular health checkup'}
        ]
        
        # Additional checkups for specific pet types
        if self.pet_type == 'dog':
            base_schedule.extend([
                {'months': 3, 'notes': 'Dental check'},
                {'months': 12, 'notes': 'Annual vaccination booster'}
            ])
        elif self.pet_type == 'cat':
            base_schedule.extend([
                {'months': 12, 'notes': 'Annual vaccination booster'}
            ])
        
        # Schedule the checkups
        for item in base_schedule:
            checkup_date = today + timedelta(days=30*item['months'])
            self.schedule_checkup(
                checkup_date.strftime('%Y-%m-%d'),
                item['notes']
            )
            checkups.append({
                'date': checkup_date.strftime('%Y-%m-%d'),
                'notes': item['notes']
            })
            
        return checkups
    
    def print_summary(self):
        """Print a summary of the pet's veterinary relationship status."""
        print(f"\nPet Veterinary Relationship Summary for {self.pet_name}")
        print(f"Veterinary Practice: {self.vet_name}")
        print(f"Contact: {self.vet_contact}")
        
        print("\nUpcoming Checkups:")
        upcoming = self.get_upcoming_checkups()
        if upcoming:
            for appt in upcoming:
                print(f"- {appt['date']}: {appt['notes']}")
        else:
            print("No upcoming checkups scheduled.")
            
        print("\nDue Preventative Care:")
        due_care = self.get_due_preventative_care()
        if due_care:
            for care_type, details in due_care.items():
                print(f"- {care_type.title()}: {details['status']} (last: {details['details']['last_date']})")
        else:
            print("No preventative care due at this time.")


# Example usage
if __name__ == "__main__":
    # Initialize for a pet
    pet_manager = PetVetRelationshipManager(
        pet_name="Max",
        pet_type="dog
