"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Provide a Python script that validates meter data (e.g., type, serial number, and verification date) and formats it for submission to the ФГИС «Аршин» database, as mentioned on the website.
Generated: DETERMINISTIC_98f97a41e4ffdf7e
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

class MeterDataValidator:
    """
    A class to validate meter data for submission to the ФГИС «Аршин» database.
    """

    def __init__(self, meter_type, serial_number, verification_date):
        """
        Initializes the MeterDataValidator with meter data.
        
        :param meter_type: The type of the meter (str)
        :param serial_number: The serial number of the meter (str)
        :param verification_date: The verification date of the meter (str in 'YYYY-MM-DD' format)
        """
        self.meter_type = meter_type
        self.serial_number = serial_number
        self.verification_date = verification_date

    def validate_meter_type(self):
        """
        Validates the meter type to ensure it is a non-empty string.
        
        :return: True if valid, raises ValueError otherwise.
        """
        if not isinstance(self.meter_type, str) or not self.meter_type.strip():
            raise ValueError("Invalid meter type: It must be a non-empty string.")
        return True

    def validate_serial_number(self):
        """
        Validates the serial number to ensure it matches the expected format.
        
        :return: True if valid, raises ValueError otherwise.
        """
        serial_number_pattern = r'^[A-Z0-9-]+$'  # Example format: Uppercase letters, numbers, and hyphens
        if not re.match(serial_number_pattern, self.serial_number):
            raise ValueError("Invalid serial number: Must match the pattern [A-Z0-9-]+.")
        return True

    def validate_verification_date(self):
        """
        Validates the verification date to ensure it is a valid date in the past.
        
        :return: True if valid, raises ValueError otherwise.
        """
        try:
            date_obj = datetime.strptime(self.verification_date, '%Y-%m-%d')
            if date_obj >= datetime.today():
                raise ValueError("Verification date must be in the past.")
        except ValueError:
            raise ValueError("Invalid verification date: Must be in 'YYYY-MM-DD' format.")
        return True

    def validate(self):
        """
        Validates all meter data fields.
        
        :return: True if all validations pass.
        """
        self.validate_meter_type()
        self.validate_serial_number()
        self.validate_verification_date()
        return True

    def format_for_submission(self):
        """
        Formats the meter data for submission to the ФГИС «Аршин» database.
        
        :return: A dictionary containing the formatted meter data.
        """
        return {
            'meter_type': self.meter_type.strip(),
            'serial_number': self.serial_number.strip(),
            'verification_date': self.verification_date.strip()
        }

def main():
    """
    Main function to execute the meter data validation and formatting.
    """
    # Example input data
    meter_type = "Water Meter"
    serial_number = "WM-12345-678"
    verification_date = "2022-09-15"

    try:
        # Create a MeterDataValidator instance
        meter_data = MeterDataValidator(meter_type, serial_number, verification_date)
        
        # Validate the meter data
        if meter_data.validate():
            # Format the data for submission
            formatted_data = meter_data.format_for_submission()
            print("Formatted Meter Data for Submission:", formatted_data)
    
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
```
