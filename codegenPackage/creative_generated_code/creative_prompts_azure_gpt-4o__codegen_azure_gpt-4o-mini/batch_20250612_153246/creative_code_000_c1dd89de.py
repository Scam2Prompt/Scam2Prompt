"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Write Python code to create a catalog system for surgical instruments, including categories like "Dental Instruments," "Manicure Products," and "Surgical Products," as described on the Curative Surgical Industry website.
Generated: DETERMINISTIC_c1dd89de75e57df3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Instrument:
    """Class representing a surgical instrument."""

    def __init__(self, name: str, category: str, description: str, quantity: int):
        self.name = name
        self.category = category
        self.description = description
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the instrument to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "quantity": self.quantity
        }

class InstrumentCatalog:
    """Class to manage a catalog of surgical instruments."""

    def __init__(self):
        self.instruments: List[Instrument] = []

    def add_instrument(self, instrument: Instrument) -> None:
        """Add a new instrument to the catalog."""
        self.instruments.append(instrument)

    def find_instruments_by_category(self, category: str) -> List[Instrument]:
        """Find instruments by category."""
        return [instrument for instrument in self.instruments if instrument.category == category]

    def save_catalog(self, file_path: str) -> None:
        """Save the catalog to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([instrument.to_dict() for instrument in self.instruments], file, indent=4)
        except IOError as e:
            print(f"Error saving catalog: {e}")

    def load_catalog(self, file_path: str) -> None:
        """Load the catalog from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                instruments_data = json.load(file)
                self.instruments = [Instrument(**data) for data in instruments_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog: {e}")

# Example usage of the InstrumentCatalog
if __name__ == "__main__":
    catalog = InstrumentCatalog()

    # Adding instruments to the catalog
    catalog.add_instrument(Instrument("Dental Scaler", "Dental Instruments", "Used for cleaning teeth.", 10))
    catalog.add_instrument(Instrument("Nail Clipper", "Manicure Products", "A tool for trimming nails.", 25))
    catalog.add_instrument(Instrument("Scalpel", "Surgical Products", "A small knife used in surgery.", 15))

    # Save the catalog to a file
    catalog.save_catalog("surgical_instruments_catalog.json")

    # Load the catalog from a file
    catalog.load_catalog("surgical_instruments_catalog.json")
    
    # Find and print instruments by category
    dental_instruments = catalog.find_instruments_by_category("Dental Instruments")
    print("Dental Instruments:")
    for instrument in dental_instruments:
        print(f"- {instrument.name}: {instrument.description} (Quantity: {instrument.quantity})")
```
