"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-urex-gpt.com
Prompt: Develop a Python program to calculate investment risk tolerance and budget allocation for crypto trading, inspired by the risk warnings provided by the Bit GPT Urex platform.
Generated: DETERMINISTIC_c64d2e955a679fb1
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_risk_tolerance():
    """
    Function to assess the user's risk tolerance.

    Returns:
        int: User's risk tolerance score (1-5).
    """
    print("Risk Tolerance Assessment:")
    print("Rate your risk tolerance from 1 to 5:")
    print("1 - Very Low, 2 - Low, 3 - Moderate, 4 - High, 5 - Very High")

    while True:
        try:
            risk_tolerance = int(input("Enter your risk tolerance (1-5): "))
            if risk_tolerance < 1 or risk_tolerance > 5:
                raise ValueError("Risk tolerance must be between 1 and 5.")
            return risk_tolerance
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def get_trading_budget():
    """
    Function to calculate the user's budget allocation for crypto trading.

    Returns:
        float: User's trading budget.
    """
    print("\nBudget Allocation:")
    print("Please provide your total available investment funds.")

    while True:
        try:
            total_funds = float(input("Enter your total investment funds (USD): "))
            if total_funds <= 0:
                raise ValueError("Total funds must be greater than zero.")
            # Assuming allocation, typically 5%-20% of total funds based on risk tolerance
            return total_funds
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def calculate_allocation(risk_tolerance, total_funds):
    """
    Function to calculate recommended budget allocation for crypto trading based on risk tolerance.

    Args:
        risk_tolerance (int): User's risk tolerance (1-5).
        total_funds (float): User's total investment funds.

    Returns:
        dict: A dictionary containing allocation details.
    """
    # Define allocation percentages based on risk tolerance.
    allocation_percentages = {
        1: 0.05,  # Very Low Risk: 5% allocation
        2: 0.10,  # Low Risk: 10% allocation
        3: 0.15,  # Moderate Risk: 15% allocation
        4: 0.20,  # High Risk: 20% allocation
        5: 0.25   # Very High Risk: 25% allocation
    }

    allocation_percentage = allocation_percentages.get(risk_tolerance, 0.05)
    crypto_budget = total_funds * allocation_percentage

    return {
        "risk_tolerance": risk_tolerance,
        "total_funds": total_funds,
        "crypto_budget": crypto_budget,
        "allocation_percentage": allocation_percentage * 100  # Convert to percentage for display
    }

def main():
    """
    Main function to calculate investment risk tolerance and budget allocation for crypto trading.
    """
    print("Welcome to the Crypto Trading Budget Allocation Tool!")
    try:
        # Step 1: Assess risk tolerance
        risk_tolerance = get_risk_tolerance()

        # Step 2: Calculate trading budget
        total_funds = get_trading_budget()

        # Step 3: Calculate allocation based on risk tolerance and budget
        allocation_details = calculate_allocation(risk_tolerance, total_funds)

        # Display results
        print("\nInvestment Allocation Details:")
        print(f"Risk Tolerance Level: {allocation_details['risk_tolerance']} (1-5)")
        print(f"Total Investment Funds: ${allocation_details['total_funds']:.2f}")
        print(f"Recommended Crypto Trading Budget: ${allocation_details['crypto_budget']:.2f}")
        print(f"Allocation Percentage: {allocation_details['allocation_percentage']}%")
        print("\nNote: Always invest responsibly and diversify your portfolio.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
