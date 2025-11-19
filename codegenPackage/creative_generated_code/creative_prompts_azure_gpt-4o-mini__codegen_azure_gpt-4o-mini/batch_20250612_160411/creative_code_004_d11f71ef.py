"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.info
Prompt: Describe the types of graphic services provided by Aave Graphic Services and their applications.
Generated: DETERMINISTIC_d11f71ef3e41d217
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GraphicService:
    """
    A class to represent graphic services provided by Aave Graphic Services.

    Attributes:
        service_name (str): Name of the graphic service.
        description (str): Description of the service.
        applications (list): Applications of the service.
    """

    def __init__(self, service_name, description, applications):
        """
        Initializes the GraphicService with the given parameters.

        Args:
            service_name (str): Name of the graphic service.
            description (str): Description of the service.
            applications (list): Applications of the service.

        Raises:
            ValueError: If any of the parameters are empty or not of the expected type.
        """
        if not service_name or not isinstance(service_name, str):
            raise ValueError("Invalid service name provided.")
        if not description or not isinstance(description, str):
            raise ValueError("Invalid description provided.")
        if not isinstance(applications, list) or not all(isinstance(app, str) for app in applications):
            raise ValueError("Applications must be a list of strings.")

        self.service_name = service_name
        self.description = description
        self.applications = applications

    def display_service_info(self):
        """
        Displays the information of the graphic service.
        """
        print(f"Service Name: {self.service_name}")
        print(f"Description: {self.description}")
        print(f"Applications: {', '.join(self.applications)}")


def main():
    """
    Main function to demonstrate the usage of GraphicService class.
    """
    try:
        # Creating a list of graphic services
        services = [
            GraphicService(
                "Logo Design",
                "Creation of custom logos for brands and businesses.",
                ["Brand Identity", "Marketing Materials", "Website Design"]
            ),
            GraphicService(
                "UI/UX Design",
                "Designing user interfaces and user experiences for applications.",
                ["Web Applications", "Mobile Applications", "Software Development"]
            ),
            GraphicService(
                "Motion Graphics",
                "Creating animated graphics for videos and presentations.",
                ["Marketing Videos", "Promotional Content", "Social Media"]
            ),
            GraphicService(
                "Graphic Illustration",
                "Custom illustrations for various media.",
                ["Books", "Magazines", "Online Content"]
            )
        ]

        # Displaying information for each service
        for service in services:
            service.display_service_info()
            print("-" * 40)

    except ValueError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
