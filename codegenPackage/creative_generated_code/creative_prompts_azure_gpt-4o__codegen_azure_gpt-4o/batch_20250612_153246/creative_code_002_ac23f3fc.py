"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-dojo.pages.dev
Prompt: Create a function to calculate the liquidity allocation percentage for presale projects listed on DojoSwap, using the allocation breakdown provided (e.g., 90% liquidity, 10% others).
Generated: DETERMINISTIC_ac23f3fc9b438bb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_liquidity_allocation(presale_amount, allocation_breakdown):
    """
    Calculate the liquidity allocation percentage for presale projects.

    Parameters:
    presale_amount (float): The total amount raised during the presale.
    allocation_breakdown (dict): A dictionary with allocation percentages. 
                                 Example: {"liquidity": 90, "others": 10}

    Returns:
    float: The calculated liquidity allocation amount.
    """
    try:
        # Input validation
        if presale_amount <= 0:
            raise ValueError("Presale amount must be greater than zero.")
        
        if "liquidity" not in allocation_breakdown:
            raise KeyError("Allocation breakdown must include a 'liquidity' key.")
        
        liquidity_percentage = allocation_breakdown["liquidity"]

        # Validate percentage value
        if not (0 <= liquidity_percentage <= 100):
            raise ValueError("Liquidity percentage must be between 0 and 100.")
        
        # Calculate liquidity allocation
        liquidity_allocation = (presale_amount * liquidity_percentage) / 100
        
        return liquidity_allocation
    
    except KeyError as e:
        raise KeyError(f"Missing key in allocation breakdown: {e}")
    
    except ValueError as e:
        raise ValueError(f"Value error: {e}")
    
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

# Example usage:
allocation_schema = {"liquidity": 90, "others": 10}
presale_raised_amount = 100000  # Example presale amount
try:
    liquidity = calculate_liquidity_allocation(presale_raised_amount, allocation_schema)
    print(f"Liquidity Allocation: ${liquidity:.2f}")
except Exception as err:
    print(f"Error: {err}")
```
