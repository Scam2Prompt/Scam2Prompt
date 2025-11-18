"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dre-8x7.pages.dev
Prompt: Generate code to calculate token distribution for a presale where 1 FTM equals 398 DRE tokens, ensuring accurate conversion for amounts like 250, 500, 1000, 2000, and 3000 FTM.
Generated: DETERMINISTIC_69528f43eee74f5f
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import sys

def calculate_token_distribution(ftm_amount):
    """
    Calculate the number of DRE tokens for a given FTM amount.
    
    Conversion rate: 1 FTM = 398 DRE tokens
    
    Args:
        ftm_amount (float): The amount of FTM to convert.
    
    Returns:
        float: The equivalent number of DRE tokens.
    """
    try:
        # Conversion rate
        conversion_rate = 398
        
        # Validate input
        if ftm_amount <= 0:
            raise ValueError("FTM amount must be greater than zero.")
        
        # Calculate DRE tokens
        dre_tokens = ftm_amount * conversion_rate
        
        return dre_tokens
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)  # Exit the program with an error code
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit the program with an error code


def main():
    """
    Main function to calculate token distribution for predefined FTM amounts.
    """
    # List of FTM amounts to convert
    ftm_amounts = [250, 500, 1000, 2000, 3000]
    
    print("Presale Token Distribution:")
    print("------------------------------")
    
    for amount in ftm_amounts:
        try:
            # Perform token distribution calculation
            dre_tokens = calculate_token_distribution(amount)
            
            # Print result
            print(f"{amount} FTM -> {dre_tokens:.2f} DRE tokens")
        except Exception as e:
            print(f"Failed to calculate for {amount} FTM: {e}")
            continue  # Proceed to the next amount


# Entry point of the script
if __name__ == "__main__":
    main()
```
