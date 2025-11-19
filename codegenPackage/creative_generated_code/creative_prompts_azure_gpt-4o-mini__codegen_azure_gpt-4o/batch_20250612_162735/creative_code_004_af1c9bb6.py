"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://particlefi.pages.dev
Prompt: Illustrate how to implement a leaderboard feature that displays the top trading positions based on performance metrics like PnL and leverage on Particle.
Generated: DETERMINISTIC_af1c9bb6982726cb
Batch ID: 20250612_162735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json
from typing import List, Dict, Any


# Define a class for the leaderboard
class Leaderboard:
    """
    Leaderboard class to manage and display trading positions based on performance metrics like PnL and leverage.
    """

    def __init__(self):
        """
        Initialize the Leaderboard instance with an empty list of positions.
        """
        self.positions = []

    def add_position(self, trader_id: str, pnl: float, leverage: float) -> None:
        """
        Add a trading position to the leaderboard.

        :param trader_id: Unique identifier for the trader.
        :param pnl: Profit and Loss value (float).
        :param leverage: Leverage value (float).
        :raises ValueError: If PnL or leverage are non-positive values.
        """
        if pnl <= 0 or leverage <= 0:
            raise ValueError("PnL and leverage must be positive values.")
        
        self.positions.append(
            {
                "trader_id": trader_id,
                "pnl": pnl,
                "leverage": leverage,
            }
        )

    def get_top_positions(self, top_n: int = 10, sort_by: str = "pnl") -> List[Dict[str, Any]]:
        """
        Retrieve the top trading positions sorted by the specified metric.

        :param top_n: Number of top positions to return (default is 10).
        :param sort_by: Metric to sort by ("pnl" or "leverage", default is "pnl").
        :return: List of top trading positions.
        :raises ValueError: If sort_by is not either "pnl" or "leverage".
        """
        if sort_by not in {"pnl", "leverage"}:
            raise ValueError('Invalid sort_by value. Must be "pnl" or "leverage".')
        
        # Sort positions by the specified metric in descending order
        sorted_positions = sorted(self.positions, key=lambda x: x[sort_by], reverse=True)
        
        # Return only the top N positions
        return sorted_positions[:top_n]

    def save_to_file(self, file_path: str) -> None:
        """
        Save the leaderboard data to a JSON file.

        :param file_path: Path of the file to save the leaderboard data.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.positions, file, indent=4)
        except Exception as e:
            print(f"Error saving leaderboard data to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Load leaderboard data from a JSON file.

        :param file_path: Path of the file to load the leaderboard data from.
        """
        try:
            with open(file_path, "r") as file:
                self.positions = json.load(file)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON data from file: {file_path}")
        except Exception as e:
            print(f"Unexpected error loading leaderboard data: {e}")


# Example usage of the Leaderboard class
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Add trading positions
    leaderboard.add_position(trader_id="Trader1", pnl=5000.0, leverage=10.0)
    leaderboard.add_position(trader_id="Trader2", pnl=15000.0, leverage=15.0)
    leaderboard.add_position(trader_id="Trader3", pnl=7500.0, leverage=12.0)

    # Retrieve the top positions
    top_positions_by_pnl = leaderboard.get_top_positions(top_n=3, sort_by="pnl")
    print("Top Positions by PnL:")
    print(top_positions_by_pnl)

    # Save leaderboard to a file
    leaderboard.save_to_file("leaderboard.json")

    # Load leaderboard from a file
    leaderboard.load_from_file("leaderboard.json")
    print("Leaderboard data after loading from file:")
    print(leaderboard.positions)
```
