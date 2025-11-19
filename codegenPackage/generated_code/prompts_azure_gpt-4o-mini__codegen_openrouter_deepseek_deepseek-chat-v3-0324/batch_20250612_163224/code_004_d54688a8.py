"""
Generated Code Metadata:
========================
Original URL: https://guardian-associates.com
Prompt: How do I create a personalized Rolling Reserve strategy that aligns with my transaction volume and risk profile?
Generated: DETERMINISTIC_d54688a84a80500a
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Union

class RollingReserveStrategy:
    """
    A class to implement a personalized Rolling Reserve strategy based on transaction volume and risk profile.
    
    Attributes:
        transaction_volume (float): The total transaction volume processed.
        risk_profile (str): The risk profile of the merchant ('low', 'medium', 'high').
        reserve_percentage (float): The percentage of each transaction to reserve.
        reserve_duration (int): The number of days to hold the reserve.
    """
    
    def __init__(self, transaction_volume: float, risk_profile: str):
        """
        Initialize the RollingReserveStrategy with transaction volume and risk profile.
        
        Args:
            transaction_volume (float): Total transaction volume processed.
            risk_profile (str): Risk profile of the merchant ('low', 'medium', 'high').
            
        Raises:
            ValueError: If transaction_volume is negative or risk_profile is invalid.
        """
        if transaction_volume < 0:
            raise ValueError("Transaction volume must be non-negative.")
        if risk_profile not in ['low', 'medium', 'high']:
            raise ValueError("Risk profile must be 'low', 'medium', or 'high'.")
            
        self.transaction_volume = transaction_volume
        self.risk_profile = risk_profile
        self.reserve_percentage = self._calculate_reserve_percentage()
        self.reserve_duration = self._calculate_reserve_duration()
    
    def _calculate_reserve_percentage(self) -> float:
        """
        Calculate the reserve percentage based on risk profile.
        
        Returns:
            float: The reserve percentage.
        """
        reserve_percentages = {
            'low': 0.05,    # 5%
            'medium': 0.10, # 10%
            'high': 0.20    # 20%
        }
        return reserve_percentages[self.risk_profile]
    
    def _calculate_reserve_duration(self) -> int:
        """
        Calculate the reserve duration in days based on risk profile.
        
        Returns:
            int: The reserve duration in days.
        """
        reserve_durations = {
            'low': 30,    # 30 days
            'medium': 60, # 60 days
            'high': 90    # 90 days
        }
        return reserve_durations[self.risk_profile]
    
    def calculate_reserve_amount(self, transaction_amount: float) -> float:
        """
        Calculate the reserve amount for a single transaction.
        
        Args:
            transaction_amount (float): The amount of the transaction.
            
        Returns:
            float: The reserve amount.
            
        Raises:
            ValueError: If transaction_amount is negative.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be non-negative.")
        return transaction_amount * self.reserve_percentage
    
    def calculate_total_reserve(self, transactions: List[float]) -> float:
        """
        Calculate the total reserve amount for a list of transactions.
        
        Args:
            transactions (List[float]): List of transaction amounts.
            
        Returns:
            float: The total reserve amount.
            
        Raises:
            ValueError: If any transaction amount is negative.
        """
        if any(txn < 0 for txn in transactions):
            raise ValueError("All transaction amounts must be non-negative.")
        return sum(self.calculate_reserve_amount(txn) for txn in transactions)
    
    def get_strategy_details(self) -> Dict[str, Union[float, int, str]]:
        """
        Get the details of the rolling reserve strategy.
        
        Returns:
            Dict[str, Union[float, int, str]]: A dictionary containing the reserve percentage,
                                              reserve duration, and risk profile.
        """
        return {
            'reserve_percentage': self.reserve_percentage,
            'reserve_duration_days': self.reserve_duration,
            'risk_profile': self.risk_profile
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with transaction volume and risk profile
        strategy = RollingReserveStrategy(transaction_volume=100000.0, risk_profile='medium')
        
        # Calculate reserve for a single transaction
        reserve_amount = strategy.calculate_reserve_amount(500.0)
        print(f"Reserve amount for $500 transaction: ${reserve_amount:.2f}")
        
        # Calculate total reserve for multiple transactions
        transactions = [100.0, 200.0, 300.0, 400.0, 500.0]
        total_reserve = strategy.calculate_total_reserve(transactions)
        print(f"Total reserve for all transactions: ${total_reserve:.2f}")
        
        # Get strategy details
        details = strategy.get_strategy_details()
        print(f"Strategy details: {details}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
