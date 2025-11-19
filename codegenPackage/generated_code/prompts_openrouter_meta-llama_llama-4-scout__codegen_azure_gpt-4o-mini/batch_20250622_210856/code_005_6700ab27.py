"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Create a data model for storing and managing Oticon hearing aid product information, including product types (e.g., Oticon Real, Oticon Own), features, and technical specifications.
Generated: DETERMINISTIC_6700ab276dd8b6bb
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any
import json

class HearingAid:
    """
    A class to represent a hearing aid product.

    Attributes:
        product_id (str): Unique identifier for the hearing aid.
        product_type (str): Type of the hearing aid (e.g., Oticon Real, Oticon Own).
        features (List[str]): List of features of the hearing aid.
        specifications (Dict[str, Any]): Technical specifications of the hearing aid.
    """

    def __init__(self, product_id: str, product_type: str, features: List[str], specifications: Dict[str, Any]):
        """
        Initializes a HearingAid instance.

        Args:
            product_id (str): Unique identifier for the hearing aid.
            product_type (str): Type of the hearing aid.
            features (List[str]): List of features of the hearing aid.
            specifications (Dict[str, Any]): Technical specifications of the hearing aid.
        """
        self.product_id = product_id
        self.product_type = product_type
        self.features = features
        self.specifications = specifications

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the HearingAid instance to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the HearingAid instance.
        """
        return {
            "product_id": self.product_id,
            "product_type": self.product_type,
            "features": self.features,
            "specifications": self.specifications
        }

    def to_json(self) -> str:
        """
        Converts the HearingAid instance to a JSON string.

        Returns:
            str: A JSON string representation of the HearingAid instance.
        """
        return json.dumps(self.to_dict(), indent=4)

class HearingAidManager:
    """
    A class to manage a collection of HearingAid products.

    Attributes:
        hearing_aids (List[HearingAid]): A list of HearingAid instances.
    """

    def __init__(self):
        """Initializes the HearingAidManager with an empty list of hearing aids."""
        self.hearing_aids = []

    def add_hearing_aid(self, hearing_aid: HearingAid) -> None:
        """
        Adds a HearingAid instance to the collection.

        Args:
            hearing_aid (HearingAid): The HearingAid instance to add.
        """
        if not isinstance(hearing_aid, HearingAid):
            raise ValueError("Expected an instance of HearingAid.")
        self.hearing_aids.append(hearing_aid)

    def get_hearing_aid(self, product_id: str) -> HearingAid:
        """
        Retrieves a HearingAid instance by its product ID.

        Args:
            product_id (str): The unique identifier of the hearing aid.

        Returns:
            HearingAid: The HearingAid instance with the specified product ID.

        Raises:
            ValueError: If no hearing aid with the specified product ID is found.
        """
        for hearing_aid in self.hearing_aids:
            if hearing_aid.product_id == product_id:
                return hearing_aid
        raise ValueError(f"Hearing aid with product ID '{product_id}' not found.")

    def list_hearing_aids(self) -> List[Dict[str, Any]]:
        """
        Lists all hearing aids in the collection.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing all hearing aids.
        """
        return [hearing_aid.to_dict() for hearing_aid in self.hearing_aids]

# Example usage
if __name__ == "__main__":
    try:
        manager = HearingAidManager()
        
        # Create some hearing aids
        hearing_aid1 = HearingAid(
            product_id="HA001",
            product_type="Oticon Real",
            features=["Bluetooth", "Rechargeable", "Noise Reduction"],
            specifications={"battery_life": "24 hours", "weight": "1.2g"}
        )
        
        hearing_aid2 = HearingAid(
            product_id="HA002",
            product_type="Oticon Own",
            features=["AI Features", "Water Resistant"],
            specifications={"battery_life": "20 hours", "weight": "1.5g"}
        )
        
        # Add hearing aids to the manager
        manager.add_hearing_aid(hearing_aid1)
        manager.add_hearing_aid(hearing_aid2)

        # List all hearing aids
        print(manager.list_hearing_aids())

        # Retrieve a specific hearing aid
        print(manager.get_hearing_aid("HA001").to_json())

    except Exception as e:
        print(f"An error occurred: {e}")
```
