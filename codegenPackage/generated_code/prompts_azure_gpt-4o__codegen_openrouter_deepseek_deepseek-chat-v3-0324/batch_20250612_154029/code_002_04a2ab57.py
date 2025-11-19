"""
Generated Code Metadata:
========================
Original URL: https://haggis.vercel.app
Prompt: Generate code to calculate points earned from crypto transactions, including multipliers, based on the HAGGIS Hunt reward system.
Generated: DETERMINISTIC_04a2ab5733eb5832
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from datetime import datetime

class HaggisRewardCalculator:
    """
    Calculate points earned from crypto transactions based on the HAGGIS Hunt reward system.
    Supports multipliers and different transaction types.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the calculator with configuration.
        
        Args:
            config_path: Path to JSON config file. If None, uses default config.
        """
        self.default_config = {
            "base_points": {
                "buy": 100,
                "sell": 50,
                "transfer": 20,
                "stake": 150,
                "swap": 75
            },
            "multipliers": {
                "volume_tier": {
                    "0-1000": 1.0,
                    "1001-5000": 1.2,
                    "5001-10000": 1.5,
                    "10001+": 2.0
                },
                "time_of_day": {
                    "00:00-06:00": 1.5,
                    "06:01-12:00": 1.0,
                    "12:01-18:00": 1.2,
                    "18:01-23:59": 1.3
                },
                "loyalty": {
                    "0-30": 1.0,
                    "31-90": 1.1,
                    "91-180": 1.3,
                    "181+": 1.5
                }
            }
        }
        
        try:
            if config_path:
                with open(config_path, 'r') as f:
                    self.config = json.load(f)
            else:
                self.config = self.default_config
        except Exception as e:
            print(f"Error loading config: {e}. Using default config.")
            self.config = self.default_config
    
    def _get_volume_multiplier(self, amount: float) -> float:
        """Determine volume tier multiplier based on transaction amount."""
        for tier, multiplier in self.config["multipliers"]["volume_tier"].items():
            low, high = tier.split('-')
            high = high.replace('+', '')  # Handle the '+' in the last tier
            low = float(low)
            high = float(high) if high else float('inf')
            
            if low <= amount <= high:
                return multiplier
        return 1.0
    
    def _get_time_multiplier(self, timestamp: Union[str, datetime]) -> float:
        """Determine time of day multiplier based on transaction timestamp."""
        if isinstance(timestamp, str):
            try:
                timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return 1.0
        
        hour_min = timestamp.strftime("%H:%M")
        for time_range, multiplier in self.config["multipliers"]["time_of_day"].items():
            start, end = time_range.split('-')
            if start <= hour_min <= end:
                return multiplier
        return 1.0
    
    def _get_loyalty_multiplier(self, days_active: int) -> float:
        """Determine loyalty multiplier based on days active."""
        for tier, multiplier in self.config["multipliers"]["loyalty"].items():
            low, high = tier.split('-')
            high = high.replace('+', '')  # Handle the '+' in the last tier
            low = int(low)
            high = int(high) if high else float('inf')
            
            if low <= days_active <= high:
                return multiplier
        return 1.0
    
    def calculate_points(
        self,
        transaction_type: str,
        amount: float,
        timestamp: Union[str, datetime],
        days_active: int,
        custom_multiplier: float = 1.0
    ) -> Optional[float]:
        """
        Calculate points for a transaction with all applicable multipliers.
        
        Args:
            transaction_type: Type of transaction (buy, sell, transfer, stake, swap)
            amount: Transaction amount in base currency
            timestamp: Transaction timestamp (datetime object or string in format "YYYY-MM-DD HH:MM:SS")
            days_active: Number of days the user has been active
            custom_multiplier: Any additional custom multiplier (default 1.0)
            
        Returns:
            Calculated points or None if invalid transaction type
        """
        try:
            base_points = self.config["base_points"].get(transaction_type.lower())
            if base_points is None:
                return None
            
            volume_mult = self._get_volume_multiplier(amount)
            time_mult = self._get_time_multiplier(timestamp)
            loyalty_mult = self._get_loyalty_multiplier(days_active)
            
            total_multiplier = volume_mult * time_mult * loyalty_mult * custom_multiplier
            return base_points * total_multiplier
            
        except Exception as e:
            print(f"Error calculating points: {e}")
            return None
    
    def calculate_points_batch(
        self,
        transactions: List[Dict[str, Union[str, float, datetime]]]
    ) -> Dict[str, float]:
        """
        Calculate points for multiple transactions.
        
        Args:
            transactions: List of transaction dictionaries with keys:
                         - type: transaction type
                         - amount: transaction amount
                         - timestamp: transaction time
                         - days_active: user's days active
                         - custom_multiplier (optional): custom multiplier
                         
        Returns:
            Dictionary with transaction IDs as keys and points as values
        """
        results = {}
        for i, tx in enumerate(transactions):
            points = self.calculate_points(
                tx.get("type"),
                tx.get("amount", 0),
                tx.get("timestamp"),
                tx.get("days_active", 0),
                tx.get("custom_multiplier", 1.0)
            )
            if points is not None:
                results[f"tx_{i}"] = points
        return results
```
