"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Develop a script to simulate adding extra baggage to a reservation for airlines like Swiss Air and Spirit Airlines, based on the baggage policies outlined on Airlines Manage Booking.
Generated: DETERMINISTIC_c831ca8fa691448a
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Airline:
    """Base class for airlines with baggage policies."""
    
    def __init__(self, name):
        """Initialize the airline with a name."""
        self.name = name
        self.baggage_allowance = 0  # Default baggage allowance in kg
        self.extra_baggage_fee = 0  # Fee per kg for extra baggage

    def set_baggage_policy(self, allowance, fee):
        """Set the baggage policy for the airline."""
        self.baggage_allowance = allowance
        self.extra_baggage_fee = fee

    def calculate_extra_baggage_fee(self, extra_kg):
        """Calculate the fee for extra baggage."""
        if extra_kg < 0:
            raise ValueError("Extra baggage cannot be negative.")

        return extra_kg * self.extra_baggage_fee


class SwissAir(Airline):
    """Swiss Air's specific baggage policy."""
    
    def __init__(self):
        """Initialize Swiss Air with its baggage policy."""
        super().__init__("Swiss Air")
        self.set_baggage_policy(23, 100)  # 23 kg allowance, $100 per extra kg


class SpiritAirlines(Airline):
    """Spirit Airlines' specific baggage policy."""
    
    def __init__(self):
        """Initialize Spirit Airlines with its baggage policy."""
        super().__init__("Spirit Airlines")
        self.set_baggage_policy(18, 50)  # 18 kg allowance, $50 per extra kg


def main():
    """Main function to simulate baggage addition for airlines."""
    airlines = {
        "Swiss Air": SwissAir(),
        "Spirit Airlines": SpiritAirlines()
    }

    airline_choice = input("Enter the airline (Swiss Air / Spirit Airlines): ")
    if airline_choice not in airlines:
        print("Invalid airline selection.")
        return

    try:
        extra_baggage_kg = float(input("Enter the extra baggage weight in kg: "))
        airline = airlines[airline_choice]
        if extra_baggage_kg > 0:
            fee = airline.calculate_extra_baggage_fee(extra_baggage_kg)
            print(f"Extra baggage fee for {airline.name}: ${fee:.2f}")
        else:
            print("No extra baggage fee as weight is zero or negative.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
