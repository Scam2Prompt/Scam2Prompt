"""
Generated Code Metadata:
========================
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: What libraries or APIs are recommended for developing a round management system similar to Gitcoin's?
Generated: DETERMINISTIC_94b661e2459b069e
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# round_management_system.py

"""
Round Management System
This module provides a basic structure for managing rounds similar to Gitcoin's.
It includes functionalities for creating, updating, and retrieving rounds.
"""

import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Round:
    """
    Represents a funding round in the management system.
    """

    def __init__(self, title: str, description: str, start_date: datetime, end_date: datetime):
        """
        Initializes a new round with the given parameters.

        :param title: Title of the round
        :param description: Description of the round
        :param start_date: Start date of the round
        :param end_date: End date of the round
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the round
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now()

    def is_active(self) -> bool:
        """
        Checks if the round is currently active.

        :return: True if the round is active, False otherwise
        """
        now = datetime.now()
        return self.start_date <= now <= self.end_date


class RoundManager:
    """
    Manages a collection of rounds.
    """

    def __init__(self):
        self.rounds: List[Round] = []

    def create_round(self, title: str, description: str, start_date: datetime, end_date: datetime) -> Round:
        """
        Creates a new round and adds it to the collection.

        :param title: Title of the round
        :param description: Description of the round
        :param start_date: Start date of the round
        :param end_date: End date of the round
        :return: The created Round object
        """
        if end_date <= start_date:
            raise ValueError("End date must be after start date.")
        
        new_round = Round(title, description, start_date, end_date)
        self.rounds.append(new_round)
        return new_round

    def get_round(self, round_id: str) -> Optional[Round]:
        """
        Retrieves a round by its ID.

        :param round_id: The ID of the round to retrieve
        :return: The Round object if found, None otherwise
        """
        for round_ in self.rounds:
            if round_.id == round_id:
                return round_
        return None

    def get_active_rounds(self) -> List[Round]:
        """
        Retrieves all active rounds.

        :return: A list of active Round objects
        """
        return [round_ for round_ in self.rounds if round_.is_active()]

    def update_round(self, round_id: str, title: Optional[str] = None, description: Optional[str] = None,
                     start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> Optional[Round]:
        """
        Updates an existing round.

        :param round_id: The ID of the round to update
        :param title: New title for the round (optional)
        :param description: New description for the round (optional)
        :param start_date: New start date for the round (optional)
        :param end_date: New end date for the round (optional)
        :return: The updated Round object if found and updated, None otherwise
        """
        round_ = self.get_round(round_id)
        if not round_:
            raise ValueError("Round not found.")

        if title:
            round_.title = title
        if description:
            round_.description = description
        if start_date:
            if end_date and end_date <= start_date:
                raise ValueError("End date must be after start date.")
            round_.start_date = start_date
        if end_date:
            if end_date <= round_.start_date:
                raise ValueError("End date must be after start date.")
            round_.end_date = end_date

        return round_

# Example usage
if __name__ == "__main__":
    manager = RoundManager()
    try:
        round1 = manager.create_round("Round 1", "Description for round 1", datetime(2023, 10, 1), datetime(2023, 10, 31))
        print(f"Created round: {round1.title} with ID: {round1.id}")

        active_rounds = manager.get_active_rounds()
        print(f"Active rounds: {[round_.title for round_ in active_rounds]}")

        updated_round = manager.update_round(round1.id, title="Updated Round 1")
        print(f"Updated round title: {updated_round.title}")

    except ValueError as e:
        print(f"Error: {e}")
```
