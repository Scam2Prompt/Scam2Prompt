"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-helix.com
Prompt: Develop a program that categorizes investments into capital, fixed-income, high-risk, and low-risk types based on Immediate Helix V9’s definitions. Include functionality for risk assessment.
Generated: DETERMINISTIC_e46b2f6d5fe38c03
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Investment Categorizer Program
# This program categorizes investments into capital, fixed-income, high-risk, and low-risk types based on Immediate Helix V9's definitions.
# It also includes functionality for risk assessment.

# Import necessary modules
import logging

# Configure logging to log errors and important information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define risk levels
RISK_LEVELS = {
    "high-risk": ["stocks", "cryptocurrency", "options"],
    "low-risk": ["bonds", "certificates_of_deposit", "stable_etfs"],
    "capital": ["real_estate", "business_investment", "venture_capital"],
    "fixed-income": ["corporate_bonds", "government_bonds", "annuities"],
}

def categorize_investment(investment_type):
    """
    Categorizes an investment based on its type.

    Args:
        investment_type (str): The type of investment.

    Returns:
        str: The category of the investment.
    """
    for category, types in RISK_LEVELS.items():
        if investment_type.lower() in types:
            return category
    return "unknown"

def assess_risk(investment_type):
    """
    Assesses the risk level of an investment.

    Args:
        investment_type (str): The type of investment.

    Returns:
        str: The risk level of the investment.
    """
    category = categorize_investment(investment_type)
    if category == "high-risk":
        return "High Risk"
    elif category == "low-risk" or category == "fixed-income":
        return "Low Risk"
    elif category == "capital":
        return "Moderate Risk"
    else:
        return "Unknown Risk"

def main():
    """
    Main function to interact with the user and categorize investments.
    """
    try:
        logging.info("Investment Categorizer Program Started")
        while True:
            # Take user input for investment type
            investment_type = input("Enter the type of investment (or type 'exit' to quit): ").strip()
            if investment_type.lower() == 'exit':
                logging.info("Program terminated by user.")
                print("Goodbye!")
                break
            
            # Categorize and assess risk
            category = categorize_investment(investment_type)
            risk = assess_risk(investment_type)

            # Display results
            print(f"Investment Type: {investment_type}")
            print(f"Category: {category.title()}")
            print(f"Risk Level: {risk}")
            print("=============================================")

    except Exception as e:
        # Log unexpected errors and inform the user
        logging.error(f"An error occurred: {e}")
        print("An unexpected error occurred. Please try again later.")

# Entry point of the program
if __name__ == "__main__":
    main()
```
