"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Write a Python script to manage a grants program, including tools for measuring program success and maximizing engagement."
Generated: DETERMINISTIC_7af5e630e98ec5cf
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# grants_program.py

import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Grant:
    """Represents a grant in the program."""

    def __init__(self, id, name, amount, start_date, end_date):
        """
        Initializes a Grant object.

        Args:
            id (int): Unique identifier for the grant.
            name (str): Name of the grant.
            amount (float): Amount of the grant.
            start_date (datetime.date): Start date of the grant.
            end_date (datetime.date): End date of the grant.
        """
        self.id = id
        self.name = name
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
        self.status = "active"

    def __str__(self):
        return f"Grant {self.id}: {self.name}, Amount: {self.amount}, Status: {self.status}"

class GrantsProgram:
    """Manages a grants program."""

    def __init__(self):
        """Initializes a GrantsProgram object."""
        self.grants = {}

    def add_grant(self, grant):
        """
        Adds a grant to the program.

        Args:
            grant (Grant): Grant to add.

        Raises:
            ValueError: If a grant with the same ID already exists.
        """
        if grant.id in self.grants:
            raise ValueError("Grant with the same ID already exists")
        self.grants[grant.id] = grant
        logger.info(f"Added grant {grant.id}: {grant.name}")

    def remove_grant(self, grant_id):
        """
        Removes a grant from the program.

        Args:
            grant_id (int): ID of the grant to remove.

        Raises:
            ValueError: If the grant does not exist.
        """
        if grant_id not in self.grants:
            raise ValueError("Grant does not exist")
        del self.grants[grant_id]
        logger.info(f"Removed grant {grant_id}")

    def update_grant_status(self, grant_id, status):
        """
        Updates the status of a grant.

        Args:
            grant_id (int): ID of the grant to update.
            status (str): New status of the grant.

        Raises:
            ValueError: If the grant does not exist.
        """
        if grant_id not in self.grants:
            raise ValueError("Grant does not exist")
        self.grants[grant_id].status = status
        logger.info(f"Updated grant {grant_id} status to {status}")

    def get_grant(self, grant_id):
        """
        Gets a grant by ID.

        Args:
            grant_id (int): ID of the grant to get.

        Returns:
            Grant: The grant with the specified ID, or None if not found.
        """
        return self.grants.get(grant_id)

    def get_all_grants(self):
        """
        Gets all grants in the program.

        Returns:
            list[Grant]: A list of all grants in the program.
        """
        return list(self.grants.values())

    def measure_success(self):
        """
        Measures the success of the program.

        Returns:
            dict: A dictionary containing success metrics.
        """
        total_amount = sum(grant.amount for grant in self.grants.values())
        active_grants = sum(1 for grant in self.grants.values() if grant.status == "active")
        return {
            "total_amount": total_amount,
            "active_grants": active_grants,
            "total_grants": len(self.grants)
        }

    def maximize_engagement(self):
        """
        Provides recommendations for maximizing engagement.

        Returns:
            list[str]: A list of recommendations.
        """
        recommendations = []
        for grant in self.grants.values():
            if grant.status == "active" and grant.end_date < datetime.date.today():
                recommendations.append(f"Grant {grant.id} is ending soon. Consider extending or re-applying.")
        return recommendations

def main():
    program = GrantsProgram()

    # Create some grants
    grant1 = Grant(1, "Grant 1", 10000.0, datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    grant2 = Grant(2, "Grant 2", 5000.0, datetime.date(2024, 6, 1), datetime.date(2025, 5, 31))

    # Add grants to the program
    program.add_grant(grant1)
    program.add_grant(grant2)

    # Measure program success
    success_metrics = program.measure_success()
    logger.info("Program Success Metrics:")
    logger.info(f"Total Amount: {success_metrics['total_amount']}")
    logger.info(f"Active Grants: {success_metrics['active_grants']}")
    logger.info(f"Total Grants: {success_metrics['total_grants']}")

    # Maximize engagement
    recommendations = program.maximize_engagement()
    logger.info("Recommendations for Maximizing Engagement:")
    for recommendation in recommendations:
        logger.info(recommendation)

if __name__ == "__main__":
    main()
```
