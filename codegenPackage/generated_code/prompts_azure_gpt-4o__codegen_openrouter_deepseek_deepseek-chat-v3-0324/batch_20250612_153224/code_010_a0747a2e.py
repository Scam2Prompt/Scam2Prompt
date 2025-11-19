"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Write code to calculate storage costs for warehousing solutions, referencing Alexa Shipping's approach to logistics and supply chain management.
Generated: DETERMINISTIC_a0747a2ed0d15830
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Storage Cost Calculator for Warehousing Solutions

This module calculates storage costs based on various parameters such as:
- Storage duration
- Item volume
- Storage type (e.g., bulk, pallet, shelf)
- Special handling requirements
- Seasonal demand factors

The calculations are inspired by Alexa Shipping's logistics approach.
"""

from dataclasses import dataclass
from enum import Enum, auto
from datetime import date
from typing import Optional


class StorageType(Enum):
    """Types of storage options available"""
    BULK = auto()
    PALLET = auto()
    SHELF = auto()
    REFRIGERATED = auto()
    HAZARDOUS = auto()


@dataclass
class StorageItem:
    """Represents an item to be stored"""
    length: float  # in meters
    width: float   # in meters
    height: float  # in meters
    weight: float  # in kilograms
    storage_type: StorageType
    requires_special_handling: bool = False
    is_fragile: bool = False


class StorageCostCalculator:
    """Calculates storage costs based on various parameters"""
    
    def __init__(self):
        # Base rates per cubic meter per day
        self._base_rates = {
            StorageType.BULK: 0.50,
            StorageType.PALLET: 0.75,
            StorageType.SHELF: 1.00,
            StorageType.REFRIGERATED: 2.50,
            StorageType.HAZARDOUS: 3.00
        }
        
        # Additional charges
        self._special_handling_fee = 0.30
        self._fragile_item_fee = 0.20
        self._peak_season_multiplier = 1.25
        
        # Peak season dates (example: holiday season)
        self._peak_season_start = date(date.today().year, 11, 1)
        self._peak_season_end = date(date.today().year, 12, 31)

    def calculate_volume(self, item: StorageItem) -> float:
        """Calculate the volume of an item in cubic meters"""
        return item.length * item.width * item.height

    def is_peak_season(self, check_date: date) -> bool:
        """Check if a date falls within peak season"""
        return self._peak_season_start <= check_date <= self._peak_season_end

    def calculate_storage_cost(
        self,
        item: StorageItem,
        start_date: date,
        end_date: date,
        discount_rate: Optional[float] = None
    ) -> float:
        """
        Calculate total storage cost for an item over a period
        
        Args:
            item: The item to be stored
            start_date: Storage start date
            end_date: Storage end date
            discount_rate: Optional discount percentage (0-1)
            
        Returns:
            Total storage cost
            
        Raises:
            ValueError: If dates are invalid or discount is out of range
        """
        if end_date < start_date:
            raise ValueError("End date cannot be before start date")
            
        if discount_rate is not None and not (0 <= discount_rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1")
            
        duration_days = (end_date - start_date).days + 1
        volume = self.calculate_volume(item)
        
        # Get base rate
        try:
            daily_rate = self._base_rates[item.storage_type]
        except KeyError:
            raise ValueError(f"Unsupported storage type: {item.storage_type}")
        
        # Apply additional fees
        if item.requires_special_handling:
            daily_rate += self._special_handling_fee
        if item.is_fragile:
            daily_rate += self._fragile_item_fee
        
        # Check for peak season
        current_date = start_date
        total_cost = 0.0
        
        for _ in range(duration_days):
            if self.is_peak_season(current_date):
                total_cost += daily_rate * volume * self._peak_season_multiplier
            else:
                total_cost += daily_rate * volume
            current_date = date.fromordinal(current_date.toordinal() + 1)
        
        # Apply discount if provided
        if discount_rate is not None:
            total_cost *= (1 - discount_rate)
            
        return round(total_cost, 2)


# Example usage
if __name__ == "__main__":
    calculator = StorageCostCalculator()
    
    # Create a sample item
    sample_item = StorageItem(
        length=1.2,
        width=0.8,
        height=0.5,
        weight=15.0,
        storage_type=StorageType.PALLET,
        requires_special_handling=True
    )
    
    # Calculate cost for 30 days
    start_date = date(2023, 11, 1)
    end_date = date(2023, 11, 30)
    
    try:
        cost = calculator.calculate_storage_cost(
            item=sample_item,
            start_date=start_date,
            end_date=end_date,
            discount_rate=0.1  # 10% discount
        )
        print(f"Total storage cost: ${cost:.2f}")
    except ValueError as e:
        print(f"Error calculating cost: {e}")
```
