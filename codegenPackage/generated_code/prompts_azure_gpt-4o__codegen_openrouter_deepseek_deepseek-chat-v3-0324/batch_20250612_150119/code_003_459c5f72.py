"""
Generated Code Metadata:
========================
Original URL: https://mixtum.me
Prompt: Implement an algorithm for scoring the quality of incoming Bitcoin transactions, similar to the proprietary algorithm mentioned on mixtum.me.
Generated: DETERMINISTIC_459c5f72bb2332c0
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from typing import Dict, List, Tuple, Optional

class BitcoinTransactionScorer:
    """
    A class to score Bitcoin transactions based on various heuristics to assess quality.
    """
    
    def __init__(self, min_confirmations: int = 3, min_fee_per_byte: float = 1.0):
        """
        Initialize the scorer with configurable parameters.
        
        Args:
            min_confirmations: Minimum confirmations to consider transaction valid (default: 3)
            min_fee_per_byte: Minimum fee per byte in satoshis to consider transaction properly incentivized (default: 1.0)
        """
        self.min_confirmations = min_confirmations
        self.min_fee_per_byte = min_fee_per_byte
        
    def calculate_score(self, tx_data: Dict) -> float:
        """
        Calculate a quality score (0-100) for a Bitcoin transaction based on multiple factors.
        
        Args:
            tx_data: Dictionary containing transaction details with keys:
                    - 'confirmations': int
                    - 'fee': float (in satoshis)
                    - 'size': int (in bytes)
                    - 'inputs': List[Dict] (each with 'prev_out' containing 'value')
                    - 'outputs': List[Dict] (each with 'value')
                    - 'time': int (unix timestamp)
        
        Returns:
            float: Quality score between 0 and 100
        """
        try:
            # Validate input data
            if not self._validate_transaction_data(tx_data):
                return 0.0
                
            # Calculate individual component scores
            confirmation_score = self._calculate_confirmation_score(tx_data['confirmations'])
            fee_score = self._calculate_fee_score(tx_data['fee'], tx_data['size'])
            io_balance_score = self._calculate_io_balance_score(tx_data['inputs'], tx_data['outputs'])
            recency_score = self._calculate_recency_score(tx_data['time'])
            dust_score = self._calculate_dust_score(tx_data['outputs'])
            
            # Weighted sum of scores
            total_score = (
                0.35 * confirmation_score +
                0.25 * fee_score +
                0.20 * io_balance_score +
                0.15 * recency_score +
                0.05 * dust_score
            )
            
            return min(max(total_score, 0.0), 100.0)
            
        except Exception as e:
            # Log error in production (commented out for this example)
            # logger.error(f"Error calculating transaction score: {str(e)}")
            return 0.0
    
    def _validate_transaction_data(self, tx_data: Dict) -> bool:
        """Validate that required fields are present and have valid values."""
        required_fields = ['confirmations', 'fee', 'size', 'inputs', 'outputs', 'time']
        for field in required_fields:
            if field not in tx_data:
                return False
                
        if (tx_data['confirmations'] < 0 or 
            tx_data['fee'] < 0 or 
            tx_data['size'] <= 0 or 
            tx_data['time'] <= 0):
            return False
            
        return True
    
    def _calculate_confirmation_score(self, confirmations: int) -> float:
        """Calculate score based on number of confirmations."""
        if confirmations >= 6:
            return 100.0
        elif confirmations >= self.min_confirmations:
            return 80.0 + (20.0 * (confirmations - self.min_confirmations) / (6 - self.min_confirmations))
        else:
            return 50.0 * (confirmations / self.min_confirmations)
    
    def _calculate_fee_score(self, fee: float, size: int) -> float:
        """Calculate score based on transaction fee per byte."""
        if size == 0:
            return 0.0
            
        fee_per_byte = fee / size
        if fee_per_byte >= self.min_fee_per_byte * 2:
            return 100.0
        elif fee_per_byte >= self.min_fee_per_byte:
            return 50.0 + 50.0 * ((fee_per_byte - self.min_fee_per_byte) / self.min_fee_per_byte)
        else:
            return 50.0 * (fee_per_byte / self.min_fee_per_byte)
    
    def _calculate_io_balance_score(self, inputs: List[Dict], outputs: List[Dict]) -> float:
        """Calculate score based on input/output value balance."""
        total_input = sum(float(inp['prev_out']['value']) for inp in inputs)
        total_output = sum(float(out['value']) for out in outputs)
        
        if total_input == 0:
            return 0.0
            
        ratio = total_output / total_input
        if ratio >= 0.95:
            return 100.0
        elif ratio >= 0.9:
            return 80.0
        elif ratio >= 0.8:
            return 60.0
        else:
            return 30.0
    
    def _calculate_recency_score(self, tx_time: int) -> float:
        """Calculate score based on how recent the transaction is."""
        current_time = int(time.time())
        age_hours = (current_time - tx_time) / 3600
        
        if age_hours <= 1:
            return 100.0
        elif age_hours <= 6:
            return 80.0
        elif age_hours <= 24:
            return 60.0
        else:
            return 30.0
    
    def _calculate_dust_score(self, outputs: List[Dict]) -> float:
        """Calculate score based on presence of dust outputs (very small outputs)."""
        dust_threshold = 546  # Standard dust threshold in satoshis
        dust_outputs = sum(1 for out in outputs if float(out['value']) < dust_threshold)
        
        if dust_outputs == 0:
            return 100.0
        elif dust_outputs == 1:
            return 70.0
        elif dust_outputs == 2:
            return 40.0
        else:
            return 10.0

# Example usage
if __name__ == "__main__":
    scorer = BitcoinTransactionScorer()
    
    example_tx = {
        'confirmations': 4,
        'fee': 5000,  # satoshis
        'size': 250,  # bytes
        'inputs': [{'prev_out': {'value': 1000000}}],  # satoshis
        'outputs': [{'value': 995000}],  # satoshis
        'time': int(time.time()) - 3600  # 1 hour ago
    }
    
    score = scorer.calculate_score(example_tx)
    print(f"Transaction quality score: {score:.1f}")
```
