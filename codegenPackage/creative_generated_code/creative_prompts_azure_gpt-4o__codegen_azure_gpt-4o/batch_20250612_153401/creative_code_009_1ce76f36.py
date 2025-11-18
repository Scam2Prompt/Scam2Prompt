"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deqodsmeta.web.app
Prompt: Write a program to calculate the percentage of $DUST claimed based on the total $DUST available, as shown on the DeGods airdrop section.
Generated: DETERMINISTIC_1ce76f36ee907429
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# A program to calculate the percentage of $DUST claimed based on the total $DUST available.

# Function to calculate the percentage of $DUST claimed
def calculate_dust_percentage(claimed_dust, total_dust):
    """
    Calculate the percentage of $DUST claimed.
    
    Parameters:
    claimed_dust (float): Amount of $DUST claimed.
    total_dust (float): Total amount of $DUST available.

    Returns:
    float: Percentage of $DUST claimed.
    """
    try:
        # Validate inputs
        if claimed_dust < 0 or total_dust <= 0:
            raise ValueError("claimed_dust must be non-negative and total_dust must be positive.")
        
        # Calculate percentage
        percentage = (claimed_dust / total_dust) * 100
        return percentage

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

# Main function to execute the program
if __name__ == "__main__":
    try:
        # Input: Amount of $DUST claimed and total $DUST available
        claimed_dust = float(input("Enter the number of $DUST claimed: "))
        total_dust = float(input("Enter the total number of $DUST available: "))

        # Calculate percentage
        result = calculate_dust_percentage(claimed_dust, total_dust)

        # Output the result
        if result is not None:
            print(f"The percentage of $DUST claimed is: {result:.2f}%")
        else:
            print("Failed to calculate the percentage due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter numeric values for claimed and total $DUST.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
