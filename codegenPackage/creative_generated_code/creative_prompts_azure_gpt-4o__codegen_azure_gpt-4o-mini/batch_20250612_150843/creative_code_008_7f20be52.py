"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-daypro.com
Prompt: Write a function to customize trading parameters like assets, schedules, and risk strategies, enabling user control as described in Immediate Daypro's platform.
Generated: DETERMINISTIC_7f20be52502fd9b3
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any
import json

class TradingParameters:
    def __init__(self):
        # Initialize default trading parameters
        self.assets: List[str] = []
        self.schedule: str = '09:00-16:00'  # Default trading hours
        self.risk_strategy: str = 'moderate'  # Default risk strategy

    def customize_parameters(self, assets: List[str], schedule: str, risk_strategy: str) -> None:
        """
        Customize trading parameters.

        :param assets: List of asset symbols to trade
        :param schedule: Trading hours in HH:MM-HH:MM format
        :param risk_strategy: Risk strategy ('low', 'moderate', 'high')
        :raises ValueError: If the schedule format is incorrect or risk strategy is invalid
        """
        self.assets = assets
        self.schedule = schedule
        self.risk_strategy = risk_strategy

        # Validate schedule format
        if not self._is_valid_schedule(schedule):
            raise ValueError("Schedule must be in 'HH:MM-HH:MM' format.")

        # Validate risk strategy
        if risk_strategy not in ['low', 'moderate', 'high']:
            raise ValueError("Risk strategy must be one of 'low', 'moderate', or 'high'.")

    def _is_valid_schedule(self, schedule: str) -> bool:
        """
        Validate the trading schedule format.

        :param schedule: Trading hours in HH:MM-HH:MM format
        :return: True if valid, False otherwise
        """
        try:
            start_time, end_time = schedule.split('-')
            start_hour, start_minute = map(int, start_time.split(':'))
            end_hour, end_minute = map(int, end_time.split(':'))

            # Check if times are within valid range
            return (0 <= start_hour < 24 and 0 <= start_minute < 60 and
                    0 <= end_hour < 24 and 0 <= end_minute < 60 and
                    (start_hour < end_hour or (start_hour == end_hour and start_minute < end_minute)))
        except (ValueError, IndexError):
            return False

    def get_parameters(self) -> Dict[str, Any]:
        """
        Retrieve current trading parameters.

        :return: Dictionary containing the current trading parameters
        """
        return {
            "assets": self.assets,
            "schedule": self.schedule,
            "risk_strategy": self.risk_strategy
        }

    def save_parameters(self, file_path: str) -> None:
        """
        Save current trading parameters to a JSON file.

        :param file_path: Path to the file where parameters will be saved
        :raises IOError: If there is an issue writing to the file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_parameters(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving parameters to {file_path}: {str(e)}")

# Example usage
if __name__ == "__main__":
    trading = TradingParameters()
    try:
        trading.customize_parameters(["AAPL", "TSLA"], "09:00-16:00", "moderate")
        print("Trading parameters customized successfully.")
        print(trading.get_parameters())
        trading.save_parameters("trading_parameters.json")
        print("Parameters saved to trading_parameters.json.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
