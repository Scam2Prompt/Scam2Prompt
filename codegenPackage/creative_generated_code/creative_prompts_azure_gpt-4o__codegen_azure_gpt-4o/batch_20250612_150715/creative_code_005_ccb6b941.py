"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Create a script to calculate and distribute shared payouts for Farcaster members, ensuring the allocation follows the Moxie Protocol's percentages (50% to the member, 20% to the channel, etc.).
Generated: DETERMINISTIC_ccb6b9415c4db911
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate and distribute shared payouts for Farcaster members
# following the Moxie Protocol's percentages.

# Import necessary modules
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define percentages based on the Moxie Protocol
PERCENTAGES = {
    "member": 0.50,  # 50% to the member
    "channel": 0.20,  # 20% to the channel
    "community": 0.15,  # 15% to the community fund
    "platform": 0.10,  # 10% to the platform
    "reserve": 0.05,  # 5% to the reserve fund
}

def calculate_payouts(total_amount):
    """
    Calculate payout distribution based on the Moxie Protocol percentages.

    Args:
        total_amount (float): Total amount to be distributed.

    Returns:
        dict: A dictionary mapping recipients to their payout amounts.
    """
    if total_amount < 0:
        raise ValueError("Total amount must be non-negative.")
    
    payouts = {recipient: round(total_amount * percentage, 2) 
               for recipient, percentage in PERCENTAGES.items()}
    return payouts

def distribute_payouts(payouts):
    """
    Distribute payouts to the respective entities.

    This is a placeholder function to simulate payout distribution.

    Args:
        payouts (dict): Payouts dictionary mapping recipients to payout amounts.
    """
    for recipient, amount in payouts.items():
        # Simulating the payout distribution process
        # In a real-world scenario, this could involve API calls or database updates.
        logging.info(f"Distributed ${amount:.2f} to {recipient}.")

def main():
    """
    Main function to execute payout calculations and distribution.
    """
    try:
        # Input: Total amount to be distributed
        total_amount = float(input("Enter the total amount to be distributed: $"))
        
        # Step 1: Calculate payouts
        payouts = calculate_payouts(total_amount)
        logging.info("Calculated payouts successfully.")

        # Step 2: Distribute payouts
        distribute_payouts(payouts)
        logging.info("Payout distribution complete.")
    
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
