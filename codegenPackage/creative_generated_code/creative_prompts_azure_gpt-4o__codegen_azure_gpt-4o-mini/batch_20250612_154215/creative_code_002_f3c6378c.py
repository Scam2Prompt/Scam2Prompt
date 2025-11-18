"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Generate code to design customizable apparel for esports participants, referencing Ace Pro Sports Technologies' approach to creating designer apparel for gaming partners.
Generated: DETERMINISTIC_f3c6378c3db59a33
Batch ID: 20250612_154215
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class ApparelItem:
    """Class representing an apparel item for esports."""
    item_type: str  # Type of apparel (e.g., Jersey, Hoodie)
    size: str       # Size of the apparel (e.g., S, M, L, XL)
    color: str      # Color of the apparel
    logo_url: str   # URL to the logo image
    custom_text: str = ""  # Custom text to be printed on the apparel, if any

    def __post_init__(self):
        """Validate the values of the apparel item."""
        valid_sizes = {"S", "M", "L", "XL", "XXL"}
        if self.size not in valid_sizes:
            raise ValueError(f"Invalid size: {self.size}. Must be one of {valid_sizes}.")
        if not self.logo_url.startswith("http"):
            raise ValueError("Logo URL must start with 'http'.")


@dataclass
class CustomApparelOrder:
    """Class representing a custom apparel order for esports participants."""
    participant_name: str
    apparel_items: List[ApparelItem] = field(default_factory=list)

    def add_apparel_item(self, item: ApparelItem):
        """Add an apparel item to the order."""
        self.apparel_items.append(item)

    def to_json(self) -> str:
        """Convert the order details to JSON format."""
        return json.dumps({
            "participant_name": self.participant_name,
            "apparel_items": [item.__dict__ for item in self.apparel_items]
        }, indent=4)

    def validate_order(self):
        """Validate the order before processing."""
        if not self.participant_name:
            raise ValueError("Participant name cannot be empty.")
        if not self.apparel_items:
            raise ValueError("Order must contain at least one apparel item.")


def main():
    """Main function to create a custom apparel order."""
    try:
        # Example participant and apparel order
        order = CustomApparelOrder(participant_name="John Doe")
        
        # Adding apparel items
        order.add_apparel_item(ApparelItem(item_type="Jersey", size="M", color="Black", logo_url="http://example.com/logo.png"))
        order.add_apparel_item(ApparelItem(item_type="Hoodie", size="L", color="Red", logo_url="http://example.com/logo.png", custom_text="GamerPro"))

        # Validate the order
        order.validate_order()

        # Output the order details in JSON format
        print("Custom Apparel Order:")
        print(order.to_json())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
