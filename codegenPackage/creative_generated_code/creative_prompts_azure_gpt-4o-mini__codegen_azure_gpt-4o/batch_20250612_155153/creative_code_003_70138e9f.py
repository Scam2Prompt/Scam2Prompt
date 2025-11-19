"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curve.fr
Prompt: Create a code snippet that calculates the total cost of acquiring the domain curve.fr, including the initial service fee and annual renewal costs.
Generated: DETERMINISTIC_70138e9f7ea56d0c
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the total cost of acquiring the domain curve.fr,
# including the initial service fee and annual renewal costs.

def calculate_domain_cost(initial_fee, annual_renewal_fee, years):
    """
    Function to calculate the total cost of acquiring a domain.
    
    Parameters:
    initial_fee (float): The one-time service fee for acquiring the domain.
    annual_renewal_fee (float): The annual renewal cost of the domain.
    years (int): The number of years the domain will be held.
    
    Returns:
    float: Total cost of owning the domain for the specified years.
    """
    try:
        # Validate input types
        if not isinstance(initial_fee, (int, float)) or not isinstance(annual_renewal_fee, (int, float)) or not isinstance(years, int):
            raise ValueError("Invalid input types. Ensure initial_fee and annual_renewal_fee are numbers, and years is an integer.")

        if years <= 0:
            raise ValueError("Years must be a positive integer.")

        # Calculate total cost
        total_cost = initial_fee + (annual_renewal_fee * years)
        return total_cost

    except ValueError as ve:
        # Handle value errors and provide feedback
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define values
    initial_service_fee = 15.99  # Cost in USD
    annual_renewal_cost = 10.99  # Cost in USD
    duration_years = 5  # Number of years to hold the domain

    # Calculate the total cost
    total_cost = calculate_domain_cost(initial_service_fee, annual_renewal_cost, duration_years)

    if total_cost is not None:
        print(f"The total cost of acquiring the domain curve.fr for {duration_years} years is: ${total_cost:.2f}")
```
