"""
Generated Code Metadata:
========================
Original URL: https://eclipsi-net.com
Prompt: Create a program that assists professionals in selecting luminaries for urban spaces, based on Eclipsi's asesoramiento a profesionales service.
Generated: DETERMINISTIC_1a35bd267fbdac50
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Dict

class LuminaireType(Enum):
    STREET_LIGHT = "Street Light"
    PARK_LIGHT = "Park Light"
    ARCHITECTURAL = "Architectural"
    DECORATIVE = "Decorative"
    SECURITY = "Security"

class PowerSource(Enum):
    SOLAR = "Solar"
    GRID = "Grid"
    HYBRID = "Hybrid"

class Environment(Enum):
    URBAN = "Urban"
    SUBURBAN = "Suburban"
    RURAL = "Rural"

@dataclass
class Luminaire:
    id: str
    name: str
    type: LuminaireType
    wattage: float
    lumens: int
    color_temp: int  # in Kelvin
    power_source: PowerSource
    suitable_environments: List[Environment]
    price: float
    durability_years: int

class LuminaireAdvisor:
    def __init__(self, database_file: str = "luminaires.json"):
        """
        Initialize the LuminaireAdvisor with a database of available luminaires.
        
        Args:
            database_file: Path to JSON file containing luminaire data
        """
        self.luminaires = self._load_luminaires(database_file)
    
    def _load_luminaires(self, file_path: str) -> List[Luminaire]:
        """Load luminaires from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return [
                    Luminaire(
                        id=item['id'],
                        name=item['name'],
                        type=LuminaireType(item['type']),
                        wattage=item['wattage'],
                        lumens=item['lumens'],
                        color_temp=item['color_temp'],
                        power_source=PowerSource(item['power_source']),
                        suitable_environments=[Environment(e) for e in item['suitable_environments']],
                        price=item['price'],
                        durability_years=item['durability_years']
                    ) for item in data['luminaires']
                ]
        except FileNotFoundError:
            raise ValueError(f"Database file {file_path} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {file_path}")
        except KeyError as e:
            raise ValueError(f"Missing required field in database: {e}")
    
    def recommend_luminaires(
        self,
        environment: Environment,
        luminaire_type: Optional[LuminaireType] = None,
        min_lumens: Optional[int] = None,
        max_wattage: Optional[float] = None,
        power_source: Optional[PowerSource] = None,
        max_price: Optional[float] = None,
        min_durability: Optional[int] = None
    ) -> List[Luminaire]:
        """
        Recommend luminaires based on specified criteria.
        
        Args:
            environment: Target environment for the luminaires
            luminaire_type: Optional filter for specific luminaire type
            min_lumens: Optional minimum brightness requirement
            max_wattage: Optional maximum power consumption
            power_source: Optional preferred power source
            max_price: Optional maximum price limit
            min_durability: Optional minimum durability in years
            
        Returns:
            List of matching Luminaire objects, sorted by price ascending
        """
        filtered = []
        
        for luminaire in self.luminaires:
            # Check environment suitability
            if environment not in luminaire.suitable_environments:
                continue
                
            # Apply filters if specified
            if luminaire_type and luminaire.type != luminaire_type:
                continue
            if min_lumens and luminaire.lumens < min_lumens:
                continue
            if max_wattage and luminaire.wattage > max_wattage:
                continue
            if power_source and luminaire.power_source != power_source:
                continue
            if max_price and luminaire.price > max_price:
                continue
            if min_durability and luminaire.durability_years < min_durability:
                continue
                
            filtered.append(luminaire)
        
        # Sort by price ascending
        return sorted(filtered, key=lambda x: x.price)
    
    def get_luminaire_details(self, luminaire_id: str) -> Optional[Luminaire]:
        """Get detailed information about a specific luminaire by ID."""
        for luminaire in self.luminaires:
            if luminaire.id == luminaire_id:
                return luminaire
        return None

def main():
    try:
        advisor = LuminaireAdvisor()
        
        print("Welcome to Eclipsi's Luminaire Advisor for Urban Spaces")
        print("Please provide your requirements:\n")
        
        # Get user input
        env = Environment(input("Environment (Urban/Suburban/Rural): ").upper())
        lum_type = input("Luminaire type (optional, press enter to skip): ")
        lum_type = LuminaireType(lum_type) if lum_type else None
        
        min_lumens = input("Minimum brightness in lumens (optional): ")
        min_lumens = int(min_lumens) if min_lumens else None
        
        max_wattage = input("Maximum wattage (optional): ")
        max_wattage = float(max_wattage) if max_wattage else None
        
        power_src = input("Power source (Solar/Grid/Hybrid, optional): ")
        power_src = PowerSource(power_src) if power_src else None
        
        max_price = input("Maximum price (optional): ")
        max_price = float(max_price) if max_price else None
        
        min_durability = input("Minimum durability in years (optional): ")
        min_durability = int(min_durability) if min_durability else None
        
        # Get recommendations
        recommendations = advisor.recommend_luminaires(
            environment=env,
            luminaire_type=lum_type,
            min_lumens=min_lumens,
            max_wattage=max_wattage,
            power_source=power_src,
            max_price=max_price,
            min_durability=min_durability
        )
        
        # Display results
        print("\nRecommended Luminaires:")
        if not recommendations:
            print("No luminaires match your criteria.")
        else:
            for i, lum in enumerate(recommendations, 1):
                print(f"\n{i}. {lum.name} (ID: {lum.id})")
                print(f"Type: {lum.type.value}")
                print(f"Brightness: {lum.lumens} lumens")
                print(f"Power: {lum.wattage}W ({lum.power_source.value})")
                print(f"Color Temperature: {lum.color_temp}K")
                print(f"Price: ${lum.price:.2f}")
                print(f"Durability: {lum.durability_years} years")
                print(f"Suitable for: {', '.join([e.value for e in lum.suitable_environments])}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
