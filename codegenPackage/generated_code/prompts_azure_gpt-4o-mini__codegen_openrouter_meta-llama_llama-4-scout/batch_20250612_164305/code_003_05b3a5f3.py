"""
Generated Code Metadata:
========================
Original URL: https://bafybeigoo2ajgc5d32j7sqglri2pqwtnmpnm6g2yfmlmcdzm2oyww2ny3u.ipfs.dweb.link
Prompt: Create a function that calculates the percentage of fees generated for each cryptocurrency listed in the Transparency Dashboard, including Binance Smart Chain and Ethereum.
Generated: DETERMINISTIC_05b3a5f39dc55f6d
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

def calculate_fee_percentages(
    total_fees: float, 
    cryptocurrency_fees: Dict[str, float]
) -> Dict[str, Dict[str, float]]:
    """
    Calculate the percentage of fees generated for each cryptocurrency.

    Args:
    - total_fees (float): The total fees generated across all cryptocurrencies.
    - cryptocurrency_fees (Dict[str, float]): A dictionary where keys are cryptocurrency names and values are their respective fees.

    Returns:
    - Dict[str, Dict[str, float]]: A dictionary where keys are cryptocurrency names and values are dictionaries containing the fee amount and its percentage of the total fees.

    Raises:
    - ValueError: If total_fees is zero or negative.
    - TypeError: If cryptocurrency_fees is not a dictionary or if total_fees is not a number.
    """

    # Check if total_fees is a valid number
    if not isinstance(total_fees, (int, float)) or total_fees <= 0:
        raise ValueError("Total fees must be a positive number.")

    # Check if cryptocurrency_fees is a dictionary
    if not isinstance(cryptocurrency_fees, dict):
        raise TypeError("Cryptocurrency fees must be a dictionary.")

    # Initialize an empty dictionary to store the results
    fee_percentages: Dict[str, Dict[str, float]] = {}

    # Iterate over each cryptocurrency and its fees
    for cryptocurrency, fees in cryptocurrency_fees.items():
        # Check if fees is a valid number
        if not isinstance(fees, (int, float)) or fees < 0:
            raise ValueError(f"Fees for {cryptocurrency} must be a non-negative number.")

        # Calculate the percentage of fees for the current cryptocurrency
        fee_percentage = (fees / total_fees) * 100

        # Store the fee amount and its percentage in the results dictionary
        fee_percentages[cryptocurrency] = {
            "fee_amount": fees,
            "fee_percentage": round(fee_percentage, 2)  # Round to 2 decimal places
        }

    return fee_percentages


def main():
    # Example usage
    total_fees = 1000.0
    cryptocurrency_fees = {
        "Binance Smart Chain": 300.0,
        "Ethereum": 700.0
    }

    try:
        fee_percentages = calculate_fee_percentages(total_fees, cryptocurrency_fees)
        for cryptocurrency, fees_info in fee_percentages.items():
            print(f" Cryptocurrency: {cryptocurrency}")
            print(f" Fee Amount: {fees_info['fee_amount']}")
            print(f" Fee Percentage: {fees_info['fee_percentage']}%")
            print("------------------------")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
