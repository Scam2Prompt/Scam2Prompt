"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.io
Prompt: Develop a program that simulates the percentage distribution of mixed Bitcoin outputs, incorporating the customizable fee structure described on the CryptoMixer website.
Generated: DETERMINISTIC_b37567a31854b9d3
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def simulate_bitcoin_distribution(total_amount, num_outputs, fee_percentage):
    """
    Simulates the percentage distribution of mixed Bitcoin outputs, incorporating a customizable fee structure.

    Parameters:
        total_amount (float): Total amount of Bitcoin to be distributed (in BTC).
        num_outputs (int): Number of output wallets.
        fee_percentage (float): Fee percentage charged by the mixer.

    Returns:
        dict: A dictionary containing the outputs with their corresponding Bitcoin amounts.
    """
    try:
        if total_amount <= 0:
            raise ValueError("Total amount must be greater than 0.")
        if num_outputs <= 0:
            raise ValueError("Number of outputs must be greater than 0.")
        if not (0 <= fee_percentage <= 100):
            raise ValueError("Fee percentage must be between 0 and 100.")

        # Calculate the fee amount
        fee_amount = total_amount * (fee_percentage / 100)

        # Remaining amount after deducting the fee
        remaining_amount = total_amount - fee_amount

        # Randomly generate distribution percentages for outputs
        distribution_percentages = [random.random() for _ in range(num_outputs)]
        total_percentage = sum(distribution_percentages)

        # Normalize percentages to ensure they sum to 100%
        normalized_percentages = [p / total_percentage for p in distribution_percentages]

        # Calculate Bitcoin amounts for each output wallet
        outputs = {}
        for i, percentage in enumerate(normalized_percentages):
            outputs[f"Output_{i + 1}"] = round(remaining_amount * percentage, 8)  # Rounded to 8 decimals (BTC standard)

        return {
            "Fee": round(fee_amount, 8),
            "Outputs": outputs
        }

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    total_bitcoin = 1.0  # 1 BTC
    number_of_outputs = 5
    fee_percentage = 2.0  # 2%

    result = simulate_bitcoin_distribution(total_bitcoin, number_of_outputs, fee_percentage)

    if result:
        print("Fee Amount (BTC):", result["Fee"])
        print("Distributed Outputs:")
        for output, amount in result["Outputs"].items():
            print(f"  {output}: {amount} BTC")
```
