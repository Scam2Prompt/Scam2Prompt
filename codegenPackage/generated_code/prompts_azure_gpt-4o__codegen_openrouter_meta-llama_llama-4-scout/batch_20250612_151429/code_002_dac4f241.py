"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: Generate code for preclinical research involving animal handling, aligning with DBCOP's Animal Handling & Preclinical Research Certificate Course.
Generated: DETERMINISTIC_dac4f2415c6519f1
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# animal_research.py

"""
Module for managing preclinical research involving animal handling.

Aligns with DBCOP's Animal Handling & Preclinical Research Certificate Course.
"""

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Animal:
    """
    Represents an animal in the preclinical research.

    Attributes:
        id (int): Unique identifier for the animal.
        species (str): Species of the animal (e.g., mouse, rat, rabbit).
        strain (str): Strain of the animal (if applicable).
        age (int): Age of the animal in weeks.
        weight (float): Weight of the animal in grams.
    """

    def __init__(self, id, species, strain=None, age=None, weight=None):
        """
        Initializes an Animal object.

        Args:
            id (int): Unique identifier for the animal.
            species (str): Species of the animal.
            strain (str, optional): Strain of the animal. Defaults to None.
            age (int, optional): Age of the animal in weeks. Defaults to None.
            weight (float, optional): Weight of the animal in grams. Defaults to None.
        """
        self.id = id
        self.species = species
        self.strain = strain
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"Animal ID: {self.id}, Species: {self.species}, Strain: {self.strain}, Age: {self.age} weeks, Weight: {self.weight} grams"


class ResearchStudy:
    """
    Represents a preclinical research study involving animal handling.

    Attributes:
        id (int): Unique identifier for the study.
        title (str): Title of the study.
        description (str): Brief description of the study.
        animals (list[Animal]): List of animals involved in the study.
        start_date (datetime.date): Start date of the study.
        end_date (datetime.date): End date of the study.
    """

    def __init__(self, id, title, description, start_date, end_date):
        """
        Initializes a ResearchStudy object.

        Args:
            id (int): Unique identifier for the study.
            title (str): Title of the study.
            description (str): Brief description of the study.
            start_date (datetime.date): Start date of the study.
            end_date (datetime.date): End date of the study.
        """
        self.id = id
        self.title = title
        self.description = description
        self.animals = []
        self.start_date = start_date
        self.end_date = end_date

    def add_animal(self, animal):
        """
        Adds an animal to the study.

        Args:
            animal (Animal): Animal to add.

        Raises:
            ValueError: If the animal is already in the study.
        """
        if animal in self.animals:
            raise ValueError("Animal is already in the study")
        self.animals.append(animal)

    def remove_animal(self, animal_id):
        """
        Removes an animal from the study.

        Args:
            animal_id (int): ID of the animal to remove.

        Raises:
            ValueError: If the animal is not in the study.
        """
        for animal in self.animals:
            if animal.id == animal_id:
                self.animals.remove(animal)
                return
        raise ValueError("Animal not found in the study")

    def __str__(self):
        study_info = f"Study ID: {self.id}, Title: {self.title}, Description: {self.description}, Start Date: {self.start_date}, End Date: {self.end_date}\n"
        animals_info = "\n".join([str(animal) for animal in self.animals])
        return study_info + animals_info


def main():
    try:
        # Create animals
        animal1 = Animal(1, "mouse", "C57BL/6", 10, 20.5)
        animal2 = Animal(2, "rat", "Sprague-Dawley", 12, 300.0)

        # Create research study
        study = ResearchStudy(1, "Example Study", "This is an example study", datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

        # Add animals to study
        study.add_animal(animal1)
        study.add_animal(animal2)

        # Print study information
        logging.info(study)

        # Remove animal from study
        study.remove_animal(1)

        # Print updated study information
        logging.info(study)

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
