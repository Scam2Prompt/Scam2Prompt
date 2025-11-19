"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Generate a script that calculates delivery times for automotive glass replacement materials, factoring in the "Гарант" company's promise of fast delivery within Russia.
Generated: DETERMINISTIC_06685cb1506439f5
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Dict, Optional, Tuple

class DeliveryRegion(Enum):
    """Enum representing different delivery regions in Russia."""
    CENTRAL = "Central"
    NORTHWEST = "Northwest"
    SOUTH = "South"
    VOLGA = "Volga"
    URAL = "Ural"
    SIBERIA = "Siberia"
    FAR_EAST = "Far East"

class DeliveryCalculator:
    """
    Calculates delivery times for automotive glass replacement materials 
    based on region and order time for "Гарант" company.
    """
    
    # Base delivery times in days for each region
    REGION_DELIVERY_TIMES = {
        DeliveryRegion.CENTRAL: 1,
        DeliveryRegion.NORTHWEST: 2,
        DeliveryRegion.SOUTH: 2,
        DeliveryRegion.VOLGA: 3,
        DeliveryRegion.URAL: 4,
        DeliveryRegion.SIBERIA: 5,
        DeliveryRegion.FAR_EAST: 7
    }
    
    # Cutoff time for same-day processing (14:00 local time)
    CUTOFF_TIME = datetime.time(14, 0)
    
    def __init__(self):
        """Initialize the delivery calculator."""
        pass
    
    def calculate_delivery_date(
        self,
        order_datetime: datetime.datetime,
        region: DeliveryRegion,
        express: bool = False
    ) -> Tuple[datetime.date, str]:
        """
        Calculate the delivery date based on order time and region.
        
        Args:
            order_datetime: The date and time when the order was placed.
            region: The delivery region.
            express: Whether express delivery is selected (50% faster).
            
        Returns:
            A tuple containing:
                - delivery_date: The estimated delivery date
                - delivery_message: A human-readable delivery estimate
            
        Raises:
            ValueError: If order_datetime is in the future or region is invalid.
        """
        # Validate inputs
        current_datetime = datetime.datetime.now()
        if order_datetime > current_datetime:
            raise ValueError("Order datetime cannot be in the future")
        
        if not isinstance(region, DeliveryRegion):
            raise ValueError("Invalid delivery region")
        
        # Calculate base delivery days
        base_days = self.REGION_DELIVERY_TIMES[region]
        
        # Apply express delivery reduction if selected
        if express:
            base_days = max(1, base_days // 2)
        
        # Check if order was placed before cutoff time
        order_time = order_datetime.time()
        if order_time < self.CUTOFF_TIME:
            # Order processed same day
            delivery_days = base_days
        else:
            # Order processed next business day
            delivery_days = base_days + 1
        
        # Calculate delivery date
        delivery_date = order_datetime.date() + datetime.timedelta(days=delivery_days)
        
        # Adjust for weekends (company doesn't deliver on weekends)
        delivery_date = self._adjust_for_weekend(delivery_date)
        
        # Generate delivery message
        if delivery_days == 1:
            delivery_message = "Next business day delivery"
        else:
            delivery_message = f"Estimated {delivery_days} business days delivery"
            
        if express:
            delivery_message += " (express)"
        
        return delivery_date, delivery_message
    
    def _adjust_for_weekend(self, date: datetime.date) -> datetime.date:
        """
        Adjust the delivery date to skip weekends.
        
        Args:
            date: The original delivery date.
            
        Returns:
            The adjusted delivery date (weekday).
        """
        while date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            date += datetime.timedelta(days=1)
        return date

# Example usage
if __name__ == "__main__":
    try:
        calculator = DeliveryCalculator()
        
        # Test cases
        test_cases = [
            (datetime.datetime(2023, 12, 1, 10, 0), DeliveryRegion.CENTRAL, False),
            (datetime.datetime(2023, 12, 1, 15, 0), DeliveryRegion.NORTHWEST, True),
            (datetime.datetime(2023, 12, 1, 9, 0), DeliveryRegion.FAR_EAST, False),
        ]
        
        for order_time, region, express in test_cases:
            delivery_date, message = calculator.calculate_delivery_date(
                order_time, region, express
            )
            print(f"Order at {order_time} to {region.value}:")
            print(f"  Delivery Date: {delivery_date.strftime('%Y-%m-%d')}")
            print(f"  Estimate: {message}")
            print()
            
    except Exception as e:
        print(f"Error calculating delivery: {str(e)}")
```
