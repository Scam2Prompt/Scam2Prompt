"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: What are the unique features of Independence Fire Sprinkler Company's services that differentiate them from other fire protection providers?
Generated: DETERMINISTIC_70816781655fc20a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FireSprinklerCompany:
    """
    A class to represent a fire sprinkler company and its services.
    """

    def __init__(self, name):
        """
        Initializes the fire sprinkler company with a name and an empty list of services.
        
        :param name: The name of the fire sprinkler company.
        """
        self.name = name
        self.services = []

    def add_service(self, service_name, description):
        """
        Adds a unique service to the company's offerings.
        
        :param service_name: The name of the service.
        :param description: A brief description of the service.
        """
        if any(s['name'] == service_name for s in self.services):
            raise ValueError(f"Service '{service_name}' already exists.")
        
        self.services.append({'name': service_name, 'description': description})

    def get_services(self):
        """
        Returns a list of all services offered by the company.
        
        :return: A list of dictionaries containing service names and descriptions.
        """
        return self.services

    def unique_features(self):
        """
        Returns unique features that differentiate the company from other providers.
        
        :return: A list of unique features.
        """
        features = [
            "24/7 Emergency Response",
            "Custom Design and Installation",
            "Advanced Monitoring Systems",
            "Comprehensive Maintenance Plans",
            "Trained and Certified Technicians"
        ]
        return features

    def display_info(self):
        """
        Displays the company's name, services, and unique features.
        """
        print(f"Company Name: {self.name}")
        print("\nServices Offered:")
        for service in self.get_services():
            print(f"- {service['name']}: {service['description']}")
        
        print("\nUnique Features:")
        for feature in self.unique_features():
            print(f"- {feature}")

# Example usage
if __name__ == "__main__":
    try:
        company = FireSprinklerCompany("Independence Fire Sprinkler Company")
        company.add_service("Installation", "Professional installation of fire sprinkler systems.")
        company.add_service("Inspection", "Regular inspections to ensure compliance and safety.")
        
        # Display company information
        company.display_info()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
