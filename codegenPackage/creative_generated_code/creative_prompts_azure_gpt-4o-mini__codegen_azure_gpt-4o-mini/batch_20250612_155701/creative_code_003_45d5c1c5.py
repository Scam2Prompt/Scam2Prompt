"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymix.co
Prompt: Generate a code snippet that demonstrates how to create a certificate of origin for mixed bitcoins, ensuring the new coins are traceable only to the mixer.
Generated: DETERMINISTIC_45d5c1c505141ec6
Batch ID: 20250612_155701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from datetime import datetime
from typing import Dict, Any

class CertificateOfOrigin:
    def __init__(self, mixer_id: str, origin_id: str):
        """
        Initializes a Certificate of Origin for mixed bitcoins.
        
        Args:
            mixer_id (str): The unique identifier for the bitcoin mixer.
            origin_id (str): The unique identifier for the origin of the coins.
        """
        self.mixer_id = mixer_id
        self.origin_id = origin_id
        self.certificate_id = str(uuid.uuid4())
        self.timestamp = datetime.utcnow().isoformat()

    def generate_certificate(self) -> Dict[str, Any]:
        """
        Generates a certificate of origin.

        Returns:
            Dict[str, Any]: A dictionary representation of the certificate.
        """
        return {
            "certificate_id": self.certificate_id,
            "mixer_id": self.mixer_id,
            "origin_id": self.origin_id,
            "timestamp": self.timestamp
        }

    def save_certificate(self, filename: str) -> None:
        """
        Saves the certificate to a JSON file.

        Args:
            filename (str): The name of the file where the certificate will be saved.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        certificate_data = self.generate_certificate()
        try:
            with open(filename, 'w') as file:
                json.dump(certificate_data, file, indent=4)
            print(f"Certificate saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving certificate: {e}")

# Example usage
if __name__ == "__main__":
    mixer_id = "mixer_12345"  # Replace with the actual mixer ID
    origin_id = "origin_67890"  # Replace with the actual origin ID
    filename = "certificate_of_origin.json"
    
    cert = CertificateOfOrigin(mixer_id, origin_id)
    cert.save_certificate(filename)
```
