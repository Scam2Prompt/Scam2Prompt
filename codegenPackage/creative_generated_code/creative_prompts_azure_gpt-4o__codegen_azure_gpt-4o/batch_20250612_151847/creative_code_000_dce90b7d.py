"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binotradefx.com
Prompt: Write a Python script to calculate ROI for cryptocurrency investments using the investment calculator logic described on BinoTrade Fx, including support for packages like Silver, Gold, and Platinum.
Generated: DETERMINISTIC_dce90b7d806e6212
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_roi(investment_amount: float, package: str) -> float:
    """
    Calculate the ROI based on the investment package.

    Parameters:
    investment_amount (float): The amount of money invested.
    package (str): The investment package type (Silver, Gold, Platinum).

    Returns:
    float: The calculated ROI.

    Raises:
    ValueError: If an invalid package type is provided.
    """
    # Package-based ROI percentages
    roi_percentages = {
        "Silver": 0.05,    # 5% ROI for Silver package
        "Gold": 0.1,       # 10% ROI for Gold package
        "Platinum": 0.15   # 15% ROI for Platinum package
    }
    
    # Validate package type
    if package not in roi_percentages:
        raise ValueError(f"Invalid package '{package}'. Choose from: Silver, Gold, or Platinum.")
    
    # Calculate ROI
    roi = investment_amount * roi_percentages[package]
    return roi

def main():
    """
    Main function to handle user input and calculate ROI.
    """
    try:
        # Display welcome message
        print("Welcome to the Cryptocurrency Investment ROI Calculator!")
        print("Available packages: Silver, Gold, Platinum")
        
        # Ask user for investment amount
        investment_amount = float(input("Enter your investment amount (e.g., 1000): "))
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        # Ask user for package type
        package = input("Enter your investment package (Silver, Gold, Platinum): ").strip().capitalize()
        
        # Calculate ROI
        roi = calculate_roi(investment_amount, package)
        
        # Display result
        print(f"\nYour investment amount: ${investment_amount:.2f}")
        print(f"Selected package: {package}")
        print(f"Your ROI: ${roi:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the ROI Calculator!")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
