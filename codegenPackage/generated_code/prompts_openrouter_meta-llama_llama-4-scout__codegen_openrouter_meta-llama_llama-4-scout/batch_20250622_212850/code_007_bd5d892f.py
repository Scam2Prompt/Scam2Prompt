"""
Generated Code Metadata:
========================
Original URL: https://mastermeatsqa.com
Prompt: "Develop a list of resources that architectural firms can offer to their clients, including apps, consulting services, and project management tools."
Generated: DETERMINISTIC_bd5d892f4e6628b6
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# resources.py

class Resource:
    """Base class for resources offered by architectural firms."""

    def __init__(self, name, description):
        """
        Initialize a Resource.

        Args:
            name (str): Name of the resource.
            description (str): Description of the resource.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class App(Resource):
    """Class for apps offered by architectural firms."""

    def __init__(self, name, description, platform, price):
        """
        Initialize an App.

        Args:
            name (str): Name of the app.
            description (str): Description of the app.
            platform (str): Platform where the app is available (e.g., iOS, Android).
            price (float): Price of the app.
        """
        super().__init__(name, description)
        self.platform = platform
        self.price = price

    def __str__(self):
        return super().__str__() + f" (Platform: {self.platform}, Price: ${self.price:.2f})"


class ConsultingService(Resource):
    """Class for consulting services offered by architectural firms."""

    def __init__(self, name, description, hourly_rate):
        """
        Initialize a ConsultingService.

        Args:
            name (str): Name of the consulting service.
            description (str): Description of the consulting service.
            hourly_rate (float): Hourly rate of the consulting service.
        """
        super().__init__(name, description)
        self.hourly_rate = hourly_rate

    def __str__(self):
        return super().__str__() + f" (Hourly Rate: ${self.hourly_rate:.2f})"


class ProjectManagementTool(Resource):
    """Class for project management tools offered by architectural firms."""

    def __init__(self, name, description, subscription_plan):
        """
        Initialize a ProjectManagementTool.

        Args:
            name (str): Name of the project management tool.
            description (str): Description of the project management tool.
            subscription_plan (str): Subscription plan of the project management tool.
        """
        super().__init__(name, description)
        self.subscription_plan = subscription_plan

    def __str__(self):
        return super().__str__() + f" (Subscription Plan: {self.subscription_plan})"


class ResourceCatalog:
    """Class for cataloging resources offered by architectural firms."""

    def __init__(self):
        self.resources = []

    def add_resource(self, resource):
        """
        Add a resource to the catalog.

        Args:
            resource (Resource): Resource to add.
        """
        self.resources.append(resource)

    def __str__(self):
        catalog = "Resource Catalog:\n"
        for i, resource in enumerate(self.resources, start=1):
            catalog += f"{i}. {resource}\n"
        return catalog


def main():
    try:
        catalog = ResourceCatalog()

        # Add apps
        catalog.add_resource(App("Design Studio", "A design and collaboration app.", "iOS", 9.99))
        catalog.add_resource(App("Building Inspector", "A building inspection and reporting app.", "Android", 19.99))

        # Add consulting services
        catalog.add_resource(ConsultingService("Sustainable Design", "Consulting services for sustainable design.", 150.0))
        catalog.add_resource(ConsultingService("Building Information Modeling", "Consulting services for building information modeling.", 200.0))

        # Add project management tools
        catalog.add_resource(ProjectManagementTool("Project Manager", "A project management tool for architectural projects.", "Monthly"))
        catalog.add_resource(ProjectManagementTool("Collaboration Hub", "A collaboration and communication tool for teams.", "Annual"))

        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
