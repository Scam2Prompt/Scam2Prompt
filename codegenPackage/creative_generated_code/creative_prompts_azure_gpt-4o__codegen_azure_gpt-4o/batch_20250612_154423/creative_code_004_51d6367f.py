"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Develop a script to manage co-management operations with country-specific HR and operations managers, leveraging Connext's approach to streamline offshore team management.
Generated: DETERMINISTIC_51d6367f15e357f4
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for managing co-management operations with country-specific HR and operations managers.
Leverages Connext's approach to streamline offshore team management.

Author: Expert Programmer
Language: Python
Version: 3.8+
"""
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CoManagementSystem:
    """
    Class to manage co-management operations with country-specific HR and operations managers.
    """
    def __init__(self):
        # Data storage for HR and operations managers by country
        self.managers = {}

    def add_manager(self, country: str, manager_type: str, manager_name: str) -> None:
        """
        Adds a manager to the system.

        Args:
            country (str): Country of the manager.
            manager_type (str): Type of manager ('HR' or 'Operations').
            manager_name (str): Name of the manager.

        Raises:
            ValueError: If manager_type is invalid.
        """
        valid_types = ['HR', 'Operations']
        if manager_type not in valid_types:
            raise ValueError(f"Invalid manager type. Must be one of {valid_types}.")

        if country not in self.managers:
            self.managers[country] = {'HR': [], 'Operations': []}

        self.managers[country][manager_type].append(manager_name)
        logging.info(f"Added {manager_type} manager '{manager_name}' for country {country}.")

    def remove_manager(self, country: str, manager_type: str, manager_name: str) -> None:
        """
        Removes a manager from the system.

        Args:
            country (str): Country of the manager.
            manager_type (str): Type of manager ('HR' or 'Operations').
            manager_name (str): Name of the manager.

        Raises:
            ValueError: If manager_type is invalid or manager does not exist.
        """
        valid_types = ['HR', 'Operations']
        if manager_type not in valid_types:
            raise ValueError(f"Invalid manager type. Must be one of {valid_types}.")

        if country in self.managers and manager_name in self.managers[country][manager_type]:
            self.managers[country][manager_type].remove(manager_name)
            logging.info(f"Removed {manager_type} manager '{manager_name}' for country {country}.")
        else:
            raise ValueError(f"Manager '{manager_name}' not found under {manager_type} in country {country}.")

    def list_managers(self, country: str) -> Dict[str, List[str]]:
        """
        Lists all managers for a given country.

        Args:
            country (str): Country to list managers for.

        Returns:
            Dict[str, List[str]]: Dictionary of manager types and their names.
        """
        if country in self.managers:
            return self.managers[country]
        else:
            logging.warning(f"No managers found for country {country}.")
            return {'HR': [], 'Operations': []}

    def list_all_managers(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Lists all managers across all countries.

        Returns:
            Dict[str, Dict[str, List[str]]]: Dictionary of countries, manager types, and their names.
        """
        return self.managers


if __name__ == "__main__":
    # Example usage of the CoManagementSystem
    try:
        cms = CoManagementSystem()

        # Adding managers
        cms.add_manager("USA", "HR", "Alice Johnson")
        cms.add_manager("USA", "Operations", "Michael Smith")
        cms.add_manager("India", "HR", "Rajesh Kumar")

        # Listing managers for a specific country
        print("Managers in USA:", cms.list_managers("USA"))
        print("Managers in India:", cms.list_managers("India"))
        print("Managers in UK:", cms.list_managers("UK"))  # No managers yet

        # Listing all managers
        print("All Managers:", cms.list_all_managers())

        # Removing a manager
        cms.remove_manager("USA", "HR", "Alice Johnson")
        print("Managers in USA after removal:", cms.list_managers("USA"))

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
