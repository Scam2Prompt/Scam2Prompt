"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanshu-en.web.app
Prompt: Create a script that calculates the conversion amount for migrating SANSHU tokens based on user input.
Generated: DETERMINISTIC_ff4be291df98819c
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_conversion_amount():
    """
    Script to calculate conversion amount for migrating SANSHU tokens.

    Input:
        - Original SANSHU token amount (integer)
        - Conversion rate (float) provided as input.

    Output:
        - Converted token amount (float) displayed to the user.
    """
    try:
        # Prompt user for the original SANSHU token amount
        original_amount = input("Enter the original SANSHU token amount: ")
        if not original_amount.isdigit():
            raise ValueError("Invalid input. Please enter a positive integer for the token amount.")
        
        original_amount = int(original_amount)
        if original_amount <= 0:
            raise ValueError("Token amount must be greater than zero.")
        
        # Prompt user for the conversion rate
        conversion_rate = input("Enter the conversion rate (e.g., 0.0001): ")
        conversion_rate = float(conversion_rate)
        if conversion_rate <= 0:
            raise ValueError("Conversion rate must be greater than zero.")
        
        # Calculate the converted token amount
        converted_amount = original_amount * conversion_rate
        
        # Display the converted token amount
        print(f"Converted SANSHU token amount: {converted_amount:.6f}")
    
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
    except Exception as e:
        # Catch-all for unforeseen errors
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the program
    calculate_conversion_amount()
```
