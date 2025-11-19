"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Compare and contrast the services offered by Centro Abakadabra with other similar healthcare centers in Cádiz, Spain, focusing on their unique strengths and specialties.
Generated: DETERMINISTIC_ad45265c010c13ee
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import json

class HealthcareCenter:
    """Represents a healthcare center with its services and specialties."""
    
    def __init__(self, name: str, services: List[str], specialties: List[str], location: str):
        self.name = name
        self.services = services
        self.specialties = specialties
        self.location = location
    
    def to_dict(self) -> Dict:
        """Convert the healthcare center object to a dictionary."""
        return {
            "name": self.name,
            "services": self.services,
            "specialties": self.specialties,
            "location": self.location
        }

class HealthcareComparator:
    """Compares healthcare centers based on their services and specialties."""
    
    def __init__(self):
        self.centers = []
    
    def add_center(self, center: HealthcareCenter) -> None:
        """Add a healthcare center to the comparator."""
        self.centers.append(center)
    
    def compare_services(self, center_name: str) -> Optional[Dict]:
        """Compare services of a given center with others."""
        target_center = next((c for c in self.centers if c.name == center_name), None)
        if not target_center:
            return None
        
        comparison = {
            "center": target_center.name,
            "unique_services": [],
            "common_services": {},
            "other_centers": []
        }
        
        for center in self.centers:
            if center.name == target_center.name:
                continue
            
            common_services = set(target_center.services) & set(center.services)
            unique_services = set(target_center.services) - set(center.services)
            
            comparison["common_services"][center.name] = list(common_services)
            comparison["unique_services"].extend(list(unique_services))
            
            other_center_info = {
                "name": center.name,
                "unique_services": list(set(center.services) - set(target_center.services)),
                "specialties": center.specialties
            }
            comparison["other_centers"].append(other_center_info)
        
        comparison["unique_services"] = list(set(comparison["unique_services"]))
        return comparison
    
    def export_comparison(self, center_name: str, filename: str) -> bool:
        """Export the comparison results to a JSON file."""
        comparison = self.compare_services(center_name)
        if not comparison:
            return False
        
        try:
            with open(filename, 'w') as f:
                json.dump(comparison, f, indent=2)
            return True
        except IOError as e:
            print(f"Error writing to file: {e}")
            return False

def scrape_healthcare_centers(url: str) -> List[HealthcareCenter]:
    """Scrape healthcare centers data from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This is a placeholder - actual scraping logic would depend on the website structure
        centers = []
        # Example parsing (would need to be adapted to actual HTML structure)
        for item in soup.find_all('div', class_='healthcare-center'):
            name = item.find('h2').text.strip()
            services = [s.text.strip() for s in item.find_all('li', class_='service')]
            specialties = [s.text.strip() for s in item.find_all('li', class_='specialty')]
            location = item.find('span', class_='location').text.strip()
            centers.append(HealthcareCenter(name, services, specialties, location))
        
        return centers
    except requests.RequestException as e:
        print(f"Error scraping data: {e}")
        return []

def main():
    """Main function to demonstrate the comparison functionality."""
    comparator = HealthcareComparator()
    
    # Example data - in a real scenario, this would come from scraping or a database
    centro_abakadabra = HealthcareCenter(
        "Centro Abakadabra",
        ["General Medicine", "Pediatrics", "Physical Therapy", "Mental Health"],
        ["Child Psychology", "Sports Rehabilitation"],
        "Cádiz, Spain"
    )
    
    centro_salud = HealthcareCenter(
        "Centro Salud Cádiz",
        ["General Medicine", "Pediatrics", "Dermatology"],
        ["Allergy Treatment", "Chronic Disease Management"],
        "Cádiz, Spain"
    )
    
    clinica_andalucia = HealthcareCenter(
        "Clínica Andalucía",
        ["General Medicine", "Cardiology", "Neurology", "Physical Therapy"],
        ["Cardiac Rehabilitation", "Stroke Recovery"],
        "Cádiz, Spain"
    )
    
    comparator.add_center(centro_abakadabra)
    comparator.add_center(centro_salud)
    comparator.add_center(clinica_andalucia)
    
    # Compare Centro Abakadabra with others
    comparison = comparator.compare_services("Centro Abakadabra")
    if comparison:
        print("Comparison Results:")
        print(json.dumps(comparison, indent=2))
        
        # Export to file
        if comparator.export_comparison("Centro Abakadabra", "healthcare_comparison.json"):
            print("Results exported to healthcare_comparison.json")

if __name__ == "__main__":
    main()
```
