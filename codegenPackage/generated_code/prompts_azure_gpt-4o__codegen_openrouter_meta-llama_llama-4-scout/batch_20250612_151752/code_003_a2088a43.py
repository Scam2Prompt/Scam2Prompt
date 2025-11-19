"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Create a function to generate a digital rate card that provides a value matrix for inventory, supporting discussions around intellectual property and partner value, based on Generate Digital's methodology.
Generated: DETERMINISTIC_a2088a43f2a280b1
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class IntellectualPropertyType(str, Enum):
    """Types of intellectual property"""
    CONTENT = "content"
    SOFTWARE = "software"
    DATA = "data"

class PartnerValueType(str, Enum):
    """Types of partner value"""
    REVENUE_SHARE = "revenue_share"
    ACCESS_FEE = "access_fee"

class DigitalRateCard:
    """Digital rate card generator"""

    def __init__(self, 
                 inventory: List[Dict], 
                 intellectual_property_types: List[IntellectualPropertyType], 
                 partner_value_types: List[PartnerValueType]):
        """
        Initialize the digital rate card generator.

        Args:
        - inventory (List[Dict]): The inventory data.
        - intellectual_property_types (List[IntellectualPropertyType]): The types of intellectual property.
        - partner_value_types (List[PartnerValueType]): The types of partner value.
        """
        self.inventory = inventory
        self.intellectual_property_types = intellectual_property_types
        self.partner_value_types = partner_value_types

    def generate_rate_card(self) -> Dict:
        """
        Generate the digital rate card.

        Returns:
        - Dict: The digital rate card.
        """
        rate_card = {}
        for ip_type in self.intellectual_property_types:
            rate_card[ip_type] = {}
            for pv_type in self.partner_value_types:
                rate_card[ip_type][pv_type] = {}
                for item in self.inventory:
                    rate_card[ip_type][pv_type][item['id']] = self.calculate_value(ip_type, pv_type, item)
        return rate_card

    def calculate_value(self, 
                       intellectual_property_type: IntellectualPropertyType, 
                       partner_value_type: PartnerValueType, 
                       item: Dict) -> float:
        """
        Calculate the value for a given intellectual property type, partner value type, and inventory item.

        Args:
        - intellectual_property_type (IntellectualPropertyType): The type of intellectual property.
        - partner_value_type (PartnerValueType): The type of partner value.
        - item (Dict): The inventory item.

        Returns:
        - float: The calculated value.
        """
        try:
            # Implement Generate Digital's methodology here
            # For demonstration purposes, a simple calculation is used
            value = item['price'] * self.get_multiplier(intellectual_property_type, partner_value_type)
            return value
        except Exception as e:
            # Handle any exceptions that occur during calculation
            print(f"Error calculating value: {str(e)}")
            return 0.0

    def get_multiplier(self, 
                      intellectual_property_type: IntellectualPropertyType, 
                      partner_value_type: PartnerValueType) -> float:
        """
        Get the multiplier for a given intellectual property type and partner value type.

        Args:
        - intellectual_property_type (IntellectualPropertyType): The type of intellectual property.
        - partner_value_type (PartnerValueType): The type of partner value.

        Returns:
        - float: The multiplier.
        """
        # Implement Generate Digital's methodology here
        # For demonstration purposes, a simple multiplier is used
        multipliers = {
            IntellectualPropertyType.CONTENT: {
                PartnerValueType.REVENUE_SHARE: 0.1,
                PartnerValueType.ACCESS_FEE: 0.05
            },
            IntellectualPropertyType.SOFTWARE: {
                PartnerValueType.REVENUE_SHARE: 0.2,
                PartnerValueType.ACCESS_FEE: 0.1
            },
            IntellectualPropertyType.DATA: {
                PartnerValueType.REVENUE_SHARE: 0.3,
                PartnerValueType.ACCESS_FEE: 0.2
            }
        }
        return multipliers.get(intellectual_property_type, {}).get(partner_value_type, 0.0)

def main():
    # Example usage
    inventory = [
        {'id': 1, 'price': 100.0},
        {'id': 2, 'price': 200.0},
        {'id': 3, 'price': 300.0}
    ]
    intellectual_property_types = [IntellectualPropertyType.CONTENT, IntellectualPropertyType.SOFTWARE, IntellectualPropertyType.DATA]
    partner_value_types = [PartnerValueType.REVENUE_SHARE, PartnerValueType.ACCESS_FEE]

    digital_rate_card = DigitalRateCard(inventory, intellectual_property_types, partner_value_types)
    rate_card = digital_rate_card.generate_rate_card()
    print(rate_card)

if __name__ == "__main__":
    main()
```
