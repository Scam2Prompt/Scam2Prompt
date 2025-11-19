"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Write Python code to simulate the rental booking process for Rigid Inflatable Boats (RIBs) in Greece, incorporating options for fleet selection like "Rock 36 MIAMI" and "Rock 36 AELIA."
Generated: DETERMINISTIC_c6c9df7512a15235
Batch ID: 20250612_150323
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
from typing import Dict, List, Optional


class RIBModel(Enum):
    """Enum representing available RIB models for rental."""
    ROCK_36_MIAMI = "Rock 36 MIAMI"
    ROCK_36_AELIA = "Rock 36 AELIA"


class RentalStatus(Enum):
    """Enum representing rental status."""
    AVAILABLE = "Available"
    BOOKED = "Booked"
    MAINTENANCE = "Maintenance"


class RIB:
    """Class representing a Rigid Inflatable Boat (RIB)."""
    
    def __init__(self, model: RIBModel, name: str, capacity: int, daily_rate: float):
        """
        Initialize a RIB instance.
        
        Args:
            model: RIBModel enum representing the model
            name: Unique name/identifier for the boat
            capacity: Maximum passenger capacity
            daily_rate: Daily rental rate in EUR
        """
        self.model = model
        self.name = name
        self.capacity = capacity
        self.daily_rate = daily_rate
        self.status = RentalStatus.AVAILABLE
        self.bookings: List[Dict] = []

    def is_available(self, start_date: datetime.date, end_date: datetime.date) -> bool:
        """
        Check if the RIB is available for the given date range.
        
        Args:
            start_date: Start date of the rental period
            end_date: End date of the rental period
            
        Returns:
            bool: True if available, False otherwise
        """
        if self.status != RentalStatus.AVAILABLE:
            return False
            
        for booking in self.bookings:
            booking_start = booking["start_date"]
            booking_end = booking["end_date"]
            
            if (start_date <= booking_end) and (end_date >= booking_start):
                return False
                
        return True

    def book(self, customer_name: str, start_date: datetime.date, end_date: datetime.date) -> bool:
        """
        Book the RIB for the given date range if available.
        
        Args:
            customer_name: Name of the customer making the booking
            start_date: Start date of the rental period
            end_date: End date of the rental period
            
        Returns:
            bool: True if booking was successful, False otherwise
        """
        if not self.is_available(start_date, end_date):
            return False
            
        self.bookings.append({
            "customer_name": customer_name,
            "start_date": start_date,
            "end_date": end_date,
            "booking_date": datetime.date.today()
        })
        
        return True


class RentalAgency:
    """Class representing a rental agency managing a fleet of RIBs."""
    
    def __init__(self):
        """Initialize the rental agency with an empty fleet."""
        self.fleet: Dict[str, RIB] = {}
        
    def add_rib(self, rib: RIB) -> bool:
        """
        Add a RIB to the fleet.
        
        Args:
            rib: RIB instance to add
            
        Returns:
            bool: True if added successfully, False if RIB with same name exists
        """
        if rib.name in self.fleet:
            return False
            
        self.fleet[rib.name] = rib
        return True
        
    def get_available_ribs(self, model: Optional[RIBModel] = None, 
                          start_date: Optional[datetime.date] = None,
                          end_date: Optional[datetime.date] = None) -> List[RIB]:
        """
        Get available RIBs optionally filtered by model and date range.
        
        Args:
            model: Optional RIBModel to filter by
            start_date: Optional start date for availability check
            end_date: Optional end date for availability check
            
        Returns:
            List[RIB]: List of available RIBs matching criteria
        """
        available_ribs = []
        
        for rib in self.fleet.values():
            if rib.status != RentalStatus.AVAILABLE:
                continue
                
            if model and rib.model != model:
                continue
                
            if start_date and end_date:
                if not rib.is_available(start_date, end_date):
                    continue
                    
            available_ribs.append(rib)
            
        return available_ribs
        
    def book_rib(self, rib_name: str, customer_name: str, 
                 start_date: datetime.date, end_date: datetime.date) -> bool:
        """
        Book a specific RIB by name.
        
        Args:
            rib_name: Name of the RIB to book
            customer_name: Name of the customer making the booking
            start_date: Start date of the rental period
            end_date: End date of the rental period
            
        Returns:
            bool: True if booking was successful, False otherwise
        """
        if rib_name not in self.fleet:
            return False
            
        rib = self.fleet[rib_name]
        return rib.book(customer_name, start_date, end_date)


def main():
    """Main function to demonstrate the rental booking process."""
    # Initialize rental agency
    agency = RentalAgency()
    
    # Add some RIBs to the fleet
    rib1 = RIB(RIBModel.ROCK_36_MIAMI, "Miami-1", 8, 350.0)
    rib2 = RIB(RIBModel.ROCK_36_MIAMI, "Miami-2", 8, 350.0)
    rib3 = RIB(RIBModel.ROCK_36_AELIA, "Aelia-1", 10, 400.0)
    
    agency.add_rib(rib1)
    agency.add_rib(rib2)
    agency.add_rib(rib3)
    
    # Get today's date and future dates for booking
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    two_weeks = today + datetime.timedelta(days=14)
    
    # Display available RIBs
    print("Available RIBs for booking:")
    available_ribs = agency.get_available_ribs()
    for rib in available_ribs:
        print(f"- {rib.name} ({rib.model.value}), Capacity: {rib.capacity}, Rate: €{rib.daily_rate}/day")
    
    # Book a RIB
    customer = "John Smith"
    booking_success = agency.book_rib("Miami-1", customer, next_week, two_weeks)
    
    if booking_success:
        print(f"\nBooking successful for {customer} on Miami-1 from {next_week} to {two_weeks}")
    else:
        print("\nBooking failed - RIB not available for the selected dates")


if __name__ == "__main__":
    main()
```
