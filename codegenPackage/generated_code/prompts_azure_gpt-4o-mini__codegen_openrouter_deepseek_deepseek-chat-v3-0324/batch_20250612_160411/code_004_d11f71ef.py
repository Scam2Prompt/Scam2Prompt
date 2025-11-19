"""
Generated Code Metadata:
========================
Original URL: https://aave.info
Prompt: Describe the types of graphic services provided by Aave Graphic Services and their applications.
Generated: DETERMINISTIC_d11f71ef3e41d217
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Aave Graphic Services - Service Types and Applications

This module defines the various graphic services provided by Aave Graphic Services
along with their typical applications.
"""

from typing import List, Dict, Tuple

class GraphicService:
    """
    Base class representing a graphic service with its description and applications.
    """
    def __init__(self, name: str, description: str, applications: List[str]):
        """
        Initialize a graphic service.
        
        Args:
            name: Name of the service
            description: Brief description of the service
            applications: List of common applications for this service
        """
        self.name = name
        self.description = description
        self.applications = applications
    
    def __str__(self) -> str:
        """Return a formatted string representation of the service."""
        apps = "\n  - ".join(self.applications)
        return f"{self.name}:\nDescription: {self.description}\nApplications:\n  - {apps}"

class AaveGraphicServices:
    """
    Main class representing all graphic services offered by Aave Graphic Services.
    """
    def __init__(self):
        """Initialize with all available services."""
        self.services = self._initialize_services()
    
    def _initialize_services(self) -> List[GraphicService]:
        """Create and return all available graphic services."""
        return [
            GraphicService(
                name="Logo Design",
                description="Creation of unique brand identifiers and visual marks",
                applications=[
                    "Brand identity development",
                    "Business branding",
                    "Product branding"
                ]
            ),
            GraphicService(
                name="Print Design",
                description="Design services for physical printed materials",
                applications=[
                    "Brochures and flyers",
                    "Business cards",
                    "Posters and banners",
                    "Packaging design"
                ]
            ),
            GraphicService(
                name="Digital Illustration",
                description="Custom artwork creation for digital platforms",
                applications=[
                    "Book and magazine illustrations",
                    "Character design",
                    "Concept art",
                    "Infographics"
                ]
            ),
            GraphicService(
                name="UI/UX Design",
                description="User interface and experience design for digital products",
                applications=[
                    "Website design",
                    "Mobile app interfaces",
                    "Software interfaces",
                    "Interactive prototypes"
                ]
            ),
            GraphicService(
                name="Motion Graphics",
                description="Animation and visual effects for video content",
                applications=[
                    "Animated logos",
                    "Explainer videos",
                    "Advertisement animations",
                    "Title sequences"
                ]
            ),
            GraphicService(
                name="3D Modeling & Rendering",
                description="Creation of three-dimensional digital assets",
                applications=[
                    "Product visualization",
                    "Architectural renderings",
                    "Game assets",
                    "Medical and scientific visualization"
                ]
            )
        ]
    
    def get_all_services(self) -> List[GraphicService]:
        """Return all available graphic services."""
        return self.services
    
    def get_service_by_name(self, name: str) -> GraphicService:
        """
        Get a specific service by name.
        
        Args:
            name: Name of the service to retrieve
            
        Returns:
            The requested GraphicService object
            
        Raises:
            ValueError: If service with given name doesn't exist
        """
        for service in self.services:
            if service.name.lower() == name.lower():
                return service
        raise ValueError(f"Service '{name}' not found")
    
    def get_services_as_dict(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Return all services formatted as a dictionary.
        
        Returns:
            Dictionary with service names as keys and dicts containing
            description and applications as values
        """
        return {
            service.name: {
                "description": service.description,
                "applications": service.applications
            }
            for service in self.services
        }

# Example usage
if __name__ == "__main__":
    try:
        aave = AaveGraphicServices()
        
        # Print all services
        print("Aave Graphic Services Offered:")
        for service in aave.get_all_services():
            print("\n" + str(service))
        
        # Get specific service example
        print("\nGetting details for 'UI/UX Design':")
        ui_service = aave.get_service_by_name("UI/UX Design")
        print(ui_service)
        
    except Exception as e:
        print(f"Error: {e}")
```
