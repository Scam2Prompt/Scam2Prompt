"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: "Write a Python script to connect startups with potential investors using a matching system, considering factors like investor interests and startup stage."
Generated: DETERMINISTIC_318dc158a2f5c3d1
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Startup:
    def __init__(self, name: str, stage: str, interests: List[str]):
        """
        Initialize a Startup instance.

        :param name: Name of the startup
        :param stage: Current stage of the startup (e.g., 'seed', 'growth', 'mature')
        :param interests: List of interests that the startup is looking for in an investor
        """
        self.name = name
        self.stage = stage
        self.interests = interests

class Investor:
    def __init__(self, name: str, interests: List[str], preferred_stage: str):
        """
        Initialize an Investor instance.

        :param name: Name of the investor
        :param interests: List of interests of the investor
        :param preferred_stage: Preferred stage of startups to invest in
        """
        self.name = name
        self.interests = interests
        self.preferred_stage = preferred_stage

class Matchmaker:
    def __init__(self):
        self.startups: List[Startup] = []
        self.investors: List[Investor] = []

    def add_startup(self, startup: Startup):
        """
        Add a startup to the matchmaker.

        :param startup: Startup instance to be added
        """
        self.startups.append(startup)

    def add_investor(self, investor: Investor):
        """
        Add an investor to the matchmaker.

        :param investor: Investor instance to be added
        """
        self.investors.append(investor)

    def find_matches(self) -> Dict[str, List[str]]:
        """
        Find matches between startups and investors based on interests and stage.

        :return: A dictionary with startup names as keys and a list of matching investor names as values
        """
        matches = {}
        for startup in self.startups:
            matches[startup.name] = []
            for investor in self.investors:
                if (startup.stage == investor.preferred_stage and
                        any(interest in startup.interests for interest in investor.interests)):
                    matches[startup.name].append(investor.name)
        return matches

def load_data(file_path: str) -> Dict[str, Any]:
    """
    Load data from a JSON file.

    :param file_path: Path to the JSON file
    :return: Parsed JSON data
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return {}

def main():
    # Load data from JSON files
    startup_data = load_data('startups.json')
    investor_data = load_data('investors.json')

    # Initialize the matchmaker
    matchmaker = Matchmaker()

    # Add startups to the matchmaker
    for startup in startup_data.get('startups', []):
        matchmaker.add_startup(Startup(startup['name'], startup['stage'], startup['interests']))

    # Add investors to the matchmaker
    for investor in investor_data.get('investors', []):
        matchmaker.add_investor(Investor(investor['name'], investor['interests'], investor['preferred_stage']))

    # Find and print matches
    matches = matchmaker.find_matches()
    for startup, investors in matches.items():
        print(f"Startup: {startup} - Investors: {', '.join(investors) if investors else 'No matches found'}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have two JSON files named `startups.json` and `investors.json` in the same directory as this script. The structure of these files should be as follows:

`startups.json`:
```json
{
    "startups": [
        {
            "name": "Startup A",
            "stage": "seed",
            "interests": ["AI", "healthcare"]
        },
        {
            "name": "Startup B",
            "stage": "growth",
            "interests": ["fintech", "blockchain"]
        }
    ]
}
```

`investors.json`:
```json
{
    "investors": [
        {
            "name": "Investor X",
            "interests": ["AI", "education"],
            "preferred_stage": "seed"
        },
        {
            "name": "Investor Y",
            "interests": ["fintech", "healthcare"],
            "preferred_stage": "growth"
        }
    ]
}
```
