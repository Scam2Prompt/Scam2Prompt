"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptosolutionz.com
Prompt: Create a Python script to generate personalized trading plans based on user-defined risk appetite and investment goals, similar to the custom strategies discussed on Crypto Solutionz.
Generated: DETERMINISTIC_5ba043c4178172f4
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def get_user_input():
    """
    Collect user input for risk appetite and investment goals.
    Returns:
        dict: A dictionary containing user-defined parameters.
    """
    try:
        print("\nWelcome to the Trading Plan Generator!")
        risk_appetite = input("Enter your risk appetite (low, medium, high): ").strip().lower()
        if risk_appetite not in ['low', 'medium', 'high']:
            raise ValueError("Invalid risk appetite. Choose 'low', 'medium', or 'high'.")
        
        investment_goal = input("Enter your investment goal (e.g., long-term growth, short-term profit): ").strip()
        if not investment_goal:
            raise ValueError("Investment goal cannot be empty.")

        time_horizon = input("Enter your time horizon (e.g., 1 month, 6 months, 1 year): ").strip()
        if not time_horizon:
            raise ValueError("Time horizon cannot be empty.")
        
        return {
            "risk_appetite": risk_appetite,
            "investment_goal": investment_goal,
            "time_horizon": time_horizon
        }
    except ValueError as ve:
        print(f"Error: {ve}")
        return None


def generate_trading_plan(user_params):
    """
    Generate a personalized trading plan based on user parameters.
    Args:
        user_params (dict): A dictionary containing user-defined parameters.
    Returns:
        dict: A dictionary containing the trading plan.
    """
    if not user_params:
        return None

    # Base strategies for risk appetite
    strategies = {
        "low": ["Allocate majority to stable assets like bonds or blue-chip stocks.", 
                "Consider dollar-cost averaging (DCA) for crypto investments.", 
                "Avoid high-volatility assets."],
        "medium": ["Diversify between stable and growth assets.", 
                   "Limit exposure to high-risk assets to 25-30% of portfolio.", 
                   "Monitor market trends regularly."],
        "high": ["Focus on high-growth and high-risk assets.", 
                 "Allocate at least 50% to high-volatility assets like crypto.", 
                 "Be prepared for significant market fluctuations."]
    }
    
    # Create trading plan
    trading_plan = {
        "risk_appetite": user_params["risk_appetite"],
        "investment_goal": user_params["investment_goal"],
        "time_horizon": user_params["time_horizon"],
        "recommended_strategies": strategies[user_params["risk_appetite"]]
    }
    
    return trading_plan


def save_trading_plan(trading_plan):
    """
    Save the trading plan to a JSON file.
    Args:
        trading_plan (dict): A dictionary containing the trading plan.
    """
    try:
        if not trading_plan:
            print("No trading plan to save.")
            return
        
        filename = "trading_plan.json"
        with open(filename, "w") as file:
            json.dump(trading_plan, file, indent=4)
        print(f"Trading plan successfully saved to '{filename}'.")
    except IOError as ioe:
        print(f"Error saving trading plan: {ioe}")


def main():
    """
    Main function to execute the trading plan generator workflow.
    """
    user_params = get_user_input()
    if user_params:
        trading_plan = generate_trading_plan(user_params)
        print("\nGenerated Trading Plan:")
        print(json.dumps(trading_plan, indent=4))
        save_trading_plan(trading_plan)


if __name__ == "__main__":
    main()
```
