"""
Generated Code Metadata:
========================
Original URL: https://adstar.network
Prompt: Create a sample code snippet for integrating user privacy features based on the practices highlighted on adstar.network.
Generated: DETERMINISTIC_be8b76a4249bc5f6
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, Optional, List
import hashlib

class UserPrivacyManager:
    """
    A class to manage user privacy features based on best practices.
    Handles consent management, data anonymization, and data retention policies.
    """

    def __init__(self, retention_period_days: int = 30):
        """
        Initialize the UserPrivacyManager with a data retention period.

        Args:
            retention_period_days (int): Number of days to retain user data. Defaults to 30.
        """
        self.retention_period = timedelta(days=retention_period_days)
        self.user_consents: Dict[str, Dict[str, bool]] = {}
        self.user_data: Dict[str, Dict] = {}

    def get_user_consent(self, user_id: str, feature: str) -> bool:
        """
        Check if a user has given consent for a specific feature.

        Args:
            user_id (str): Unique identifier for the user.
            feature (str): Feature to check consent for.

        Returns:
            bool: True if consent is given, False otherwise.
        """
        return self.user_consents.get(user_id, {}).get(feature, False)

    def set_user_consent(self, user_id: str, feature: str, granted: bool) -> None:
        """
        Set user consent for a specific feature.

        Args:
            user_id (str): Unique identifier for the user.
            feature (str): Feature to set consent for.
            granted (bool): Whether consent is granted.
        """
        if user_id not in self.user_consents:
            self.user_consents[user_id] = {}
        self.user_consents[user_id][feature] = granted

    def anonymize_data(self, data: Dict) -> Dict:
        """
        Anonymize user data by removing or hashing personally identifiable information (PII).

        Args:
            data (Dict): Original user data.

        Returns:
            Dict: Anonymized data.
        """
        anonymized = data.copy()
        if 'email' in anonymized:
            anonymized['email'] = hashlib.sha256(anonymized['email'].encode()).hexdigest()
        if 'name' in anonymized:
            del anonymized['name']
        if 'ip_address' in anonymized:
            anonymized['ip_address'] = hashlib.sha256(anonymized['ip_address'].encode()).hexdigest()
        return anonymized

    def store_user_data(self, user_id: str, data: Dict, require_consent: bool = True) -> bool:
        """
        Store user data after applying privacy checks and anonymization.

        Args:
            user_id (str): Unique identifier for the user.
            data (Dict): User data to store.
            require_consent (bool): Whether to check for consent before storing. Defaults to True.

        Returns:
            bool: True if data was stored successfully, False otherwise.
        """
        if require_consent and not self.get_user_consent(user_id, 'data_collection'):
            return False

        anonymized_data = self.anonymize_data(data)
        anonymized_data['timestamp'] = datetime.utcnow().isoformat()

        if user_id not in self.user_data:
            self.user_data[user_id] = []
        self.user_data[user_id].append(anonymized_data)
        return True

    def purge_old_data(self) -> None:
        """
        Purge user data older than the retention period.
        """
        cutoff = datetime.utcnow() - self.retention_period
        for user_id, records in list(self.user_data.items()):
            updated_records = [
                record for record in records
                if datetime.fromisoformat(record['timestamp']) > cutoff
            ]
            if updated_records:
                self.user_data[user_id] = updated_records
            else:
                del self.user_data[user_id]

    def export_user_data(self, user_id: str) -> Optional[List[Dict]]:
        """
        Export a user's data if they have given consent.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            Optional[List[Dict]]: User data if consent is given, None otherwise.
        """
        if not self.get_user_consent(user_id, 'data_export'):
            return None
        return self.user_data.get(user_id, [])

    def delete_user_data(self, user_id: str) -> bool:
        """
        Delete all data for a specific user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            bool: True if data was deleted, False if no data existed.
        """
        if user_id in self.user_data:
            del self.user_data[user_id]
            return True
        return False

# Example usage
if __name__ == "__main__":
    privacy_manager = UserPrivacyManager(retention_period_days=30)

    # Simulate user consent
    user_id = "user123"
    privacy_manager.set_user_consent(user_id, 'data_collection', True)
    privacy_manager.set_user_consent(user_id, 'data_export', True)

    # Store some user data
    user_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'ip_address': '192.168.1.1',
        'preferences': {'theme': 'dark'}
    }
    privacy_manager.store_user_data(user_id, user_data)

    # Export and print user data
    exported_data = privacy_manager.export_user_data(user_id)
    print(json.dumps(exported_data, indent=2))

    # Purge old data
    privacy_manager.purge_old_data()

    # Delete user data
    privacy_manager.delete_user_data(user_id)
```
