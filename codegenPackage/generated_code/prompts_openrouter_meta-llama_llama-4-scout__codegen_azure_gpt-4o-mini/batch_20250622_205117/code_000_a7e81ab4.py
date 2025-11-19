"""
Generated Code Metadata:
========================
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Explain the concept of selective transparency in the context of the Data Ownership Protocol (DOP) and how it achieves flexible transparency for users.
Generated: DETERMINISTIC_a7e81ab497969591
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DataOwnershipProtocol:
    """
    A class to represent the Data Ownership Protocol (DOP) which implements selective transparency.
    This protocol allows users to control the visibility of their data while maintaining ownership.
    """

    def __init__(self):
        """
        Initializes the DataOwnershipProtocol with an empty data store.
        """
        self.data_store = {}
        self.user_permissions = {}

    def add_data(self, user_id, data_id, data_content):
        """
        Adds data to the user's data store.

        Parameters:
        user_id (str): The ID of the user.
        data_id (str): The ID of the data to be added.
        data_content (str): The content of the data.

        Raises:
        ValueError: If the data_id already exists for the user.
        """
        if user_id not in self.data_store:
            self.data_store[user_id] = {}
        
        if data_id in self.data_store[user_id]:
            raise ValueError(f"Data ID {data_id} already exists for user {user_id}.")

        self.data_store[user_id][data_id] = data_content
        self.user_permissions[user_id] = self.user_permissions.get(user_id, {})
        self.user_permissions[user_id][data_id] = True  # Default to visible

    def set_transparency(self, user_id, data_id, is_visible):
        """
        Sets the visibility of the specified data for the user.

        Parameters:
        user_id (str): The ID of the user.
        data_id (str): The ID of the data.
        is_visible (bool): True to make the data visible, False to hide it.

        Raises:
        KeyError: If the user_id or data_id does not exist.
        """
        if user_id not in self.data_store or data_id not in self.data_store[user_id]:
            raise KeyError(f"User ID {user_id} or Data ID {data_id} does not exist.")

        self.user_permissions[user_id][data_id] = is_visible

    def get_data(self, user_id, data_id):
        """
        Retrieves the data for the user if it is visible.

        Parameters:
        user_id (str): The ID of the user.
        data_id (str): The ID of the data.

        Returns:
        str: The content of the data if visible.

        Raises:
        KeyError: If the user_id or data_id does not exist.
        PermissionError: If the data is not visible to the user.
        """
        if user_id not in self.data_store or data_id not in self.data_store[user_id]:
            raise KeyError(f"User ID {user_id} or Data ID {data_id} does not exist.")

        if not self.user_permissions[user_id].get(data_id, False):
            raise PermissionError(f"Data ID {data_id} is not visible to user {user_id}.")

        return self.data_store[user_id][data_id]

# Example usage
if __name__ == "__main__":
    try:
        dop = DataOwnershipProtocol()
        dop.add_data("user1", "data1", "This is some sensitive data.")
        dop.set_transparency("user1", "data1", True)  # Make data visible
        print(dop.get_data("user1", "data1"))  # Should print the data content

        dop.set_transparency("user1", "data1", False)  # Hide data
        print(dop.get_data("user1", "data1"))  # Should raise PermissionError
    except Exception as e:
        print(f"An error occurred: {e}")
```
