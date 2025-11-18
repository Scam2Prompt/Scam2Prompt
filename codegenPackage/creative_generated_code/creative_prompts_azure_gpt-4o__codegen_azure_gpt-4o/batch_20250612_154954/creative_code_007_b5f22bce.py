"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoxglobal.com
Prompt: Write code to implement a trading schedule for metals (Gold, XAG, XPD, XPT) that adheres to Cryptoexglobal's server time constraints.
Generated: DETERMINISTIC_b5f22bcecdf793d0
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, time

class TradingSchedule:
    """
    A class to manage the trading schedules for metals on Cryptoexglobal's server.
    
    Metals supported:
        - Gold (XAU)
        - Silver (XAG)
        - Palladium (XPD)
        - Platinum (XPT)

    Server time constraints assumed:
        - Trading Hours: Monday to Friday, 00:00 - 22:00 (UTC)
        - Closed during weekends (Saturday and Sunday)
    """

    def __init__(self):
        """
        Initializes the trading schedule with the supported metals and trading hours.
        """
        self.metals = ["XAU", "XAG", "XPD", "XPT"]
        self.trading_start_time = time(hour=0, minute=0)  # 00:00 UTC
        self.trading_end_time = time(hour=22, minute=0)   # 22:00 UTC

    def is_trading_open(self, metal: str) -> bool:
        """
        Checks if trading is open for the specified metal based on server time.
        
        Args:
            metal (str): The metal symbol (e.g., 'XAU', 'XAG', 'XPD', 'XPT').

        Returns:
            bool: True if trading is open, False otherwise.
        """
        # Validate the input metal
        if metal not in self.metals:
            raise ValueError(f"Unsupported metal: {metal}. Supported metals are: {', '.join(self.metals)}")

        # Get the current server time in UTC
        now = datetime.utcnow()
        current_time = now.time()
        current_day = now.weekday()  # 0 = Monday, ..., 6 = Sunday

        # Check if today is a trading day (Monday to Friday) and within trading hours
        if current_day < 5 and self.trading_start_time <= current_time <= self.trading_end_time:
            return True
        return False

    def get_trading_schedule(self) -> str:
        """
        Provides the trading schedule details for supported metals.

        Returns:
            str: A formatted string describing the trading schedule.
        """
        schedule = (
            "Trading Schedule for Metals:\n"
            " - Trading Hours: Monday to Friday, 00:00 - 22:00 (UTC)\n"
            " - Closed during weekends (Saturday and Sunday)\n"
            "Supported Metals: " + ", ".join(self.metals)
        )
        return schedule


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the trading schedule
        schedule = TradingSchedule()
        
        # Print the trading schedule
        print(schedule.get_trading_schedule())
        
        # Check if trading is open for Gold (XAU)
        metal = "XAU"
        if schedule.is_trading_open(metal):
            print(f"Trading is OPEN for {metal}.")
        else:
            print(f"Trading is CLOSED for {metal}.")
    except ValueError as e:
        # Handle unsupported metals
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An unexpected error occurred: {e}")
```
