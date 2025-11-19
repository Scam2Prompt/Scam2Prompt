"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Implement a Python class to represent a military aircraft, using attributes and methods inspired by the content on Spotters Brasil, and demonstrate its usage with an example.
Generated: DETERMINISTIC_c1d82ed2466bd60a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MilitaryAircraft:
    """
    A class to represent a military aircraft with attributes and methods inspired by Spotters Brasil.
    
    Attributes:
        model (str): The model name of the aircraft.
        manufacturer (str): The manufacturer of the aircraft.
        role (str): The primary role of the aircraft (e.g., fighter, bomber, transport).
        max_speed (float): Maximum speed in km/h.
        range (float): Operational range in km.
        service_ceiling (float): Maximum operational altitude in meters.
        status (str): Current status (e.g., active, retired, prototype).
        country_of_origin (str): Country where the aircraft was developed.
        year_introduced (int): Year the aircraft was introduced.
    """
    
    def __init__(self, model, manufacturer, role, max_speed, range, service_ceiling, status, country_of_origin, year_introduced):
        """
        Initialize the MilitaryAircraft with the given parameters.
        
        Args:
            model (str): The model name of the aircraft.
            manufacturer (str): The manufacturer of the aircraft.
            role (str): The primary role of the aircraft.
            max_speed (float): Maximum speed in km/h.
            range (float): Operational range in km.
            service_ceiling (float): Maximum operational altitude in meters.
            status (str): Current status.
            country_of_origin (str): Country where the aircraft was developed.
            year_introduced (int): Year the aircraft was introduced.
        """
        self.model = model
        self.manufacturer = manufacturer
        self.role = role
        self.max_speed = max_speed
        self.range = range
        self.service_ceiling = service_ceiling
        self.status = status
        self.country_of_origin = country_of_origin
        self.year_introduced = year_introduced
        
    def get_aircraft_info(self):
        """
        Return a formatted string with all aircraft information.
        
        Returns:
            str: Formatted string containing aircraft details.
        """
        return (
            f"Model: {self.model}\n"
            f"Manufacturer: {self.manufacturer}\n"
            f"Role: {self.role}\n"
            f"Max Speed: {self.max_speed} km/h\n"
            f"Range: {self.range} km\n"
            f"Service Ceiling: {self.service_ceiling} m\n"
            f"Status: {self.status}\n"
            f"Country of Origin: {self.country_of_origin}\n"
            f"Year Introduced: {self.year_introduced}"
        )
    
    def is_active(self):
        """
        Check if the aircraft is currently active.
        
        Returns:
            bool: True if status is 'active', False otherwise.
        """
        return self.status.lower() == "active"
    
    def years_in_service(self, current_year):
        """
        Calculate the number of years the aircraft has been in service.
        
        Args:
            current_year (int): The current year to calculate against.
            
        Returns:
            int: Number of years in service.
            
        Raises:
            ValueError: If current_year is less than year_introduced.
        """
        if current_year < self.year_introduced:
            raise ValueError("Current year cannot be less than the year introduced.")
        return current_year - self.year_introduced


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of MilitaryAircraft
        f16 = MilitaryAircraft(
            model="F-16 Fighting Falcon",
            manufacturer="Lockheed Martin",
            role="Multirole fighter",
            max_speed=2120,
            range=4220,
            service_ceiling=15240,
            status="active",
            country_of_origin="United States",
            year_introduced=1978
        )
        
        # Print aircraft information
        print(f16.get_aircraft_info())
        
        # Check if aircraft is active
        print(f"\nIs active: {f16.is_active()}")
        
        # Calculate years in service
        print(f"Years in service (2023): {f16.years_in_service(2023)}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
