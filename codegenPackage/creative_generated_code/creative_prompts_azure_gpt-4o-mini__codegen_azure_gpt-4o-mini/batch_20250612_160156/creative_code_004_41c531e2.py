"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nebulawealth-ai-software.com
Prompt: How does Nebula Wealth AI enhance financial literacy through its educational programs and workshops for new investors?
Generated: DETERMINISTIC_41c531e24c2a4861
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FinancialLiteracyProgram:
    """
    A class to represent a financial literacy program offered by Nebula Wealth AI.
    This program includes educational resources and workshops aimed at new investors.
    """

    def __init__(self):
        """
        Initializes the FinancialLiteracyProgram with an empty list of resources and workshops.
        """
        self.resources = []  # List to store educational resources
        self.workshops = []   # List to store workshops

    def add_resource(self, resource_name: str, resource_type: str) -> None:
        """
        Adds an educational resource to the program.

        :param resource_name: The name of the educational resource
        :param resource_type: The type of the resource (e.g., 'article', 'video', 'webinar')
        :raises ValueError: If resource_name or resource_type is empty
        """
        if not resource_name or not resource_type:
            raise ValueError("Resource name and type cannot be empty.")

        resource = {
            "name": resource_name,
            "type": resource_type
        }
        self.resources.append(resource)

    def add_workshop(self, workshop_name: str, date: str) -> None:
        """
        Adds a workshop to the program.

        :param workshop_name: The name of the workshop
        :param date: The date of the workshop in 'YYYY-MM-DD' format
        :raises ValueError: If workshop_name or date is empty
        """
        if not workshop_name or not date:
            raise ValueError("Workshop name and date cannot be empty.")

        workshop = {
            "name": workshop_name,
            "date": date
        }
        self.workshops.append(workshop)

    def list_resources(self) -> list:
        """
        Returns a list of all educational resources.

        :return: List of resources
        """
        return self.resources

    def list_workshops(self) -> list:
        """
        Returns a list of all workshops.

        :return: List of workshops
        """
        return self.workshops

    def find_resource(self, resource_name: str) -> dict:
        """
        Finds a resource by its name.

        :param resource_name: The name of the resource to find
        :return: The resource if found, else None
        """
        for resource in self.resources:
            if resource["name"].lower() == resource_name.lower():
                return resource
        return None

    def find_workshop(self, workshop_name: str) -> dict:
        """
        Finds a workshop by its name.

        :param workshop_name: The name of the workshop to find
        :return: The workshop if found, else None
        """
        for workshop in self.workshops:
            if workshop["name"].lower() == workshop_name.lower():
                return workshop
        return None


def main():
    """
    Main function to demonstrate the FinancialLiteracyProgram functionality.
    """
    try:
        program = FinancialLiteracyProgram()
        
        # Adding resources
        program.add_resource("Investing Basics", "article")
        program.add_resource("Understanding Stocks", "video")
        
        # Adding workshops
        program.add_workshop("Introduction to Investment", "2023-11-15")
        program.add_workshop("Advanced Portfolio Management", "2023-12-01")
        
        # Listing resources and workshops
        print("Educational Resources:")
        for resource in program.list_resources():
            print(f"- {resource['name']} ({resource['type']})")

        print("\nWorkshops:")
        for workshop in program.list_workshops():
            print(f"- {workshop['name']} on {workshop['date']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
