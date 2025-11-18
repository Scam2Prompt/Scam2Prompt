"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Generate code to calculate the number of MON tokens claimable upon the Token Generation Event (TGE) using the presale allocation percentages and the price per lot described on the webpage.
Generated: DETERMINISTIC_b0dc27f13604e52b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate the number of MON tokens claimable upon the Token Generation Event (TGE).

def calculate_claimable_tokens(presale_allocation_percentage, price_per_lot, lots_purchased, total_tokens_generated):
    """
    Calculate the number of MON tokens claimable at the Token Generation Event (TGE).
    
    Parameters:
        presale_allocation_percentage (float): Presale allocation percentage (e.g., 0.10 for 10%).
        price_per_lot (float): Price per lot in the presale.
        lots_purchased (int): Number of lots purchased by the user.
        total_tokens_generated (int): Total number of MON tokens generated during TGE.
    
    Returns:
        float: Number of MON tokens claimable for the user.
    """
    try:
        # Validate inputs
        if presale_allocation_percentage <= 0 or presale_allocation_percentage > 1:
            raise ValueError("Presale allocation percentage must be between 0 and 1 (exclusive).")
        if price_per_lot <= 0:
            raise ValueError("Price per lot must be greater than 0.")
        if lots_purchased <= 0:
            raise ValueError("Lots purchased must be a positive integer.")
        if total_tokens_generated <= 0:
            raise ValueError("Total tokens generated must be a positive number.")
        
        # Calculate the presale allocation of tokens
        presale_tokens = total_tokens_generated * presale_allocation_percentage
        
        # Calculate tokens claimable by the user
        user_claimable_tokens = (lots_purchased * price_per_lot) / presale_tokens * presale_tokens
        
        return user_claimable_tokens

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Inputs
        presale_allocation_percentage = 0.10  # 10% allocation for presale
        price_per_lot = 1000.0  # Price per lot in the presale
        lots_purchased = 5  # Number of lots purchased by the user
        total_tokens_generated = 1000000  # Total tokens generated during TGE

        # Calculate claimable tokens
        claimable_tokens = calculate_claimable_tokens(
            presale_allocation_percentage, price_per_lot, lots_purchased, total_tokens_generated
        )

        if claimable_tokens is not None:
            print(f"Claimable MON Tokens: {claimable_tokens}")
        else:
            print("Failed to calculate claimable tokens.")
    
    except Exception as e:
        print(f"An error occurred during execution: {e}")
```
