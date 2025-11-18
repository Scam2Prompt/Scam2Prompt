"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://investmentbrokertransactions.com
Prompt: Create a Python script to automate the process of connecting startups with venture capitalists and angel investors, ensuring high success rates as highlighted by Investment Brokers.
Generated: DETERMINISTIC_40c1639cd2dafa3d
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import logging
from typing import List, Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Company:
    """Class to represent a startup company."""
    
    def __init__(self, name: str, industry: str, funding_needed: float):
        self.name = name
        self.industry = industry
        self.funding_needed = funding_needed

class Investor:
    """Class to represent an investor (Venture Capitalist or Angel Investor)."""
    
    def __init__(self, name: str, preferred_industry: str, max_investment: float):
        self.name = name
        self.preferred_industry = preferred_industry
        self.max_investment = max_investment

def load_data(file_path: str) -> List[Dict[str, Any]]:
    """Load startup and investor data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logging.info("Data loaded successfully.")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the file.")
        return []

def match_investors_to_startups(startups: List[Company], investors: List[Investor]) -> Dict[str, List[str]]:
    """Match investors with startups based on criteria."""
    matches = {}
    
    for startup in startups:
        matches[startup.name] = []
        for investor in investors:
            if (startup.industry == investor.preferred_industry and 
                startup.funding_needed <= investor.max_investment):
                matches[startup.name].append(investor.name)
    
    logging.info("Matching process completed.")
    return matches

def main():
    """Main function to execute the matching process."""
    # Load data for startups and investors
    startup_data = load_data('startups.json')
    investor_data = load_data('investors.json')
    
    startups = [Company(**startup) for startup in startup_data]
    investors = [Investor(**investor) for investor in investor_data]

    # Match investors to startups
    matches = match_investors_to_startups(startups, investors)

    # Output matching results
    for startup, matched_investors in matches.items():
        if matched_investors:
            print(f"{startup} is matched with investors: {', '.join(matched_investors)}")
        else:
            print(f"{startup} has no matches.")

if __name__ == "__main__":
    main()
``` 

### Note:
- Ensure you have a `startups.json` and `investors.json` file with the appropriate structure for the code to run successfully.
- Example structure for `startups.json`:
  ```json
  [
      {"name": "Startup A", "industry": "Tech", "funding_needed": 500000},
      {"name": "Startup B", "industry": "Health", "funding_needed": 300000}
  ]
  ```
- Example structure for `investors.json`:
  ```json
  [
      {"name": "Investor 1", "preferred_industry": "Tech", "max_investment": 1000000},
      {"name": "Investor 2", "preferred_industry": "Health", "max_investment": 250000}
  ]
  ```
