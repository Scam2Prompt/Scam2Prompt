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
from typing import List, Dict, Optional

# Sample data structure representing slot games
SLOT_GAMES = [
    {
        "name": "Book of Dead",
        "provider": "Play'n GO",
        "rtp": 96.21,
        "volatility": "High",
        "theme": "Egyptian",
        "features": ["Free Spins", "Expanding Symbols"]
    },
    {
        "name": "Starburst",
        "provider": "NetEnt",
        "rtp": 96.09,
        "volatility": "Low",
        "theme": "Space",
        "features": ["Wilds", "Re-spins"]
    },
    {
        "name": "Gonzo's Quest",
        "provider": "NetEnt",
        "rtp": 95.77,
        "volatility": "Medium",
        "theme": "Adventure",
        "features": ["Avalanche", "Free Falls"]
    },
    {
        "name": "Mega Moolah",
        "provider": "Microgaming",
        "rtp": 88.12,
        "volatility": "High",
        "theme": "African",
        "features": ["Progressive Jackpot", "Free Spins"]
    }
]

def filter_games(
    games: List[Dict],
    min_rtp: Optional[float] = None,
    max_rtp: Optional[float] = None,
    provider: Optional[str] = None,
    volatility: Optional[str] = None,
    theme: Optional[str] = None,
    feature: Optional[str] = None
) -> List[Dict]:
    """
    Filter slot games based on given criteria.
    
    Args:
        games: List of slot game dictionaries
        min_rtp: Minimum RTP percentage
        max_rtp: Maximum RTP percentage
        provider: Game provider name
        volatility: Game volatility level
        theme: Game theme
        feature: Game feature to look for
        
    Returns:
        Filtered list of games matching criteria
    """
    filtered = games
    
    if min_rtp is not None:
        filtered = [g for g in filtered if g["rtp"] >= min_rtp]
    
    if max_rtp is not None:
        filtered = [g for g in filtered if g["rtp"] <= max_rtp]
    
    if provider is not None:
        filtered = [g for g in filtered if g["provider"].lower() == provider.lower()]
    
    if volatility is not None:
        filtered = [g for g in filtered if g["volatility"].lower() == volatility.lower()]
    
    if theme is not None:
        filtered = [g for g in filtered if g["theme"].lower() == theme.lower()]
    
    if feature is not None:
        filtered = [g for g in filtered if feature.lower() in [f.lower() for f in g["features"]]]
    
    return filtered

def display_games(games: List[Dict]):
    """Display games in a formatted table."""
    if not games:
        print("No games found matching your criteria.")
        return
    
    print("\nFound Games:")
    print("-" * 80)
    print(f"{'Name':<20} {'Provider':<15} {'RTP':<8} {'Volatility':<10} {'Theme':<15} {'Features'}")
    print("-" * 80)
    
    for game in games:
        features = ", ".join(game["features"])
        print(f"{game['name']:<20} {game['provider']:<15} {game['rtp']:<8.2f} "
              f"{game['volatility']:<10} {game['theme']:<15} {features}")

def load_games_from_file(filename: str) -> List[Dict]:
    """Load games from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Using default game data.")
        return SLOT_GAMES
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file '{filename}'. Using default game data.")
        return SLOT_GAMES

def main():
    parser = argparse.ArgumentParser(description="Slot Game Finder for Slots City")
    
    parser.add_argument(
        "--min-rtp",
        type=float,
        help="Minimum RTP percentage (e.g., 95.0)"
    )
    
    parser.add_argument(
        "--max-rtp",
        type=float,
        help="Maximum RTP percentage (e.g., 97.0)"
    )
    
    parser.add_argument(
        "--provider",
        type=str,
        help="Filter by game provider (e.g., 'NetEnt')"
    )
    
    parser.add_argument(
        "--volatility",
        type=str,
        choices=["low", "medium", "high"],
        help="Filter by volatility level (low, medium, high)"
    )
    
    parser.add_argument(
        "--theme",
        type=str,
        help="Filter by game theme (e.g., 'Egyptian')"
    )
    
    parser.add_argument(
        "--feature",
        type=str,
        help="Filter by game feature (e.g., 'Free Spins')"
    )
    
    parser.add_argument(
        "--file",
        type=str,
        help="Load games from JSON file"
    )
    
    args = parser.parse_args()
    
    # Load games from file or use default
    games = load_games_from_file(args.file) if args.file else SLOT_GAMES
    
    # Filter games based on provided criteria
    filtered_games = filter_games(
        games,
        min_rtp=args.min_rtp,
        max_rtp=args.max_rtp,
        provider=args.provider,
        volatility=args.volatility,
        theme=args.theme,
        feature=args.feature
    )
    
    # Display results
    display_games(filtered_games)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
