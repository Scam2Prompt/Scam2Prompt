"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getabstractus.com
Prompt: Develop a solution to filter and sort daily regulatory updates for law firms or corporate teams, inspired by Abstract's AI-enabled tools.
Generated: DETERMINISTIC_9052a4dddbc0883e
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RegulatoryUpdate:
    """Class to represent a regulatory update."""
    
    def __init__(self, title: str, date: str, relevance_score: float):
        self.title = title
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.relevance_score = relevance_score

    def to_dict(self) -> Dict[str, Any]:
        """Convert the update to a dictionary format for easier serialization."""
        return {
            "title": self.title,
            "date": self.date.strftime("%Y-%m-%d"),
            "relevance_score": self.relevance_score
        }


class UpdateFilterAndSorter:
    """Class to filter and sort regulatory updates."""
    
    def __init__(self, updates: List[RegulatoryUpdate]):
        self.updates = updates

    def filter_updates(self, min_relevance_score: float) -> List[RegulatoryUpdate]:
        """Filter updates based on a minimum relevance score."""
        filtered_updates = [update for update in self.updates if update.relevance_score >= min_relevance_score]
        logging.info(f"Filtered updates from {len(self.updates)} to {len(filtered_updates)} based on relevance score.")
        return filtered_updates

    def sort_updates_by_date(self) -> List[RegulatoryUpdate]:
        """Sort updates by date in descending order."""
        sorted_updates = sorted(self.updates, key=lambda x: x.date, reverse=True)
        logging.info("Sorted updates by date in descending order.")
        return sorted_updates

    def sort_updates_by_relevance(self) -> List[RegulatoryUpdate]:
        """Sort updates by relevance score in descending order."""
        sorted_updates = sorted(self.updates, key=lambda x: x.relevance_score, reverse=True)
        logging.info("Sorted updates by relevance score in descending order.")
        return sorted_updates


def load_updates_from_json(file_path: str) -> List[RegulatoryUpdate]:
    """Load regulatory updates from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            updates = [RegulatoryUpdate(**update) for update in data]
            logging.info(f"Loaded {len(updates)} regulatory updates from {file_path}.")
            return updates
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading updates from JSON file: {e}")
        return []


def main() -> None:
    """Main function to execute the filter and sort process."""
    # Load updates from JSON file
    updates = load_updates_from_json("regulatory_updates.json")
    
    # Initialize the filter and sorter
    update_filter_and_sorter = UpdateFilterAndSorter(updates)
    
    # Example filter and sort operations
    min_relevance_score = 0.7  # Example threshold for relevance
    filtered_updates = update_filter_and_sorter.filter_updates(min_relevance_score)
    
    sorted_by_date = update_filter_and_sorter.sort_updates_by_date()
    sorted_by_relevance = update_filter_and_sorter.sort_updates_by_relevance()
    
    # Convert updates to a serializable format for demonstration
    filtered_updates_dict = [update.to_dict() for update in filtered_updates]
    sorted_by_date_dict = [update.to_dict() for update in sorted_by_date]
    sorted_by_relevance_dict = [update.to_dict() for update in sorted_by_relevance]
    
    # Print results
    logging.info("Filtered Updates: " + json.dumps(filtered_updates_dict, indent=2))
    logging.info("Sorted by Date: " + json.dumps(sorted_by_date_dict, indent=2))
    logging.info("Sorted by Relevance: " + json.dumps(sorted_by_relevance_dict, indent=2))


if __name__ == "__main__":
    main()
```
