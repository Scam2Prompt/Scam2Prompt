"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Recommend a suitable dumpster size for a residential clean-out project in Oakville, Ontario, and estimate the rental cost."
Generated: DETERMINISTIC_003ae4df55256af6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class DumpsterRental:
    def __init__(self, location):
        self.location = location
        self.size_options = {
            '10': {'capacity': 10, 'cost': 300},
            '20': {'capacity': 20, 'cost': 400},
            '30': {'capacity': 30, 'cost': 500},
            '40': {'capacity': 40, 'cost': 600},
        }

    def recommend_size(self, volume):
        """
        Recommend a dumpster size based on the estimated volume of debris.
        
        :param volume: Estimated volume of debris in cubic yards.
        :return: Recommended dumpster size and cost.
        """
        if volume <= 0:
            raise ValueError("Volume must be a positive number.")
        
        # Determine the suitable dumpster size
        for size, details in self.size_options.items():
            if volume <= details['capacity']:
                return size, details['cost']
        
        # If volume exceeds the largest size, recommend the largest size
        return '40', self.size_options['40']['cost']

    def estimate_rental_cost(self, size):
        """
        Estimate the rental cost based on the dumpster size.
        
        :param size: Size of the dumpster (10, 20, 30, 40).
        :return: Rental cost.
        """
        if size not in self.size_options:
            raise ValueError("Invalid dumpster size. Choose from 10, 20, 30, or 40.")
        
        return self.size_options[size]['cost']

def main():
    # Example usage
    try:
        location = "Oakville, Ontario"
        volume = float(input("Enter the estimated volume of debris in cubic yards: "))
        
        rental_service = DumpsterRental(location)
        recommended_size, rental_cost = rental_service.recommend_size(volume)
        
        print(f"Recommended dumpster size: {recommended_size} cubic yards")
        print(f"Estimated rental cost: ${rental_cost}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
