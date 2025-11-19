"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://block-dagnetwork.pages.dev
Prompt: Generate a script that calculates the ROI for BDAG coin investments based on the total sales and coins sold from the BlockDAG Dashboard.
Generated: DETERMINISTIC_0e2c2b4c9015b367
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_roi(total_sales, coins_sold):
    """
    Calculate the Return on Investment (ROI) for BDAG coin investments.

    Formula:
    ROI (%) = (Total Sales / Number of Coins Sold - 1) * 100

    Args:
        total_sales (float): Total amount earned from sales of BDAG coins.
        coins_sold (int): Total number of BDAG coins sold.

    Returns:
        float: The ROI percentage.
    Raises:
        ValueError: If coins_sold is zero or negative.
    """
    if coins_sold <= 0:
        raise ValueError("The number of coins sold must be greater than zero.")
    
    # Calculate ROI
    roi = ((total_sales / coins_sold) - 1) * 100
    return roi

def main():
    """
    Main function to calculate the ROI for BDAG coin investments.
    Fetches input from the user and calculates the ROI.
    """
    try:
        # Get user input for total sales and coins sold
        print("Welcome to the BDAG ROI Calculator")
        total_sales = float(input("Enter the total sales amount (e.g., 1000.50): "))
        coins_sold = int(input("Enter the total number of coins sold (e.g., 500): "))

        # Validate input
        if total_sales < 0:
            print("Error: Total sales amount cannot be negative.")
            sys.exit(1)
        
        # Calculate ROI
        roi = calculate_roi(total_sales, coins_sold)

        # Print the calculated ROI
        print(f"The ROI for BDAG coin investments is {roi:.2f}%.")
    
    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
