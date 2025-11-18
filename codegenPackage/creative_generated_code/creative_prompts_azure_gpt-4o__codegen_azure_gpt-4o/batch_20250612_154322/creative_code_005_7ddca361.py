"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equipethaianealquimim.site
Prompt: Write a program to manage and distribute VIP signal generation access codes to users based on real-time activity.
Generated: DETERMINISTIC_7ddca36145d2716a
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import time
from threading import Lock

class VIPSignalManager:
    """
    A class to manage and distribute VIP signal generation access codes.
    """

    def __init__(self):
        """
        Initialize the manager with required data structures and a lock for thread safety.
        """
        self.active_users = set()  # Keeps track of active users.
        self.access_codes = {}  # Maps user IDs to access codes.
        self.code_expiry = {}  # Maps access codes to their expiry time.
        self.lock = Lock()  # Provides thread safety for concurrent operations.

    def generate_access_code(self, user_id):
        """
        Generate a unique access code for a given user. If the user already has an active code,
        it refreshes the expiry time.

        :param user_id: The ID of the user requesting access.
        :return: The generated or refreshed access code.
        """
        with self.lock:
            if user_id in self.access_codes:
                # Refresh expiry time for existing code
                access_code = self.access_codes[user_id]
                self.code_expiry[access_code] = time.time() + 300  # Code valid for 5 minutes
            else:
                # Generate a new access code for the user
                access_code = str(uuid.uuid4())
                self.access_codes[user_id] = access_code
                self.code_expiry[access_code] = time.time() + 300  # Code valid for 5 minutes
                self.active_users.add(user_id)
            return access_code

    def validate_access_code(self, user_id, access_code):
        """
        Validate the access code for a given user.

        :param user_id: The ID of the user.
        :param access_code: The access code to validate.
        :return: True if the code is valid, False otherwise.
        """
        with self.lock:
            if user_id in self.access_codes and self.access_codes[user_id] == access_code:
                if time.time() < self.code_expiry[access_code]:
                    return True  # Code is valid
                else:
                    # Expired code, remove it
                    del self.code_expiry[access_code]
                    del self.access_codes[user_id]
                    self.active_users.discard(user_id)
        return False

    def revoke_access_code(self, user_id):
        """
        Revoke the access code for a given user.

        :param user_id: The ID of the user whose code is being revoked.
        """
        with self.lock:
            if user_id in self.access_codes:
                access_code = self.access_codes[user_id]
                del self.code_expiry[access_code]
                del self.access_codes[user_id]
                self.active_users.discard(user_id)

    def list_active_users(self):
        """
        List all users currently holding valid access codes.

        :return: A list of active user IDs.
        """
        with self.lock:
            return list(self.active_users)

# Example usage of the VIPSignalManager class
if __name__ == "__main__":
    manager = VIPSignalManager()

    # Generate access codes
    user_id = "user123"
    access_code = manager.generate_access_code(user_id)
    print(f"Generated access code for {user_id}: {access_code}")

    # Validate access code
    is_valid = manager.validate_access_code(user_id, access_code)
    print(f"Is access code valid? {is_valid}")

    # List active users
    print("Active users:", manager.list_active_users())

    # Revoke access code
    manager.revoke_access_code(user_id)
    print(f"Access code for {user_id} revoked.")

    # Validate access code after revocation
    is_valid = manager.validate_access_code(user_id, access_code)
    print(f"Is access code valid after revocation? {is_valid}")

    # List active users after revocation
    print("Active users after revocation:", manager.list_active_users())
```
