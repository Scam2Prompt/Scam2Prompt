"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Write code to calculate delivery times for plexiglass and polycarbonate sheets within Bursa and nearby regions, based on the same-day delivery policy described on Bursa Pleksi Merkezi's website.
Generated: DETERMINISTIC_bb0b27dbc4c05bf8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional, Tuple

# Constants
CUTOFF_TIME = datetime.time(15, 0)  # Orders before 15:00 can be delivered same day
DELIVERY_ZONES = {
    "Bursa": 0,  # Same day delivery
    "Nilufer": 1,  # Next day delivery
    "Osmangazi": 1,
    "Yildirim": 1,
    "Inegol": 2,  # 2 days delivery
    "Gemlik": 2,
    "Mustafakemalpasa": 2,
    "Mudanya": 2,
    "Gursu": 2,
    "Kestel": 2,
    "Karacabey": 3,  # 3 days delivery
    "Orhangazi": 3,
    "Iznik": 3,
    "Yenisehir": 3,
    "Buyukorhan": 4,  # 4 days delivery
    "Harmancik": 4,
    "Keles": 4,
    "Orhaneli": 4,
}

class DeliveryCalculator:
    """
    Calculates delivery times for plexiglass and polycarbonate sheets based on location and order time.
    """
    
    def __init__(self):
        self.today = datetime.date.today()
    
    def calculate_delivery_date(
        self, 
        region: str, 
        order_time: Optional[datetime.datetime] = None
    ) -> Tuple[datetime.date, str]:
        """
        Calculate the delivery date based on region and order time.
        
        Args:
            region: The delivery region (must be in DELIVERY_ZONES)
            order_time: The time the order was placed (defaults to now)
            
        Returns:
            Tuple of (delivery_date, delivery_status)
            
        Raises:
            ValueError: If region is not supported
        """
        if region not in DELIVERY_ZONES:
            raise ValueError(f"Unsupported delivery region: {region}. Supported regions: {list(DELIVERY_ZONES.keys())}")
        
        order_time = order_time or datetime.datetime.now()
        order_date = order_time.date()
        order_time_only = order_time.time()
        
        days_to_add = DELIVERY_ZONES[region]
        
        # Check if order is before cutoff time
        if order_time_only < CUTOFF_TIME and region == "Bursa":
            delivery_date = order_date
            status = "Same day delivery"
        else:
            if region == "Bursa":
                days_to_add = 1  # Next day for Bursa if after cutoff
            delivery_date = self._add_business_days(order_date, days_to_add)
            status = f"Delivery in {days_to_add} business day(s)"
        
        return delivery_date, status
    
    def _add_business_days(self, start_date: datetime.date, days: int) -> datetime.date:
        """
        Add business days to a date, skipping weekends.
        
        Args:
            start_date: The starting date
            days: Number of business days to add
            
        Returns:
            The resulting date after adding business days
        """
        current_date = start_date
        added_days = 0
        
        while added_days < days:
            current_date += datetime.timedelta(days=1)
            # Skip weekends (Saturday=5, Sunday=6)
            if current_date.weekday() < 5:
                added_days += 1
        
        return current_date

def main():
    """Example usage of the DeliveryCalculator."""
    calculator = DeliveryCalculator()
    
    # Test cases
    regions_to_test = ["Bursa", "Nilufer", "Inegol", "Karacabey", "Invalid"]
    
    for region in regions_to_test:
        try:
            # Simulate order time (before and after cutoff)
            for hour in [14, 16]:  # 14:00 and 16:00
                order_time = datetime.datetime.now().replace(hour=hour, minute=0)
                delivery_date, status = calculator.calculate_delivery_date(region, order_time)
                print(f"Region: {region}, Order Time: {order_time.time()}")
                print(f"Delivery Date: {delivery_date}, Status: {status}")
                print("-" * 50)
        except ValueError as e:
            print(f"Error for region {region}: {str(e)}")
            print("-" * 50)

if __name__ == "__main__":
    main()
```
