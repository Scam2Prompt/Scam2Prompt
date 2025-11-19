"""
Generated Code Metadata:
========================
Original URL: https://dimensions-solar.com
Prompt: "Create a technical documentation for a solar plant solution, including system architecture, component selection, and installation guidelines."
Generated: DETERMINISTIC_7dc2ca210c37acf8
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar Plant Solution Technical Documentation Generator

This script generates a comprehensive technical documentation for a solar plant solution,
including system architecture, component selection, and installation guidelines.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class SolarPlantDocumentation:
    """
    A class to generate technical documentation for solar plant solutions.
    """
    
    def __init__(self, project_name: str, client_name: str, location: str):
        """
        Initialize the documentation generator with project details.
        
        Args:
            project_name: Name of the solar plant project
            client_name: Name of the client/organization
            location: Geographic location of the plant
        """
        self.project_name = project_name
        self.client_name = client_name
        self.location = location
        self.created_date = datetime.now().strftime("%Y-%m-%d")
        self.sections = {
            "system_architecture": {},
            "component_selection": {},
            "installation_guidelines": {}
        }
        
    def add_system_architecture(self, 
                               system_type: str,
                               capacity_kw: float,
                               components: List[str],
                               diagram_path: Optional[str] = None) -> None:
        """
        Add system architecture details to the documentation.
        
        Args:
            system_type: Type of solar system (e.g., grid-tied, off-grid)
            capacity_kw: Total system capacity in kW
            components: List of main system components
            diagram_path: Optional path to system diagram
        """
        self.sections["system_architecture"] = {
            "system_type": system_type,
            "capacity_kw": capacity_kw,
            "main_components": components,
            "diagram": diagram_path,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def add_component_selection(self,
                               panels: Dict,
                               inverters: Dict,
                               mounting: Dict,
                               batteries: Optional[Dict] = None) -> None:
        """
        Add component selection details to the documentation.
        
        Args:
            panels: Dictionary containing panel specifications
            inverters: Dictionary containing inverter specifications
            mounting: Dictionary containing mounting system details
            batteries: Optional dictionary for battery storage details
        """
        self.sections["component_selection"] = {
            "solar_panels": panels,
            "inverters": inverters,
            "mounting_system": mounting,
            "battery_storage": batteries if batteries else {},
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def add_installation_guidelines(self,
                                    site_prep: List[str],
                                    safety_procedures: List[str],
                                    commissioning: List[str],
                                    maintenance: List[str]) -> None:
        """
        Add installation guidelines to the documentation.
        
        Args:
            site_prep: List of site preparation steps
            safety_procedures: List of safety procedures
            commissioning: List of commissioning steps
            maintenance: List of maintenance procedures
        """
        self.sections["installation_guidelines"] = {
            "site_preparation": site_prep,
            "safety_procedures": safety_procedures,
            "commissioning": commissioning,
            "maintenance": maintenance,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def generate_document(self, output_format: str = "json") -> Dict:
        """
        Generate the complete documentation in the specified format.
        
        Args:
            output_format: Output format ('json' or 'dict')
            
        Returns:
            Documentation in requested format
            
        Raises:
            ValueError: If output format is not supported
        """
        document = {
            "project": self.project_name,
            "client": self.client_name,
            "location": self.location,
            "created_date": self.created_date,
            "sections": self.sections
        }
        
        if output_format.lower() == "json":
            return json.dumps(document, indent=4)
        elif output_format.lower() == "dict":
            return document
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the documentation to a JSON file.
        
        Args:
            filename: Name of the file to save
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "project": self.project_name,
                    "client": self.client_name,
                    "location": self.location,
                    "created_date": self.created_date,
                    "sections": self.sections
                }, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write documentation file: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize documentation
        doc = SolarPlantDocumentation(
            project_name="Sunshine Solar Farm",
            client_name="Green Energy Co.",
            location="California, USA"
        )
        
        # Add system architecture
        doc.add_system_architecture(
            system_type="Grid-tied with battery backup",
            capacity_kw=500.0,
            components=[
                "Solar panels",
                "String inverters",
                "Battery storage",
                "Monitoring system"
            ],
            diagram_path="diagrams/system_architecture.png"
        )
        
        # Add component selection
        doc.add_component_selection(
            panels={
                "model": "SunPower X-Series",
                "quantity": 1200,
                "power_rating_w": 400,
                "efficiency": 0.225
            },
            inverters={
                "model": "SMA Sunny Boy",
                "quantity": 10,
                "capacity_kw": 50
            },
            mounting={
                "type": "Ground-mounted",
                "tilt_angle": 30,
                "azimuth": 180
            },
            batteries={
                "model": "Tesla Powerwall",
                "quantity": 20,
                "capacity_kwh": 13.5
            }
        )
        
        # Add installation guidelines
        doc.add_installation_guidelines(
            site_prep=[
                "Clear vegetation",
                "Level ground",
                "Install fencing"
            ],
            safety_procedures=[
                "Use proper PPE",
                "Lockout/tagout procedures",
                "Fall protection"
            ],
            commissioning=[
                "System testing",
                "Performance verification",
                "Client training"
            ],
            maintenance=[
                "Quarterly panel cleaning",
                "Annual system inspection",
                "Battery health monitoring"
            ]
        )
        
        # Save to file
        doc.save_to_file("solar_plant_documentation.json")
        print("Documentation generated successfully!")
        
    except Exception as e:
        print(f"Error generating documentation: {str(e)}")
```
