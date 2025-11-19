"""
Generated Code Metadata:
========================
Original URL: https://newparadigm.manta.technology
Prompt: Generate a code snippet that demonstrates the use of Manta for data privacy compliance.
Generated: DETERMINISTIC_8651590d1175c520
Batch ID: 20250622_212533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from manta import MantaClient
from manta.exceptions import MantaError

class DataPrivacyCompliance:
    """
    Demonstrates the use of Manta for data privacy compliance.
    Handles sensitive data with proper encryption and access controls.
    """

    def __init__(self, api_key=None):
        """
        Initialize Manta client with API key.
        Defaults to environment variable if no key provided.
        """
        self.api_key = api_key or os.getenv('MANTA_API_KEY')
        if not self.api_key:
            raise ValueError("Manta API key not provided and MANTA_API_KEY environment variable not set")
        
        try:
            self.client = MantaClient(api_key=self.api_key)
        except MantaError as e:
            raise RuntimeError(f"Failed to initialize Manta client: {str(e)}")

    def anonymize_data(self, data, fields_to_anonymize):
        """
        Anonymize sensitive fields in the provided data.
        
        Args:
            data: Dictionary containing the data to process
            fields_to_anonymize: List of field names to anonymize
            
        Returns:
            Dictionary with anonymized data
            
        Raises:
            MantaError: If anonymization fails
        """
        try:
            return self.client.anonymize(
                data=data,
                fields=fields_to_anonymize,
                method='pseudonymization'
            )
        except MantaError as e:
            raise MantaError(f"Data anonymization failed: {str(e)}")

    def check_compliance(self, data, regulation='gdpr'):
        """
        Check if data complies with specified privacy regulation.
        
        Args:
            data: Dictionary containing the data to check
            regulation: Privacy regulation to check against (default: 'gdpr')
            
        Returns:
            Dictionary with compliance results
            
        Raises:
            MantaError: If compliance check fails
        """
        try:
            return self.client.compliance_check(
                data=data,
                regulation=regulation
            )
        except MantaError as e:
            raise MantaError(f"Compliance check failed: {str(e)}")

    def generate_consent_record(self, user_id, purposes):
        """
        Generate a consent record for a user.
        
        Args:
            user_id: Unique identifier for the user
            purposes: List of purposes the user has consented to
            
        Returns:
            Dictionary with consent record details
            
        Raises:
            MantaError: If record generation fails
        """
        try:
            return self.client.create_consent(
                user_id=user_id,
                purposes=purposes
            )
        except MantaError as e:
            raise MantaError(f"Consent record creation failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with API key from environment
        privacy = DataPrivacyCompliance()
        
        # Example data to process
        user_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "ssn": "123-45-6789"
        }
        
        # Anonymize sensitive fields
        anonymized_data = privacy.anonymize_data(
            data=user_data,
            fields_to_anonymize=["email", "ssn"]
        )
        print("Anonymized data:", anonymized_data)
        
        # Check GDPR compliance
        compliance_result = privacy.check_compliance(
            data=user_data,
            regulation='gdpr'
        )
        print("Compliance result:", compliance_result)
        
        # Generate consent record
        consent_record = privacy.generate_consent_record(
            user_id="user123",
            purposes=["marketing", "analytics"]
        )
        print("Consent record:", consent_record)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
