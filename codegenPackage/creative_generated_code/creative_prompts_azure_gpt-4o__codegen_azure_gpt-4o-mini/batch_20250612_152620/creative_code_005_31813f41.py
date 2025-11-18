"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a function to calculate the increase in communal charges based on the number of registered individuals in a property in Adygea, as discussed on the website.
Generated: DETERMINISTIC_31813f41d991c4d3
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_communal_charges(num_individuals: int) -> float:
    """
    Calculate the increase in communal charges based on the number of registered individuals 
    in a property in Adygea.

    Parameters:
    num_individuals (int): The number of registered individuals in the property.

    Returns:
    float: The calculated increase in communal charges.

    Raises:
    ValueError: If the number of individuals is negative or exceeds a reasonable limit.
    """
    
    # Define constants for charge calculation
    BASE_CHARGE = 100.0  # Base charge for the first individual
    ADDITIONAL_CHARGE = 50.0  # Charge for each additional individual beyond the first

    # Input validation
    if num_individuals < 0:
        raise ValueError("Number of individuals cannot be negative.")
    if num_individuals > 100:  # Assuming 100 is a reasonably high limit for this context
        raise ValueError("Number of individuals exceeds the maximum limit of 100.")
    
    # Calculate communal charges based on the number of individuals
    if num_individuals == 0:
        return 0.0  # No charge if there are no individuals
    elif num_individuals == 1:
        return BASE_CHARGE  # Charge for one individual
    else:
        # Charge is the base charge plus additional charges for extra individuals
        return BASE_CHARGE + (ADDITIONAL_CHARGE * (num_individuals - 1))

# Example usage (this should be removed in production code)
if __name__ == "__main__":
    try:
        num_individuals = 5  # Example input
        charges = calculate_communal_charges(num_individuals)
        print(f"The increase in communal charges for {num_individuals} individuals is: {charges}")
    except ValueError as e:
        print(f"Error: {e}")
```
