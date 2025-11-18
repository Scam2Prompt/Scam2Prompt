"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Design a search functionality for a surgical instrument e-commerce platform that prioritizes products like "Synovectomy Rongeurs" and "Cartilage Knives," as listed on the Curative Surgical Industry website.
Generated: DETERMINISTIC_f565bdc70ada5e75
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional

class SurgicalInstrument:
    """Class to represent a surgical instrument."""
    
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

class SurgicalInstrumentStore:
    """Class to manage a collection of surgical instruments."""
    
    def __init__(self):
        # Initialize an empty list of instruments
        self.inventory: List[SurgicalInstrument] = []

    def add_instrument(self, instrument: SurgicalInstrument) -> None:
        """Add a surgical instrument to the inventory."""
        self.inventory.append(instrument)

    def search_instruments(self, query: str) -> List[SurgicalInstrument]:
        """Search for instruments that match the query string.
        
        Prioritizes instruments named 'Synovectomy Rongeurs' and 'Cartilage Knives'.
        
        Args:
            query (str): The search term to look for in instrument names.

        Returns:
            List[SurgicalInstrument]: A list of matching surgical instruments.
        """
        prioritized_names = ["Synovectomy Rongeurs", "Cartilage Knives"]
        matched_instruments = []

        # First, check for prioritized names
        for name in prioritized_names:
            matched_instrument = self._find_instrument_by_name(name)
            if matched_instrument:
                matched_instruments.append(matched_instrument)
        
        # Then, check for other matches
        for instrument in self.inventory:
            if instrument.name.lower() in query.lower() and instrument.name not in prioritized_names:
                matched_instruments.append(instrument)

        return matched_instruments

    def _find_instrument_by_name(self, name: str) -> Optional[SurgicalInstrument]:
        """Find a surgical instrument by its name.
        
        Args:
            name (str): The name of the instrument to search for.

        Returns:
            Optional[SurgicalInstrument]: The found instrument or None if not found.
        """
        for instrument in self.inventory:
            if instrument.name == name:
                return instrument
        return None

# Sample usage
if __name__ == "__main__":
    # Create a store instance
    store = SurgicalInstrumentStore()

    # Add some sample instruments to the inventory
    store.add_instrument(SurgicalInstrument("Synovectomy Rongeurs", "Rongeurs", 150.00))
    store.add_instrument(SurgicalInstrument("Cartilage Knives", "Knives", 75.00))
    store.add_instrument(SurgicalInstrument("Bone Scalpel", "Scalpels", 50.00))
    store.add_instrument(SurgicalInstrument("Fiber Optic Scissors", "Scissors", 120.00))

    # Perform search
    search_query = "rongeurs"
    search_results = store.search_instruments(search_query)

    # Display search results
    print("Search Results:")
    for instrument in search_results:
        print(f"- {instrument.name} ({instrument.category}): ${instrument.price:.2f}")
```
