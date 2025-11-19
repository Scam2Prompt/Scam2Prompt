"""
Generated Code Metadata:
========================
Original URL: https://getabstractus.com
Prompt: Develop a solution to filter and sort daily regulatory updates for law firms or corporate teams, inspired by Abstract's AI-enabled tools.
Generated: DETERMINISTIC_9052a4dddbc0883e
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# regulatory_update_filter.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class UpdateType(str, Enum):
    """Type of regulatory update"""
    COMPLIANCE = "compliance"
    LEGISLATION = "legislation"
    REGULATORY_ACTION = "regulatory_action"

@dataclass
class RegulatoryUpdate:
    """Represents a regulatory update"""
    id: int
    update_type: UpdateType
    title: str
    description: str
    published_at: datetime.datetime

class RegulatoryUpdateFilter:
    """Filters and sorts regulatory updates"""

    def __init__(self, updates: List[RegulatoryUpdate]):
        self.updates = updates

    def filter_by_type(self, update_type: UpdateType) -> List[RegulatoryUpdate]:
        """Filters updates by type"""
        return [update for update in self.updates if update.update_type == update_type]

    def filter_by_date_range(self, start_date: datetime.date, end_date: datetime.date) -> List[RegulatoryUpdate]:
        """Filters updates by date range"""
        return [
            update for update in self.updates 
            if start_date <= update.published_at.date() <= end_date
        ]

    def sort_by_published_at(self, ascending: bool = True) -> List[RegulatoryUpdate]:
        """Sorts updates by published at date"""
        return sorted(self.updates, key=lambda x: x.published_at, reverse=not ascending)

def main():
    try:
        # Example usage
        updates = [
            RegulatoryUpdate(
                id=1,
                update_type=UpdateType.COMPLIANCE,
                title="Update 1",
                description="Description 1",
                published_at=datetime.datetime(2022, 1, 1, 12, 0, 0)
            ),
            RegulatoryUpdate(
                id=2,
                update_type=UpdateType.LEGISLATION,
                title="Update 2",
                description="Description 2",
                published_at=datetime.datetime(2022, 1, 15, 12, 0, 0)
            ),
            RegulatoryUpdate(
                id=3,
                update_type=UpdateType.COMPLIANCE,
                title="Update 3",
                description="Description 3",
                published_at=datetime.datetime(2022, 2, 1, 12, 0, 0)
            ),
        ]

        filter = RegulatoryUpdateFilter(updates)

        filtered_updates = filter.filter_by_type(UpdateType.COMPLIANCE)
        print("Filtered by type:")
        for update in filtered_updates:
            print(update)

        sorted_updates = filter.sort_by_published_at()
        print("\nSorted by published at:")
        for update in sorted_updates:
            print(update)

        date_range_updates = filter.filter_by_date_range(datetime.date(2022, 1, 1), datetime.date(2022, 1, 31))
        print("\nFiltered by date range:")
        for update in date_range_updates:
            print(update)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
