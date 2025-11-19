"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Generate a code snippet to create a virtual wine tasting guide for an event like FestiVin Caraquet, highlighting wines from France, Italy, and Spain.
Generated: DETERMINISTIC_ba560a8131a65948
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Wine:
    """Represents a wine with its attributes."""
    
    def __init__(self, name: str, country: str, region: str, grape_variety: str, 
                 tasting_notes: str, pairing_suggestions: str, year: Optional[int] = None):
        """Initialize a Wine instance.
        
        Args:
            name: Name of the wine.
            country: Country of origin.
            region: Region within the country.
            grape_variety: Grape variety used.
            tasting_notes: Description of taste profile.
            pairing_suggestions: Suggested food pairings.
            year: Vintage year (optional).
        """
        self.name = name
        self.country = country
        self.region = region
        self.grape_variety = grape_variety
        self.tasting_notes = tasting_notes
        self.pairing_suggestions = pairing_suggestions
        self.year = year
    
    def to_dict(self) -> Dict:
        """Convert Wine object to dictionary for serialization."""
        return {
            'name': self.name,
            'country': self.country,
            'region': self.region,
            'grape_variety': self.grape_variety,
            'tasting_notes': self.tasting_notes,
            'pairing_suggestions': self.pairing_suggestions,
            'year': self.year
        }

class WineTastingGuide:
    """Virtual wine tasting guide for an event."""
    
    def __init__(self, event_name: str):
        """Initialize the guide with an event name."""
        self.event_name = event_name
        self.wines: List[Wine] = []
    
    def add_wine(self, wine: Wine) -> None:
        """Add a wine to the guide.
        
        Args:
            wine: Wine object to add.
        """
        self.wines.append(wine)
    
    def get_wines_by_country(self, country: str) -> List[Wine]:
        """Get all wines from a specific country.
        
        Args:
            country: Country to filter by.
            
        Returns:
            List of Wine objects from the specified country.
        """
        return [wine for wine in self.wines if wine.country.lower() == country.lower()]
    
    def save_to_file(self, filename: str) -> None:
        """Save the wine guide to a JSON file.
        
        Args:
            filename: Name of the file to save to.
            
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'event_name': self.event_name,
                    'wines': [wine.to_dict() for wine in self.wines]
                }, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save wine guide: {e}")
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'WineTastingGuide':
        """Load a wine guide from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Returns:
            WineTastingGuide instance loaded from file.
            
        Raises:
            IOError: If file cannot be read.
            ValueError: If file content is invalid.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
        except IOError as e:
            raise IOError(f"Failed to load wine guide: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON file: {e}")
        
        guide = cls(data['event_name'])
        for wine_data in data['wines']:
            guide.add_wine(Wine(**wine_data))
        return guide

def create_festivin_guide() -> WineTastingGuide:
    """Create a sample wine guide for FestiVin Caraquet."""
    guide = WineTastingGuide("FestiVin Caraquet")
    
    # French wines
    guide.add_wine(Wine(
        name="Château Margaux",
        country="France",
        region="Bordeaux",
        grape_variety="Cabernet Sauvignon",
        tasting_notes="Elegant with notes of blackcurrant, violet, and spice.",
        pairing_suggestions="Red meat, game, strong cheeses.",
        year=2015
    ))
    
    guide.add_wine(Wine(
        name="Domaine Leflaive Puligny-Montrachet",
        country="France",
        region="Burgundy",
        grape_variety="Chardonnay",
        tasting_notes="Buttery with citrus, apple, and mineral notes.",
        pairing_suggestions="Seafood, poultry, creamy sauces.",
        year=2018
    ))
    
    # Italian wines
    guide.add_wine(Wine(
        name="Sassicaia",
        country="Italy",
        region="Tuscany",
        grape_variety="Cabernet Sauvignon",
        tasting_notes="Full-bodied with dark fruit, tobacco, and vanilla.",
        pairing_suggestions="Grilled meats, aged cheeses.",
        year=2016
    ))
    
    guide.add_wine(Wine(
        name="Gaja Barbaresco",
        country="Italy",
        region="Piedmont",
        grape_variety="Nebbiolo",
        tasting_notes="Complex with rose, cherry, and truffle notes.",
        pairing_suggestions="Pasta, risotto, truffle dishes.",
        year=2017
    ))
    
    # Spanish wines
    guide.add_wine(Wine(
        name="Vega Sicilia Unico",
        country="Spain",
        region="Ribera del Duero",
        grape_variety="Tempranillo",
        tasting_notes="Rich with dark fruit, leather, and spice.",
        pairing_suggestions="Lamb, roasted meats, cured ham.",
        year=2012
    ))
    
    guide.add_wine(Wine(
        name="Albariño Pazo de Señorans",
        country="Spain",
        region="Rías Baixas",
        grape_variety="Albariño",
        tasting_notes="Crisp with peach, citrus, and saline notes.",
        pairing_suggestions="Shellfish, seafood, light appetizers.",
        year=2020
    ))
    
    return guide

# Example usage
if __name__ == "__main__":
    try:
        # Create and save the guide
        guide = create_festivin_guide()
        guide.save_to_file("festivin_guide.json")
        
        # Load and display wines from France
        loaded_guide = WineTastingGuide.load_from_file("festivin_guide.json")
        french_wines = loaded_guide.get_wines_by_country("France")
        
        print(f"Wine Tasting Guide for {loaded_guide.event_name}")
        print("\nFrench Wines:")
        for wine in french_wines:
            print(f"\n{wine.name} ({wine.year})")
            print(f"Region: {wine.region}, Grape: {wine.grape_variety}")
            print(f"Tasting Notes: {wine.tasting_notes}")
            print(f"Pairing Suggestions: {wine.pairing_suggestions}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
