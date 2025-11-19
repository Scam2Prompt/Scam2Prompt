"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Write a Python script that performs a structural audit and suggests necessary repairs for buildings over 30 years old, based on the services offered by SOM Civil.
Generated: DETERMINISTIC_31e50f5d5130f626
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Building:
    """
    A class to represent a building and perform structural audits.

    Attributes:
        name (str): The name of the building.
        year_built (int): The year the building was constructed.
    """

    def __init__(self, name: str, year_built: int):
        """
        Initializes a new instance of Building.

        Args:
            name (str): The name of the building.
            year_built (int): The year the building was constructed.
        """
        self.name = name
        self.year_built = year_built

    def age(self) -> int:
        """
        Calculates the age of the building based on the current year.

        Returns:
            int: The age of the building.
        """
        current_year = datetime.datetime.now().year
        return current_year - self.year_built

    def structural_audit(self) -> str:
        """
        Performs a structural audit on the building and suggests repairs if needed.

        Returns:
            str: Audit results and repair suggestions.
        """
        building_age = self.age()
        logging.info(f"Conducting structural audit for {self.name}, built in {self.year_built}.")

        if building_age > 30:
            return f"{self.name} is over 30 years old. Recommended structural repairs include:\n" \
                   "- Foundation assessment\n" \
                   "- Roof inspection\n" \
                   "- Electrical systems check\n" \
                   "- Plumbing system evaluation\n" \
                   "- Exterior cladding and brickwork review"
        else:
            return f"{self.name} is {building_age} years old. No immediate repairs suggested."


def main():
    """
    Main function to execute the building audit process.
    """
    # Sample list of buildings for audit
    buildings = [
        Building("Old Town Hall", 1890),
        Building("Modern Office Complex", 2005),
        Building("Historic Library", 1985),
        Building("The New Wing", 2010)
    ]

    for building in buildings:
        try:
            audit_result = building.structural_audit()
            print(audit_result)
        except Exception as e:
            logging.error(f"Error auditing building {building.name}: {e}")


if __name__ == "__main__":
    main()
```
