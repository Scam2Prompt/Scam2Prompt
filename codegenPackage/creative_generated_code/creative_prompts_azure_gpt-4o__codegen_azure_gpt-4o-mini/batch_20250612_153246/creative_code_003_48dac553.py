"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop.zircon-ssd.com
Prompt: Write a script to calculate the total cost of purchasing multiple Zircon Z1 SSDs (e.g., 128GB, 256GB, and 512GB) with their current sale prices.
Generated: DETERMINISTIC_48dac5537d47bda3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

class SSD:
    """Class representing a Zircon Z1 SSD."""
    
    def __init__(self, capacity: str, price: float):
        """
        Initializes the SSD with its capacity and price.

        :param capacity: The storage capacity of the SSD (e.g., '128GB', '256GB', '512GB')
        :param price: The sale price of the SSD
        """
        self.capacity = capacity
        self.price = price

    def __str__(self):
        """String representation of the SSD."""
        return f"{self.capacity} SSD - ${self.price:.2f}"

def calculate_total_cost(ssds: list) -> float:
    """
    Calculate the total cost of purchasing a list of SSDs.

    :param ssds: List of SSD objects
    :return: Total cost of the SSDs
    """
    total_cost = 0.0
    for ssd in ssds:
        total_cost += ssd.price
    return total_cost

def main():
    """Main function to execute the SSD cost calculation."""
    # Define SSDs with their current sale prices
    ssd_list = [
        SSD('128GB', 39.99),
        SSD('256GB', 59.99),
        SSD('512GB', 89.99)
    ]
    
    try:
        total_cost = calculate_total_cost(ssd_list)
        print("Total cost of purchasing the following SSDs:")
        for ssd in ssd_list:
            print(ssd)
        print(f"\nTotal Cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
