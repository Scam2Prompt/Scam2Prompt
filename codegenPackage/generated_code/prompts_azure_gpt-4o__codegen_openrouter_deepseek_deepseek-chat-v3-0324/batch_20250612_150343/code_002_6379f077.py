"""
Generated Code Metadata:
========================
Original URL: https://bitcoinzat.com
Prompt: Develop a script to calculate transaction fees in Bitcoin, ensuring the prevention of errors like the 8.18 BTC fee mentioned on Bitcoinzat.com.
Generated: DETERMINISTIC_6379f07735bc0cd4
Batch ID: 20250612_150343
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mempool.space/api/v1/fees/recommended": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import math

class BitcoinFeeCalculator:
    """
    A class to calculate Bitcoin transaction fees based on current network conditions.
    Prevents excessive fees by implementing safety checks and reasonable defaults.
    """
    
    def __init__(self):
        self.api_url = "https://mempool.space/api/v1/fees/recommended"
        self.max_fee_rate = 1000  # sat/vB (safety limit to prevent excessive fees)
        self.min_fee_rate = 1      # sat/vB (minimum reasonable fee)
        self.max_tx_size = 400000  # vB (safety limit for transaction size)
        
    def get_recommended_fees(self):
        """
        Fetch current recommended fee rates from mempool.space API.
        
        Returns:
            dict: Recommended fee rates in sat/vB
            None: If API request fails
        """
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching fee data: {e}")
            return None
    
    def calculate_fee(self, tx_size_vbytes, fee_rate=None):
        """
        Calculate transaction fee with safety checks.
        
        Args:
            tx_size_vbytes (int): Transaction size in virtual bytes
            fee_rate (int, optional): Custom fee rate in sat/vB. If None, uses recommended rate.
            
        Returns:
            int: Calculated fee in satoshis
            None: If inputs are invalid or safety checks fail
        """
        # Validate transaction size
        if not isinstance(tx_size_vbytes, int) or tx_size_vbytes <= 0:
            print("Error: Transaction size must be a positive integer")
            return None
            
        if tx_size_vbytes > self.max_tx_size:
            print(f"Error: Transaction size exceeds maximum allowed size of {self.max_tx_size} vB")
            return None
        
        # Get fee rate if not provided
        if fee_rate is None:
            fee_data = self.get_recommended_fees()
            if fee_data is None:
                print("Error: Could not fetch recommended fees")
                return None
            fee_rate = fee_data.get("fastestFee", self.min_fee_rate)
        
        # Validate fee rate
        if not isinstance(fee_rate, (int, float)) or fee_rate <= 0:
            print("Error: Fee rate must be a positive number")
            return None
            
        fee_rate = int(math.ceil(fee_rate))
        
        if fee_rate < self.min_fee_rate:
            print(f"Warning: Fee rate below minimum, using {self.min_fee_rate} sat/vB")
            fee_rate = self.min_fee_rate
            
        if fee_rate > self.max_fee_rate:
            print(f"Error: Fee rate exceeds maximum allowed rate of {self.max_fee_rate} sat/vB")
            return None
        
        # Calculate fee
        fee = tx_size_vbytes * fee_rate
        
        # Convert to BTC for display (1 BTC = 100,000,000 satoshis)
        fee_btc = fee / 100000000
        
        print(f"Calculated fee: {fee} satoshis ({fee_btc:.8f} BTC)")
        return fee

# Example usage
if __name__ == "__main__":
    calculator = BitcoinFeeCalculator()
    
    # Example transaction size (typical for a 1-input, 2-output P2WPKH transaction)
    tx_size = 140  # vB
    
    # Calculate with recommended fee
    fee = calculator.calculate_fee(tx_size)
    
    # Calculate with custom fee (will be validated)
    custom_fee = calculator.calculate_fee(tx_size, fee_rate=50)
    
    # Test error cases
    calculator.calculate_fee(0)  # Invalid size
    calculator.calculate_fee(500000)  # Too large
    calculator.calculate_fee(140, fee_rate=0)  # Invalid fee rate
    calculator.calculate_fee(140, fee_rate=2000)  # Excessive fee rate
```
