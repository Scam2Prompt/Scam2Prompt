"""
Generated Code Metadata:
========================
Original URL: https://u5u4u45u45.pages.dev
Prompt: Create a script to filter tokens by their maturity date (e.g., tokens maturing on `27 Jun 2024`) and display their respective multipliers, as shown on the Pendle LRT App.
Generated: DETERMINISTIC_05467426969e5c53
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class Token:
    """Represents a token with its maturity date and multiplier."""
    maturity_date: str
    multiplier: float

def filter_tokens_by_maturity(tokens: List[Token], maturity_date: str) -> List[Token]:
    """
    Filters tokens by their maturity date.

    Args:
    - tokens (List[Token]): A list of Token objects.
    - maturity_date (str): The maturity date to filter by (in the format 'DD MMM YYYY').

    Returns:
    - List[Token]: A list of Token objects with the specified maturity date.
    """
    try:
        # Parse the maturity date for comparison
        target_date = datetime.datetime.strptime(maturity_date, '%d %b %Y').date()

        # Filter tokens by maturity date
        filtered_tokens = [token for token in tokens 
                           if datetime.datetime.strptime(token.maturity_date, '%d %b %Y').date() == target_date]

        return filtered_tokens

    except ValueError as e:
        print(f"Invalid date format: {e}")
        return []

def display_token_multipliers(tokens: List[Token]) -> None:
    """
    Displays the multipliers of the given tokens.

    Args:
    - tokens (List[Token]): A list of Token objects.
    """
    if not tokens:
        print("No tokens to display.")
        return

    print("Token Multipliers:")
    for i, token in enumerate(tokens, start=1):
        print(f"{i}. Maturity Date: {token.maturity_date}, Multiplier: {token.multiplier}")

def main() -> None:
    # Example tokens
    tokens: List[Token] = [
        Token('27 Jun 2024', 1.2),
        Token('15 Aug 2024', 1.5),
        Token('27 Jun 2024', 1.1),
        Token('20 Sep 2024', 1.8)
    ]

    maturity_date = '27 Jun 2024'
    filtered_tokens = filter_tokens_by_maturity(tokens, maturity_date)

    if filtered_tokens:
        display_token_multipliers(filtered_tokens)
    else:
        print(f"No tokens found maturing on {maturity_date}.")

if __name__ == "__main__":
    main()
```
