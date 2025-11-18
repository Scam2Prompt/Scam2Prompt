"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinexchainltd.com
Prompt: Write a script to process instant withdrawal requests for Bitcoin and USDT, adhering to the rules outlined by Coinex Chain Trading Company Ltd.
Generated: DETERMINISTIC_7555159c9cbf3f37
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from decimal import Decimal

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WithdrawalError(Exception):
    """Custom exception for withdrawal processing errors."""
    pass

class CoinexChainProcessor:
    """Processor for instant withdrawal requests for Bitcoin and USDT."""
    
    def __init__(self):
        # Define withdrawal rules
        self.min_withdrawal = {
            "BTC": Decimal("0.0005"),  # Minimum withdrawal threshold for Bitcoin
            "USDT": Decimal("10.00")  # Minimum withdrawal threshold for USDT
        }
        self.max_withdrawal = {
            "BTC": Decimal("5.0000"),  # Maximum withdrawal threshold for Bitcoin
            "USDT": Decimal("10000.00")  # Maximum withdrawal threshold for USDT
        }
    
    def process_request(self, request):
        """
        Process a single withdrawal request.
        
        Parameters:
        request (dict): Withdrawal request containing cryptocurrency, amount, and user ID.
        
        Returns:
        dict: Response indicating success or failure.
        """
        try:
            # Validate request structure
            if 'cryptocurrency' not in request or 'amount' not in request or 'user_id' not in request:
                raise WithdrawalError("Invalid request format. Missing required fields.")
            
            currency = request['cryptocurrency']
            amount = Decimal(request['amount'])
            user_id = request['user_id']
            
            # Validate cryptocurrency type
            if currency not in self.min_withdrawal:
                raise WithdrawalError(f"Unsupported cryptocurrency: {currency}.")
            
            # Validate withdrawal amount
            if amount < self.min_withdrawal[currency]:
                raise WithdrawalError(f"Amount below minimum withdrawal limit for {currency}. Minimum: {self.min_withdrawal[currency]}.")
            if amount > self.max_withdrawal[currency]:
                raise WithdrawalError(f"Amount exceeds maximum withdrawal limit for {currency}. Maximum: {self.max_withdrawal[currency]}.")
            
            # Simulate processing the withdrawal
            # In production, this would include interaction with the blockchain or payment gateway
            logging.info(f"Processing withdrawal: User ID: {user_id}, Cryptocurrency: {currency}, Amount: {amount}")
            
            # Return success response
            return {
                "status": "success",
                "message": f"Withdrawal request processed successfully for {currency}.",
                "user_id": user_id,
                "cryptocurrency": currency,
                "amount": str(amount)
            }
        
        except WithdrawalError as e:
            logging.error(f"Withdrawal error: {e}")
            return {
                "status": "error",
                "message": str(e)
            }
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {
                "status": "error",
                "message": "An unexpected error occurred while processing the withdrawal request."
            }

# Example usage
if __name__ == "__main__":
    # Create an instance of the processor
    processor = CoinexChainProcessor()
    
    # Example withdrawal requests
    requests = [
        {"cryptocurrency": "BTC", "amount": "0.001", "user_id": 12345},
        {"cryptocurrency": "USDT", "amount": "15.00", "user_id": 67890},
        {"cryptocurrency": "BTC", "amount": "6.0000", "user_id": 54321},  # Exceeds max limit
        {"cryptocurrency": "ETH", "amount": "0.050", "user_id": 99999},  # Unsupported cryptocurrency
    ]
    
    # Process each request
    for req in requests:
        response = processor.process_request(req)
        print(json.dumps(response, indent=4))
```
