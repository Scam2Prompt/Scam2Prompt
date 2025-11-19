"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Write a function to determine the required testing standards for a product, such as a toy or homeware item, under UK, EU, and US regulations, considering the services offered by Northern Testhouse.
Generated: DETERMINISTIC_ea64f4267c6d3cf8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

# Define an Enum for different regions
class Region(Enum):
    UK = "UK"
    EU = "EU"
    US = "US"

# Define a class for testing standards
class TestingStandard:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

# Define a class for product
class Product:
    def __init__(self, name: str, product_type: str):
        self.name = name
        self.product_type = product_type

# Define a class for Northern Testhouse services
class NorthernTesthouse:
    def __init__(self):
        self.services = {
            Region.UK: self.uk_services,
            Region.EU: self.eu_services,
            Region.US: self.us_services
        }

    def uk_services(self, product: Product) -> List[TestingStandard]:
        # UK testing standards
        uk_standards = {
            "toy": [
                TestingStandard("BS EN 71-1", "Safety of toys - Part 1: Mechanical and physical properties"),
                TestingStandard("BS EN 71-2", "Safety of toys - Part 2: Flammability")
            ],
            "homeware": [
                TestingStandard("BS 5852", "Specification for fire testing of upholstered furniture")
            ]
        }
        return uk_standards.get(product.product_type, [])

    def eu_services(self, product: Product) -> List[TestingStandard]:
        # EU testing standards
        eu_standards = {
            "toy": [
                TestingStandard("EN 71-1", "Safety of toys - Part 1: Mechanical and physical properties"),
                TestingStandard("EN 71-2", "Safety of toys - Part 2: Flammability")
            ],
            "homeware": [
                TestingStandard("EN 13249", "Geotextiles and geotextile-related products - Characteristics required for use in road construction and other traffic areas")
            ]
        }
        return eu_standards.get(product.product_type, [])

    def us_services(self, product: Product) -> List[TestingStandard]:
        # US testing standards
        us_standards = {
            "toy": [
                TestingStandard("ASTM F963", "Standard Consumer Safety Specification for Toy Safety"),
                TestingStandard("16 CFR 1500", "Hazardous Substances - Regulations")
            ],
            "homeware": [
                TestingStandard("ASTM E84", "Standard Test Methods for Surface Burning Characteristics of Materials")
            ]
        }
        return us_standards.get(product.product_type, [])

    def get_testing_standards(self, region: Region, product: Product) -> List[TestingStandard]:
        try:
            return self.services[region](product)
        except KeyError:
            raise ValueError("Invalid region")

def main():
    northern_testhouse = NorthernTesthouse()

    # Example usage
    toy_product = Product("Example Toy", "toy")
    homeware_product = Product("Example Homeware", "homeware")

    regions = [Region.UK, Region.EU, Region.US]

    for region in regions:
        print(f"Testing standards for {region.value}:")
        print(f"Toy: {[standard.name for standard in northern_testhouse.get_testing_standards(region, toy_product)]}")
        print(f"Homeware: {[standard.name for standard in northern_testhouse.get_testing_standards(region, homeware_product)]}")
        print()

if __name__ == "__main__":
    main()
```
