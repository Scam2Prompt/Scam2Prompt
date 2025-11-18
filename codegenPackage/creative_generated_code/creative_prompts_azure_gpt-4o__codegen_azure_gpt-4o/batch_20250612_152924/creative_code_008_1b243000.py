"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-in.pages.dev
Prompt: Develop a tool that tracks the Green Bitcoin presale stages and dynamically updates the $GBTC token price based on the current presale phase.
Generated: DETERMINISTIC_1b243000ca6d3e36
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class GreenBitcoinPresale:
    """
    A class to track the Green Bitcoin ($GBTC) presale stages and dynamically update the token price.
    """

    def __init__(self):
        # Define presale stages with their respective prices
        self.presale_stages = [
            {"phase": 1, "price": 0.01, "end_date": datetime.datetime(2023, 12, 1, 23, 59, 59)},
            {"phase": 2, "price": 0.02, "end_date": datetime.datetime(2023, 12, 15, 23, 59, 59)},
            {"phase": 3, "price": 0.03, "end_date": datetime.datetime(2023, 12, 31, 23, 59, 59)},
        ]
        self.current_stage = None
        self.current_price = None
        self.update_stage()

    def update_stage(self):
        """
        Dynamically updates the presale stage and token price based on the current date and time.
        """
        now = datetime.datetime.now()

        for stage in self.presale_stages:
            if now <= stage["end_date"]:
                self.current_stage = stage["phase"]
                self.current_price = stage["price"]
                return

        # If no stages match, presale has ended
        self.current_stage = None
        self.current_price = None

    def get_current_price(self):
        """
        Returns the current $GBTC token price. Updates the stage before returning.
        """
        self.update_stage()
        if self.current_price is not None:
            return self.current_price
        else:
            raise ValueError("Presale has ended. $GBTC tokens are no longer available at presale pricing.")

    def get_current_stage(self):
        """
        Returns the current presale stage. Updates the stage before returning.
        """
        self.update_stage()
        if self.current_stage is not None:
            return self.current_stage
        else:
            raise ValueError("Presale has ended. No active presale stage.")

# Example usage:
if __name__ == "__main__":
    try:
        presale_tracker = GreenBitcoinPresale()
        print(f"Current Presale Stage: {presale_tracker.get_current_stage()}")
        print(f"Current $GBTC Price: ${presale_tracker.get_current_price():.2f}")
    except ValueError as e:
        print(str(e))
```
