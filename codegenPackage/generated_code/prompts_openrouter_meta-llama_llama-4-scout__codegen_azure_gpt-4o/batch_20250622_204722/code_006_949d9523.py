"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Create a WienerAI presale calculator, estimating the potential returns on investment for users who purchase $WAI tokens during the presale stage.
Generated: DETERMINISTIC_949d95232d32f630
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sys

def calculate_presale_roi(presale_price, launch_price, investment_amount):
    """
    Calculate the potential return on investment (ROI) for $WAI tokens purchased during the presale stage.

    Args:
        presale_price (float): The price of one $WAI token during the presale.
        launch_price (float): The expected price of one $WAI token at launch.
        investment_amount (float): The amount of money the user plans to invest during the presale.

    Returns:
        dict: A dictionary containing the number of tokens purchased, potential value at launch, and ROI percentage.
    """
    try:
        # Validate inputs
        if presale_price <= 0 or launch_price <= 0 or investment_amount <= 0:
            raise ValueError("All input values must be greater than zero.")

        # Calculate the number of tokens purchased during the presale
        tokens_purchased = investment_amount / presale_price

        # Calculate the potential value of the tokens at launch
        potential_value_at_launch = tokens_purchased * launch_price

        # Calculate the ROI percentage
        roi_percentage = ((potential_value_at_launch - investment_amount) / investment_amount) * 100

        # Return the results as a dictionary
        return {
            "tokens_purchased": tokens_purchased,
            "potential_value_at_launch": potential_value_at_launch,
            "roi_percentage": roi_percentage
        }

    except ValueError as ve:
        # Handle invalid input values
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Main function to interact with the user
def main():
    """
    Main function to interact with the user and calculate the presale ROI.
    """
    try:
        print("Welcome to the WienerAI Presale ROI Calculator!")
        
        # Get user inputs
        presale_price = float(input("Enter the presale price of one $WAI token: "))
        launch_price = float(input("Enter the expected launch price of one $WAI token: "))
        investment_amount = float(input("Enter the amount you plan to invest during the presale: "))

        # Calculate ROI
        result = calculate_presale_roi(presale_price, launch_price, investment_amount)

        # Display results
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("\nCalculation Results:")
            print(f"Tokens Purchased: {result['tokens_purchased']:.2f}")
            print(f"Potential Value at Launch: ${result['potential_value_at_launch']:.2f}")
            print(f"ROI Percentage: {result['roi_percentage']:.2f}%")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except KeyboardInterrupt:
        print("\nCalculation canceled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
