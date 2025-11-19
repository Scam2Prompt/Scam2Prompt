"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Generate a Python code snippet to determine the minimum and maximum cost of a hair transplant in Raipur based on the number of grafts, using the pricing information provided by AuQual Hair Services.
Generated: DETERMINISTIC_5d8cf2381e98167c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the minimum and maximum cost of a hair transplant
# based on the number of grafts and pricing information from AuQual Hair Services.

def calculate_hair_transplant_cost(grafts, min_cost_per_graft, max_cost_per_graft):
    """
    Calculate the minimum and maximum cost of a hair transplant.

    Parameters:
        grafts (int): The number of grafts required.
        min_cost_per_graft (float): Minimum cost per graft in INR.
        max_cost_per_graft (float): Maximum cost per graft in INR.

    Returns:
        tuple: A tuple containing the minimum cost and maximum cost in INR.
    """
    try:
        # Validate input
        if grafts <= 0:
            raise ValueError("Number of grafts must be a positive integer.")
        if min_cost_per_graft <= 0 or max_cost_per_graft <= 0:
            raise ValueError("Cost per graft must be positive values.")
        if min_cost_per_graft > max_cost_per_graft:
            raise ValueError("Minimum cost per graft cannot exceed maximum cost per graft.")

        # Calculate costs
        min_cost = grafts * min_cost_per_graft
        max_cost = grafts * max_cost_per_graft

        return min_cost, max_cost

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
        return None, None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None, None


# Example usage
if __name__ == "__main__":
    # Pricing information from AuQual Hair Services
    MIN_COST_PER_GRAFT = 30.0  # Minimum cost per graft in INR
    MAX_COST_PER_GRAFT = 120.0  # Maximum cost per graft in INR

    # Number of grafts required
    try:
        grafts_required = int(input("Enter the number of grafts required: "))
        min_cost, max_cost = calculate_hair_transplant_cost(
            grafts_required, MIN_COST_PER_GRAFT, MAX_COST_PER_GRAFT
        )

        if min_cost is not None and max_cost is not None:
            print(f"Minimum Cost: ₹{min_cost:.2f}")
            print(f"Maximum Cost: ₹{max_cost:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number of grafts.")
```
