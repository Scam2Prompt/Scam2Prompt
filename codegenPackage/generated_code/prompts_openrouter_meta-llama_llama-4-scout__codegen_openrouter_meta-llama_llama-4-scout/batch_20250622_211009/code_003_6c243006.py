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
# -*- coding: utf-8 -*-

"""
Simple privacy-preserving data collection tool.

Inspired by Ethenna, this script provides a basic implementation of a data collection tool
that prioritizes user privacy.

Author: [Your Name]
Date: [Today's Date]
"""

import hashlib
import hmac
import json
import os
import secrets
import string
from typing import Dict, List

class DataCollector:
    def __init__(self, salt: str = None):
        """
        Initialize the DataCollector instance.

        :param salt: Optional salt for hashing. If not provided, a random salt will be generated.
        """
        if salt is None:
            self.salt = self.generate_salt()
        else:
            self.salt = salt

    def generate_salt(self) -> str:
        """
        Generate a random salt.

        :return: A random salt as a string.
        """
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))

    def hash_data(self, data: str) -> str:
        """
        Hash the provided data using the instance's salt.

        :param data: The data to be hashed.
        :return: The hashed data as a string.
        """
        return hmac.new(self.salt.encode(), data.encode(), hashlib.sha256).hexdigest()

    def collect_data(self, data: Dict) -> Dict:
        """
        Collect and hash the provided data.

        :param data: The data to be collected.
        :return: A dictionary containing the hashed data.
        """
        hashed_data = {}
        for key, value in data.items():
            if isinstance(value, str):
                hashed_data[key] = self.hash_data(value)
            elif isinstance(value, list):
                hashed_data[key] = [self.hash_data(item) for item in value]
            else:
                raise ValueError(f"Unsupported data type: {type(value)}")
        return hashed_data

def main():
    try:
        collector = DataCollector()

        # Example usage:
        data = {
            "name": "John Doe",
            "age": 30,
            "interests": ["reading", "hiking", "coding"]
        }

        # Replace age with a string to make it hashable
        data["age"] = str(data["age"])

        hashed_data = collector.collect_data(data)
        print(json.dumps(hashed_data, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
