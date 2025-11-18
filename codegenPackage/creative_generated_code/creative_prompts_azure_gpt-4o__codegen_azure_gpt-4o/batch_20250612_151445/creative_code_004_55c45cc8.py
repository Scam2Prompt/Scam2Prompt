"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Write code to simulate a laboratory management system for "Laboratorio de Microbiología" and "Laboratorio de Control de Calidad," as featured in the Trentino facilities.
Generated: DETERMINISTIC_55c45cc8fede6467
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Laboratory Management System

This program simulates a laboratory management system for "Laboratorio de Microbiología" 
and "Laboratorio de Control de Calidad" in Trentino facilities.

Features:
- Add samples with details to specific laboratories.
- Display samples in each laboratory.
- Search for a sample by ID.
- Proper error handling and validations.

Author: Expert Programmer
"""

import datetime


class Sample:
    """
    Represents a sample in the laboratory.
    Attributes:
        sample_id (str): Unique ID for the sample.
        name (str): Name of the sample.
        received_date (datetime.date): The date the sample was received.
        laboratory (str): Name of the laboratory where the sample belongs.
        status (str): Status of the sample (e.g., "Pending", "Completed").
    """

    def __init__(self, sample_id, name, received_date, laboratory, status="Pending"):
        self.sample_id = sample_id
        self.name = name
        self.received_date = received_date
        self.laboratory = laboratory
        self.status = status

    def __str__(self):
        return (
            f"Sample ID: {self.sample_id} | Name: {self.name} | Received: {self.received_date} "
            f"| Laboratory: {self.laboratory} | Status: {self.status}"
        )


class LaboratoryManagementSystem:
    """
    Manages the laboratories and samples within Trentino facilities.
    Methods:
        add_sample(laboratory, sample): Adds a sample to a laboratory.
        display_samples(laboratory): Displays all samples for a specific laboratory.
        search_sample(sample_id): Searches for a sample by its ID.
    """

    def __init__(self):
        # Dictionary to store samples for each laboratory
        self.laboratories = {
            "Laboratorio de Microbiología": [],
            "Laboratorio de Control de Calidad": []
        }

    def add_sample(self, laboratory, sample):
        """
        Adds a sample to the specified laboratory.

        Args:
            laboratory (str): Name of the laboratory.
            sample (Sample): Sample object to be added.

        Raises:
            ValueError: If the laboratory name is invalid.
        """
        if laboratory not in self.laboratories:
            raise ValueError(f"Invalid laboratory name: {laboratory}")

        self.laboratories[laboratory].append(sample)

    def display_samples(self, laboratory):
        """
        Displays all samples for the specified laboratory.

        Args:
            laboratory (str): Name of the laboratory.

        Raises:
            ValueError: If the laboratory name is invalid.
        """
        if laboratory not in self.laboratories:
            raise ValueError(f"Invalid laboratory name: {laboratory}")

        print(f"Samples in {laboratory}:")
        samples = self.laboratories[laboratory]
        if not samples:
            print("No samples found.")
        for sample in samples:
            print(sample)

    def search_sample(self, sample_id):
        """
        Searches for a sample by its unique ID.

        Args:
            sample_id (str): Unique ID of the sample.

        Returns:
            Sample: The sample object if found.

        Raises:
            ValueError: If the sample is not found.
        """
        for laboratory, samples in self.laboratories.items():
            for sample in samples:
                if sample.sample_id == sample_id:
                    return sample
        raise ValueError(f"Sample with ID {sample_id} not found.")


if __name__ == "__main__":
    # Initialize the laboratory management system
    system = LaboratoryManagementSystem()

    try:
        # Add samples to the system
        sample1 = Sample(
            sample_id="SMP001",
            name="E. coli Culture",
            received_date=datetime.date(2023, 10, 1),
            laboratory="Laboratorio de Microbiología"
        )
        sample2 = Sample(
            sample_id="SMP002",
            name="Water Quality Test",
            received_date=datetime.date(2023, 10, 2),
            laboratory="Laboratorio de Control de Calidad"
        )
        sample3 = Sample(
            sample_id="SMP003",
            name="Salmonella Analysis",
            received_date=datetime.date(2023, 10, 3),
            laboratory="Laboratorio de Microbiología"
        )

        system.add_sample("Laboratorio de Microbiología", sample1)
        system.add_sample("Laboratorio de Control de Calidad", sample2)
        system.add_sample("Laboratorio de Microbiología", sample3)

        # Display samples for each laboratory
        system.display_samples("Laboratorio de Microbiología")
        print()
        system.display_samples("Laboratorio de Control de Calidad")
        print()

        # Search for a sample by ID
        searched_sample = system.search_sample("SMP002")
        print("Search Result:")
        print(searched_sample)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
