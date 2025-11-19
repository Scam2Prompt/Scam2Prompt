"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donk-meme.pages.dev
Prompt: Write a script to calculate the total amount of $SOL needed to buy $DONKM tokens based on the presale allocation details.
Generated: DETERMINISTIC_e18ba9126532d6e8
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total amount of $SOL needed to buy $DONKM tokens
based on presale allocation details.

Assumptions:
- $DONKM token price in $SOL is known (price_per_token).
- User specifies the number of $DONKM tokens they want to purchase (donkm_tokens_requested).
- Script handles basic input validation and error scenarios.
"""

def calculate_sol_needed(donkm_tokens_requested, price_per_token):
    """
    Calculate the total amount of $SOL required for the purchase.
    
    Parameters:
        donkm_tokens_requested (float): Number of $DONKM tokens the user wants to purchase.
        price_per_token (float): Price of 1 $DONKM token in $SOL.
    
    Returns:
        float: Total amount of $SOL required.
    """
    try:
        # Ensure inputs are valid types
        if not isinstance(donkm_tokens_requested, (int, float)) or not isinstance(price_per_token, (int, float)):
            raise ValueError("Both donkm_tokens_requested and price_per_token must be numbers.")
        
        # Ensure inputs are positive numbers
        if donkm_tokens_requested <= 0 or price_per_token <= 0:
            raise ValueError("Both donkm_tokens_requested and price_per_token must be greater than 0.")
        
        # Calculate the total $SOL needed
        total_sol = donkm_tokens_requested * price_per_token
        return total_sol
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

# Main function
if __name__ == "__main__":
    try:
        # Presale details
        price_per_token = 0.05  # Example: 1 $DONKM = 0.05 $SOL

        # User input: Number of $DONKM tokens they want to purchase
        user_input = input("Enter the number of $DONKM tokens you want to purchase: ")
        
        # Validate and parse user input
        try:
            donkm_tokens_requested = float(user_input)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            exit(1)
        
        # Calculate the total $SOL needed
        total_sol_needed = calculate_sol_needed(donkm_tokens_requested, price_per_token)
        
        # Display result if calculation is successful
        if total_sol_needed is not None:
            print(f"To purchase {donkm_tokens_requested} $DONKM tokens, you will need {total_sol_needed:.4f} $SOL.")
        else:
            print("Failed to calculate the required $SOL due to input errors.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
