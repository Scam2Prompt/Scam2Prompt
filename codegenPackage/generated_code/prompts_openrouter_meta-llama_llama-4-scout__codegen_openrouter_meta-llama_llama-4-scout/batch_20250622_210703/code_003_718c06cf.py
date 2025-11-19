"""
Generated Code Metadata:
========================
Original URL: https://dextranslogistics.com
Prompt: "Compare the features of Dextrans Logistics' air freight and sea freight services, highlighting their benefits for international trade."
Generated: DETERMINISTIC_718c06cf141b8d15
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define Enum for FreightType
class FreightType(str, Enum):
    """Enum for freight types"""
    AIR = "air"
    SEA = "sea"

# Define dataclass for FreightService
@dataclass
class FreightService:
    """Dataclass for freight services"""
    name: str
    description: str
    benefits: List[str]
    freight_type: FreightType

# Define dataclass for LogisticsCompany
@dataclass
class LogisticsCompany:
    """Dataclass for logistics company"""
    name: str
    freight_services: List[FreightService]

# Define function to compare freight services
def compare_freight_services(logistics_company: LogisticsCompany, freight_type: FreightType):
    """
    Compare the features of logistics company's freight services.

    Args:
    logistics_company (LogisticsCompany): The logistics company.
    freight_type (FreightType): The type of freight.

    Returns:
    FreightService: The freight service of the given type.
    """
    for service in logistics_company.freight_services:
        if service.freight_type == freight_type:
            return service
    raise ValueError("Freight service not found")

# Define function to print freight service details
def print_freight_service_details(freight_service: FreightService):
    """
    Print the details of a freight service.

    Args:
    freight_service (FreightService): The freight service.
    """
    print(f"**{freight_service.name}**")
    print(f"Description: {freight_service.description}")
    print("Benefits:")
    for benefit in freight_service.benefits:
        print(f"- {benefit}")

# Main function
def main():
    try:
        # Create freight services
        air_freight_service = FreightService(
            name="Air Freight",
            description="Fast and reliable air freight services",
            benefits=["Fast transit times", "Reliable delivery", "Global coverage"],
            freight_type=FreightType.AIR
        )
        sea_freight_service = FreightService(
            name="Sea Freight",
            description="Cost-effective and efficient sea freight services",
            benefits=["Cost-effective", "High capacity", "Environmentally friendly"],
            freight_type=FreightType.SEA
        )

        # Create logistics company
        dextrans_logistics = LogisticsCompany(
            name="Dextrans Logistics",
            freight_services=[air_freight_service, sea_freight_service]
        )

        # Compare and print freight services
        air_freight = compare_freight_services(dextrans_logistics, FreightType.AIR)
        sea_freight = compare_freight_services(dextrans_logistics, FreightType.SEA)

        print("Air Freight Service:")
        print_freight_service_details(air_freight)
        print("\nSea Freight Service:")
        print_freight_service_details(sea_freight)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
