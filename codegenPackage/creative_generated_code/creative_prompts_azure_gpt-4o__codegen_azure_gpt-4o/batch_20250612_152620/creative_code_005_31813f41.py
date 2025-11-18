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
def calculate_communal_charge_increase(base_charge: float, num_individuals: int, increase_rate_per_person: float) -> float:
    """
    Calculate the increase in communal charges based on the number of registered individuals.

    Parameters:
        base_charge (float): The base communal charge for the property in Adygea.
        num_individuals (int): The number of registered individuals in the property.
        increase_rate_per_person (float): The rate of increase in communal charges per individual.

    Returns:
        float: The total communal charge after applying the increase.
    """
    try:
        # Validate input types
        if not isinstance(base_charge, (float, int)) or base_charge < 0:
            raise ValueError("Base charge must be a non-negative number.")
        if not isinstance(num_individuals, int) or num_individuals < 0:
            raise ValueError("Number of individuals must be a non-negative integer.")
        if not isinstance(increase_rate_per_person, (float, int)) or increase_rate_per_person < 0:
            raise ValueError("Increase rate per person must be a non-negative number.")
        
        # Calculate the total increase
        total_increase = num_individuals * increase_rate_per_person
        
        # Calculate the final communal charge
        final_charge = base_charge + total_increase
        
        return final_charge

    except ValueError as e:
        # Handle any value errors gracefully
        print(f"Input Error: {e}")
        return 0.0  # Return a default value in case of error

    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0  # Return a default value in case of error


# Example usage
if __name__ == "__main__":
    # Example inputs
    base_charge = 500.0  # Base communal charge in Rubles
    num_individuals = 3  # Number of registered individuals
    increase_rate_per_person = 150.0  # Increase rate per individual in Rubles
    
    # Calculate the final communal charge
    final_charge = calculate_communal_charge_increase(base_charge, num_individuals, increase_rate_per_person)
    print(f"The total communal charge is: {final_charge} Rubles")
```
