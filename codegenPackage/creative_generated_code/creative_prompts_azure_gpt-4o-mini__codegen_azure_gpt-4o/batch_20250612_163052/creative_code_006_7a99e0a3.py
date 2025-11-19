"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-folex.org
Prompt: How does Instant Akpro 0.7 facilitate connections between aspiring learners and investment education firms globally?
Generated: DETERMINISTIC_7a99e0a3b95c9cb0
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This code demonstrates how Instant Akpro 0.7 could facilitate connections between 
aspiring learners and investment education firms globally. The platform acts as a connector, 
matching learners with firms using geographical preferences, interests, and learning goals.

Assumptions:
1. The platform has access to a database of learners and firms.
2. Each learner specifies preferences such as location, topics, and mode of learning.
3. The firms provide details about their offerings, availability, and specialization.
"""

import json
from typing import List, Dict, Any

class InstantAkpro:
    def __init__(self):
        """
        Initialize the Instant Akpro system.
        """
        self.learners = []  # List to hold learner profiles
        self.firms = []     # List to hold firm profiles

    def load_data(self, learners_file: str, firms_file: str):
        """
        Load learners and firms data from JSON files.
        :param learners_file: Path to the JSON file containing learner profiles.
        :param firms_file: Path to the JSON file containing firm profiles.
        """
        try:
            with open(learners_file, 'r') as file:
                self.learners = json.load(file)
            
            with open(firms_file, 'r') as file:
                self.firms = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            raise

    def match_learners_to_firms(self) -> Dict[str, List[str]]:
        """
        Match learners to suitable investment education firms based on preferences.
        :return: A dictionary with learner names as keys and a list of matched firm names as values.
        """
        matches = {}
        for learner in self.learners:
            matched_firms = []
            for firm in self.firms:
                # Match based on location, topics of interest, and mode of learning
                if (learner['location'] in firm['locations'] and
                    any(topic in firm['specializations'] for topic in learner['topics_of_interest']) and
                    learner['preferred_mode'] in firm['available_modes']):
                    
                    matched_firms.append(firm['name'])
            
            matches[learner['name']] = matched_firms
        
        return matches

    def display_matches(self, matches: Dict[str, List[str]]):
        """
        Display the matches in a user-friendly format.
        :param matches: Dictionary containing matches.
        """
        if not matches:
            print("No matches found.")
            return

        print("Learner-to-Firm Matches:")
        for learner, firms in matches.items():
            print(f"  Learner: {learner}")
            if firms:
                print(f"    Matched Firms: {', '.join(firms)}")
            else:
                print("    Matched Firms: None")

# Example Usage
if __name__ == "__main__":
    # Create an instance of Instant Akpro
    akpro = InstantAkpro()

    # Load data (replace 'learners.json' and 'firms.json' with actual file paths)
    try:
        akpro.load_data('learners.json', 'firms.json')
    except Exception as e:
        print(f"Failed to load data: {e}")
        exit(1)

    # Perform matching
    matches = akpro.match_learners_to_firms()

    # Display matches
    akpro.display_matches(matches)
```

### Sample JSON Files Structure
#### learners.json
```json
[
    {
        "name": "John Doe",
        "location": "USA",
        "topics_of_interest": ["Stocks", "Bonds"],
        "preferred_mode": "Online"
    },
    {
        "name": "Jane Smith",
        "location": "UK",
        "topics_of_interest": ["Cryptocurrency", "Real Estate"],
        "preferred_mode": "In-Person"
    }
]
```

#### firms.json
```json
[
    {
        "name": "InvestPro Education",
        "locations": ["USA", "Canada"],
        "specializations": ["Stocks", "Bonds", "Options"],
        "available_modes": ["Online", "In-Person"]
    },
    {
        "name": "CryptoLearn Academy",
        "locations": ["UK", "Germany"],
        "specializations": ["Cryptocurrency", "Blockchain"],
        "available_modes": ["Online"]
    }
]
```
