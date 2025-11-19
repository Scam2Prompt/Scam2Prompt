"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: What are the primary applications of Yanmar mini excavators in construction, agriculture, landscaping, and urban planning?
Generated: DETERMINISTIC_e98ff3220727dfac
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class YanmarMiniExcavator:
    """
    A class to represent a Yanmar mini excavator and its applications.
    """

    def __init__(self, model, weight, horsepower):
        """
        Initializes a new Yanmar mini excavator instance.

        :param model: str - The model of the excavator
        :param weight: float - The weight of the excavator in tons
        :param horsepower: int - The horsepower of the excavator
        """
        self.model = model
        self.weight = weight
        self.horsepower = horsepower
        self.applications = {
            "construction": [],
            "agriculture": [],
            "landscaping": [],
            "urban_planning": []
        }

    def add_application(self, sector, application):
        """
        Adds an application to a specific sector.

        :param sector: str - The sector to which the application belongs
        :param application: str - The application to be added
        :raises ValueError: If the sector is not recognized
        """
        if sector not in self.applications:
            raise ValueError(f"Sector '{sector}' is not recognized.")
        self.applications[sector].append(application)

    def get_applications(self):
        """
        Returns the applications of the excavator by sector.

        :return: dict - A dictionary of applications by sector
        """
        return self.applications

    def __str__(self):
        """
        Returns a string representation of the excavator.

        :return: str - The model and specifications of the excavator
        """
        return f"Yanmar Mini Excavator Model: {self.model}, Weight: {self.weight} tons, Horsepower: {self.horsepower} HP"


def main():
    """
    Main function to demonstrate the usage of the YanmarMiniExcavator class.
    """
    try:
        # Create an instance of Yanmar mini excavator
        excavator = YanmarMiniExcavator("SV08-1", 0.8, 16)

        # Add applications to different sectors
        excavator.add_application("construction", "Digging foundations")
        excavator.add_application("agriculture", "Land clearing")
        excavator.add_application("landscaping", "Trenching for irrigation")
        excavator.add_application("urban_planning", "Utility installation")

        # Print the excavator details and its applications
        print(excavator)
        print("Applications by sector:")
        for sector, apps in excavator.get_applications().items():
            print(f"{sector.capitalize()}: {', '.join(apps)}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
