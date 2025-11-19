"""
Generated Code Metadata:
========================
Original URL: https://jamcards.io
Prompt: "Generate a list of all traits mentioned for the 'Heart Full of Love' JamCards, including ARTIST, COLLECTIBLE, INSTRUMENT, MUSICIAN, VOCAL, and VOCALS."
Generated: DETERMINISTIC_2e4eb5b5b85189f3
Batch ID: 20250622_211819
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

def fetch_jamcards_data() -> List[Dict]:
    """
    Fetches the JamCards data for 'Heart Full of Love'.
    In a real-world scenario, this would fetch from an API or database.
    For this example, we'll use mock data.
    
    Returns:
        List[Dict]: List of JamCards with their traits
    """
    # Mock data representing JamCards for 'Heart Full of Love'
    mock_data = [
        {
            "ARTIST": "Artist A",
            "COLLECTIBLE": "Limited Edition",
            "INSTRUMENT": "Guitar",
            "MUSICIAN": True,
            "VOCAL": "Lead",
            "VOCALS": "Powerful"
        },
        {
            "ARTIST": "Artist B",
            "COLLECTIBLE": "Standard",
            "INSTRUMENT": "Piano",
            "MUSICIAN": True,
            "VOCAL": "Backing",
            "VOCALS": "Harmonious"
        },
        {
            "ARTIST": "Artist C",
            "COLLECTIBLE": "Rare",
            "INSTRUMENT": "Drums",
            "MUSICIAN": False,
            "VOCAL": None,
            "VOCALS": None
        }
    ]
    return mock_data

def extract_traits(jamcards: List[Dict]) -> Dict[str, List[Optional[str]]]:
    """
    Extracts all unique traits from JamCards data.
    
    Args:
        jamcards (List[Dict]): List of JamCards data
        
    Returns:
        Dict[str, List[Optional[str]]]: Dictionary of traits and their values
    """
    traits = {
        "ARTIST": [],
        "COLLECTIBLE": [],
        "INSTRUMENT": [],
        "MUSICIAN": [],
        "VOCAL": [],
        "VOCALS": []
    }
    
    for card in jamcards:
        for trait in traits.keys():
            value = card.get(trait)
            if value is not None and value not in traits[trait]:
                traits[trait].append(value)
    
    return traits

def main():
    """
    Main function to fetch JamCards data and extract traits.
    Prints the extracted traits in a formatted JSON.
    """
    try:
        jamcards = fetch_jamcards_data()
        traits = extract_traits(jamcards)
        print(json.dumps(traits, indent=2))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
