"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Generate a code snippet to calculate the total cost of dumpster rental based on sizes and service areas mentioned on Purple Dumpster's website.
Generated: DETERMINISTIC_c5e49e4a98298f8d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DumpsterRentalCalculator:
    """
    A class to calculate the total cost of dumpster rental based on size and service area.
    
    Attributes:
        dumpster_sizes (dict): A dictionary mapping dumpster sizes to their base prices.
        service_areas (dict): A dictionary mapping service areas to their additional fees.
    """
    
    def __init__(self):
        """Initialize the calculator with dumpster sizes and service areas."""
        self.dumpster_sizes = {
            '10-yard': 300,
            '15-yard': 350,
            '20-yard': 400,
            '30-yard': 500,
            '40-yard': 600
        }
        
        self.service_areas = {
            'local': 0,
            'regional': 50,
            'national': 100
        }
    
    def calculate_total_cost(self, size: str, area: str, rental_days: int) -> float:
        """
        Calculate the total cost of dumpster rental.
        
        Args:
            size (str): The size of the dumpster (e.g., '10-yard').
            area (str): The service area (e.g., 'local').
            rental_days (int): The number of rental days.
            
        Returns:
            float: The total cost of the rental.
            
        Raises:
            ValueError: If the size or area is not valid, or rental_days is not positive.
        """
        if size not in self.dumpster_sizes:
            raise ValueError(f"Invalid dumpster size. Available sizes: {list(self.dumpster_sizes.keys())}")
        
        if area not in self.service_areas:
            raise ValueError(f"Invalid service area. Available areas: {list(self.service_areas.keys())}")
        
        if rental_days <= 0:
            raise ValueError("Rental days must be a positive integer.")
        
        base_price = self.dumpster_sizes[size]
        area_fee = self.service_areas[area]
        
        total_cost = (base_price + area_fee) * rental_days
        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = DumpsterRentalCalculator()
    
    try:
        size = '20-yard'
        area = 'regional'
        rental_days = 7
        
        total_cost = calculator.calculate_total_cost(size, area, rental_days)
        print(f"Total cost for {size} dumpster in {area} area for {rental_days} days: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
