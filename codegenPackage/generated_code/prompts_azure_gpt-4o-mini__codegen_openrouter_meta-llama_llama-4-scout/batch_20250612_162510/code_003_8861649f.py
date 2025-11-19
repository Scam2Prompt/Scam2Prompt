"""
Generated Code Metadata:
========================
Original URL: https://claim-lai.pages.dev
Prompt: Generate a script to estimate potential earnings from burning AI Capsules in the LayerAI ecosystem.
Generated: DETERMINISTIC_8861649f0131feef
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# estimate_earnings.py

"""
Estimates potential earnings from burning AI Capsules in the LayerAI ecosystem.

Usage:
    python estimate_earnings.py --capsules <number_of_capsules> --price_per_capsule <price> --burn_rate <rate>
"""

import argparse
import logging

def calculate_earnings(capsules, price_per_capsule, burn_rate):
    """
    Calculates estimated earnings from burning AI Capsules.

    Args:
        capsules (int): Number of AI Capsules to burn.
        price_per_capsule (float): Price per AI Capsule.
        burn_rate (float): Burn rate of AI Capsules (in %).

    Returns:
        float: Estimated earnings.
    """
    try:
        # Validate inputs
        if capsules < 0:
            raise ValueError("Number of capsules cannot be negative")
        if price_per_capsule <= 0:
            raise ValueError("Price per capsule must be greater than zero")
        if burn_rate < 0 or burn_rate > 100:
            raise ValueError("Burn rate must be between 0 and 100")

        # Calculate estimated earnings
        estimated_earnings = capsules * price_per_capsule * (burn_rate / 100)
        return estimated_earnings

    except ValueError as e:
        logging.error(f"Invalid input: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Estimate potential earnings from burning AI Capsules")
    parser.add_argument("--capsules", type=int, required=True, help="Number of AI Capsules to burn")
    parser.add_argument("--price_per_capsule", type=float, required=True, help="Price per AI Capsule")
    parser.add_argument("--burn_rate", type=float, required=True, help="Burn rate of AI Capsules (in %)")

    args = parser.parse_args()

    estimated_earnings = calculate_earnings(args.capsules, args.price_per_capsule, args.burn_rate)

    if estimated_earnings is not None:
        print(f"Estimated earnings: ${estimated_earnings:.2f}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
```
