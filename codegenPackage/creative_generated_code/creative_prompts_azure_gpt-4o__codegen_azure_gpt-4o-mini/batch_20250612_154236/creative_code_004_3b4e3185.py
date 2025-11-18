"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Write a script to validate customer inputs for booking BPL appliance repair services, ensuring correct appliance type, location, and contact details are provided before submission.
Generated: DETERMINISTIC_3b4e318542c18a45
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class BookingValidationError(Exception):
    """Custom exception for booking validation errors."""
    pass

class ApplianceRepairBooking:
    """Class to handle the validation of appliance repair bookings."""
    
    VALID_APPLIANCE_TYPES = {"Washing Machine", "Dryer", "Refrigerator", "Dishwasher", "Oven"}
    
    def __init__(self, appliance_type, location, contact_number):
        self.appliance_type = appliance_type
        self.location = location
        self.contact_number = contact_number
        
    def validate(self):
        """Validate the booking details for appliance repair."""
        self.validate_appliance_type()
        self.validate_location()
        self.validate_contact_number()

    def validate_appliance_type(self):
        """Validate the appliance type."""
        if self.appliance_type not in self.VALID_APPLIANCE_TYPES:
            raise BookingValidationError(f"Invalid appliance type: {self.appliance_type}. "
                                         f"Valid types are: {', '.join(self.VALID_APPLIANCE_TYPES)}.")

    def validate_location(self):
        """Validate the location."""
        if not self.location or len(self.location) < 5:
            raise BookingValidationError("Location must be a non-empty string of at least 5 characters.")

    def validate_contact_number(self):
        """Validate the contact number."""
        if not re.match(r'^\+?\d{10,15}$', self.contact_number):
            raise BookingValidationError("Contact number must be a valid phone number (10 to 15 digits long).")
        
def main():
    """Main function to run the booking validation."""
    try:
        # Sample input for demonstration
        appliance_type = "Washing Machine"  # Change as needed
        location = "123 Main St"             # Change as needed
        contact_number = "+1234567890"       # Change as needed
        
        # Create a booking instance
        booking = ApplianceRepairBooking(appliance_type, location, contact_number)
        
        # Validate booking details
        booking.validate()
        
        print("Booking details are valid. Proceeding with the booking...")
        
    except BookingValidationError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
