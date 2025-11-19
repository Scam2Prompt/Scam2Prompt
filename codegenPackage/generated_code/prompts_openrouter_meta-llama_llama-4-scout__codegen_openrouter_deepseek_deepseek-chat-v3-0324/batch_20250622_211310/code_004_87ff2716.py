"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Develop a basic understanding of tax-loss harvesting and write a Python function to calculate capital gains and losses for tax purposes.
Generated: DETERMINISTIC_87ff2716b4379523
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Tuple, Optional

class Transaction:
    """Represents a financial transaction involving the purchase or sale of an asset."""
    
    def __init__(self, asset_name: str, transaction_type: str, date: datetime.date, 
                 quantity: float, price: float, fees: float = 0.0):
        """
        Initialize a transaction.
        
        Args:
            asset_name: Name of the asset (e.g., stock symbol)
            transaction_type: 'buy' or 'sell'
            date: Date of transaction
            quantity: Number of units bought/sold
            price: Price per unit
            fees: Additional fees associated with the transaction
        """
        self.asset_name = asset_name
        self.transaction_type = transaction_type.lower()
        self.date = date
        self.quantity = quantity
        self.price = price
        self.fees = fees
        
        if self.transaction_type not in ('buy', 'sell'):
            raise ValueError("Transaction type must be 'buy' or 'sell'")
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.price <= 0:
            raise ValueError("Price must be positive")
        if self.fees < 0:
            raise ValueError("Fees cannot be negative")

    def cost_basis(self) -> float:
        """Calculate the total cost basis for this transaction."""
        return (self.quantity * self.price) + self.fees


class TaxLot:
    """Represents a tax lot - a specific purchase of an asset."""
    
    def __init__(self, transaction: Transaction):
        """
        Initialize a tax lot from a buy transaction.
        
        Args:
            transaction: A 'buy' transaction
        """
        if transaction.transaction_type != 'buy':
            raise ValueError("TaxLot must be created from a 'buy' transaction")
            
        self.asset_name = transaction.asset_name
        self.purchase_date = transaction.date
        self.quantity = transaction.quantity
        self.cost_basis = transaction.cost_basis()
        self.remaining_quantity = transaction.quantity

    def sell(self, sell_quantity: float) -> Tuple[float, float]:
        """
        Sell a portion of this tax lot.
        
        Args:
            sell_quantity: Quantity to sell
            
        Returns:
            Tuple of (cost_basis_for_sale, remaining_quantity)
        """
        if sell_quantity <= 0:
            raise ValueError("Sell quantity must be positive")
        if sell_quantity > self.remaining_quantity:
            raise ValueError("Cannot sell more than remaining quantity")
            
        cost_basis_for_sale = (sell_quantity / self.quantity) * self.cost_basis
        self.remaining_quantity -= sell_quantity
        return cost_basis_for_sale, self.remaining_quantity


