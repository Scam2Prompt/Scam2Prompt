"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinzat.com
Prompt: Develop a script to calculate transaction fees in Bitcoin, ensuring the prevention of errors like the 8.18 BTC fee mentioned on Bitcoinzat.com.
Generated: DETERMINISTIC_6379f07735bc0cd4
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to track errors and important information
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_transaction_fee(input_amounts, output_amounts, fee_rate_per_byte, transaction_size_bytes):
    """
    Calculate the transaction fee for a Bitcoin transaction.

    Args:
        input_amounts (list of float): List of input amounts in BTC.
        output_amounts (list of float): List of output amounts in BTC.
        fee_rate_per_byte (float): Fee rate in BTC per byte.
        transaction_size_bytes (int): Total size of the transaction in bytes.

    Returns:
        float: Calculated transaction fee in BTC.
    """
    try:
        # Validate input data
        if not isinstance(input_amounts, list) or not isinstance(output_amounts, list):
            raise ValueError("Input and output amounts must be lists.")
        if not all(isinstance(amount, (int, float)) and amount >= 0 for amount in input_amounts + output_amounts):
            raise ValueError("Amounts must be non-negative numbers.")
        if not isinstance(fee_rate_per_byte, (int, float)) or fee_rate_per_byte < 0:
            raise ValueError("Fee rate must be a non-negative number.")
        if not isinstance(transaction_size_bytes, int) or transaction_size_bytes <= 0:
            raise ValueError("Transaction size must be a positive integer.")

        # Calculate total input and output amounts
        total_input = sum(input_amounts)
        total_output = sum(output_amounts)

        # Calculate fee based on the fee rate and transaction size
        fee = fee_rate_per_byte * transaction_size_bytes

        # Ensure fee doesn't exceed the difference between inputs and outputs
        if fee > (total_input - total_output):
            raise ValueError(
                f"Calculated fee ({fee:.8f} BTC) exceeds the difference "
                f"between total inputs ({total_input:.8f} BTC) and outputs ({total_output:.8f} BTC)."
            )

        logging.info(f"Transaction Fee calculated successfully: {fee:.8f} BTC")
        return fee

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise


# Example usage (replace with real transaction data in production)
if __name__ == "__main__":
    try:
        # Example data
        inputs = [0.5, 0.3]  # Total inputs: 0.8 BTC
        outputs = [0.75]  # Total outputs: 0.75 BTC
        fee_rate = 0.00000001  # Fee rate per byte
        size = 250  # Transaction size in bytes

        fee = calculate_transaction_fee(inputs, outputs, fee_rate, size)
        print(f"Transaction fee: {fee:.8f} BTC")

    except Exception as e:
        print(f"Error: {e}")
```
