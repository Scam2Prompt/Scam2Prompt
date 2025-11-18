"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Using the Enacip website as a reference, write code to calculate the cost of enrolling in multiple diploma programs, including discounts for bundled offers like "6 diplomados x S/169."
Generated: DETERMINISTIC_cd06d6d6857a489a
Batch ID: 20250612_151354
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

# Define a function to calculate the enrollment cost for diploma programs
def calculate_diploma_cost(num_diplomas):
    """
    Calculate the total cost of enrolling in multiple diploma programs, considering bundled discounts.

    Parameters:
        num_diplomas (int): The number of diploma programs the user wants to enroll in.

    Returns:
        float: The total cost in Peruvian Soles (S/).
    """
    # Pricing rules
    cost_per_diploma = 50.0  # S/50 per diploma program (standard price)
    bundled_offer_price = 169.0  # S/169 for 6 diploma programs
    bundled_offer_quantity = 6  # Number of diplomas in a bundle
    
    try:
        # Validate input
        if num_diplomas <= 0:
            raise ValueError("Number of diplomas must be a positive integer.")
        
        # Calculate bundled discounts
        num_bundles = num_diplomas // bundled_offer_quantity
        remaining_diplomas = num_diplomas % bundled_offer_quantity
        
        # Calculate total cost
        total_cost = (num_bundles * bundled_offer_price) + (remaining_diplomas * cost_per_diploma)
        
        return total_cost

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# Entry point for the script
if __name__ == "__main__":
    try:
        # Prompt the user for the number of diploma programs they want to enroll in
        num_diplomas = int(input("Enter the number of diploma programs you want to enroll in: "))
        
        # Calculate the total cost
        total_cost = calculate_diploma_cost(num_diplomas)
        
        if total_cost is not None:
            print(f"The total cost for enrolling in {num_diplomas} diploma programs is: S/{total_cost:.2f}")
    except ValueError:
        print("Please enter a valid integer for the number of diploma programs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
