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
import json
from datetime import datetime, timedelta

class ServiceScheduler:
    """
    A class to schedule repair services for BPL appliances based on location.
    Supported locations: Delhi, Noida, Gurgaon, Faridabad.
    """

    def __init__(self):
        # Predefined service slots
        self.service_slots = {
            'Delhi': [],
            'Noida': [],
            'Gurgaon': [],
            'Faridabad': []
        }
        self.generate_service_slots()

    def generate_service_slots(self):
        """
        Generates service slots for the next 7 days.
        Each day will have three slots: Morning, Afternoon, and Evening.
        """
        today = datetime.now()
        for day_offset in range(7):
            for location in self.service_slots.keys():
                date = (today + timedelta(days=day_offset)).date()
                self.service_slots[location].append({
                    'date': str(date),
                    'slots': ['Morning', 'Afternoon', 'Evening']
                })

    def schedule_service(self, location, appliance_type, preferred_slot):
        """
        Schedules a repair service for a specified location and appliance type.

        :param location: str - The location for the service.
        :param appliance_type: str - The type of appliance.
        :param preferred_slot: str - The preferred time slot (Morning, Afternoon, Evening).
        :return: dict - Confirmation of the scheduled service or error message.
        """
        if location not in self.service_slots:
            return {"error": "Invalid location. Supported locations are Delhi, Noida, Gurgaon, Faridabad."}
        
        for day in self.service_slots[location]:
            if preferred_slot in day['slots']:
                # Remove the preferred slot from available slots
                day['slots'].remove(preferred_slot)
                return {
                    "status": "success",
                    "message": f"Service scheduled for {appliance_type} in {location} on {day['date']} during {preferred_slot}."
                }
        
        return {"error": "Preferred slot is not available."}

    def get_available_slots(self, location):
        """
        Retrieves available service slots for the specified location.

        :param location: str - The location for which to check available slots.
        :return: list - Available slots for the location or error message if invalid.
        """
        if location not in self.service_slots:
            return {"error": "Invalid location. Supported locations are Delhi, Noida, Gurgaon, Faridabad."}
        
        return self.service_slots[location]

if __name__ == "__main__":
    scheduler = ServiceScheduler()
    
    # Sample interaction with the ServiceScheduler
    location = "Delhi"
    appliance_type = "AC"
    preferred_slot = "Morning"

    available_slots = scheduler.get_available_slots(location)
    print(json.dumps(available_slots, indent=4))

    scheduling_result = scheduler.schedule_service(location, appliance_type, preferred_slot)
    print(json.dumps(scheduling_result, indent=4))
```
