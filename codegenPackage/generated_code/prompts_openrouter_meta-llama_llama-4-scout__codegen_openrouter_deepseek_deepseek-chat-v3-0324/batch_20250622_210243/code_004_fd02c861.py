"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: What are the different types of dental services provided by Heroes Dental, including general dentistry, orthodontics, and pediatric dentistry?
Generated: DETERMINISTIC_fd02c861c1553b3f
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DentalService:
    """Base class representing a dental service."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class GeneralDentistry(DentalService):
    """Class representing general dentistry services."""
    def __init__(self):
        super().__init__(
            name="General Dentistry",
            description="Routine dental care including cleanings, fillings, and exams."
        )


class Orthodontics(DentalService):
    """Class representing orthodontic services."""
    def __init__(self):
        super().__init__(
            name="Orthodontics",
            description="Specialized care for teeth alignment including braces and retainers."
        )


class PediatricDentistry(DentalService):
    """Class representing pediatric dental services."""
    def __init__(self):
        super().__init__(
            name="Pediatric Dentistry",
            description="Dental care specialized for children and adolescents."
        )


class CosmeticDentistry(DentalService):
    """Class representing cosmetic dentistry services."""
    def __init__(self):
        super().__init__(
            name="Cosmetic Dentistry",
            description="Services focused on improving dental aesthetics including veneers and whitening."
        )


class DentalImplant(DentalService):
    """Class representing dental implant services."""
    def __init__(self):
        super().__init__(
            name="Dental Implants",
            description="Permanent tooth replacement solutions using implants."
        )


class HeroesDentalServices:
    """Class representing all dental services offered by Heroes Dental."""
    def __init__(self):
        self.services = [
            GeneralDentistry(),
            Orthodontics(),
            PediatricDentistry(),
            CosmeticDentistry(),
            DentalImplant()
        ]

    def get_services(self):
        """Returns list of all available dental services."""
        return self.services

    def get_service_by_name(self, name):
        """
        Returns a specific service by name.
        
        Args:
            name (str): Name of the service to retrieve
            
        Returns:
            DentalService: The requested service or None if not found
        """
        for service in self.services:
            if service.name.lower() == name.lower():
                return service
        return None


# Example usage
if __name__ == "__main__":
    heroes_dental = HeroesDentalServices()
    
    # Print all services
    print("Heroes Dental Services:")
    for service in heroes_dental.get_services():
        print(f"- {service}")
    
    # Get specific service example
    ortho = heroes_dental.get_service_by_name("orthodontics")
    if ortho:
        print(f"\nFound service: {ortho}")
```
