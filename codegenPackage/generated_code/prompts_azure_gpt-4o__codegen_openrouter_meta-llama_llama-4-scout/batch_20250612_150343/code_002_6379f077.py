"""
Generated Code Metadata:
========================
Original URL: https://bitcoinzat.com
Prompt: Develop a script to calculate transaction fees in Bitcoin, ensuring the prevention of errors like the 8.18 BTC fee mentioned on Bitcoinzat.com.
Generated: DETERMINISTIC_6379f07735bc0cd4
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Transaction Fee Calculator in Bitcoin

This script calculates the transaction fee in Bitcoin, preventing errors like 
the 8.18 BTC fee mentioned on Bitcoinzat.com.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_transaction_fee(input_amount, output_amount, fee_per_kb, transaction_size):
    """
    Calculate the transaction fee in Bitcoin.

    Args:
        input_amount (float): The total input amount in BTC.
        output_amount (float): The total output amount in BTC.
        fee_per_kb (float): The fee per kilobyte in BTC.
        transaction_size (int): The transaction size in bytes.

    Returns:
        float: The calculated transaction fee in BTC.

    Raises:
        ValueError: If input or output amounts are negative.
        ValueError: If fee per kilobyte or transaction size is non-positive.
    """
    if input_amount < 0 or output_amount < 0:
        raise ValueError("Input and output amounts must be non-negative.")

    if fee_per_kb <= 0:
        raise ValueError("Fee per kilobyte must be positive.")

    if transaction_size <= 0:
        raise ValueError("Transaction size must be positive.")

    # Calculate the transaction fee
    fee = (transaction_size / 1000) * fee_per_kb

    # Ensure the fee is not excessive (e.g., 8.18 BTC)
    if fee > input_amount:
        logging.warning("Calculated fee exceeds input amount. Using maximum allowed fee instead.")
        fee = input_amount * 0.01  # 1% of input amount as maximum allowed fee

    return fee

def main():
    try:
        # Example usage
        input_amount = 10.0  # 10 BTC input
        output_amount = 5.0   # 5 BTC output
        fee_per_kb = 0.0001  # 0.0001 BTC per kilobyte
        transaction_size = 500  # 500 bytes transaction size

        calculated_fee = calculate_transaction_fee(input_amount, output_amount, fee_per_kb, transaction_size)
        logging.info(f"Calculated transaction fee: {calculated_fee:.8f} BTC")

    except ValueError as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```
