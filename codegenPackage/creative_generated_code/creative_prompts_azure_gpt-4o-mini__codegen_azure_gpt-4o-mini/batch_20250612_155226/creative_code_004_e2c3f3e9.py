"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gass-fee.pages.dev
Prompt: How do gas fees impact the cost basis for individual investors when buying or selling crypto assets?
Generated: DETERMINISTIC_e2c3f3e933b2adeb
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from typing import List, Dict

# Set the precision for Decimal operations
decimal.getcontext().prec = 10

class CryptoTransaction:
    """
    A class to represent a cryptocurrency transaction.
    
    Attributes:
        asset (str): The name of the cryptocurrency.
        quantity (Decimal): The quantity of the cryptocurrency bought or sold.
        price_per_unit (Decimal): The price per unit of the cryptocurrency.
        gas_fee (Decimal): The gas fee associated with the transaction.
    """
    
    def __init__(self, asset: str, quantity: str, price_per_unit: str, gas_fee: str):
        self.asset = asset
        self.quantity = decimal.Decimal(quantity)
        self.price_per_unit = decimal.Decimal(price_per_unit)
        self.gas_fee = decimal.Decimal(gas_fee)

    def total_cost(self) -> decimal.Decimal:
        """
        Calculate the total cost (including gas fees) for buying or selling the asset.
        
        Returns:
            Decimal: Total cost of the transaction.
        """
        try:
            return (self.quantity * self.price_per_unit) + self.gas_fee
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return decimal.Decimal('0')

    def cost_basis(self) -> decimal.Decimal:
        """
        Calculate the cost basis of the transaction.
        
        Returns:
            Decimal: Cost basis per unit of the asset.
        """
        try:
            if self.quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            return self.total_cost() / self.quantity
        except Exception as e:
            print(f"Error calculating cost basis: {e}")
            return decimal.Decimal('0')

def analyze_transactions(transactions: List[Dict]) -> List[Dict]:
    """
    Analyze a list of transactions to compute total costs and cost basis.
    
    Args:
        transactions (List[Dict]): A list of transaction dictionaries with keys: 
                                    'asset', 'quantity', 'price_per_unit', 'gas_fee'.
    
    Returns:
        List[Dict]: A list of dictionaries containing the asset, total cost, and cost basis.
    """
    results = []
    
    for txn in transactions:
        try:
            transaction = CryptoTransaction(
                asset=txn['asset'],
                quantity=txn['quantity'],
                price_per_unit=txn['price_per_unit'],
                gas_fee=txn['gas_fee']
            )
            
            results.append({
                'asset': transaction.asset,
                'total_cost': str(transaction.total_cost()),
                'cost_basis': str(transaction.cost_basis())
            })
        except KeyError as e:
            print(f"Missing key in transaction data: {e}")
        except ValueError as e:
            print(f"Invalid value in transaction data: {e}")
    
    return results

# Example usage
if __name__ == "__main__":
    transaction_data = [
        {'asset': 'Bitcoin', 'quantity': '0.001', 'price_per_unit': '60000', 'gas_fee': '5'},
        {'asset': 'Ethereum', 'quantity': '0.5', 'price_per_unit': '4000', 'gas_fee': '10'},
        {'asset': 'Litecoin', 'quantity': '2', 'price_per_unit': '200', 'gas_fee': '2'}
    ]
    
    analysis_results = analyze_transactions(transaction_data)
    for result in analysis_results:
        print(result)
```
