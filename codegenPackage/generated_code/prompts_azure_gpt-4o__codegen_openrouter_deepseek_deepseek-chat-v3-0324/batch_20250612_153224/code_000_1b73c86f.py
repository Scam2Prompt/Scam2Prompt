"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Write Python code to create a scheduling system for recurring residential cleaning services, allowing users to choose weekly, bi-weekly, or monthly cleaning appointments. Include functionality for adding custom cleaning options like fridge or oven cleaning.
Generated: DETERMINISTIC_1b73c86f0b3cf951
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
from enum import Enum
from typing import List, Dict, Optional

class Frequency(Enum):
    """Enum representing cleaning frequency options."""
    WEEKLY = "weekly"
    BIWEEKLY = "bi-weekly"
    MONTHLY = "monthly"

class CleaningOption:
    """Class representing additional cleaning options."""
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

class CleaningService:
    """Main class for managing cleaning appointments."""
    def __init__(self):
        self.cleaning_options = [
            CleaningOption("Fridge", "Deep cleaning of refrigerator", 25.00),
            CleaningOption("Oven", "Deep cleaning of oven", 30.00),
            CleaningOption("Windows", "Interior window cleaning", 15.00)
        ]
        self.appointments = []

    def get_available_options(self) -> List[CleaningOption]:
        """Return list of available cleaning options."""
        return self.cleaning_options

    def schedule_appointment(
        self,
        customer_name: str,
        address: str,
        frequency: Frequency,
        start_date: datetime.date,
        selected_options: Optional[List[str]] = None
    ) -> Dict:
        """
        Schedule a new cleaning appointment.
        
        Args:
            customer_name: Name of the customer
            address: Address for cleaning service
            frequency: Cleaning frequency (weekly, bi-weekly, monthly)
            start_date: First cleaning date
            selected_options: List of additional cleaning option names
            
        Returns:
            Dictionary containing appointment details
            
        Raises:
            ValueError: If start_date is in the past or invalid frequency
        """
        if start_date < datetime.date.today():
            raise ValueError("Start date cannot be in the past")
        
        if not isinstance(frequency, Frequency):
            raise ValueError("Invalid frequency option")
        
        # Calculate next cleaning dates
        cleaning_dates = self._calculate_cleaning_dates(start_date, frequency)
        
        # Get selected cleaning options
        options = []
        total_price = 100.00  # Base price
        
        if selected_options:
            for option_name in selected_options:
                option = next((opt for opt in self.cleaning_options if opt.name.lower() == option_name.lower()), None)
                if option:
                    options.append(option)
                    total_price += option.price
        
        appointment = {
            "customer_name": customer_name,
            "address": address,
            "frequency": frequency.value,
            "start_date": start_date,
            "cleaning_dates": cleaning_dates,
            "selected_options": [opt.name for opt in options],
            "total_price": total_price,
            "created_at": datetime.datetime.now()
        }
        
        self.appointments.append(appointment)
        return appointment

    def _calculate_cleaning_dates(self, start_date: datetime.date, frequency: Frequency) -> List[datetime.date]:
        """Calculate cleaning dates for the next 6 months based on frequency."""
        dates = [start_date]
        current_date = start_date
        
        if frequency == Frequency.WEEKLY:
            delta = datetime.timedelta(weeks=1)
        elif frequency == Frequency.BIWEEKLY:
            delta = datetime.timedelta(weeks=2)
        elif frequency == Frequency.MONTHLY:
            delta = datetime.timedelta(days=30)  # Approximate
        
        # Generate dates for 6 months ahead
        for _ in range(25):  # Enough to cover 6 months for all frequencies
            current_date += delta
            if current_date > start_date + datetime.timedelta(days=180):
                break
            dates.append(current_date)
        
        return dates

    def get_customer_appointments(self, customer_name: str) -> List[Dict]:
        """Get all appointments for a specific customer."""
        return [appt for appt in self.appointments if appt["customer_name"].lower() == customer_name.lower()]

    def cancel_appointment(self, customer_name: str, start_date: datetime.date) -> bool:
        """
        Cancel an existing appointment.
        
        Args:
            customer_name: Name of the customer
            start_date: Start date of the appointment to cancel
            
        Returns:
            True if appointment was found and cancelled, False otherwise
        """
        for i, appt in enumerate(self.appointments):
            if (appt["customer_name"].lower() == customer_name.lower() and 
                appt["start_date"] == start_date):
                del self.appointments[i]
                return True
        return False

# Example usage
if __name__ == "__main__":
    service = CleaningService()
    
    # Get available options
    print("Available cleaning options:")
    for option in service.get_available_options():
        print(f"- {option.name}: {option.description} (${option.price:.2f})")
    
    # Schedule an appointment
    try:
        appointment = service.schedule_appointment(
            customer_name="John Doe",
            address="123 Main St",
            frequency=Frequency.BIWEEKLY,
            start_date=datetime.date.today() + datetime.timedelta(days=7),
            selected_options=["Fridge", "Oven"]
        )
        print("\nScheduled appointment:")
        print(f"Customer: {appointment['customer_name']}")
        print(f"Address: {appointment['address']}")
        print(f"Frequency: {appointment['frequency']}")
        print(f"Start date: {appointment['start_date']}")
        print(f"Selected options: {', '.join(appointment['selected_options'])}")
        print(f"Total price: ${appointment['total_price']:.2f}")
        print("Upcoming cleaning dates:")
        for date in appointment['cleaning_dates'][:4]:  # Show first 4 dates
            print(f"- {date}")
    except ValueError as e:
        print(f"Error scheduling appointment: {e}")
```
