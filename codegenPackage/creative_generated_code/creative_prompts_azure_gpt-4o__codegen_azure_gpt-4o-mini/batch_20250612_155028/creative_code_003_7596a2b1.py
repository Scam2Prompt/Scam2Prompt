"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelllar.org
Prompt: Create a program to optimize freight management across multiple carriers and schedules, inspired by Stelllar Logistics' coordinated shipping approach.
Generated: DETERMINISTIC_7596a2b12187d28a
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict
from datetime import datetime, timedelta

class Carrier:
    """Class representing a shipping carrier."""
    
    def __init__(self, name: str, schedules: List[Dict[str, str]]):
        """
        Initializes a carrier with a name and a list of schedules.

        :param name: The name of the carrier.
        :param schedules: A list of dictionaries containing schedule info. 
                          Each dict should have 'departure', 'arrival', and 'capacity'.
        """
        self.name = name
        self.schedules = pd.DataFrame(schedules)
        self.schedules['departure'] = pd.to_datetime(self.schedules['departure'])
        self.schedules['arrival'] = pd.to_datetime(self.schedules['arrival'])
        self.schedules['capacity'] = self.schedules['capacity'].astype(int)

    def available_capacity(self, start_date: datetime, end_date: datetime) -> int:
        """Calculates the total available capacity within a date range."""
        available = self.schedules[
            (self.schedules['departure'] >= start_date) & 
            (self.schedules['arrival'] <= end_date)
        ]['capacity'].sum()
        return available

class FreightManager:
    """Class to manage freight across multiple carriers."""
    
    def __init__(self, carriers: List[Carrier]):
        """
        Initializes the freight manager with a list of carriers.

        :param carriers: A list of Carrier objects.
        """
        self.carriers = carriers

    def optimize_freight(self, cargo_weight: int, start_date: str, end_date: str) -> Dict[str, int]:
        """
        Optimizes freight by finding carriers with available capacity.

        :param cargo_weight: The weight of the cargo to be shipped.
        :param start_date: The starting date for shipping (format: 'YYYY-MM-DD').
        :param end_date: The ending date for shipping (format: 'YYYY-MM-DD').
        :return: A dictionary with carrier names and their available capacities.
        """
        try:
            start = pd.to_datetime(start_date)
            end = pd.to_datetime(end_date)
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e
        
        available_carriers = {}
        
        for carrier in self.carriers:
            capacity = carrier.available_capacity(start, end)
            if capacity >= cargo_weight:
                available_carriers[carrier.name] = capacity
        
        return available_carriers

# Example usage
if __name__ == "__main__":
    # Define schedules for each carrier
    carrier_data = [
        {
            'name': 'Carrier A',
            'schedules': [
                {'departure': '2023-10-01 10:00', 'arrival': '2023-10-02 10:00', 'capacity': '100'},
                {'departure': '2023-10-05 12:00', 'arrival': '2023-10-06 14:00', 'capacity': '200'},
            ]
        },
        {
            'name': 'Carrier B',
            'schedules': [
                {'departure': '2023-10-03 09:00', 'arrival': '2023-10-04 09:00', 'capacity': '150'},
                {'departure': '2023-10-04 15:00', 'arrival': '2023-10-05 17:00', 'capacity': '300'},
            ]
        }
    ]

    # Create carrier instances
    carriers = [Carrier(data['name'], data['schedules']) for data in carrier_data]

    # Create freight manager
    freight_manager = FreightManager(carriers)

    # Optimize freight
    try:
        cargo_weight = 120
        available_options = freight_manager.optimize_freight(cargo_weight, '2023-10-01', '2023-10-05')
        print("Available carriers with sufficient capacity:", available_options)
    except ValueError as e:
        print("Error:", e)
```
