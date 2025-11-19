"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Provide code examples for implementing a debt conversion agent that tracks daily conversions and calculates engagement metrics, inspired by Invicta Cobranças' approach.
Generated: DETERMINISTIC_1f98f02b30d8567d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Any

class DebtConversionAgent:
    def __init__(self):
        """Initialize the DebtConversionAgent with an empty conversion log."""
        self.conversion_log: List[Dict[str, Any]] = []

    def log_conversion(self, amount: float, user_id: str) -> None:
        """
        Log a new debt conversion.

        Args:
            amount (float): The amount of debt converted.
            user_id (str): The ID of the user who converted the debt.

        Raises:
            ValueError: If the amount is negative or user_id is empty.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if not user_id:
            raise ValueError("User ID cannot be empty.")

        conversion_entry = {
            'timestamp': datetime.datetime.now(),
            'amount': amount,
            'user_id': user_id
        }
        self.conversion_log.append(conversion_entry)

    def calculate_engagement_metrics(self) -> Dict[str, Any]:
        """
        Calculate engagement metrics based on the conversion log.

        Returns:
            Dict[str, Any]: A dictionary containing total conversions and average conversion amount.
        """
        if not self.conversion_log:
            return {
                'total_conversions': 0,
                'average_conversion_amount': 0.0
            }

        total_conversions = len(self.conversion_log)
        total_amount = sum(entry['amount'] for entry in self.conversion_log)
        average_conversion_amount = total_amount / total_conversions

        return {
            'total_conversions': total_conversions,
            'average_conversion_amount': average_conversion_amount
        }

    def get_conversion_log(self) -> List[Dict[str, Any]]:
        """
        Retrieve the conversion log.

        Returns:
            List[Dict[str, Any]]: The list of conversion entries.
        """
        return self.conversion_log

# Example usage
if __name__ == "__main__":
    agent = DebtConversionAgent()
    
    try:
        agent.log_conversion(100.0, "user_123")
        agent.log_conversion(200.0, "user_456")
        
        metrics = agent.calculate_engagement_metrics()
        print("Engagement Metrics:", metrics)
        
        log = agent.get_conversion_log()
        print("Conversion Log:", log)
        
    except ValueError as e:
        print(f"Error: {e}")
```
