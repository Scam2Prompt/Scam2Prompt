"""
Generated Code Metadata:
========================
Original URL: https://dresale.pages.dev
Prompt: "Generate a Python script to calculate the amount of $DRE tokens a user can buy based on the provided FTM amounts and presale cap."
Generated: DETERMINISTIC_3f4285af1082e013
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the amount of $DRE tokens a user can buy based on the provided FTM amounts and presale cap.

Assumptions:
- Exchange rate between FTM and $DRE is fixed and provided.
- Presale cap is the maximum number of $DRE tokens available for purchase.
- User input is validated to ensure it is a positive number.
"""

# Constants
EXCHANGE_RATE_FTM_TO_DRE = 100  # Number of $DRE tokens per 1 FTM
PRESALE_CAP_DRE = 50000         # Maximum number of $DRE tokens available for presale

def calculate_dre_tokens(ftm_amount):
    """
    Calculate the number of $DRE tokens a user can buy based on the FTM amount.
    
    Args:
        ftm_amount (float): The amount of FTM provided by the user.
    
    Returns:
        float: The number of $DRE tokens the user can buy.
    """
    # Calculate the number of $DRE tokens
    dre_tokens = ftm_amount * EXCHANGE_RATE_FTM_TO_DRE
    
    # Ensure the calculated tokens do not exceed the presale cap
    if dre_tokens > PRESALE_CAP_DRE:
        return PRESALE_CAP_DRE
    
    return dre_tokens

def main():
    """
    Main function to handle user input and calculate $DRE tokens.
    """
    try:
        # Prompt the user for the amount of FTM
        ftm_amount = float(input("Enter the amount of FTM you want to spend: "))
        
        # Validate the input
        if ftm_amount <= 0:
            print("Error: The amount of FTM must be a positive number.")
            return
        
        # Calculate the $DRE tokens
        dre_tokens = calculate_dre_tokens(ftm_amount)
        
        # Display the result
        print(f"You can buy {dre_tokens:.2f} $DRE tokens.")
        
        # Notify if the presale cap is reached
        if dre_tokens == PRESALE_CAP_DRE:
            print("Note: You have reached the presale cap.")
    
    except ValueError:
        # Handle invalid input
        print("Error: Please enter a valid number for the FTM amount.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
