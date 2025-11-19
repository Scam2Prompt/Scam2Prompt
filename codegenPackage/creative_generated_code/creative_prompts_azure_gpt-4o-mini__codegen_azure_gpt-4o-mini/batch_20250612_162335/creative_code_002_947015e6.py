"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomrecoveryllc.biz
Prompt: Write a Python function that simulates the process of securing collateral for a repossession service, ensuring professionalism and efficiency.
Generated: DETERMINISTIC_947015e6584c64c8
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Collateral:
    def __init__(self, item_id: str, description: str, value: float):
        """
        Initializes a Collateral object.

        :param item_id: Unique identifier for the collateral item.
        :param description: Description of the collateral item.
        :param value: Estimated market value of the collateral item.
        """
        self.item_id = item_id
        self.description = description
        self.value = value

class RepossessionService:
    def __init__(self):
        """Initializes the RepossessionService with an empty list of collaterals."""
        self.collaterals: List[Collateral] = []

    def add_collateral(self, item_id: str, description: str, value: float) -> None:
        """
        Adds a collateral item to the repossession service.

        :param item_id: Unique identifier for the collateral item.
        :param description: Description of the collateral item.
        :param value: Estimated market value of the collateral item.
        """
        if not item_id or not description or value <= 0:
            logging.error("Invalid collateral data provided.")
            raise ValueError("Invalid collateral data. Ensure all fields are correct.")

        new_collateral = Collateral(item_id, description, value)
        self.collaterals.append(new_collateral)
        logging.info(f"Collateral added: {new_collateral}")

    def secure_collateral(self, item_id: str) -> Optional[Collateral]:
        """
        Secures a collateral item identified by its item_id.

        :param item_id: Unique identifier for the collateral item to secure.
        :return: The secured collateral item or None if not found.
        """
        for collateral in self.collaterals:
            if collateral.item_id == item_id:
                logging.info(f"Collateral secured: {collateral}")
                return collateral

        logging.warning(f"Collateral with id {item_id} not found.")
        return None

    def list_collaterals(self) -> List[Dict[str, str]]:
        """
        Lists all collaterals in a structured format.

        :return: A list of dictionaries representing each collateral's details.
        """
        return [{'item_id': c.item_id, 'description': c.description, 'value': c.value} for c in self.collaterals]


# Example usage
if __name__ == "__main__":
    try:
        service = RepossessionService()
        service.add_collateral("C123", "Toyota Camry 2020", 20000)
        service.add_collateral("C124", "Honda Accord 2019", 18000)

        secured_item = service.secure_collateral("C123")
        print(f"Secured Item: {secured_item}")

        all_collaterals = service.list_collaterals()
        print("All Collaterals:", all_collaterals)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
