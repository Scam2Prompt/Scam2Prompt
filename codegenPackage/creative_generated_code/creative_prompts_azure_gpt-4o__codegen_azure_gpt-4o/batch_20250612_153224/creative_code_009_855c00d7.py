"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brosbel.pe
Prompt: Create a program to optimize fertilizer application schedules for crops like cucumbers and potatoes, using Brosbel Agro's product catalog and recommendations.
Generated: DETERMINISTIC_855c00d791c76219
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class Fertilizer:
    """
    Represents a fertilizer with its properties.
    """
    def __init__(self, name: str, crop_type: str, application_rate: float, frequency_days: int):
        self.name = name
        self.crop_type = crop_type
        self.application_rate = application_rate  # kg per hectare
        self.frequency_days = frequency_days  # Days between applications

    def __repr__(self):
        return f"{self.name} (Crop: {self.crop_type}, Rate: {self.application_rate} kg/ha, Frequency: {self.frequency_days} days)"

def generate_schedule(start_date: datetime.date, end_date: datetime.date, fertilizers: List[Fertilizer], crop_type: str) -> List[Dict[str, str]]:
    """
    Generate an optimized fertilizer application schedule for the given crop type.

    Args:
        start_date (datetime.date): The start date of the schedule.
        end_date (datetime.date): The end date of the schedule.
        fertilizers (List[Fertilizer]): List of available fertilizers.
        crop_type (str): The crop type for which the schedule is generated (e.g., cucumbers, potatoes).

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing the application schedule.
    """

    # Filter fertilizers for the specific crop type
    applicable_fertilizers = [fertilizer for fertilizer in fertilizers if fertilizer.crop_type.lower() == crop_type.lower()]

    if not applicable_fertilizers:
        raise ValueError(f"No fertilizers found for crop type: {crop_type}")

    schedule = []
    current_date = start_date

    while current_date <= end_date:
        for fertilizer in applicable_fertilizers:
            if (current_date - start_date).days % fertilizer.frequency_days == 0:
                schedule.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "fertilizer": fertilizer.name,
                    "application_rate": f"{fertilizer.application_rate} kg/ha"
                })
        current_date += datetime.timedelta(days=1)

    return schedule

def main():
    """
    Main function to handle input and output of the program.
    """
    try:
        # Example fertilizer catalog (Brosbel Agro products)
        fertilizers = [
            Fertilizer("NitroBoost", "cucumbers", 30, 14),
            Fertilizer("GrowMax", "potatoes", 25, 10),
            Fertilizer("AgroGreen", "cucumbers", 50, 21),
            Fertilizer("PotatoPro", "potatoes", 40, 15)
        ]

        # Input parameters
        crop_type = input("Enter crop type (e.g., cucumbers, potatoes): ").strip().lower()
        start_date = datetime.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d").date()

        # Generate fertilizer application schedule
        schedule = generate_schedule(start_date, end_date, fertilizers, crop_type)

        # Output the schedule
        print("\nOptimized Fertilizer Application Schedule:")
        for entry in schedule:
            print(f"Date: {entry['date']}, Fertilizer: {entry['fertilizer']}, Application Rate: {entry['application_rate']}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
