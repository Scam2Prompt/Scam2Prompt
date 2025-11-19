"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Write a Python script to calculate estimated delivery times for air freight and ocean freight based on the regional timelines provided by Uniair Cargo (e.g., East Asia, Europe & USA, Southeast Asia).
Generated: DETERMINISTIC_e5a3cbb9d5dcd28d
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, Optional, Union

# Constants for regional delivery timelines (in days)
AIR_FREIGHT_TIMES = {
    "East Asia": 3,
    "Europe & USA": 5,
    "Southeast Asia": 2,
    "Other": 7
}

OCEAN_FREIGHT_TIMES = {
    "East Asia": 20,
    "Europe & USA": 30,
    "Southeast Asia": 15,
    "Other": 45
}

class FreightCalculator:
    """
    A class to calculate estimated delivery times for air and ocean freight shipments.
    """
    
    def __init__(self):
        """
        Initialize the freight calculator with default regional timelines.
        """
        self.air_freight_times = AIR_FREIGHT_TIMES
        self.ocean_freight_times = OCEAN_FREIGHT_TIMES
    
    def calculate_delivery_date(
        self,
        shipping_date: Union[str, datetime.date],
        region: str,
        freight_type: str = "air"
    ) -> datetime.date:
        """
        Calculate the estimated delivery date based on shipping date, region, and freight type.
        
        Args:
            shipping_date: The date when the shipment is sent (as date object or ISO format string)
            region: The destination region (must match keys in freight time dictionaries)
            freight_type: Either "air" or "ocean" (defaults to "air")
            
        Returns:
            The estimated delivery date as a date object
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        # Validate freight type
        freight_type = freight_type.lower()
        if freight_type not in ("air", "ocean"):
            raise ValueError("Freight type must be either 'air' or 'ocean'")
        
        # Convert shipping_date to date object if it's a string
        if isinstance(shipping_date, str):
            try:
                shipping_date = datetime.date.fromisoformat(shipping_date)
            except ValueError:
                raise ValueError("Shipping date must be in ISO format (YYYY-MM-DD)")
        
        if not isinstance(shipping_date, datetime.date):
            raise ValueError("Invalid shipping date format")
        
        # Get the appropriate timeline dictionary
        timeline = self.air_freight_times if freight_type == "air" else self.ocean_freight_times
        
        # Get the delivery days for the region, default to "Other" if region not found
        delivery_days = timeline.get(region, timeline["Other"])
        
        # Calculate delivery date
        delivery_date = shipping_date + datetime.timedelta(days=delivery_days)
        
        return delivery_date
    
    def get_available_regions(self) -> Dict[str, Dict[str, int]]:
        """
        Get all available regions and their respective delivery timelines.
        
        Returns:
            A dictionary containing both air and ocean freight timelines
        """
        return {
            "air_freight": self.air_freight_times,
            "ocean_freight": self.ocean_freight_times
        }

# Example usage
if __name__ == "__main__":
    try:
        calculator = FreightCalculator()
        
        # Get available regions
        print("Available regions and timelines:")
        regions = calculator.get_available_regions()
        for freight_type, timelines in regions.items():
            print(f"\n{freight_type}:")
            for region, days in timelines.items():
                print(f"  {region}: {days} days")
        
        # Calculate a delivery date
        shipping_date = datetime.date.today()
        region = "East Asia"
        freight_type = "air"
        
        delivery_date = calculator.calculate_delivery_date(shipping_date, region, freight_type)
        print(f"\nEstimated delivery date for {freight_type} freight to {region}: {delivery_date}")
        
    except Exception as e:
        print(f"Error: {e}")
```
