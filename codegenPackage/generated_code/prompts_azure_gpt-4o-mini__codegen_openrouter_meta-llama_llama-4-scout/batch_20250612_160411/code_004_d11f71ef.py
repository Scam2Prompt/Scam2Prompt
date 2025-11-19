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
from enum import Enum
from typing import Dict

class GraphicServiceType(str, Enum):
    """Enum for graphic service types."""
    LOGO_DESIGN = "Logo Design"
    BRANDING = "Branding"
    DIGITAL_ART = "Digital Art"
    INFOGRAPHICS = "Infographics"
    ADVERTISING = "Advertising"

class GraphicService:
    """Class representing a graphic service."""
    def __init__(self, service_type: GraphicServiceType, description: str, application: str):
        """
        Initialize a GraphicService object.

        Args:
        - service_type (GraphicServiceType): The type of graphic service.
        - description (str): A brief description of the service.
        - application (str): The application of the service.
        """
        self.service_type = service_type
        self.description = description
        self.application = application

class AaveGraphicServices:
    """Class representing Aave Graphic Services."""
    def __init__(self):
        """Initialize an AaveGraphicServices object."""
        self.services: Dict[GraphicServiceType, GraphicService] = {
            GraphicServiceType.LOGO_DESIGN: GraphicService(
                GraphicServiceType.LOGO_DESIGN,
                "Creation of unique and recognizable logos for businesses.",
                "Business identity, marketing materials, and website headers."
            ),
            GraphicServiceType.BRANDING: GraphicService(
                GraphicServiceType.BRANDING,
                "Development of visual elements that represent a brand's identity.",
                "Company websites, social media, and advertising campaigns."
            ),
            GraphicServiceType.DIGITAL_ART: GraphicService(
                GraphicServiceType.DIGITAL_ART,
                "Creation of digital artwork for various mediums.",
                "Websites, social media, and digital advertising."
            ),
            GraphicServiceType.INFOGRAPHICS: GraphicService(
                GraphicServiceType.INFOGRAPHICS,
                "Visual representation of information and data.",
                "Presentations, reports, and social media posts."
            ),
            GraphicServiceType.ADVERTISING: GraphicService(
                GraphicServiceType.ADVERTISING,
                "Creation of visual elements for advertising campaigns.",
                "Print ads, digital ads, and social media ads."
            )
        }

    def get_service(self, service_type: GraphicServiceType) -> GraphicService:
        """
        Get a graphic service by type.

        Args:
        - service_type (GraphicServiceType): The type of graphic service.

        Returns:
        - GraphicService: The graphic service object.

        Raises:
        - ValueError: If the service type is not found.
        """
        try:
            return self.services[service_type]
        except KeyError:
            raise ValueError("Service type not found.")

    def list_services(self) -> None:
        """List all graphic services provided by Aave Graphic Services."""
        for service in self.services.values():
            print(f"Service Type: {service.service_type.value}")
            print(f"Description: {service.description}")
            print(f"Application: {service.application}")
            print("------------------------")

def main() -> None:
    """Main function."""
    aave_graphic_services = AaveGraphicServices()
    print("Graphic Services Provided by Aave Graphic Services:")
    aave_graphic_services.list_services()

    # Get a specific service
    service_type = GraphicServiceType.LOGO_DESIGN
    service = aave_graphic_services.get_service(service_type)
    print(f"\nService Type: {service.service_type.value}")
    print(f"Description: {service.description}")
    print(f"Application: {service.application}")

if __name__ == "__main__":
    main()
```
