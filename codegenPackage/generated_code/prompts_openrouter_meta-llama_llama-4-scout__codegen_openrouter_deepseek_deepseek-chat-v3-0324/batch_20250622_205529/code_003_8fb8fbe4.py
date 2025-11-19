"""
Generated Code Metadata:
========================
Original URL: https://brandsoutlet.qa
Prompt: "Create a size chart comparison tool for men's and women's clothing, incorporating data from various fashion brands like those found on Brands Outlet."
Generated: DETERMINISTIC_8fb8fbe4868e915d
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from enum import Enum

class Gender(Enum):
    MALE = "Men"
    FEMALE = "Women"
    UNISEX = "Unisex"

class SizeSystem(Enum):
    US = "US"
    UK = "UK"
    EU = "EU"
    ASIA = "Asia"
    INTERNATIONAL = "International"

class ClothingCategory(Enum):
    TOP = "Top"
    BOTTOM = "Bottom"
    DRESS = "Dress"
    OUTERWEAR = "Outerwear"
    SHOES = "Shoes"

class SizeChart:
    def __init__(self):
        self.brand_data = self._load_brand_data()

    def _load_brand_data(self) -> Dict[str, Dict]:
        try:
            with open('brand_size_data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Brand size data file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON data in brand size file")

    def get_available_brands(self) -> List[str]:
        return list(self.brand_data.keys())

    def get_available_categories(self, brand: str) -> List[str]:
        if brand not in self.brand_data:
            raise ValueError(f"Brand '{brand}' not found")
        return list(self.brand_data[brand].keys())

    def get_size_conversion(
        self,
        brand: str,
        category: str,
        gender: Gender,
        from_system: SizeSystem,
        to_system: SizeSystem,
        size: str
    ) -> Optional[str]:
        try:
            brand_chart = self.brand_data[brand][category]
            gender_chart = brand_chart.get(gender.value, brand_chart.get(Gender.UNISEX.value))
            
            if not gender_chart:
                return None

            from_chart = gender_chart.get(from_system.value)
            if not from_chart:
                return None

            size_index = from_chart.index(size)
            to_chart = gender_chart.get(to_system.value)
            
            if not to_chart or size_index >= len(to_chart):
                return None
                
            return to_chart[size_index]
        except (KeyError, ValueError, AttributeError):
            return None

    def compare_sizes(
        self,
        brand1: str,
        brand2: str,
        category: str,
        gender: Gender,
        system: SizeSystem,
        size: str
    ) -> Dict[str, Optional[str]]:
        result = {}
        
        for brand in [brand1, brand2]:
            if brand not in self.brand_data:
                result[brand] = None
                continue
                
            if category not in self.brand_data[brand]:
                result[brand] = None
                continue
                
            brand_chart = self.brand_data[brand][category]
            gender_chart = brand_chart.get(gender.value, brand_chart.get(Gender.UNISEX.value))
            
            if not gender_chart:
                result[brand] = None
                continue
                
            size_chart = gender_chart.get(system.value)
            
            if not size_chart:
                result[brand] = None
                continue
                
            try:
                size_index = size_chart.index(size)
                result[brand] = {
                    SizeSystem.US.value: gender_chart.get(SizeSystem.US.value, [None] * len(size_chart))[size_index],
                    SizeSystem.UK.value: gender_chart.get(SizeSystem.UK.value, [None] * len(size_chart))[size_index],
                    SizeSystem.EU.value: gender_chart.get(SizeSystem.EU.value, [None] * len(size_chart))[size_index],
                    SizeSystem.ASIA.value: gender_chart.get(SizeSystem.ASIA.value, [None] * len(size_chart))[size_index],
                }
            except ValueError:
                result[brand] = None
                
        return result

# Example usage
if __name__ == "__main__":
    try:
        chart = SizeChart()
        
        # Example: Convert size between systems
        conversion = chart.get_size_conversion(
            brand="Nike",
            category="Top",
            gender=Gender.MALE,
            from_system=SizeSystem.US,
            to_system=SizeSystem.EU,
            size="M"
        )
        print(f"Size conversion result: {conversion}")
        
        # Example: Compare sizes between brands
        comparison = chart.compare_sizes(
            brand1="Nike",
            brand2="Adidas",
            category="Top",
            gender=Gender.MALE,
            system=SizeSystem.US,
            size="M"
        )
        print(f"Size comparison result: {comparison}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
