"""
Generated Code Metadata:
========================
Original URL: https://minnimi.com.ua
Prompt: Create a simple command-line tool to help users find and filter slot games on Slots City based on their RTP, provider, and other criteria.
Generated: DETERMINISTIC_cb56d124d9dbce25
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import json
import sys

# Sample data representing slot games (in a real-world scenario, this would come from a database or API)
SLOT_GAMES = [
    {"name": "Game A", "provider": "Provider 1", "rtp": 96.5, "volatility": "High"},
    {"name": "Game B", "provider": "Provider 2", "rtp": 94.0, "volatility": "Medium"},
    {"name": "Game C", "provider": "Provider 1", "rtp": 97.2, "volatility": "Low"},
    {"name": "Game D", "provider": "Provider 3", "rtp": 95.5, "volatility": "High"},
    {"name": "Game E", "provider": "Provider 2", "rtp": 92.3, "volatility": "Medium"},
]

def filter_slot_games(rtp=None, provider=None, volatility=None):
    """
    Filters slot games based on the given criteria.

    :param rtp: Minimum RTP value to filter by (float).
    :param provider: Provider name to filter by (str).
    :param volatility: Volatility level to filter by (str).
    :return: List of filtered slot games.
    """
    filtered_games = SLOT_GAMES

    if rtp is not None:
        filtered_games = [game for game in filtered_games if game["rtp"] >= rtp]

    if provider is not None:
        filtered_games = [game for game in filtered_games if game["provider"].lower() == provider.lower()]

    if volatility is not None:
        filtered_games = [game for game in filtered_games if game["volatility"].lower() == volatility.lower()]

    return filtered_games

def main():
    """
    Main function to parse command-line arguments and filter slot games.
    """
    parser = argparse.ArgumentParser(
        description="Filter slot games based on RTP, provider, and volatility."
    )
    parser.add_argument("--rtp", type=float, help="Minimum RTP value to filter by.")
    parser.add_argument("--provider", type=str, help="Provider name to filter by.")
    parser.add_argument("--volatility", type=str, help="Volatility level to filter by (e.g., High, Medium, Low).")

    args = parser.parse_args()

    try:
        # Filter games based on user input
        filtered_games = filter_slot_games(rtp=args.rtp, provider=args.provider, volatility=args.volatility)

        # Display the filtered games
        if filtered_games:
            print(json.dumps(filtered_games, indent=4))
        else:
            print("No games found matching the criteria.")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
