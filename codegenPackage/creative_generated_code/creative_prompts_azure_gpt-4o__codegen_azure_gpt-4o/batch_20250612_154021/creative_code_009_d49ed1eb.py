"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrdex.com
Prompt: Develop a Python program to switch between Simple Mode and Pro Mode on Aster DEX and execute trades based on user preferences.
Generated: DETERMINISTIC_d49ed1ebdccd0a2e
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class AsterDEX:
    def __init__(self):
        self.mode = "Simple"  # Default mode: Simple Mode
        self.trade_history = []

    def switch_mode(self):
        """Switch between Simple Mode and Pro Mode."""
        if self.mode == "Simple":
            self.mode = "Pro"
        else:
            self.mode = "Simple"
        print(f"Mode switched to: {self.mode}")

    def execute_trade(self, trade_type, amount, price):
        """
        Execute a trade based on user preferences.

        :param trade_type: Type of trade ('buy' or 'sell')
        :param amount: Amount of asset to trade
        :param price: Price per unit of the asset
        """
        try:
            if trade_type not in ['buy', 'sell']:
                raise ValueError("Invalid trade type. Please use 'buy' or 'sell'.")
            
            if amount <= 0 or price <= 0:
                raise ValueError("Amount and price must be positive numbers.")
            
            trade = {
                'type': trade_type,
                'amount': amount,
                'price': price,
                'mode': self.mode
            }
            # Simulate trade execution
            self.trade_history.append(trade)
            print(f"Trade executed: {trade}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_trade_history(self):
        """Display all executed trades."""
        if not self.trade_history:
            print("No trades have been executed yet.")
        else:
            print("Trade History:")
            for trade in self.trade_history:
                print(trade)

def main():
    dex = AsterDEX()
    
    print("Welcome to Aster DEX!")
    print("Commands: switch_mode, execute_trade, view_trade_history, exit")
    
    while True:
        command = input("\nEnter a command: ").strip().lower()
        if command == 'switch_mode':
            dex.switch_mode()
        elif command == 'execute_trade':
            try:
                trade_type = input("Enter trade type (buy/sell): ").strip().lower()
                amount = float(input("Enter amount: "))
                price = float(input("Enter price: "))
                dex.execute_trade(trade_type, amount, price)
            except ValueError:
                print("Invalid input. Please try again.")
        elif command == 'view_trade_history':
            dex.view_trade_history()
        elif command == 'exit':
            print("Exiting Aster DEX. Goodbye!")
            sys.exit(0)
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
```
