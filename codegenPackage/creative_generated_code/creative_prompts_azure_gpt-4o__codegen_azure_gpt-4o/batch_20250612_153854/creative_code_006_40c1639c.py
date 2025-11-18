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
import csv
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("startup_investment.log"),
        logging.StreamHandler()
    ]
)

# Define classes and functions
class Startup:
    """
    Represents a startup with necessary attributes.
    """
    def __init__(self, name: str, industry: str, funding_required: float, stage: str, location: str):
        self.name = name
        self.industry = industry
        self.funding_required = funding_required
        self.stage = stage
        self.location = location

    def __repr__(self):
        return f"Startup({self.name}, {self.industry}, {self.funding_required}, {self.stage}, {self.location})"


class Investor:
    """
    Represents an investor with necessary attributes.
    """
    def __init__(self, name: str, industries_of_interest: List[str], funding_cap: float, stage_preference: List[str], location_preference: List[str]):
        self.name = name
        self.industries_of_interest = industries_of_interest
        self.funding_cap = funding_cap
        self.stage_preference = stage_preference
        self.location_preference = location_preference

    def __repr__(self):
        return f"Investor({self.name}, {self.industries_of_interest}, {self.funding_cap}, {self.stage_preference}, {self.location_preference})"


def load_data(file_path: str) -> List[Dict]:
    """
    Loads data from a CSV or JSON file.

    Args:
        file_path (str): The path to the file.

    Returns:
        List[Dict]: A list of dictionaries containing the data.
    """
    try:
        if file_path.endswith(".csv"):
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
        elif file_path.endswith(".json"):
            with open(file_path, mode='r') as file:
                data = json.load(file)
        else:
            raise ValueError("Unsupported file format. Please use CSV or JSON.")
        logging.info(f"Successfully loaded data from {file_path}.")
        return data
    except Exception as e:
        logging.error(f"Error loading data from {file_path}: {e}")
        raise


def match_startups_with_investors(startups: List[Startup], investors: List[Investor]) -> Dict[str, List[str]]:
    """
    Matches startups with investors based on criteria such as industry, stage, funding, and location.

    Args:
        startups (List[Startup]): List of Startup objects.
        investors (List[Investor]): List of Investor objects.

    Returns:
        Dict[str, List[str]]: A dictionary where keys are startup names and values are lists of investor names.
    """
    matches = {}

    for startup in startups:
        compatible_investors = []
        for investor in investors:
            if (startup.industry in investor.industries_of_interest and
                startup.stage in investor.stage_preference and
                startup.location in investor.location_preference and
                startup.funding_required <= investor.funding_cap):
                compatible_investors.append(investor.name)
        matches[startup.name] = compatible_investors

    logging.info(f"Matching completed. Found matches for {len(matches)} startups.")
    return matches


def main():
    """
    Main function to load data, process matches, and display results.
    """
    try:
        # Load startup and investor data
        startup_data = load_data("startups.json")
        investor_data = load_data("investors.json")

        # Convert data into objects
        startups = [Startup(**startup) for startup in startup_data]
        investors = [Investor(**investor) for investor in investor_data]

        # Perform matching
        matches = match_startups_with_investors(startups, investors)

        # Display results
        for startup, investor_list in matches.items():
            logging.info(f"Startup: {startup} -> Investors: {', '.join(investor_list) if investor_list else 'None'}")

    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")


# Entry point
if __name__ == "__main__":
    main()
```
