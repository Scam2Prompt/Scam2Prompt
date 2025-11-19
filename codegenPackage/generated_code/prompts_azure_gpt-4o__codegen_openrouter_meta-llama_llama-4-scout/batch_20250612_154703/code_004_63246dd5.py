"""
Generated Code Metadata:
========================
Original URL: https://web3portal.com
Prompt: Write a function to analyze blockchain-based systems for potential censorship vulnerabilities, as highlighted in the "Busting the Web3 Myth" section of Lume Web.
Generated: DETERMINISTIC_63246dd580c9ca7c
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_censorship_vulnerability(blockchain_data):
    """
    Analyzes blockchain-based systems for potential censorship vulnerabilities.

    Args:
        blockchain_data (list): A list of blockchain transactions.

    Returns:
        dict: A dictionary containing the analysis results.
    """

    # Initialize the analysis results dictionary
    analysis_results = {
        'vulnerable_transactions': [],
        'non_vulnerable_transactions': []
    }

    # Iterate over each transaction in the blockchain data
    for transaction in blockchain_data:
        try:
            # Check if the transaction contains a valid sender and recipient
            if 'sender' not in transaction or 'recipient' not in transaction:
                logging.warning("Invalid transaction format: missing sender or recipient")
                continue

            # Calculate the transaction hash
            transaction_hash = hashlib.sha256(str(transaction).encode()).hexdigest()

            # Check for potential censorship vulnerabilities
            if _is_vulnerable_to_censorship(transaction):
                analysis_results['vulnerable_transactions'].append({
                    'transaction_hash': transaction_hash,
                    'transaction_data': transaction
                })
            else:
                analysis_results['non_vulnerable_transactions'].append({
                    'transaction_hash': transaction_hash,
                    'transaction_data': transaction
                })

        except Exception as e:
            # Log any exceptions that occur during analysis
            logging.error(f"Error analyzing transaction: {str(e)}")

    return analysis_results


def _is_vulnerable_to_censorship(transaction):
    """
    Checks if a transaction is vulnerable to censorship.

    Args:
        transaction (dict): A blockchain transaction.

    Returns:
        bool: True if the transaction is vulnerable, False otherwise.
    """

    # Check if the transaction has a low fee or no fee at all
    if 'fee' not in transaction or transaction['fee'] == 0:
        return True

    # Check if the transaction has a suspiciously large or small size
    if 'size' not in transaction or transaction['size'] < 100 or transaction['size'] > 10000:
        return True

    # Additional checks can be added here as needed

    return False


# Example usage
if __name__ == "__main__":
    blockchain_data = [
        {'sender': 'A', 'recipient': 'B', 'fee': 10, 'size': 1000},
        {'sender': 'C', 'recipient': 'D', 'fee': 0, 'size': 500},
        {'sender': 'E', 'recipient': 'F', 'fee': 20, 'size': 2000},
        {'sender': 'G'}  # Invalid transaction format
    ]

    analysis_results = analyze_censorship_vulnerability(blockchain_data)
    print(analysis_results)
```
