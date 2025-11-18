"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Provide an example of code for managing GDPR-compliant data protection protocols for businesses, referencing the privacy-focused services mentioned on Assistenza Tecnica Palermo's site.
Generated: DETERMINISTIC_bc88059300ed39f2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
GDPR-Compliant Data Protection Management Example
This code demonstrates how to manage data protection protocols aligned with GDPR requirements
for businesses, including user consent, data access control, and secure data storage.

Author: Expert Programmer
"""

import json
import logging
from datetime import datetime
from cryptography.fernet import Fernet
from typing import Dict, Optional

# Set up logging for debugging and auditing purposes
logging.basicConfig(level=logging.INFO, filename="gdpr_log.log", format="%(asctime)s - %(levelname)s - %(message)s")

class GDPRComplianceManager:
    """
    A class to manage GDPR-compliant data protection protocols for businesses.
    """
    
    def __init__(self, encryption_key: Optional[bytes] = None):
        """
        Initialize the GDPRComplianceManager with an optional encryption key.

        :param encryption_key: (Optional) Key for encrypting sensitive data.
        """
        if encryption_key:
            self.encryption_key = encryption_key
        else:
            self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.data_storage = {}  # Example storage for user data

    def collect_user_consent(self, user_id: str, consent: bool) -> None:
        """
        Collect and store user consent.

        :param user_id: Unique identifier for the user.
        :param consent: Boolean indicating whether the user has given consent.
        """
        self.data_storage[user_id] = {
            "consent": consent,
            "timestamp": datetime.now().isoformat()
        }
        logging.info(f"User {user_id} consent stored: {self.data_storage[user_id]}")

    def store_sensitive_data(self, user_id: str, sensitive_data: str) -> None:
        """
        Store sensitive user data securely after encrypting it.

        :param user_id: Unique identifier for the user.
        :param sensitive_data: The sensitive data to store (e.g., name, email, etc.).
        """
        if user_id not in self.data_storage or not self.data_storage[user_id].get("consent"):
            logging.error(f"Cannot store data for user {user_id} - consent not given.")
            raise PermissionError("User did not grant data storage consent.")
        
        encrypted_data = self.cipher.encrypt(sensitive_data.encode())
        self.data_storage[user_id]["encrypted_data"] = encrypted_data
        logging.info(f"Sensitive data for user {user_id} stored securely.")

    def retrieve_sensitive_data(self, user_id: str) -> Optional[str]:
        """
        Retrieve encrypted sensitive data for a user after decrypting it.

        :param user_id: Unique identifier for the user.
        :return: The decrypted sensitive data (if available).
        """
        if user_id not in self.data_storage or "encrypted_data" not in self.data_storage[user_id]:
            logging.warning(f"No sensitive data found for user {user_id}.")
            return None
        
        encrypted_data = self.data_storage[user_id]["encrypted_data"]
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        logging.info(f"Sensitive data for user {user_id} retrieved.")
        return decrypted_data

    def delete_user_data(self, user_id: str) -> None:
        """
        Delete all stored data for a user to comply with GDPR's "Right to be Forgotten".

        :param user_id: Unique identifier for the user.
        """
        if user_id in self.data_storage:
            del self.data_storage[user_id]
            logging.info(f"User data for {user_id} deleted as per GDPR request.")
        else:
            logging.warning(f"No data found for user {user_id} to delete.")

    def export_user_data(self, user_id: str) -> Optional[Dict]:
        """
        Export user data in a structured format for GDPR's "Data Portability" compliance.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing user data (if available).
        """
        if user_id not in self.data_storage:
            logging.warning(f"No data found for user {user_id} to export.")
            return None
        
        user_data = self.data_storage[user_id].copy()
        if "encrypted_data" in user_data:
            user_data["decrypted_data"] = self.cipher.decrypt(user_data["encrypted_data"]).decode()
            del user_data["encrypted_data"]
        
        logging.info(f"User data for {user_id} exported.")
        return user_data

# Example usage
if __name__ == "__main__":
    try:
        # Initialize GDPR manager
        gdpr_manager = GDPRComplianceManager()

        # Generate a user ID
        user_id = "user123"

        # Collect consent from the user
        gdpr_manager.collect_user_consent(user_id, consent=True)

        # Store sensitive data
        gdpr_manager.store_sensitive_data(user_id, sensitive_data="John Doe, john.doe@example.com")

        # Retrieve sensitive data
        sensitive_data = gdpr_manager.retrieve_sensitive_data(user_id)
        print(f"Retrieved sensitive data: {sensitive_data}")

        # Export user data
        exported_data = gdpr_manager.export_user_data(user_id)
        print(f"Exported user data: {json.dumps(exported_data, indent=2)}")

        # Delete user data
        gdpr_manager.delete_user_data(user_id)
        print("User data deleted successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
