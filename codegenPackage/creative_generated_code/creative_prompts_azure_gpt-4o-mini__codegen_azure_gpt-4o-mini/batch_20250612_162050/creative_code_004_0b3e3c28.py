"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rimedyahotel.com
Prompt: Illustrate how to implement a secure tourism certification check within a hotel management system using the Grand Rimedya hotel as a case study.
Generated: DETERMINISTIC_0b3e3c28bca37e6d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from datetime import datetime
from werkzeug.exceptions import BadRequest

class Certification:
    """Class to represent a tourism certification for a hotel."""
    
    def __init__(self, hotel_name, cert_id, issued_date, expiration_date):
        self.hotel_name = hotel_name
        self.cert_id = cert_id
        self.issued_date = issued_date  # Format: YYYY-MM-DD
        self.expiration_date = expiration_date  # Format: YYYY-MM-DD

    def is_valid(self):
        """Check if the certification is currently valid."""
        today = datetime.now().date()
        return today >= datetime.strptime(self.issued_date, '%Y-%m-%d').date() and \
               today <= datetime.strptime(self.expiration_date, '%Y-%m-%d').date()

    def to_dict(self):
        """Convert certification details to a dictionary."""
        return {
            'hotel_name': self.hotel_name,
            'cert_id': self.cert_id,
            'issued_date': self.issued_date,
            'expiration_date': self.expiration_date,
            'valid': self.is_valid()
        }

class CertificationManager:
    """Class to manage tourism certifications."""
    
    def __init__(self):
        self.certifications = {}

    def add_certification(self, cert: Certification):
        """Add a new certification to the system."""
        if cert.cert_id in self.certifications:
            raise ValueError("Certification ID already exists.")
        self.certifications[cert.cert_id] = cert

    def check_certification(self, cert_id):
        """Check if a certification is valid based on its ID."""
        if cert_id not in self.certifications:
            raise KeyError("Certification not found.")
        return self.certifications[cert_id].is_valid()

    def get_certification_details(self, cert_id):
        """Retrieve certification details if it exists."""
        if cert_id not in self.certifications:
            raise KeyError("Certification not found.")
        return self.certifications[cert_id].to_dict()

def main():
    """Main function to demonstrate certification checking."""
    manager = CertificationManager()

    # Example certification for Grand Rimedya Hotel
    grand_rimedya_cert = Certification(
        hotel_name="Grand Rimedya",
        cert_id="GR2023-001",
        issued_date="2023-01-01",
        expiration_date="2024-01-01"
    )

    try:
        # Add certification to the manager
        manager.add_certification(grand_rimedya_cert)
        
        # Check if the certification is valid
        cert_id = "GR2023-001"
        is_valid = manager.check_certification(cert_id)
        print(f"Certification {cert_id} valid: {is_valid}")

        # Get certification details
        cert_details = manager.get_certification_details(cert_id)
        print(json.dumps(cert_details, indent=4))

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
