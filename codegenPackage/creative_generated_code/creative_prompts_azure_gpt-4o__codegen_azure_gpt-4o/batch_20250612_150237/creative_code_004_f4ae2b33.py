"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketmaventrade.com
Prompt: Create a program that calculates the return on investment for Market Maven Trade's plans (e.g., Basic: 15% after 6 hours, Standard: 30% after 6 hours, Entrep: 40% after 24 hours) and displays the capital back amount.
Generated: DETERMINISTIC_f4ae2b335f05a8fb
Batch ID: 20250612_150237
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

def calculate_roi(plan, investment):
    """
    Function to calculate the return on investment (ROI) based on the selected plan and investment amount.

    :param plan: str - The investment plan name ('Basic', 'Standard', 'Entrep').
    :param investment: float - The amount of money invested.
    :return: float - The total capital back amount (original investment + profit).
    """
    try:
        # Define the investment plans with their respective ROI percentages and durations
        plans = {
            "Basic": {"roi_percentage": 15, "duration_hours": 6},
            "Standard": {"roi_percentage": 30, "duration_hours": 6},
            "Entrep": {"roi_percentage": 40, "duration_hours": 24},
        }

        # Check if the selected plan exists
        if plan not in plans:
            raise ValueError(f"Invalid plan '{plan}'. Available plans: {', '.join(plans.keys())}")

        # Calculate the profit based on the ROI percentage
        roi_percentage = plans[plan]["roi_percentage"]
        profit = (investment * roi_percentage) / 100

        # Calculate the total capital back amount
        capital_back = investment + profit

        return capital_back

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate ROI.
    """
    print("Welcome to Market Maven Trade's ROI Calculator!")
    print("Available Plans:")
    print("1. Basic: 15% ROI after 6 hours")
    print("2. Standard: 30% ROI after 6 hours")
    print("3. Entrep: 40% ROI after 24 hours")

    try:
        # Prompt the user for the investment plan
        plan = input("Enter the name of the plan (Basic, Standard, Entrep): ").strip()

        # Prompt the user for the investment amount
        investment = float(input("Enter the investment amount ($): ").strip())

        # Validate investment amount
        if investment <= 0:
            raise ValueError("Investment amount must be greater than 0.")

        # Calculate the ROI
        capital_back = calculate_roi(plan, investment)

        # Display the results to the user
        print(f"\nSelected Plan: {plan}")
        print(f"Investment Amount: ${investment:.2f}")
        print(f"Total Capital Back Amount (including profit): ${capital_back:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main function
    main()
```
