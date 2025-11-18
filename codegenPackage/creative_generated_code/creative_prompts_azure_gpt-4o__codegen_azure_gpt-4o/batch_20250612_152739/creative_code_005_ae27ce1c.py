"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Create a Python program that simulates the distribution of JESSE tokens based on the presale cap of 1000 BASE and the pricing structure provided.
Generated: DETERMINISTIC_ae27ce1cac580d99
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to simulate the distribution of JESSE tokens based on the presale cap and pricing structure

# Constants
PRE_SALE_CAP_BASE = 1000  # Presale cap in BASE
TOKEN_NAME = "JESSE"
TOKEN_PRICING_STRUCTURE = {
    "tier_1": {"threshold": 200, "rate": 10},  # First 200 BASE: 10 JESSE per BASE
    "tier_2": {"threshold": 500, "rate": 8},   # Next 300 BASE (200-500): 8 JESSE per BASE
    "tier_3": {"threshold": 1000, "rate": 5}  # Remaining 500 BASE (500-1000): 5 JESSE per BASE
}

# Function to calculate token distribution based on BASE contribution
def calculate_token_distribution(base_contribution):
    """
    Calculate the number of JESSE tokens distributed based on BASE contribution.
    
    Args:
        base_contribution (float): The amount of BASE contributed by the user.
    
    Returns:
        int: Number of JESSE tokens distributed.
    """
    if base_contribution <= 0:
        raise ValueError("BASE contribution must be greater than zero.")
    
    if base_contribution > PRE_SALE_CAP_BASE:
        raise ValueError(f"BASE contribution exceeds the presale cap of {PRE_SALE_CAP_BASE}.")
    
    tokens_distributed = 0
    remaining_contribution = base_contribution

    # Tier 1
    if remaining_contribution > 0:
        tier_1_contribution = min(remaining_contribution, TOKEN_PRICING_STRUCTURE["tier_1"]["threshold"])
        tokens_distributed += tier_1_contribution * TOKEN_PRICING_STRUCTURE["tier_1"]["rate"]
        remaining_contribution -= tier_1_contribution

    # Tier 2
    if remaining_contribution > 0:
        tier_2_contribution = min(remaining_contribution, 
                                  TOKEN_PRICING_STRUCTURE["tier_2"]["threshold"] - TOKEN_PRICING_STRUCTURE["tier_1"]["threshold"])
        tokens_distributed += tier_2_contribution * TOKEN_PRICING_STRUCTURE["tier_2"]["rate"]
        remaining_contribution -= tier_2_contribution

    # Tier 3
    if remaining_contribution > 0:
        tier_3_contribution = min(remaining_contribution, 
                                  TOKEN_PRICING_STRUCTURE["tier_3"]["threshold"] - TOKEN_PRICING_STRUCTURE["tier_2"]["threshold"])
        tokens_distributed += tier_3_contribution * TOKEN_PRICING_STRUCTURE["tier_3"]["rate"]
        remaining_contribution -= tier_3_contribution

    return tokens_distributed

# Main function to simulate token distribution
def main():
    """
    Main function to simulate the distribution of JESSE tokens based on user input.
    """
    print(f"Welcome to the {TOKEN_NAME} token presale!")
    print(f"The presale cap is {PRE_SALE_CAP_BASE} BASE.")
    print("Pricing Structure:")
    for tier, details in TOKEN_PRICING_STRUCTURE.items():
        print(f"  {tier.capitalize()}: {details['rate']} {TOKEN_NAME} per BASE (Up to {details['threshold']} BASE)")

    try:
        # Get user contribution input
        base_contribution = float(input("Enter the amount of BASE you want to contribute: "))
        
        # Calculate token distribution
        tokens_received = calculate_token_distribution(base_contribution)
        print(f"You will receive {tokens_received} {TOKEN_NAME} tokens for your contribution of {base_contribution} BASE.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
