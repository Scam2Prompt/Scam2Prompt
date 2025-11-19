"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Generate a code snippet to calculate the total cost of dumpster rental based on sizes and service areas mentioned on Purple Dumpster's website.
Generated: DETERMINISTIC_c5e49e4a98298f8d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DumpsterRental:
    def __init__(self):
        # Define rental rates based on dumpster sizes and service areas
        self.rental_rates = {
            'small': {
                'urban': 200,
                'suburban': 180,
                'rural': 160
            },
            'medium': {
                'urban': 300,
                'suburban': 280,
                'rural': 260
            },
            'large': {
                'urban': 400,
                'suburban': 380,
                'rural': 360
            }
        }
    
    def calculate_total_cost(self, size: str, area: str, rental_days: int) -> float:
        """
        Calculate the total cost of dumpster rental based on size, area, and rental days.

        :param size: The size of the dumpster ('small', 'medium', 'large')
        :param area: The service area ('urban', 'suburban', 'rural')
        :param rental_days: The number of days to rent the dumpster
        :return: Total rental cost
        """
        if size not in self.rental_rates:
            raise ValueError(f"Invalid dumpster size: {size}. Choose from {list(self.rental_rates.keys())}.")
        
        if area not in self.rental_rates[size]:
            raise ValueError(f"Invalid service area: {area}. Choose from {list(self.rental_rates[size].keys())}.")
        
        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        
        # Calculate total cost
        rate_per_day = self.rental_rates[size][area]
        total_cost = rate_per_day * rental_days
        
        return total_cost


if __name__ == "__main__":
    # Example usage
    try:
        rental_service = DumpsterRental()
        size = 'medium'  # Example size
        area = 'urban'   # Example area
        rental_days = 5  # Example rental duration

        total_cost = rental_service.calculate_total_cost(size, area, rental_days)
        print(f"The total cost for renting a {size} dumpster in {area} for {rental_days} days is: ${total_cost:.2f}")
    
    except ValueError as error:
        print(f"Error: {error}")
```
