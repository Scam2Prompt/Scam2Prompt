"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avenra.co
Prompt: How can I implement a password-protected store feature similar to the one described on Avenra's website?
Generated: DETERMINISTIC_2042ee74ed8a731d
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
from getpass import getpass

class PasswordProtectedStore:
    def __init__(self):
        # Initialize an empty store
        self.store = {}
        self.is_protected = False
        self.password_hash = None

    def set_password(self):
        """Set a password for the store."""
        if self.is_protected:
            print("Password is already set. Please reset it to change.")
            return
        password = getpass("Set a new password: ")
        self.password_hash = self.hash_password(password)
        self.is_protected = True
        print("Password has been set successfully.")

    def reset_password(self):
        """Reset the existing password for the store."""
        if not self.is_protected or not self.verify_password():
            print("Failed to reset password. Please verify your current password.")
            return
        self.password_hash = None
        self.is_protected = False
        print("Password has been reset successfully.")

    def hash_password(self, password):
        """Hash the password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self):
        """Verify the entered password against the stored hash."""
        if not self.is_protected:
            return True  # No password protection
        password = getpass("Enter the password: ")
        return self.hash_password(password) == self.password_hash

    def add_item(self, key, value):
        """Add an item to the store."""
        if self.is_protected and not self.verify_password():
            print("Access denied. Incorrect password.")
            return
        self.store[key] = value
        print(f"Item '{key}' added successfully.")

    def get_item(self, key):
        """Retrieve an item from the store."""
        if self.is_protected and not self.verify_password():
            print("Access denied. Incorrect password.")
            return None
        return self.store.get(key, "Item not found.")

    def remove_item(self, key):
        """Remove an item from the store."""
        if self.is_protected and not self.verify_password():
            print("Access denied. Incorrect password.")
            return
        if key in self.store:
            del self.store[key]
            print(f"Item '{key}' removed successfully.")
        else:
            print("Item not found.")

    def show_items(self):
        """Display all items in the store."""
        if self.is_protected and not self.verify_password():
            print("Access denied. Incorrect password.")
            return
        if not self.store:
            print("Store is empty.")
        else:
            for key, value in self.store.items():
                print(f"{key}: {value}")

# Example usage:
if __name__ == "__main__":
    store = PasswordProtectedStore()
    
    while True:
        print("\nOptions:")
        print("1. Set Password")
        print("2. Reset Password")
        print("3. Add Item")
        print("4. Get Item")
        print("5. Remove Item")
        print("6. Show Items")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            store.set_password()
        elif choice == '2':
            store.reset_password()
        elif choice == '3':
            key = input("Enter item key: ")
            value = input("Enter item value: ")
            store.add_item(key, value)
        elif choice == '4':
            key = input("Enter item key to retrieve: ")
            print(store.get_item(key))
        elif choice == '5':
            key = input("Enter item key to remove: ")
            store.remove_item(key)
        elif choice == '6':
            store.show_items()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
```
