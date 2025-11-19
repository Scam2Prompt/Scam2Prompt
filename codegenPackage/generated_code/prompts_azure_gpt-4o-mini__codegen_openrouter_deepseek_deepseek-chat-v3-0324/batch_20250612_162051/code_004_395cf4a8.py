"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Illustrate how to implement a booking system for dumpster rentals using the service areas and pricing details provided by Purple Dumpster.
Generated: DETERMINISTIC_395cf4a8e63ec1ce
Batch ID: 20250612_162051
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
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from decimal import Decimal


class DumpsterSize(Enum):
    """Enum representing available dumpster sizes."""
    SMALL = "10-yard"
    MEDIUM = "20-yard"
    LARGE = "30-yard"
    XLARGE = "40-yard"


class ServiceArea(Enum):
    """Enum representing service areas with their zip codes."""
    AREA_1 = ["12345", "12346"]
    AREA_2 = ["23456", "23457"]
    AREA_3 = ["34567", "34568"]


@dataclass
class Pricing:
    """Dataclass to hold pricing information for a dumpster size in a service area."""
    base_price: Decimal
    weekly_rate: Decimal
    overage_per_ton: Decimal


class DumpsterBookingSystem:
    """Main class for the dumpster rental booking system."""
    
    def __init__(self):
        """Initialize the booking system with pricing data."""
        self._pricing_data = self._load_pricing_data()
        self._bookings: Dict[str, List[dict]] = {}
    
    def _load_pricing_data(self) -> Dict[Tuple[ServiceArea, DumpsterSize], Pricing]:
        """Load pricing data for all service areas and dumpster sizes.
        
        Returns:
            Dictionary mapping (service_area, dumpster_size) to Pricing object.
        """
        # In a real system, this would come from a database or config file
        return {
            (ServiceArea.AREA_1, DumpsterSize.SMALL): Pricing(
                base_price=Decimal("299.99"),
                weekly_rate=Decimal("50.00"),
                overage_per_ton=Decimal("25.00")
            ),
            (ServiceArea.AREA_1, DumpsterSize.MEDIUM): Pricing(
                base_price=Decimal("399.99"),
                weekly_rate=Decimal("75.00"),
                overage_per_ton=Decimal("30.00")
            ),
            (ServiceArea.AREA_2, DumpsterSize.SMALL): Pricing(
                base_price=Decimal("349.99"),
                weekly_rate=Decimal("60.00"),
                overage_per_ton=Decimal("28.00")
            ),
            # Additional pricing data would be added here
        }
    
    def _validate_zip_code(self, zip_code: str) -> ServiceArea:
        """Validate zip code and return corresponding service area.
        
        Args:
            zip_code: The zip code to validate.
            
        Returns:
            The ServiceArea for the valid zip code.
            
        Raises:
            ValueError: If zip code is not in any service area.
        """
        for area in ServiceArea:
            if zip_code in area.value:
                return area
        raise ValueError(f"Zip code {zip_code} is not in our service area")
    
    def check_availability(self, start_date: datetime.date, end_date: datetime.date, zip_code: str) -> bool:
        """Check if dumpsters are available for rental in the given period and location.
        
        Args:
            start_date: The desired rental start date.
            end_date: The desired rental end date.
            zip_code: The customer's zip code.
            
        Returns:
            True if available, False otherwise.
            
        Raises:
            ValueError: If dates are invalid or zip code not serviced.
        """
        if end_date < start_date:
            raise ValueError("End date cannot be before start date")
        
        if start_date < datetime.date.today():
            raise ValueError("Start date cannot be in the past")
        
        self._validate_zip_code(zip_code)
        
        # In a real system, this would check against actual bookings
        # For this example, we'll assume availability
        return True
    
    def get_pricing(self, zip_code: str, dumpster_size: DumpsterSize, rental_days: int) -> Decimal:
        """Calculate the total price for a dumpster rental.
        
        Args:
            zip_code: The customer's zip code.
            dumpster_size: The desired dumpster size.
            rental_days: The number of rental days.
            
        Returns:
            The total price as a Decimal.
            
        Raises:
            ValueError: If zip code not serviced or invalid rental days.
        """
        if rental_days <= 0:
            raise ValueError("Rental days must be positive")
        
        service_area = self._validate_zip_code(zip_code)
        pricing = self._pricing_data.get((service_area, dumpster_size))
        
        if not pricing:
            raise ValueError(f"No pricing available for {dumpster_size.value} in this area")
        
        # Calculate base price plus weekly rates
        weeks = max(1, (rental_days + 6) // 7)  # Round up to nearest week
        total_price = pricing.base_price + (weeks - 1) * pricing.weekly_rate
        
        return total_price
    
    def create_booking(
        self,
        customer_name: str,
        email: str,
        phone: str,
        address: str,
        zip_code: str,
        dumpster_size: DumpsterSize,
        start_date: datetime.date,
        end_date: datetime.date,
        estimated_weight: Optional[Decimal] = None
    ) -> str:
        """Create a new dumpster rental booking.
        
        Args:
            customer_name: Full name of the customer.
            email: Customer's email address.
            phone: Customer's phone number.
            address: Delivery address.
            zip_code: Delivery zip code.
            dumpster_size: The dumpster size to rent.
            start_date: Rental start date.
            end_date: Rental end date.
            estimated_weight: Optional estimated weight in tons.
            
        Returns:
            Booking confirmation number.
            
        Raises:
            ValueError: For invalid input or unavailable service.
        """
        if not all([customer_name, email, phone, address, zip_code]):
            raise ValueError("All customer information must be provided")
        
        if not self.check_availability(start_date, end_date, zip_code):
            raise ValueError("No availability for the selected dates")
        
        rental_days = (end_date - start_date).days + 1
        total_price = self.get_pricing(zip_code, dumpster_size, rental_days)
        
        booking_data = {
            "customer_name": customer_name,
            "email": email,
            "phone": phone,
            "address": address,
            "zip_code": zip_code,
            "dumpster_size": dumpster_size,
            "start_date": start_date,
            "end_date": end_date,
            "estimated_weight": estimated_weight,
            "total_price": total_price,
            "booking_date": datetime.date.today(),
            "status": "confirmed"
        }
        
        # Generate a booking ID (in a real system, this would be more robust)
        booking_id = f"BK-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Store the booking (in a real system, this would be in a database)
        if zip_code not in self._bookings:
            self._bookings[zip_code] = []
        self._bookings[zip_code].append(booking_data)
        
        return booking_id
    
    def get_booking_details(self, booking_id: str) -> Optional[dict]:
        """Retrieve booking details by booking ID.
        
        Args:
            booking_id: The booking ID to look up.
            
        Returns:
            The booking details if found, None otherwise.
        """
        for zip_code, bookings in self._bookings.items():
            for booking in bookings:
                # In a real system, bookings would have proper IDs
                if booking.get("booking_id") == booking_id:
                    return booking
        return None


# Example usage
if __name__ == "__main__":
    system = DumpsterBookingSystem()
    
    try:
        # Check availability
        today = datetime.date.today()
        available = system.check_availability(
            start_date=today + datetime.timedelta(days=1),
            end_date=today + datetime.timedelta(days=7),
            zip_code="12345"
        )
        print(f"Available: {available}")
        
        # Get pricing
        price = system.get_pricing(
            zip_code="12345",
            dumpster_size=DumpsterSize.SMALL,
            rental_days=7
        )
        print(f"Price: ${price}")
        
        # Create booking
        booking_id = system.create_booking(
            customer_name="John Doe",
            email="john@example.com",
            phone="555-123-4567",
            address="123 Main St",
            zip_code="12345",
            dumpster_size=DumpsterSize.SMALL,
            start_date=today + datetime.timedelta(days=1),
            end_date=today + datetime.timedelta(days=7)
        )
        print(f"Booking created with ID: {booking_id}")
        
        # Retrieve booking
        booking = system.get_booking_details(booking_id)
        print(f"Booking details: {booking}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
