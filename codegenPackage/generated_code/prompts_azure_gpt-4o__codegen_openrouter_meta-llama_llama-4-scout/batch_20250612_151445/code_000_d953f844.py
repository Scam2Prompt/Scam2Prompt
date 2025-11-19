"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: Generate Python code to automate the creation of a chain of custody form for environmental sample testing, referencing A & B Labs' analytical service guide.
Generated: DETERMINISTIC_d953f84425452ba7
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chain_of_custody.py

import datetime
from typing import List

class Sample:
    def __init__(self, sample_id: str, sample_type: str, location: str):
        """
        Represents an environmental sample.

        Args:
            sample_id (str): Unique identifier for the sample.
            sample_type (str): Type of environmental sample (e.g., water, soil, air).
            location (str): Location where the sample was collected.
        """
        self.sample_id = sample_id
        self.sample_type = sample_type
        self.location = location

class ChainOfCustody:
    def __init__(self, lab_name: str = "A & B Labs"):
        """
        Represents a chain of custody form.

        Args:
            lab_name (str): Name of the laboratory (default: A & B Labs).
        """
        self.lab_name = lab_name
        self.samples = []
        self.handlers = []

    def add_sample(self, sample: Sample):
        """
        Adds a sample to the chain of custody.

        Args:
            sample (Sample): Sample to add.
        """
        self.samples.append(sample)

    def add_handler(self, handler: str):
        """
        Adds a handler to the chain of custody.

        Args:
            handler (str): Name of the handler.
        """
        self.handlers.append(handler)

    def generate_form(self) -> str:
        """
        Generates the chain of custody form.

        Returns:
            str: Chain of custody form as a string.
        """
        form = f"{self.lab_name} Chain of Custody Form\n"
        form += "-----------------------------------------\n"
        form += f"Date: {datetime.date.today().strftime('%Y-%m-%d')}\n"
        form += "\n"

        form += "Sample Information:\n"
        for i, sample in enumerate(self.samples, start=1):
            form += f"Sample {i}:\n"
            form += f"  Sample ID: {sample.sample_id}\n"
            form += f"  Sample Type: {sample.sample_type}\n"
            form += f"  Location: {sample.location}\n"
            form += "\n"

        form += "Chain of Custody:\n"
        for i, handler in enumerate(self.handlers, start=1):
            form += f"{i}. {handler}\n"

        form += "\n"
        form += "Analytical Service Guide Reference:\n"
        form += "A & B Labs' Analytical Service Guide\n"

        return form

def main():
    try:
        # Create samples
        sample1 = Sample("SAMPLE-001", "Water", "River A")
        sample2 = Sample("SAMPLE-002", "Soil", "Site B")

        # Create chain of custody
        coc = ChainOfCustody()
        coc.add_sample(sample1)
        coc.add_sample(sample2)
        coc.add_handler("John Doe")
        coc.add_handler("Jane Smith")

        # Generate form
        form = coc.generate_form()
        print(form)

        # Save form to file
        with open("chain_of_custody.txt", "w") as f:
            f.write(form)

        print("Chain of custody form saved to chain_of_custody.txt")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
