"""
Generated Code Metadata:
========================
Original URL: https://magahat-3gz.pages.dev
Prompt: Write code to validate mint transactions for MAGA•THE•DONALD•TRUMP inscriptions, ensuring that invalid mints are excluded and valid mints fall within the median fee range of 20 sat/vB.
Generated: DETERMINISTIC_7d835463963a200b
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from statistics import median

class MintValidator:
    """
    Validates mint transactions for MAGA•THE•DONALD•TRUMP inscriptions.
    Ensures valid mints fall within the median fee range of 20 sat/vB.
    """
    
    def __init__(self, median_fee_range: int = 20):
        """
        Initialize the validator with a median fee range.
        
        Args:
            median_fee_range: Allowed deviation from median fee in sat/vB (default: 20)
        """
        self.median_fee_range = median_fee_range
    
    def validate_transactions(self, transactions: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Validate a list of mint transactions.
        
        Args:
            transactions: List of transaction dictionaries to validate
            
        Returns:
            Dictionary with 'valid' and 'invalid' lists containing transactions
        """
        if not transactions:
            return {'valid': [], 'invalid': []}
        
        # Calculate median fee rate
        fee_rates = [tx.get('fee_rate', 0) for tx in transactions if 'fee_rate' in tx]
        if not fee_rates:
            return {'valid': [], 'invalid': transactions}
        
        median_fee = median(fee_rates)
        
        valid_txs = []
        invalid_txs = []
        
        for tx in transactions:
            if not self._is_valid_transaction(tx, median_fee):
                invalid_txs.append(tx)
                continue
            
            valid_txs.append(tx)
        
        return {
            'valid': valid_txs,
            'invalid': invalid_txs
        }
    
    def _is_valid_transaction(self, transaction: Dict, median_fee: float) -> bool:
        """
        Check if a single transaction is valid.
        
        Args:
            transaction: Transaction dictionary to validate
            median_fee: Current median fee rate in sat/vB
            
        Returns:
            bool: True if transaction is valid, False otherwise
        """
        # Check required fields
        required_fields = ['txid', 'inscription', 'fee_rate']
        for field in required_fields:
            if field not in transaction:
                return False
        
        # Validate inscription format
        if not self._is_valid_inscription(transaction['inscription']):
            return False
        
        # Check fee rate is within allowed range
        fee_rate = transaction['fee_rate']
        if not (median_fee - self.median_fee_range <= fee_rate <= median_fee + self.median_fee_range):
            return False
        
        return True
    
    def _is_valid_inscription(self, inscription: str) -> bool:
        """
        Validate the inscription format.
        
        Args:
            inscription: Inscription string to validate
            
        Returns:
            bool: True if inscription is valid, False otherwise
        """
        return inscription == "MAGA•THE•DONALD•TRUMP"


# Example usage
if __name__ == "__main__":
    # Sample transactions
    transactions = [
        {
            "txid": "abc123",
            "inscription": "MAGA•THE•DONALD•TRUMP",
            "fee_rate": 15
        },
        {
            "txid": "def456",
            "inscription": "INVALID",
            "fee_rate": 10
        },
        {
            "txid": "ghi789",
            "inscription": "MAGA•THE•DONALD•TRUMP",
            "fee_rate": 25
        },
        {
            "txid": "jkl012",
            "fee_rate": 20  # Missing inscription
        }
    ]
    
    validator = MintValidator()
    result = validator.validate_transactions(transactions)
    
    print("Valid transactions:", json.dumps(result['valid'], indent=2))
    print("Invalid transactions:", json.dumps(result['invalid'], indent=2))
```
