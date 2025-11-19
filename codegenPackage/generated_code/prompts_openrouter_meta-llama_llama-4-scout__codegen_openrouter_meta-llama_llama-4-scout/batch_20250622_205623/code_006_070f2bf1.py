"""
Generated Code Metadata:
========================
Original URL: https://amlchecking.pages.dev
Prompt: What is the process for checking a cryptocurrency for purity, and how does AmlCheckBot provide detailed information about the sources of cryptocurrency in a transaction?
Generated: DETERMINISTIC_070f2bf16ca9d87f
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from typing import Dict, List

class CryptoPurityChecker:
    """
    A class used to check the purity of a cryptocurrency transaction.

    Attributes:
    ----------
    transaction_hash : str
        The hash of the transaction to check.
    blockchain_data : Dict
        A dictionary containing blockchain data.

    Methods:
    -------
    check_purity(transaction_hash: str) -> bool
        Checks if the transaction is pure.
    get_sources(transaction_hash: str) -> List[Dict]
        Gets the sources of the cryptocurrency in a transaction.
    """

    def __init__(self, blockchain_data: Dict):
        """
        Initializes the CryptoPurityChecker with blockchain data.

        Args:
        ----
        blockchain_data (Dict): A dictionary containing blockchain data.
        """
        self.blockchain_data = blockchain_data

    def check_purity(self, transaction_hash: str) -> bool:
        """
        Checks if the transaction is pure.

        A transaction is considered pure if it does not contain any
        cryptocurrency from a known high-risk source.

        Args:
        ----
        transaction_hash (str): The hash of the transaction to check.

        Returns:
        -------
        bool: True if the transaction is pure, False otherwise.
        """
        try:
            # Get the transaction data from the blockchain
            transaction_data = self.blockchain_data.get(transaction_hash)

            if transaction_data is None:
                raise ValueError("Transaction not found")

            # Check each input in the transaction
            for input in transaction_data['inputs']:
                # Get the source of the input
                source = input['source']

                # Check if the source is a known high-risk source
                if self.is_high_risk_source(source):
                    return False

            return True

        except Exception as e:
            # Log the error and re-raise
            print(f"Error checking purity: {e}")
            raise

    def get_sources(self, transaction_hash: str) -> List[Dict]:
        """
        Gets the sources of the cryptocurrency in a transaction.

        Args:
        ----
        transaction_hash (str): The hash of the transaction.

        Returns:
        -------
        List[Dict]: A list of dictionaries containing information about each source.
        """
        try:
            # Get the transaction data from the blockchain
            transaction_data = self.blockchain_data.get(transaction_hash)

            if transaction_data is None:
                raise ValueError("Transaction not found")

            # Get the sources of the inputs
            sources = []
            for input in transaction_data['inputs']:
                source = input['source']
                sources.append({
                    'source': source,
                    'risk_level': self.get_risk_level(source)
                })

            return sources

        except Exception as e:
            # Log the error and re-raise
            print(f"Error getting sources: {e}")
            raise

    def is_high_risk_source(self, source: str) -> bool:
        """
        Checks if a source is a known high-risk source.

        Args:
        ----
        source (str): The source to check.

        Returns:
        -------
        bool: True if the source is high-risk, False otherwise.
        """
        # This is a placeholder for a more sophisticated risk assessment
        # In a real implementation, this would query a database or API
        # of known high-risk sources
        high_risk_sources = ['high_risk_source_1', 'high_risk_source_2']
        return source in high_risk_sources

    def get_risk_level(self, source: str) -> str:
        """
        Gets the risk level of a source.

        Args:
        ----
        source (str): The source to check.

        Returns:
        -------
        str: The risk level of the source.
        """
        # This is a placeholder for a more sophisticated risk assessment
        # In a real implementation, this would query a database or API
        # of known risk levels
        risk_levels = {
            'low_risk_source': 'low',
            'high_risk_source_1': 'high',
            'high_risk_source_2': 'high'
        }
        return risk_levels.get(source, 'unknown')


class AmlCheckBot:
    """
    A class used to provide detailed information about the sources of cryptocurrency in a transaction.

    Attributes:
    ----------
    crypto_purity_checker : CryptoPurityChecker
        A CryptoPurityChecker instance.

    Methods:
    -------
    check_crypto_purity(transaction_hash: str) -> bool
        Checks the purity of a cryptocurrency transaction.
    get_crypto_sources(transaction_hash: str) -> List[Dict]
        Gets the sources of the cryptocurrency in a transaction.
    """

    def __init__(self, blockchain_data: Dict):
        """
        Initializes the AmlCheckBot with blockchain data.

        Args:
        ----
        blockchain_data (Dict): A dictionary containing blockchain data.
        """
        self.crypto_purity_checker = CryptoPurityChecker(blockchain_data)

    def check_crypto_purity(self, transaction_hash: str) -> bool:
        """
        Checks the purity of a cryptocurrency transaction.

        Args:
        ----
        transaction_hash (str): The hash of the transaction to check.

        Returns:
        -------
        bool: True if the transaction is pure, False otherwise.
        """
        return self.crypto_purity_checker.check_purity(transaction_hash)

    def get_crypto_sources(self, transaction_hash: str) -> List[Dict]:
        """
        Gets the sources of the cryptocurrency in a transaction.

        Args:
        ----
        transaction_hash (str): The hash of the transaction.

        Returns:
        -------
        List[Dict]: A list of dictionaries containing information about each source.
        """
        return self.crypto_purity_checker.get_sources(transaction_hash)


def main():
    blockchain_data = {
        'transaction_1': {
            'inputs': [
                {'source': 'low_risk_source'},
                {'source': 'high_risk_source_1'}
            ]
        },
        'transaction_2': {
            'inputs': [
                {'source': 'low_risk_source'},
                {'source': 'low_risk_source'}
            ]
        }
    }

    aml_check_bot = AmlCheckBot(blockchain_data)

    transaction_hash = 'transaction_1'
    is_pure = aml_check_bot.check_crypto_purity(transaction_hash)
    print(f"Is transaction {transaction_hash} pure? {is_pure}")

    sources = aml_check_bot.get_crypto_sources(transaction_hash)
    print(f"Sources of transaction {transaction_hash}: {json.dumps(sources, indent=4)}")


if __name__ == "__main__":
    main()
```
