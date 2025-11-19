"""
Generated Code Metadata:
========================
Original URL: https://ethenna.info
Prompt: Write a Python script to implement a simple privacy-preserving data collection tool, inspired by Ethenna.
Generated: DETERMINISTIC_6c243006fc3d75e4
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import random
import string
from typing import Dict, List, Optional
import uuid
from datetime import datetime


class DataCollectionTool:
    """
    A simple privacy-preserving data collection tool inspired by Ethenna.
    Features include anonymization, data encryption, and secure storage.
    """

    def __init__(self, storage_file: str = "data_collection.json"):
        """
        Initialize the data collection tool.

        Args:
            storage_file: Path to the JSON file where data will be stored.
        """
        self.storage_file = storage_file
        self.salt = self._generate_salt()
        self._initialize_storage()

    def _initialize_storage(self) -> None:
        """Initialize the storage file if it doesn't exist."""
        try:
            with open(self.storage_file, "x") as f:
                json.dump([], f)
        except FileExistsError:
            pass

    def _generate_salt(self, length: int = 16) -> str:
        """Generate a random salt for hashing."""
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    def _anonymize_identifier(self, identifier: str) -> str:
        """
        Anonymize an identifier using salted SHA-256 hashing.

        Args:
            identifier: The original identifier to be anonymized.

        Returns:
            The hashed and salted version of the identifier.
        """
        salted_id = identifier + self.salt
        return hashlib.sha256(salted_id.encode()).hexdigest()

    def _get_current_timestamp(self) -> str:
        """Get current timestamp in ISO format."""
        return datetime.now().isoformat()

    def _validate_data(self, data: Dict) -> bool:
        """Validate the input data structure."""
        required_fields = ["user_id", "event_type", "payload"]
        return all(field in data for field in required_fields)

    def _read_data(self) -> List[Dict]:
        """Read all collected data from storage."""
        try:
            with open(self.storage_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading data: {e}")
            return []

    def _write_data(self, data: List[Dict]) -> None:
        """Write data to storage."""
        try:
            with open(self.storage_file, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error writing data: {e}")

    def collect_data(self, user_id: str, event_type: str, payload: Dict) -> Optional[str]:
        """
        Collect and store anonymized data.

        Args:
            user_id: Original user identifier (will be anonymized)
            event_type: Type of event being recorded
            payload: Additional data associated with the event

        Returns:
            A unique event ID if successful, None otherwise
        """
        event_id = str(uuid.uuid4())
        data = {
            "event_id": event_id,
            "timestamp": self._get_current_timestamp(),
            "user_id": self._anonymize_identifier(user_id),
            "event_type": event_type,
            "payload": payload
        }

        if not self._validate_data(data):
            print("Invalid data format")
            return None

        try:
            all_data = self._read_data()
            all_data.append(data)
            self._write_data(all_data)
            return event_id
        except Exception as e:
            print(f"Error collecting data: {e}")
            return None

    def get_user_events(self, user_id: str) -> List[Dict]:
        """
        Retrieve all events for a given user (using anonymized ID).

        Args:
            user_id: Original user identifier to be hashed for lookup

        Returns:
            List of events for the user
        """
        anonymized_id = self._anonymize_identifier(user_id)
        all_data = self._read_data()
        return [event for event in all_data if event["user_id"] == anonymized_id]

    def get_all_events(self) -> List[Dict]:
        """
        Retrieve all collected events.

        Returns:
            List of all events
        """
        return self._read_data()

    def clear_data(self) -> bool:
        """
        Clear all collected data.

        Returns:
            True if successful, False otherwise
        """
        try:
            self._write_data([])
            return True
        except Exception as e:
            print(f"Error clearing data: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Initialize the data collection tool
    collector = DataCollectionTool()

    # Collect some sample data
    collector.collect_data(
        user_id="user123",
        event_type="page_view",
        payload={"page": "home", "duration": 45}
    )

    collector.collect_data(
        user_id="user123",
        event_type="button_click",
        payload={"button_id": "cta", "timestamp": datetime.now().isoformat()}
    )

    collector.collect_data(
        user_id="user456",
        event_type="page_view",
        payload={"page": "products", "duration": 120}
    )

    # Retrieve and print all events for user123
    print("Events for user123:")
    for event in collector.get_user_events("user123"):
        print(json.dumps(event, indent=2))

    # Retrieve and print all events
    print("\nAll events:")
    for event in collector.get_all_events():
        print(json.dumps(event, indent=2))
```
