"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Write a function that calculates the effective leverage for a given portfolio on the CVEX platform, considering both long and short positions.
Generated: DETERMINISTIC_cf195edd06e45905
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Portfolio:
    def __init__(self):
        self.positions = []

    def add_position(self, position):
        """
        Add a position to the portfolio.
        
        Args:
            position (dict): A dictionary containing 'type' ('long' or 'short'), 
                             'amount' (float), and 'leverage' (float).
        """
        if position['type'] not in ['long', 'short']:
            raise ValueError("Position type must be 'long' or 'short'.")
        if position['amount'] <= 0 or position['leverage'] <= 0:
            raise ValueError("Amount and leverage must be greater than zero.")
        self.positions.append(position)

    def calculate_effective_leverage(self):
        """
        Calculate the effective leverage of the portfolio.
        
        Returns:
            float: The effective leverage of the portfolio.
        
        Raises:
            ZeroDivisionError: If the total equity is zero, preventing division by zero.
        """
        total_equity = 0
        total_loan = 0

        for position in self.positions:
            if position['type'] == 'long':
                total_equity += position['amount']  # Equity from long positions
                total_loan += position['amount'] * (position['leverage'] - 1)  # Loan from long leverage
            elif position['type'] == 'short':
                total_equity -= position['amount']  # Equity loss from short positions
                total_loan += position['amount'] * (position['leverage'] - 1)  # Loan from short leverage

        if total_equity == 0:
            raise ZeroDivisionError("Total equity cannot be zero when calculating effective leverage.")

        effective_leverage = (total_loan + total_equity) / total_equity
        return effective_leverage

# Example usage
if __name__ == "__main__":
    portfolio = Portfolio()
    try:
        portfolio.add_position({'type': 'long', 'amount': 1000, 'leverage': 2})
        portfolio.add_position({'type': 'short', 'amount': 500, 'leverage': 1.5})
        print("Effective Leverage:", portfolio.calculate_effective_leverage())
    except Exception as e:
        print("An error occurred:", str(e))
```
