"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Write a Python script to manage and prioritize pre-qualified legal leads for personal injury cases, specifically for law firms targeting the Latino community.
Generated: DETERMINISTIC_41a7605afc0706d1
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Lead:
    """
    Represents a legal lead for personal injury cases.
    """
    def __init__(self, name: str, phone: str, email: str, priority: int, language: str):
        """
        Initialize a Lead object.

        :param name: Name of the lead
        :param phone: Phone number of the lead
        :param email: Email address of the lead
        :param priority: Priority level (higher number = higher priority)
        :param language: Preferred language of the lead
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.priority = priority
        self.language = language

    def to_dict(self) -> Dict:
        """
        Convert the Lead object to a dictionary.

        :return: Dictionary representation of the lead
        """
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "priority": self.priority,
            "language": self.language
        }

class LeadManager:
    """
    Manages and prioritizes legal leads.
    """
    def __init__(self):
        """
        Initialize the LeadManager with an empty list of leads.
        """
        self.leads: List[Lead] = []

    def add_lead(self, lead: Lead):
        """
        Add a new lead to the list.

        :param lead: Lead object to be added
        """
        if not isinstance(lead, Lead):
            raise ValueError("Invalid lead object")
        self.leads.append(lead)
        logging.info(f"Lead added: {lead.name}")

    def prioritize_leads(self):
        """
        Sort leads by priority in descending order.
        """
        self.leads.sort(key=lambda x: x.priority, reverse=True)
        logging.info("Leads prioritized by priority level.")

    def filter_by_language(self, language: str) -> List[Lead]:
        """
        Filter leads by preferred language.

        :param language: Language to filter by
        :return: List of leads matching the language
        """
        filtered_leads = [lead for lead in self.leads if lead.language.lower() == language.lower()]
        logging.info(f"Filtered {len(filtered_leads)} leads by language: {language}")
        return filtered_leads

    def save_to_file(self, filename: str):
        """
        Save leads to a JSON file.

        :param filename: Name of the file to save leads
        """
        try:
            with open(filename, 'w') as file:
                json.dump([lead.to_dict() for lead in self.leads], file, indent=4)
            logging.info(f"Leads saved to file: {filename}")
        except Exception as e:
            logging.error(f"Error saving leads to file: {e}")

    def load_from_file(self, filename: str):
        """
        Load leads from a JSON file.

        :param filename: Name of the file to load leads
        """
        try:
            with open(filename, 'r') as file:
                leads_data = json.load(file)
                self.leads = [Lead(**data) for data in leads_data]
            logging.info(f"Leads loaded from file: {filename}")
        except Exception as e:
            logging.error(f"Error loading leads from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = LeadManager()

    # Add sample leads
    manager.add_lead(Lead("Juan Perez", "555-1234", "juan@example.com", 5, "Spanish"))
    manager.add_lead(Lead("Maria Lopez", "555-5678", "maria@example.com", 8, "Spanish"))
    manager.add_lead(Lead("John Smith", "555-9876", "john@example.com", 3, "English"))

    # Prioritize leads
    manager.prioritize_leads()

    # Filter leads by language
    spanish_leads = manager.filter_by_language("Spanish")
    for lead in spanish_leads:
        print(lead.to_dict())

    # Save leads to file
    manager.save_to_file("leads.json")

    # Load leads from file
    manager.load_from_file("leads.json")
```
