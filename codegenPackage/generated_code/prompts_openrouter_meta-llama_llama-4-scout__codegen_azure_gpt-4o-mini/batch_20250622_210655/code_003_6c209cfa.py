"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Develop a system for managing agricultural certifications, including tracking and reporting, using a B2B platform similar to Azagros.
Generated: DETERMINISTIC_6c209cfac4929188
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agricultural_certification_manager.py

import json
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Certification:
    """Class to represent an agricultural certification."""
    
    def __init__(self, cert_id: str, name: str, issued_to: str, issue_date: str, expiry_date: str):
        self.cert_id = cert_id
        self.name = name
        self.issued_to = issued_to
        self.issue_date = issue_date
        self.expiry_date = expiry_date

    def to_dict(self) -> Dict:
        """Convert Certification object to dictionary."""
        return {
            "cert_id": self.cert_id,
            "name": self.name,
            "issued_to": self.issued_to,
            "issue_date": self.issue_date,
            "expiry_date": self.expiry_date
        }

class CertificationManager:
    """Class to manage agricultural certifications."""
    
    def __init__(self):
        self.certifications: List[Certification] = []

    def add_certification(self, cert: Certification) -> None:
        """Add a new certification to the manager."""
        self.certifications.append(cert)
        logging.info(f"Certification added: {cert.to_dict()}")

    def remove_certification(self, cert_id: str) -> bool:
        """Remove a certification by its ID."""
        for cert in self.certifications:
            if cert.cert_id == cert_id:
                self.certifications.remove(cert)
                logging.info(f"Certification removed: {cert_id}")
                return True
        logging.warning(f"Certification not found: {cert_id}")
        return False

    def get_certification(self, cert_id: str) -> Optional[Certification]:
        """Retrieve a certification by its ID."""
        for cert in self.certifications:
            if cert.cert_id == cert_id:
                logging.info(f"Certification retrieved: {cert.to_dict()}")
                return cert
        logging.warning(f"Certification not found: {cert_id}")
        return None

    def list_certifications(self) -> List[Dict]:
        """List all certifications."""
        return [cert.to_dict() for cert in self.certifications]

    def save_to_file(self, filename: str) -> None:
        """Save certifications to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([cert.to_dict() for cert in self.certifications], file, indent=4)
            logging.info(f"Certifications saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load certifications from a JSON file."""
        try:
            with open(filename, 'r') as file:
                certs_data = json.load(file)
                for cert_data in certs_data:
                    cert = Certification(**cert_data)
                    self.add_certification(cert)
            logging.info(f"Certifications loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = CertificationManager()
    
    # Adding certifications
    cert1 = Certification("001", "Organic Certification", "Farm A", "2023-01-01", "2024-01-01")
    manager.add_certification(cert1)

    cert2 = Certification("002", "Fair Trade Certification", "Farm B", "2023-02-01", "2024-02-01")
    manager.add_certification(cert2)

    # Listing certifications
    print(manager.list_certifications())

    # Saving to file
    manager.save_to_file("certifications.json")

    # Loading from file
    manager.load_from_file("certifications.json")
```
