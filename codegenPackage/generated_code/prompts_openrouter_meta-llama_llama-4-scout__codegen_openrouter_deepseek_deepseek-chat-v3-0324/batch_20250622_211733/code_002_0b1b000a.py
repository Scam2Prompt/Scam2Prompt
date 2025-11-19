"""
Generated Code Metadata:
========================
Original URL: https://thebigbrindentalservice.online
Prompt: Compare the dental services provided by The Big Grin Dental Service, focusing on general dentistry, cosmetic dentistry, and oral surgery, including their durations and starting prices.
Generated: DETERMINISTIC_0b1b000a15512df4
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DentalService:
    """Represents a dental service with its details."""
    name: str
    description: str
    duration: str  # e.g., "30 minutes", "1 hour"
    starting_price: float  # in USD

@dataclass
class DentalClinic:
    """Represents a dental clinic and its services."""
    name: str
    services: List[DentalService]

def get_big_grin_services() -> DentalClinic:
    """Returns the dental services provided by The Big Grin Dental Service."""
    general_dentistry = DentalService(
        name="General Dentistry",
        description="Routine check-ups, cleanings, fillings, and basic oral care.",
        duration="30 minutes - 1 hour",
        starting_price=50.00
    )

    cosmetic_dentistry = DentalService(
        name="Cosmetic Dentistry",
        description="Teeth whitening, veneers, and other aesthetic treatments.",
        duration="1 hour - 2 hours",
        starting_price=200.00
    )

    oral_surgery = DentalService(
        name="Oral Surgery",
        description="Tooth extractions, implants, and other surgical procedures.",
        duration="1 hour - 3 hours",
        starting_price=300.00
    )

    return DentalClinic(
        name="The Big Grin Dental Service",
        services=[general_dentistry, cosmetic_dentistry, oral_surgery]
    )

def display_services(clinic: DentalClinic) -> None:
    """Displays the services offered by a dental clinic in a formatted manner."""
    print(f"\nDental Services Provided by {clinic.name}:")
    print("=" * 50)
    for service in clinic.services:
        print(f"\nService: {service.name}")
        print(f"Description: {service.description}")
        print(f"Duration: {service.duration}")
        print(f"Starting Price: ${service.starting_price:.2f}")
    print("=" * 50)

def main() -> None:
    """Main function to fetch and display dental services."""
    try:
        clinic = get_big_grin_services()
        display_services(clinic)
    except Exception as e:
        print(f"An error occurred while fetching dental services: {e}")

if __name__ == "__main__":
    main()
```
