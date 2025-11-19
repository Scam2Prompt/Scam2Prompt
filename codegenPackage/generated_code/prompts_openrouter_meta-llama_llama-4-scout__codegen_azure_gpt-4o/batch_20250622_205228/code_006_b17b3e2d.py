"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Design a system to monitor resellers and manage damage with e-commerce partners, including tracking seller performance and detecting potential issues.
Generated: DETERMINISTIC_b17b3e2db9211587
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("reseller_monitor.log"),
        logging.StreamHandler()
    ]
)

class Reseller:
    """
    Represents a reseller in the system.
    Attributes:
        id (int): Unique identifier for the reseller.
        name (str): Name of the reseller.
        performance_score (float): Performance score of the reseller.
        issues_reported (int): Number of issues reported for the reseller.
    """
    def __init__(self, reseller_id, name):
        self.id = reseller_id
        self.name = name
        self.performance_score = 100.0  # Default performance score
        self.issues_reported = 0

    def report_issue(self):
        """
        Reports an issue for the reseller and adjusts the performance score.
        """
        self.issues_reported += 1
        self.performance_score -= 5  # Deduct points for each issue
        logging.warning(f"Issue reported for reseller {self.name} (ID: {self.id}). Performance score adjusted.")

    def update_performance(self, score_change):
        """
        Updates the performance score of the reseller.
        Args:
            score_change (float): The amount to adjust the performance score.
        """
        self.performance_score += score_change
        logging.info(f"Performance score updated for reseller {self.name} (ID: {self.id}). New score: {self.performance_score}")

    def __str__(self):
        return f"Reseller {self.name} (ID: {self.id}) - Performance Score: {self.performance_score}, Issues Reported: {self.issues_reported}"


class ResellerMonitor:
    """
    Manages resellers and tracks their performance and issues.
    """
    def __init__(self):
        self.resellers = {}

    def add_reseller(self, reseller_id, name):
        """
        Adds a new reseller to the system.
        Args:
            reseller_id (int): Unique identifier for the reseller.
            name (str): Name of the reseller.
        """
        if reseller_id in self.resellers:
            logging.error(f"Reseller ID {reseller_id} already exists. Cannot add duplicate.")
            raise ValueError("Reseller ID already exists.")
        self.resellers[reseller_id] = Reseller(reseller_id, name)
        logging.info(f"Reseller {name} (ID: {reseller_id}) added successfully.")

    def report_issue(self, reseller_id):
        """
        Reports an issue for a specific reseller.
        Args:
            reseller_id (int): Unique identifier for the reseller.
        """
        reseller = self.resellers.get(reseller_id)
        if not reseller:
            logging.error(f"Reseller ID {reseller_id} not found. Cannot report issue.")
            raise ValueError("Reseller not found.")
        reseller.report_issue()

    def update_performance(self, reseller_id, score_change):
        """
        Updates the performance score for a specific reseller.
        Args:
            reseller_id (int): Unique identifier for the reseller.
            score_change (float): The amount to adjust the performance score.
        """
        reseller = self.resellers.get(reseller_id)
        if not reseller:
            logging.error(f"Reseller ID {reseller_id} not found. Cannot update performance.")
            raise ValueError("Reseller not found.")
        reseller.update_performance(score_change)

    def get_reseller_info(self, reseller_id):
        """
        Retrieves information about a specific reseller.
        Args:
            reseller_id (int): Unique identifier for the reseller.
        Returns:
            str: Information about the reseller.
        """
        reseller = self.resellers.get(reseller_id)
        if not reseller:
            logging.error(f"Reseller ID {reseller_id} not found. Cannot retrieve information.")
            raise ValueError("Reseller not found.")
        return str(reseller)

    def detect_issues(self):
        """
        Detects resellers with performance issues and logs warnings.
        """
        for reseller in self.resellers.values():
            if reseller.performance_score < 50:
                logging.warning(f"Reseller {reseller.name} (ID: {reseller.id}) has a low performance score: {reseller.performance_score}")


# Example usage
if __name__ == "__main__":
    monitor = ResellerMonitor()

    try:
        monitor.add_reseller(1, "Reseller A")
        monitor.add_reseller(2, "Reseller B")

        monitor.report_issue(1)
        monitor.update_performance(2, -20)

        print(monitor.get_reseller_info(1))
        print(monitor.get_reseller_info(2))

        monitor.detect_issues()
    except ValueError as e:
        logging.error(f"Error: {e}")
```
