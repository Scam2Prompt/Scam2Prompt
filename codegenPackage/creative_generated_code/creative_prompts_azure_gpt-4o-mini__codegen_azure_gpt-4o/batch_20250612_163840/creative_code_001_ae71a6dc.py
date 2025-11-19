"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paraxweb3dapp.pages.dev
Prompt: Write a function to calculate the Loan To Value (LTV) ratio for NFTs on the ParaX marketplace.
Generated: DETERMINISTIC_ae71a6dc7f4f12ec
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing required modules
class InvalidInputError(Exception):
    """Custom exception for invalid inputs."""
    pass

def calculate_nft_ltv(loan_amount, nft_value):
    """
    Calculate the Loan-To-Value (LTV) ratio for NFTs on the ParaX marketplace.

    Parameters:
        loan_amount (float): The amount of the loan given in USD.
        nft_value (float): The market value of the NFT in USD.

    Returns:
        float: The Loan-To-Value (LTV) ratio as a percentage.

    Raises:
        InvalidInputError: If loan_amount or nft_value is less than or equal to zero.
        TypeError: If loan_amount or nft_value are not numeric types.
    """
    # Validate input types
    if not isinstance(loan_amount, (int, float)) or not isinstance(nft_value, (int, float)):
        raise TypeError("Both loan_amount and nft_value must be numeric types (int or float).")
    
    # Validate input values
    if loan_amount <= 0 or nft_value <= 0:
        raise InvalidInputError("Both loan_amount and nft_value must be greater than zero.")
    
    # Calculate LTV ratio
    ltv_ratio = (loan_amount / nft_value) * 100
    
    return round(ltv_ratio, 2)  # Returning LTV ratio rounded to 2 decimal places

# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        loan_amount = 5000  # USD
        nft_value = 20000  # USD
        
        # Calculate LTV ratio
        ltv_ratio = calculate_nft_ltv(loan_amount, nft_value)
        print(f"Loan-To-Value (LTV) Ratio: {ltv_ratio}%")
    
    except Exception as e:
        print(f"Error: {e}")
```
