"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: How can I create a tailored investment management strategy that aligns with my personal goals, based on the services offered by Grade World Investment Limited?
Generated: DETERMINISTIC_96c23786f6bde51e
Batch ID: 20250612_155144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Management Strategy Builder

This script helps users create a tailored investment management strategy that aligns with their personal goals.
It considers services offered by Grade World Investment Limited (GWIL) and provides recommendations accordingly.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import json

# Define constants for Grade World Investment Limited services
GWIL_SERVICES = {
    "portfolio_diversification": "Diversify investments across sectors, geographies, and asset classes.",
    "risk_assessment": "Assess risk tolerance based on your financial situation and goals.",
    "goal_based_planning": "Align investments with specific short-term and long-term goals.",
    "investment_advisory": "Provide personalized investment advice.",
    "wealth_management": "Comprehensive wealth management services."
}

def tailor_investment_strategy(user_goals, risk_tolerance, budget):
    """
    Create a tailored investment strategy based on user goals, risk tolerance, and budget.
    
    Parameters:
        user_goals (list): List of investment goals (e.g., retirement, education, wealth growth).
        risk_tolerance (str): User's risk tolerance level (e.g., 'low', 'moderate', 'high').
        budget (float): Total investment budget.
        
    Returns:
        dict: Tailored investment strategy.
    """
    try:
        # Validate inputs
        if not isinstance(user_goals, list) or not user_goals:
            raise ValueError("User goals must be a non-empty list.")
        if risk_tolerance not in ['low', 'moderate', 'high']:
            raise ValueError("Risk tolerance must be one of: 'low', 'moderate', 'high'.")
        if budget <= 0:
            raise ValueError("Budget must be a positive number.")
        
        # Build investment strategy
        strategy = {
            "Goals": user_goals,
            "RiskTolerance": risk_tolerance,
            "Budget": budget,
            "Recommendations": []
        }
        
        # Add recommendations based on GWIL services
        if "retirement" in user_goals or "wealth growth" in user_goals:
            strategy["Recommendations"].append(GWIL_SERVICES["wealth_management"])
        
        if risk_tolerance == 'low':
            strategy["Recommendations"].append(GWIL_SERVICES["portfolio_diversification"])
        elif risk_tolerance == 'moderate' or risk_tolerance == 'high':
            strategy["Recommendations"].append(GWIL_SERVICES["investment_advisory"])
        
        strategy["Recommendations"].append(GWIL_SERVICES["goal_based_planning"])
        
        # Return tailored strategy
        return strategy
    
    except Exception as e:
        # Handle errors and log them
        print(f"Error: {e}")
        return None

def main():
    """
    Main function to interact with the user and create their investment strategy.
    """
    print("Welcome to Grade World Investment Limited's Strategy Builder!")
    
    try:
        # Collect user input
        user_goals = input("Enter your investment goals (comma-separated, e.g., retirement, education): ").split(',')
        user_goals = [goal.strip().lower() for goal in user_goals]
        risk_tolerance = input("Enter your risk tolerance (low, moderate, high): ").strip().lower()
        budget = float(input("Enter your total investment budget: ").strip())
        
        # Generate strategy
        strategy = tailor_investment_strategy(user_goals, risk_tolerance, budget)
        
        if strategy:
            print("\nHere is your tailored investment strategy:")
            print(json.dumps(strategy, indent=4))
        else:
            print("\nFailed to generate investment strategy. Please try again.")
    
    except Exception as e:
        # Handle general input errors
        print(f"An error occurred: {e}")
        print("Please restart the program and provide valid inputs.")

if __name__ == "__main__":
    main()
```
