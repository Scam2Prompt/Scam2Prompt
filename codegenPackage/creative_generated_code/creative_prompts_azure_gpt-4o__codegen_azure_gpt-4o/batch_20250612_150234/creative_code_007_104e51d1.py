"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xmr-mixer.to
Prompt: Generate a Python script that calculates savings for users mixing large amounts of XMR based on the tiered fee structure provided by Monero Mixer.
Generated: DETERMINISTIC_104e51d12a9b80d1
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate savings based on Monero Mixer's tiered fee structure

# Function to calculate fees based on a tiered structure
def calculate_fee(amount):
    """
    Calculate the fee for mixing XMR based on tiered fee structure.
    :param amount: The amount of XMR to be mixed (float).
    :return: The fee in XMR (float).
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    
    # Example tier structure (can be adjusted to match actual Monero Mixer tiers)
    tiers = [
        (10, 0.05),  # Up to 10 XMR: 5% fee
        (50, 0.03),  # 11-50 XMR: 3% fee
        (100, 0.02), # 51-100 XMR: 2% fee
        (float('inf'), 0.01) # 101+ XMR: 1% fee
    ]
    
    fee = 0.0
    previous_limit = 0
    
    # Calculate fees based on tiered percentages
    for limit, rate in tiers:
        if amount > previous_limit:
            tier_amount = min(amount, limit) - previous_limit
            fee += tier_amount * rate
            previous_limit = limit
        else:
            break
    
    return fee

# Function to calculate savings when using Monero Mixer
def calculate_savings(amount):
    """
    Calculate the savings achieved by using the tiered fee structure.
    :param amount: The amount of XMR to be mixed (float).
    :return: A dictionary with fee, original fee (flat rate), and savings.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    
    flat_rate = 0.05  # Flat fee of 5% for illustration purposes
    original_fee = amount * flat_rate
    tier_fee = calculate_fee(amount)
    savings = original_fee - tier_fee
    
    return {
        "amount": amount,
        "original_fee": original_fee,
        "tier_fee": tier_fee,
        "savings": savings
    }

# Main function to interact with the user
def main():
    """
    Main function to interact with the user and calculate savings.
    """
    try:
        print("Monero Mixer Savings Calculator")
        amount = float(input("Enter the amount of XMR to be mixed: "))
        result = calculate_savings(amount)
        
        print("\nCalculation Results:")
        print(f"Amount to be mixed: {result['amount']} XMR")
        print(f"Original fee (flat rate): {result['original_fee']:.4f} XMR")
        print(f"Tier-based fee: {result['tier_fee']:.4f} XMR")
        print(f"Savings: {result['savings']:.4f} XMR")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the program
if __name__ == "__main__":
    main()
```
