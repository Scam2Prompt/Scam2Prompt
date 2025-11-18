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
import datetime
import json
from typing import List, Dict

# Define a class to represent regulatory updates
class RegulatoryUpdate:
    def __init__(self, title: str, summary: str, date: str, category: str):
        """
        Initialize a regulatory update.

        Args:
            title (str): Title of the regulatory update.
            summary (str): Summary or content of the regulatory update.
            date (str): Date of the update in 'YYYY-MM-DD' format.
            category (str): Category of the update (e.g., "Tax", "Compliance").
        """
        self.title = title
        self.summary = summary
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.category = category

    def __repr__(self):
        """
        Represent the regulatory update as a string for easier debugging.
        """
        return f"<RegulatoryUpdate title={self.title}, date={self.date.date()}, category={self.category}>"

# Function to filter updates by category
def filter_updates_by_category(updates: List[RegulatoryUpdate], category: str) -> List[RegulatoryUpdate]:
    """
    Filter regulatory updates by a given category.

    Args:
        updates (List[RegulatoryUpdate]): List of regulatory updates.
        category (str): Category to filter by.

    Returns:
        List[RegulatoryUpdate]: List of updates that match the category.
    """
    return [update for update in updates if update.category.lower() == category.lower()]

# Function to sort updates by date (latest first)
def sort_updates_by_date(updates: List[RegulatoryUpdate]) -> List[RegulatoryUpdate]:
    """
    Sort regulatory updates by date in descending order (latest first).

    Args:
        updates (List[RegulatoryUpdate]): List of regulatory updates.

    Returns:
        List[RegulatoryUpdate]: Sorted list of updates.
    """
    return sorted(updates, key=lambda update: update.date, reverse=True)

# Function to load updates from a JSON file
def load_updates_from_json(file_path: str) -> List[RegulatoryUpdate]:
    """
    Load regulatory updates from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[RegulatoryUpdate]: List of regulatory updates.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            updates = []
            for item in data:
                updates.append(RegulatoryUpdate(
                    title=item['title'],
                    summary=item['summary'],
                    date=item['date'],
                    category=item['category']
                ))
            return updates
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading updates from file: {e}")
        return []

# Main function to demonstrate functionality
def main():
    """
    Main function to demonstrate filtering and sorting regulatory updates.
    """
    # Load updates from a JSON file (example path provided)
    updates = load_updates_from_json("regulatory_updates.json")

    if not updates:
        print("No regulatory updates to process.")
        return

    # Filter updates by the "Compliance" category
    compliance_updates = filter_updates_by_category(updates, "Compliance")
    print("Filtered Compliance Updates:")
    for update in compliance_updates:
        print(update)

    # Sort updates by date (latest first)
    sorted_updates = sort_updates_by_date(updates)
    print("\nSorted Updates by Date:")
    for update in sorted_updates:
        print(update)


if __name__ == "__main__":
    main()
```

### Example JSON File Structure (`regulatory_updates.json`)
```json
[
    {
        "title": "Compliance Update 2023",
        "summary": "Details about the latest compliance regulations.",
        "date": "2023-10-01",
        "category": "Compliance"
    },
    {
        "title": "Tax Law Revision",
        "summary": "Recent changes to tax laws and implications.",
        "date": "2023-09-25",
        "category": "Tax"
    },
    {
        "title": "Employment Law Expansion",
        "summary": "New guidelines for employment law.",
        "date": "2023-10-02",
        "category": "Compliance"
    }
]
```
