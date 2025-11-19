"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write code to implement a pre-workshop module for parents of adolescents undergoing DBT therapy, as described in the FAQs section of the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_26b115fe76a3bcf3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pre_workshop_module.py

import json
from typing import List, Dict, Any

class PreWorkshopModule:
    """
    A class to represent a pre-workshop module for parents of adolescents undergoing DBT therapy.
    """

    def __init__(self, workshop_title: str, faqs: List[Dict[str, str]]):
        """
        Initializes the PreWorkshopModule with a title and a list of FAQs.

        Args:
            workshop_title (str): The title of the workshop.
            faqs (List[Dict[str, str]]): A list of FAQs where each FAQ is a dictionary with 'question' and 'answer'.
        """
        self.workshop_title = workshop_title
        self.faqs = faqs

    def add_faq(self, question: str, answer: str) -> None:
        """
        Adds a new FAQ to the module.

        Args:
            question (str): The question to be added.
            answer (str): The answer to the question.

        Raises:
            ValueError: If the question or answer is empty.
        """
        if not question or not answer:
            raise ValueError("Question and answer cannot be empty.")
        
        self.faqs.append({"question": question, "answer": answer})

    def remove_faq(self, question: str) -> None:
        """
        Removes an FAQ from the module by question.

        Args:
            question (str): The question of the FAQ to be removed.

        Raises:
            ValueError: If the question is not found in the FAQs.
        """
        for faq in self.faqs:
            if faq['question'] == question:
                self.faqs.remove(faq)
                return
        raise ValueError("Question not found in FAQs.")

    def get_faqs(self) -> List[Dict[str, str]]:
        """
        Returns the list of FAQs.

        Returns:
            List[Dict[str, str]]: The list of FAQs.
        """
        return self.faqs

    def save_to_file(self, filename: str) -> None:
        """
        Saves the workshop module data to a JSON file.

        Args:
            filename (str): The name of the file to save the data.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "workshop_title": self.workshop_title,
                    "faqs": self.faqs
                }, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'PreWorkshopModule':
        """
        Loads the workshop module data from a JSON file.

        Args:
            filename (str): The name of the file to load the data from.

        Returns:
            PreWorkshopModule: An instance of PreWorkshopModule with loaded data.

        Raises:
            IOError: If there is an error reading the file.
            ValueError: If the file does not contain valid data.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return cls(data['workshop_title'], data['faqs'])
        except IOError as e:
            raise IOError(f"An error occurred while reading the file: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid data in file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a pre-workshop module instance
    faqs = [
        {"question": "What is DBT?", "answer": "Dialectical Behavior Therapy is a type of cognitive-behavioral therapy."},
        {"question": "How can I support my child?", "answer": "Be present, listen actively, and encourage open communication."}
    ]
    
    module = PreWorkshopModule("DBT for Parents Workshop", faqs)
    
    # Add a new FAQ
    module.add_faq("What should I expect during the workshop?", "You will learn strategies to support your child.")
    
    # Save the module to a file
    module.save_to_file("pre_workshop_module.json")
    
    # Load the module from a file
    loaded_module = PreWorkshopModule.load_from_file("pre_workshop_module.json")
    print(loaded_module.get_faqs())
```
