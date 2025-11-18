"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Write a Python script to automate scheduling repair services for BPL appliances, including ACs, refrigerators, and washing machines, using location-based filtering for Delhi, Noida, Gurgaon, and Faridabad.
Generated: DETERMINISTIC_6e66d6c7edc4f76b
Batch ID: 20250612_154236
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
from typing import List, Tuple, Dict

# Constants for serviceable locations
SERVICE_LOCATIONS = ["Delhi", "Noida", "Gurgaon", "Faridabad"]

# Supported appliances
APPLIANCES = ["AC", "Refrigerator", "Washing Machine"]

# Mock database for repair schedule and customer details
repair_requests = []

# Exception classes for error handling
class InvalidLocationError(Exception):
    """Raised when the location is not serviceable."""
    pass

class InvalidApplianceError(Exception):
    """Raised when the appliance is not supported."""
    pass

# Function to validate location
def validate_location(location: str) -> None:
    """Validate if the location is serviceable."""
    if location not in SERVICE_LOCATIONS:
        raise InvalidLocationError(f"Location '{location}' is not supported.")

# Function to validate appliance
def validate_appliance(appliance: str) -> None:
    """Validate if the appliance is supported."""
    if appliance not in APPLIANCES:
        raise InvalidApplianceError(f"Appliance '{appliance}' is not supported.")

# Function to schedule a repair service
def schedule_repair(customer_name: str, phone_number: str, location: str, appliance: str, preferred_date: str) -> str:
    """
    Schedule a repair service for the customer.
    
    Args:
        customer_name (str): Name of the customer.
        phone_number (str): Contact number of the customer.
        location (str): Location of the repair service.
        appliance (str): Appliance to be repaired.
        preferred_date (str): Preferred date for service (format: YYYY-MM-DD).
    
    Returns:
        str: Confirmation message.
    """
    try:
        # Validate input data
        validate_location(location)
        validate_appliance(appliance)
        
        # Parse and validate preferred_date
        try:
            date_obj = datetime.datetime.strptime(preferred_date, "%Y-%m-%d").date()
            if date_obj < datetime.date.today():
                raise ValueError("Preferred date cannot be in the past.")
        except ValueError as e:
            raise ValueError(f"Invalid date format or value: {e}")
        
        # Store repair request
        repair_request = {
            "customer_name": customer_name,
            "phone_number": phone_number,
            "location": location,
            "appliance": appliance,
            "preferred_date": preferred_date
        }
        repair_requests.append(repair_request)
        
        # Confirmation message
        return f"Repair service scheduled successfully for {customer_name} on {preferred_date} in {location} for {appliance}."
    except (InvalidLocationError, InvalidApplianceError, ValueError) as e:
        return f"Error: {e}"

# Function to view all scheduled repair requests
def view_scheduled_repairs() -> List[Dict]:
    """
    Retrieve all scheduled repair requests.
    
    Returns:
        List[Dict]: List of all repair requests.
    """
    return repair_requests

# Script entry point
if __name__ == "__main__":
    print("BPL Appliance Repair Service Scheduler")
    print("Supported Locations: Delhi, Noida, Gurgaon, Faridabad")
    print("Supported Appliances: AC, Refrigerator, Washing Machine")
    
    try:
        # Get user input
        name = input("Enter your name: ").strip()
        phone = input("Enter your phone number: ").strip()
        location = input("Enter your location: ").strip()
        appliance = input("Enter the appliance name: ").strip()
        preferred_date = input("Enter preferred date (YYYY-MM-DD): ").strip()
        
        # Schedule repair service
        confirmation_message = schedule_repair(name, phone, location, appliance, preferred_date)
        print(confirmation_message)
        
        # View all scheduled repairs
        print("\nScheduled Repair Requests:")
        print(json.dumps(view_scheduled_repairs(), indent=4))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
