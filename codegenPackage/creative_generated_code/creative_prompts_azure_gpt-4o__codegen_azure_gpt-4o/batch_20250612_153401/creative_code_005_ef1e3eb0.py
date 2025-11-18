"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundfa.com
Prompt: Generate code to recommend a prop firm based on user preferences for trading style, account types, and transparency, using Fundfa’s step-by-step guide for selecting a prop firm.
Generated: DETERMINISTIC_ef1e3eb022b1a5eb
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a dictionary to store prop firm data
prop_firm_data = [
    {
        "name": "Firm A",
        "trading_styles_supported": ["scalping", "day trading"],
        "account_types": ["standard", "ECN"],
        "transparency_score": 9.5
    },
    {
        "name": "Firm B",
        "trading_styles_supported": ["swing trading", "day trading"],
        "account_types": ["micro", "standard"],
        "transparency_score": 8.0
    },
    {
        "name": "Firm C",
        "trading_styles_supported": ["position trading"],
        "account_types": ["standard", "VIP"],
        "transparency_score": 9.0
    }
]

def recommend_prop_firm(trading_style, account_type, min_transparency_score):
    """
    Function to recommend a prop firm based on user preferences.
    
    Parameters:
        trading_style (str): The user's preferred trading style (e.g., scalping, day trading).
        account_type (str): The user's preferred account type (e.g., standard, ECN).
        min_transparency_score (float): Minimum transparency score the user requires.

    Returns:
        list: A list of recommended prop firms matching the criteria.
    """
    try:
        # Filter firms based on user preferences
        matching_firms = [
            firm for firm in prop_firm_data
            if trading_style in firm["trading_styles_supported"]
            and account_type in firm["account_types"]
            and firm["transparency_score"] >= min_transparency_score
        ]

        if not matching_firms:
            return ["No prop firms meet your criteria. Please adjust your preferences."]

        return matching_firms

    except Exception as e:
        # Handle unexpected errors
        return [f"An error occurred: {str(e)}"]

# Main function to interact with the user
def main():
    """
    Main function to interact with the user and recommend a prop firm.
    """
    print("Welcome to the Prop Firm Recommendation System!")
    print("Please provide your preferences.")

    # Collect user input for preferences
    trading_style = input("Enter your preferred trading style (e.g., scalping, day trading): ").strip().lower()
    account_type = input("Enter your preferred account type (e.g., standard, ECN): ").strip().lower()
    try:
        min_transparency_score = float(input("Enter your minimum transparency score (e.g., 8.0): ").strip())
    except ValueError:
        print("Invalid transparency score. Please enter a numeric value.")
        return

    # Get recommendations
    recommendations = recommend_prop_firm(trading_style, account_type, min_transparency_score)

    # Display recommendations
    print("\nRecommended Prop Firms:")
    for firm in recommendations:
        if isinstance(firm, dict):
            print(json.dumps(firm, indent=4))  # Print firm details in a readable JSON format
        else:
            print(firm)

# Run main function if script is executed directly
if __name__ == "__main__":
    main()
```
