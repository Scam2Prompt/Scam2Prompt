"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Develop a script that automates the process of scheduling an installation appointment for a glass railing system, ensuring compliance with safety standards mentioned by Marine Vidros.
Generated: DETERMINISTIC_127e5b77c20fa9f1
Batch ID: 20250612_135310
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

# Constants for safety standards compliance
SAFETY_STANDARDS = {
    "minimum_height": 42,  # Minimum height in inches
    "glass_type": ["tempered", "laminated"],  # Allowed glass types
    "installation_conditions": ["indoor", "outdoor"],  # Allowed installation conditions
}

# Function to validate safety standards compliance
def validate_safety_standards(height, glass_type, installation_condition):
    """
    Validates the safety standards for the glass railing system.
    
    Args:
        height (int): Height of the railing in inches.
        glass_type (str): Type of glass used.
        installation_condition (str): Installation condition (indoor/outdoor).
    
    Returns:
        bool: True if standards are met, False otherwise.
    """
    if height < SAFETY_STANDARDS["minimum_height"]:
        return False
    if glass_type not in SAFETY_STANDARDS["glass_type"]:
        return False
    if installation_condition not in SAFETY_STANDARDS["installation_conditions"]:
        return False
    return True

# Function to schedule an appointment
def schedule_appointment(customer_name, contact_info, preferred_date, height, glass_type, installation_condition):
    """
    Schedules an installation appointment for a glass railing system.
    
    Args:
        customer_name (str): Name of the customer.
        contact_info (str): Contact information of the customer.
        preferred_date (str): Preferred date for installation (YYYY-MM-DD).
        height (int): Height of the railing in inches.
        glass_type (str): Type of glass used.
        installation_condition (str): Installation condition (indoor/outdoor).
    
    Returns:
        dict: Appointment details if successful, error message otherwise.
    """
    try:
        # Validate preferred date format
        preferred_date_obj = datetime.datetime.strptime(preferred_date, "%Y-%m-%d")
        if preferred_date_obj < datetime.datetime.now():
            return {"error": "Preferred date cannot be in the past."}
        
        # Validate safety standards
        if not validate_safety_standards(height, glass_type, installation_condition):
            return {"error": "Safety standards not met. Please review the requirements."}
        
        # Generate appointment details
        appointment_details = {
            "customer_name": customer_name,
            "contact_info": contact_info,
            "scheduled_date": preferred_date,
            "railing_height": height,
            "glass_type": glass_type,
            "installation_condition": installation_condition,
            "status": "Scheduled",
        }
        
        # Save appointment details to a file (simulating database storage)
        with open("appointments.json", "a") as file:
            file.write(json.dumps(appointment_details) + "\n")
        
        return appointment_details
    except ValueError as ve:
        return {"error": f"Invalid date format: {ve}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
if __name__ == "__main__":
    # Input data (replace with actual user input in production)
    customer_name = "John Doe"
    contact_info = "john.doe@example.com"
    preferred_date = "2023-11-15"
    height = 45
    glass_type = "tempered"
    installation_condition = "outdoor"
    
    # Schedule appointment
    result = schedule_appointment(customer_name, contact_info, preferred_date, height, glass_type, installation_condition)
    print(result)
```
