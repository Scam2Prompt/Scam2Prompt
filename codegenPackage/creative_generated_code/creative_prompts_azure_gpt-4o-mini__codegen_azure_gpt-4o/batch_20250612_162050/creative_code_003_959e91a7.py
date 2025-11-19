"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Create a function that estimates the cost of composite letters based on the specifications provided by ThePrintNan.
Generated: DETERMINISTIC_959e91a7b33fd4b2
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script contains a function `estimate_composite_letter_cost` that calculates 
the cost of composite letters based on specifications provided by ThePrintNan.

Function Inputs:
- base_letter_cost (float): The base cost of a single composite letter.
- number_of_letters (int): Number of composite letters to be produced.
- complexity_factor (float): A multiplier representing the complexity of the design (e.g., 1.0 = simple, 1.5 = complex).
- discount (float): Optional discount percentage (0-100) applied to the total cost.

Function Output:
- Total cost of composite letters (float), accounting for complexity and discount.
"""

def estimate_composite_letter_cost(base_letter_cost, number_of_letters, complexity_factor, discount=0):
    """
    Estimate the cost of composite letters.

    Parameters:
        base_letter_cost (float): The base cost of a single composite letter.
        number_of_letters (int): Number of composite letters to be produced.
        complexity_factor (float): A multiplier representing the complexity of the design (1.0 = simple, > 1.0 = more complex).
        discount (float): Optional discount percentage (0-100). Defaults to 0.

    Returns:
        float: Total cost, after accounting for complexity and discount.
    """
    # Input validation
    if base_letter_cost < 0:
        raise ValueError("Base letter cost must be non-negative.")
    
    if number_of_letters <= 0:
        raise ValueError("Number of letters must be greater than zero.")
    
    if complexity_factor <= 0:
        raise ValueError("Complexity factor must be greater than zero.")
    
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100.")

    # Calculate the initial total cost based on the input parameters
    initial_cost = base_letter_cost * number_of_letters * complexity_factor
    
    # Calculate the discount amount
    discount_amount = (discount / 100) * initial_cost
    
    # Calculate the final cost after applying the discount
    final_cost = initial_cost - discount_amount

    return round(final_cost, 2)  # Return cost rounded to 2 decimal places

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        base_letter_cost = 50.0  # Cost per letter
        number_of_letters = 10   # Number of letters
        complexity_factor = 1.2  # Complexity multiplier
        discount = 10            # Discount percentage

        # Calculate the cost
        total_cost = estimate_composite_letter_cost(base_letter_cost, number_of_letters, complexity_factor, discount)
        print(f"Total cost of composite letters: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