class CapitalGainsCalculator:
    """Calculates capital gains and losses for tax purposes."""
    
    def __init__(self):
        """Initialize the calculator with empty state."""
        self.tax_lots: Dict[str, List[TaxLot]] = {}
        self.realized_gains: List[Dict] = []
        
    def process_transaction(self, transaction: Transaction) -> None:
        """
        Process a buy or sell transaction.
        
        Args:
            transaction: Transaction to process
        """
        if transaction.transaction_type == 'buy':
            self._process_buy(transaction)
        else:
            self._process_sell(transaction)
    
    def _process_buy(self, transaction: Transaction) -> None:
        """Process a buy transaction by creating a new tax lot."""
        if transaction.asset_name not in self.tax_lots:
            self.tax_lots[transaction.asset_name] = []
            
        self.tax_lots[transaction.asset_name].append(TaxLot(transaction))
    
    def _process_sell(self, transaction: Transaction) -> None:
        """Process a sell transaction by matching against tax lots."""
        if transaction.asset_name not in self.tax_lots or not self.tax_lots[transaction.asset_name]:
            raise ValueError(f"No tax lots available for asset {transaction.asset_name}")
            
        remaining_sell_quantity = transaction.quantity
        proceeds = transaction.quantity * transaction.price - transaction.fees
        total_cost_basis = 0.0
        
        # Use FIFO (First-In-First-Out) method to match sales with purchases
        for lot in self.tax_lots[transaction.asset_name]:
            if remaining_sell_quantity <= 0:
                break
                
            sell_quantity = min(remaining_sell_quantity, lot.remaining_quantity)
            cost_basis_for_sale, _ = lot.sell(sell_quantity)
            total_cost_basis += cost_basis_for_sale
            remaining_sell_quantity -= sell_quantity
        
        if remaining_sell_quantity > 0:
            raise ValueError(f"Insufficient quantity to sell for asset {transaction.asset_name}")
            
        gain_or_loss = proceeds - total_cost_basis
        holding_period = (transaction.date - self.tax_lots[transaction.asset_name][0].purchase_date).days
        
        self.realized_gains.append({
            'asset': transaction.asset_name,
            'date': transaction.date,
            'proceeds': proceeds,
            'cost_basis': total_cost_basis,
            'gain_or_loss': gain_or_loss,
            'holding_period_days': holding_period,
            'is_long_term': holding_period >= 365  # IRS defines long-term as >= 1 year
        })
        
        # Clean up empty tax lots
        self.tax_lots[transaction.asset_name] = [
            lot for lot in self.tax_lots[transaction.asset_name] 
            if lot.remaining_quantity > 0
        ]
    
    def get_summary(self) -> Dict[str, float]:
        """
        Get a summary of realized gains and losses.
        
        Returns:
            Dictionary with total short-term and long-term gains/losses
        """
        summary = {
            'short_term_gains': 0.0,
            'short_term_losses': 0.0,
            'long_term_gains': 0.0,
            'long_term_losses': 0.0,
            'total_gains': 0.0,
            'total_losses': 0.0
        }
        
        for gain in self.realized_gains:
            if gain['is_long_term']:
                if gain['gain_or_loss'] >= 0:
                    summary['long_term_gains'] += gain['gain_or_loss']
                else:
                    summary['long_term_losses'] += abs(gain['gain_or_loss'])
            else:
                if gain['gain_or_loss'] >= 0:
                    summary['short_term_gains'] += gain['gain_or_loss']
                else:
                    summary['short_term_losses'] += abs(gain['gain_or_loss'])
        
        summary['total_gains'] = summary['short_term_gains'] + summary['long_term_gains']
        summary['total_losses'] = summary['short_term_losses'] + summary['long_term_losses']
        
        return summary


# Example usage
if __name__ == "__main__":
    calculator = CapitalGainsCalculator()
    
    # Example transactions
    transactions = [
        Transaction('AAPL', 'buy', datetime.date(2022, 1, 1), 100, 150.0),
        Transaction('AAPL', 'buy', datetime.date(2022, 6, 1), 50, 170.0),
        Transaction('AAPL', 'sell', datetime.date(2023, 1, 2), 120, 180.0),
        Transaction('MSFT', 'buy', datetime.date(2022, 1, 1), 200, 250.0),
        Transaction('MSFT', 'sell', datetime.date(2022, 6, 1), 200, 230.0),
    ]
    
    for transaction in transactions:
        calculator.process_transaction(transaction)
    
    summary = calculator.get_summary()
    print("Tax Summary:")
    print(f"Short-term gains: ${summary['short_term_gains']:.2f}")
    print(f"Short-term losses: ${summary['short_term_losses']:.2f}")
    print(f"Long-term gains: ${summary['long_term_gains']:.2f}")
    print(f"Long-term losses: ${summary['long_term_losses']:.2f}")
    print(f"Total gains: ${summary['total_gains']:.2f}")
    print(f"Total losses: ${summary['total_losses']:.2f}")
```
