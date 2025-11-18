"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blendbit.org
Prompt: Write a script to automate the selection of SIM cards based on tariff plans for internet, calls, and business use, referencing the types of SIM cards and operators available on BlendBit.
Generated: DETERMINISTIC_1c79436151faaf36
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define the available SIM card options
SIM_CARDS = [
    {"type": "Internet", "operator": "BlendBit", "tariff_plan": "Unlimited Data"},
    {"type": "Calls", "operator": "BlendBit", "tariff_plan": "Unlimited Calls"},
    {"type": "Business", "operator": "BlendBit", "tariff_plan": "Corporate Plan"},
    {"type": "Internet", "operator": "BlendBit", "tariff_plan": "Basic Data"},
    {"type": "Calls", "operator": "BlendBit", "tariff_plan": "Pay-As-You-Go"},
    {"type": "Business", "operator": "BlendBit", "tariff_plan": "Small Business Plan"},
]

# Define a function to automate the selection of SIM cards
def select_sim_card(sim_type, tariff_plan):
    """
    Select SIM card based on type and tariff plan from the available options.

    Parameters:
        sim_type (str): Type of SIM card (e.g., "Internet", "Calls", "Business").
        tariff_plan (str): Desired tariff plan (e.g., "Unlimited Data", "Corporate Plan").

    Returns:
        dict: Matching SIM card details if found.
        str: Error message if no match is found.
    """
    try:
        # Filter SIM cards based on the user's criteria
        for sim_card in SIM_CARDS:
            if sim_card["type"] == sim_type and sim_card["tariff_plan"] == tariff_plan:
                return sim_card
        return f"No SIM card found for type '{sim_type}' and tariff plan '{tariff_plan}'."
    except Exception as e:
        # Handle unexpected errors
        return f"An error occurred while selecting a SIM card: {str(e)}"


def main():
    """
    Main function to demonstrate SIM card selection.
    """
    print("Welcome to the BlendBit SIM Card Selection Tool!\n")

    # Ask the user for desired SIM type and tariff plan
    sim_type = input("Enter SIM type (Internet/Calls/Business): ").strip()
    tariff_plan = input("Enter desired tariff plan: ").strip()

    # Select the SIM card based on user input
    result = select_sim_card(sim_type, tariff_plan)

    # Print the result (either SIM card details or an error message)
    if isinstance(result, dict):
        print("\nSelected SIM Card:")
        print(json.dumps(result, indent=4))
    else:
        print(f"\nError: {result}")


if __name__ == "__main__":
    # Run the script
    main()
```
