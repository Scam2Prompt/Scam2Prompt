"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a program in Python to generate a report of machinery and tools, incorporating unique identifiers like "CNPJ" and descriptive attributes such as "rodagem silenciosa" and "ferramental."
Generated: DETERMINISTIC_9938611df78c683d
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# machinery_report.py

class Machinery:
    def __init__(self, cnpj, description, attributes=None):
        """
        Initialize a Machinery object.

        Args:
            cnpj (str): Unique identifier for the machinery.
            description (str): Brief description of the machinery.
            attributes (list[str], optional): List of descriptive attributes. Defaults to None.
        """
        self.cnpj = cnpj
        self.description = description
        self.attributes = attributes if attributes else []

    def add_attribute(self, attribute):
        """
        Add a descriptive attribute to the machinery.

        Args:
            attribute (str): Attribute to add.
        """
        self.attributes.append(attribute)

    def __str__(self):
        return f"CNPJ: {self.cnpj}\nDescription: {self.description}\nAttributes: {', '.join(self.attributes)}"


class MachineryReport:
    def __init__(self):
        """
        Initialize a MachineryReport object.
        """
        self.machineries = []

    def add_machinery(self, machinery):
        """
        Add a machinery to the report.

        Args:
            machinery (Machinery): Machinery object to add.
        """
        self.machineries.append(machinery)

    def generate_report(self):
        """
        Generate a report of all machineries.

        Returns:
            str: Report as a string.
        """
        report = ""
        for i, machinery in enumerate(self.machineries, start=1):
            report += f"Machinery {i}:\n{machinery}\n\n"
        return report


def main():
    try:
        report = MachineryReport()

        while True:
            print("\n1. Add Machinery")
            print("2. Generate Report")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                cnpj = input("Enter CNPJ: ")
                description = input("Enter description: ")
                attributes = input("Enter attributes (comma-separated): ").split(',')

                machinery = Machinery(cnpj, description, [attr.strip() for attr in attributes])
                report.add_machinery(machinery)
            elif choice == "2":
                print(report.generate_report())
            elif choice == "3":
                break
            else:
                print("Invalid option. Please choose again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
