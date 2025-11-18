"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ststoned.pages.dev
Prompt: Create a script to bridge STONE tokens to Scroll and calculate earned STONE Points and Scroll Points as described in StakeStone's migration gateway.
Generated: DETERMINISTIC_a4dd660327169a9c
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TokenBridge:
    def __init__(self, stone_balance, scroll_balance):
        """
        Initialize the TokenBridge instance with given balances.

        Args:
            stone_balance (float): Initial balance of STONE tokens.
            scroll_balance (float): Initial balance of Scroll tokens.
        """
        self.stone_balance = stone_balance
        self.scroll_balance = scroll_balance
        self.stone_points = 0
        self.scroll_points = 0

    def bridge_tokens(self, stone_to_bridge):
        """
        Bridge STONE tokens to Scroll, update balances, and calculate points.

        Args:
            stone_to_bridge (float): Amount of STONE tokens to bridge.

        Returns:
            dict: Updated balances and points after bridging.
        """
        try:
            # Validate input
            if stone_to_bridge <= 0:
                raise ValueError("Amount to bridge must be greater than zero.")
            if stone_to_bridge > self.stone_balance:
                raise ValueError("Insufficient STONE balance to bridge.")

            # Perform bridging
            self.stone_balance -= stone_to_bridge
            self.scroll_balance += stone_to_bridge * 1.1  # Assuming a 1:1.1 conversion rate

            # Calculate points
            self.stone_points += stone_to_bridge * 0.5  # Earn 0.5 STONE Points per bridged token
            self.scroll_points += stone_to_bridge * 0.3  # Earn 0.3 Scroll Points per bridged token

            return {
                "stone_balance": self.stone_balance,
                "scroll_balance": self.scroll_balance,
                "stone_points": self.stone_points,
                "scroll_points": self.scroll_points
            }

        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

def main():
    """
    Main function to demonstrate token bridging.
    """
    try:
        # Initialize token bridge with sample balances
        stone_balance = 1000.0
        scroll_balance = 0.0
        bridge = TokenBridge(stone_balance, scroll_balance)

        print("Welcome to StakeStone's Migration Gateway!")
        print(f"Current STONE Balance: {bridge.stone_balance}")
        print(f"Current Scroll Balance: {bridge.scroll_balance}")

        # Input: amount of STONE tokens to bridge
        stone_to_bridge = float(input("Enter the amount of STONE tokens to bridge: "))

        # Perform token bridging and display results
        result = bridge.bridge_tokens(stone_to_bridge)
        if result:
            print("\nBridging Successful!")
            print(f"Updated STONE Balance: {result['stone_balance']}")
            print(f"Updated Scroll Balance: {result['scroll_balance']}")
            print(f"Earned STONE Points: {result['stone_points']}")
            print(f"Earned Scroll Points: {result['scroll_points']}")
        else:
            print("Failed to bridge tokens.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
