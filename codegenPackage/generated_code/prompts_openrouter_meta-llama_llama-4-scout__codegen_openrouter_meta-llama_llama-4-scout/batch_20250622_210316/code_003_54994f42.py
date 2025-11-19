"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: Design an API for tracking token sale progress, including metrics like presale cap and total supply, using the $JESSE sale as a reference.
Generated: DETERMINISTIC_54994f428e76a04b
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_sale_tracker.py

from typing import Dict
from dataclasses import dataclass

@dataclass
class TokenSale:
    """Represents a token sale with its metrics."""
    presale_cap: float
    total_supply: float
    sold: float = 0.0

    def sell_tokens(self, amount: float) -> None:
        """Sells a certain amount of tokens and updates the sold amount."""
        if amount < 0:
            raise ValueError("Token sale amount cannot be negative.")
        if self.sold + amount > self.presale_cap:
            raise ValueError("Token sale amount exceeds presale cap.")
        self.sold += amount

    def get_progress(self) -> float:
        """Returns the progress of the token sale as a percentage."""
        if self.presale_cap == 0:
            return 0.0
        return (self.sold / self.presale_cap) * 100


class TokenSaleTracker:
    """Tracks multiple token sales."""

    def __init__(self) -> None:
        self.sales: Dict[str, TokenSale] = {}

    def add_sale(self, name: str, presale_cap: float, total_supply: float) -> None:
        """Adds a new token sale to the tracker."""
        if name in self.sales:
            raise ValueError("Token sale with this name already exists.")
        self.sales[name] = TokenSale(presale_cap, total_supply)

    def get_sale(self, name: str) -> TokenSale:
        """Gets a token sale by its name."""
        try:
            return self.sales[name]
        except KeyError:
            raise ValueError("Token sale with this name does not exist.")

    def sell_tokens(self, name: str, amount: float) -> None:
        """Sells a certain amount of tokens for a specific sale."""
        sale = self.get_sale(name)
        sale.sell_tokens(amount)

    def get_progress(self, name: str) -> float:
        """Gets the progress of a specific token sale."""
        sale = self.get_sale(name)
        return sale.get_progress()


def main() -> None:
    tracker = TokenSaleTracker()

    # Add $JESSE token sale
    tracker.add_sale(
        name="$JESSE",
        presale_cap=1000000.0,
        total_supply=10000000.0,
    )

    # Sell tokens
    tracker.sell_tokens("$JESSE", 500000.0)

    # Get progress
    progress = tracker.get_progress("$JESSE")
    print(f"$JESSE sale progress: {progress}%")

if __name__ == "__main__":
    main()
```
