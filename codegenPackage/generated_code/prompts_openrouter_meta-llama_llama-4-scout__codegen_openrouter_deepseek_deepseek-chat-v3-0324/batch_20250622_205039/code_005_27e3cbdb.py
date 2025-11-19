"""
Generated Code Metadata:
========================
Original URL: https://remoticassettrade.com
Prompt: Develop a simple calculator in Python to determine the total assets under management for Remotic Asset Trade, given the number of investors and their respective investment amounts.
Generated: DETERMINISTIC_27e3cbdb5b5a0701
Batch ID: 20250622_205039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_total_assets():
    """
    Calculates the total assets under management for Remotic Asset Trade.
    
    Prompts the user to input the number of investors and their respective investment amounts,
    then calculates and displays the total assets under management.
    
    Handles invalid inputs gracefully with appropriate error messages.
    """
    try:
        # Get the number of investors
        num_investors = int(input("Enter the number of investors: "))
        if num_investors <= 0:
            print("Error: Number of investors must be a positive integer.")
            return
        
        total_assets = 0.0
        
        # Get each investor's amount and accumulate the total
        for i in range(1, num_investors + 1):
            while True:
                try:
                    amount = float(input(f"Enter investment amount for investor {i}: $"))
                    if amount < 0:
                        print("Error: Investment amount cannot be negative.")
                        continue
                    total_assets += amount
                    break
                except ValueError:
                    print("Error: Please enter a valid number.")
        
        # Display the result
        print(f"\nTotal assets under management: ${total_assets:,.2f}")
    
    except ValueError:
        print("Error: Please enter a valid integer for the number of investors.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    calculate_total_assets()
```
