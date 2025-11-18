"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardian-associates.com
Prompt: Write code to track and visualize Rolling Reserve account movements, providing real-time monitoring and detailed reporting, similar to the solutions offered by Guardian Associates.
Generated: DETERMINISTIC_c28831d7f3c87397
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class RollingReserveTracker:
    def __init__(self):
        """Initialize the tracker with an empty DataFrame to store account movements."""
        self.movements = pd.DataFrame(columns=['date', 'amount', 'description'])
    
    def add_movement(self, amount: float, description: str) -> None:
        """
        Add a movement to the Rolling Reserve account.

        Args:
            amount (float): The amount of the movement (positive for deposits, negative for withdrawals).
            description (str): A description of the movement.
        
        Raises:
            ValueError: If the amount is zero or if the description is empty.
        """
        if amount == 0:
            raise ValueError("Amount must be non-zero.")
        if not description:
            raise ValueError("Description must not be empty.")

        movement = {
            'date': datetime.now(),
            'amount': amount,
            'description': description
        }
        self.movements = self.movements.append(movement, ignore_index=True)
    
    def get_balance(self) -> float:
        """Calculate the current balance of the Rolling Reserve account."""
        return self.movements['amount'].sum()

    def visualize_movements(self) -> None:
        """Visualize the account movements over time using a line chart."""
        if self.movements.empty:
            print("No movements to visualize.")
            return
        
        plt.figure(figsize=(10, 5))
        plt.plot(self.movements['date'], self.movements['amount'].cumsum(), marker='o')
        plt.title('Rolling Reserve Account Movements')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Amount')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()
    
    def generate_report(self) -> pd.DataFrame:
        """Generate a detailed report of the account movements.

        Returns:
            pd.DataFrame: A DataFrame containing the report of movements.
        """
        if self.movements.empty:
            print("No movements to report.")
            return pd.DataFrame()
        
        report = self.movements.copy()
        report['cumulative'] = report['amount'].cumsum()
        return report

# Example usage
if __name__ == "__main__":
    try:
        tracker = RollingReserveTracker()
        tracker.add_movement(1000, "Initial deposit")
        tracker.add_movement(-200, "Withdrawal for expenses")
        tracker.add_movement(500, "Deposit for funding")
        
        print("Current Balance:", tracker.get_balance())
        
        report_df = tracker.generate_report()
        print(report_df)
        
        tracker.visualize_movements()
    except ValueError as e:
        print(f"Error: {e}")
```
