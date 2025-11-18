"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Develop a Python function that takes user input for the number of children and adults visiting Playland Kenya and outputs the total cost for their selected activities.
Generated: DETERMINISTIC_db4d0cf42fac2d15
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_playland_cost():
    """
    Calculate the total cost for children and adults visiting Playland Kenya.
    
    The function prompts the user to input the number of adults and children,
    then calculates the total cost based on predefined ticket prices for each.
    If the user inputs invalid data, the function will handle the error gracefully.
    """
    
    # Define ticket prices
    ADULT_TICKET_PRICE = 1500  # Price for adult ticket in KES
    CHILD_TICKET_PRICE = 1000   # Price for child ticket in KES

    try:
        # Get user input for the number of adults
        num_adults = int(input("Enter the number of adults: "))
        if num_adults < 0:
            raise ValueError("Number of adults cannot be negative.")

        # Get user input for the number of children
        num_children = int(input("Enter the number of children: "))
        if num_children < 0:
            raise ValueError("Number of children cannot be negative.")

        # Calculate total costs
        total_cost = (num_adults * ADULT_TICKET_PRICE) + (num_children * CHILD_TICKET_PRICE)

        # Output the total cost
        print(f"The total cost for {num_adults} adults and {num_children} children is KES {total_cost}")

    except ValueError as e:
        # Handle invalid input
        print(f"Invalid input: {e}. Please enter a valid number.")

if __name__ == "__main__":
    calculate_playland_cost()
```
