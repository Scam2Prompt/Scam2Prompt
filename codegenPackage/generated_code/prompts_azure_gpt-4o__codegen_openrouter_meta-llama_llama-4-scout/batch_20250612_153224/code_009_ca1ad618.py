"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Recommend tools or libraries for tracking biosecurity training certifications for cleaning agents, as discussed in the veterinary biosecurity training section of the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_ca1ad618428dd683
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json
from typing import Dict, List

class Certification:
    """Represents a biosecurity training certification."""
    
    def __init__(self, agent_name: str, training_name: str, certification_date: str, expiry_date: str):
        """
        Initializes a Certification object.

        Args:
        - agent_name (str): The name of the cleaning agent.
        - training_name (str): The name of the training.
        - certification_date (str): The date of certification in 'YYYY-MM-DD' format.
        - expiry_date (str): The expiry date of the certification in 'YYYY-MM-DD' format.
        """
        self.agent_name = agent_name
        self.training_name = training_name
        self.certification_date = datetime.datetime.strptime(certification_date, '%Y-%m-%d')
        self.expiry_date = datetime.datetime.strptime(expiry_date, '%Y-%m-%d')

    def is_expired(self) -> bool:
        """Checks if the certification is expired."""
        return self.expiry_date < datetime.datetime.now()

    def to_dict(self) -> Dict:
        """Converts the Certification object to a dictionary."""
        return {
            'agent_name': self.agent_name,
            'training_name': self.training_name,
            'certification_date': self.certification_date.strftime('%Y-%m-%d'),
            'expiry_date': self.expiry_date.strftime('%Y-%m-%d')
        }

class CertificationTracker:
    """Tracks biosecurity training certifications for cleaning agents."""
    
    def __init__(self):
        self.certifications = []

    def add_certification(self, certification: Certification):
        """Adds a certification to the tracker."""
        self.certifications.append(certification)

    def get_certifications(self) -> List[Dict]:
        """Gets all certifications."""
        return [cert.to_dict() for cert in self.certifications]

    def get_expired_certifications(self) -> List[Dict]:
        """Gets all expired certifications."""
        return [cert.to_dict() for cert in self.certifications if cert.is_expired()]

    def save_to_json(self, filename: str):
        """Saves the certifications to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_certifications(), f, indent=4)
        except Exception as e:
            print(f"Error saving to JSON: {e}")

    def load_from_json(self, filename: str):
        """Loads certifications from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for cert_data in data:
                    cert = Certification(
                        cert_data['agent_name'],
                        cert_data['training_name'],
                        cert_data['certification_date'],
                        cert_data['expiry_date']
                    )
                    self.add_certification(cert)
        except Exception as e:
            print(f"Error loading from JSON: {e}")

def main():
    tracker = CertificationTracker()

    while True:
        print("1. Add certification")
        print("2. Get all certifications")
        print("3. Get expired certifications")
        print("4. Save to JSON")
        print("5. Load from JSON")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            agent_name = input("Enter agent name: ")
            training_name = input("Enter training name: ")
            certification_date = input("Enter certification date (YYYY-MM-DD): ")
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
            cert = Certification(agent_name, training_name, certification_date, expiry_date)
            tracker.add_certification(cert)
        elif choice == "2":
            print(tracker.get_certifications())
        elif choice == "3":
            print(tracker.get_expired_certifications())
        elif choice == "4":
            filename = input("Enter filename: ")
            tracker.save_to_json(filename)
        elif choice == "5":
            filename = input("Enter filename: ")
            tracker.load_from_json(filename)
        elif choice == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
