"""
Generated Code Metadata:
========================
Original URL: https://monadverse2.testnet.nfts2.me
Prompt: Create a script that calculates referral earnings based on the number of NFT mints completed through a referral link on Monadverse2.
Generated: DETERMINISTIC_1a2794ed00112d8e
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_earnings_calculator.py

"""
Calculates referral earnings based on the number of NFT mints completed through a referral link on Monadverse2.

Usage:
    python referral_earnings_calculator.py --referral_link <referral_link> --nft_mints <nft_mints>
"""

import argparse
import logging

# Define a dictionary to store referral earnings rates
REFERRAL_EARNINGS_RATES = {
    "bronze": 0.01,  # 1% earnings rate for bronze referrals
    "silver": 0.05,  # 5% earnings rate for silver referrals
    "gold": 0.10,   # 10% earnings rate for gold referrals
    "platinum": 0.20  # 20% earnings rate for platinum referrals
}

def calculate_referral_earnings(referral_link, nft_mints, nft_mint_price):
    """
    Calculates referral earnings based on the number of NFT mints completed.

    Args:
        referral_link (str): The referral link used to track NFT mints.
        nft_mints (int): The number of NFT mints completed.
        nft_mint_price (float): The price of each NFT mint.

    Returns:
        float: The total referral earnings.
    """

    # Determine the referral earnings rate based on the referral link
    # For simplicity, assume the referral link contains the referral tier (bronze, silver, gold, platinum)
    referral_tier = referral_link.split("-")[-1].lower()
    if referral_tier not in REFERRAL_EARNINGS_RATES:
        raise ValueError(f"Invalid referral tier: {referral_tier}")

    # Get the referral earnings rate
    referral_earnings_rate = REFERRAL_EARNINGS_RATES[referral_tier]

    # Calculate the total referral earnings
    total_referral_earnings = nft_mints * nft_mint_price * referral_earnings_rate

    return total_referral_earnings

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Calculate referral earnings")
    parser.add_argument("--referral_link", type=str, required=True, help="The referral link used to track NFT mints")
    parser.add_argument("--nft_mints", type=int, required=True, help="The number of NFT mints completed")
    parser.add_argument("--nft_mint_price", type=float, required=True, help="The price of each NFT mint")
    args = parser.parse_args()

    try:
        # Calculate referral earnings
        referral_earnings = calculate_referral_earnings(args.referral_link, args.nft_mints, args.nft_mint_price)

        # Log the result
        logger.info(f"Referral earnings: ${referral_earnings:.2f}")

    except Exception as e:
        # Log any errors
        logger.error(f"Error calculating referral earnings: {str(e)}")

if __name__ == "__main__":
    main()
```
