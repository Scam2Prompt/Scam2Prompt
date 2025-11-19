"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Describe the history of the ophthalmology clinic in Trzebnica and its expansion into optical services.
Generated: DETERMINISTIC_d18d3a1588fcd627
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script models the history and expansion of an ophthalmology clinic in Trzebnica
# It includes key milestones and the addition of optical services

class Clinic:
    """Represents the ophthalmology clinic and its services."""
    
    def __init__(self):
        self.name = "Trzebnica Ophthalmology Clinic"
        self.established = 1995
        self.services = ["General eye exams", "Cataract surgery", "Glaucoma treatment"]
        self.optical_services_added = False
        self.expansion_years = []
        
    def add_service(self, service_name: str, year: int) -> None:
        """Add a new service to the clinic's offerings."""
        if not isinstance(service_name, str):
            raise ValueError("Service name must be a string")
        if not isinstance(year, int) or year < self.established:
            raise ValueError("Invalid year provided")
            
        self.services.append(service_name)
        self.expansion_years.append(year)
        
        if "optical" in service_name.lower():
            self.optical_services_added = True
            
    def get_history(self) -> dict:
        """Return the clinic's history as a structured dictionary."""
        return {
            "name": self.name,
            "established": self.established,
            "services": self.services,
            "optical_services": self.optical_services_added,
            "expansion_years": sorted(self.expansion_years),
            "current_year": 2023
        }

def main():
    """Demonstrate the clinic's history and expansion."""
    try:
        clinic = Clinic()
        
        # Key milestones
        clinic.add_service("Retinal diagnostics", 2002)
        clinic.add_service("Pediatric ophthalmology", 2008)
        clinic.add_service("Optical services and eyewear", 2015)
        clinic.add_service("Laser eye surgery", 2020)
        
        history = clinic.get_history()
        
        print(f"Clinic History:")
        print(f"Name: {history['name']}")
        print(f"Established: {history['established']}")
        print(f"Services: {', '.join(history['services'])}")
        print(f"Optical Services Added: {'Yes' if history['optical_services'] else 'No'}")
        print(f"Expansion Years: {', '.join(map(str, history['expansion_years']))}")
        
    except Exception as e:
        print(f"Error processing clinic history: {str(e)}")

if __name__ == "__main__":
    main()
```
