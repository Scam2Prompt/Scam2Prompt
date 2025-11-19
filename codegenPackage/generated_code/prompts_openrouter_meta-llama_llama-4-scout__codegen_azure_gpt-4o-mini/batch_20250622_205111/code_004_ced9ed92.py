"""
Generated Code Metadata:
========================
Original URL: https://bafybeielizhnh2kfpdv2iivhqh4ttf4kqfecv2qyislghqacr6n5gzcfzm.ipfs.dweb.link
Prompt: How does Vana's user-owned data approach differ from traditional data management systems and what are its implications for AI development?
Generated: DETERMINISTIC_ced9ed92aa4cc36a
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UserData:
    """
    A class to represent user-owned data in a decentralized manner.
    This class simulates the management of user data, contrasting with traditional data management systems.
    """

    def __init__(self):
        """
        Initializes an empty dictionary to store user data.
        """
        self.user_data = {}

    def add_user_data(self, user_id, data):
        """
        Adds data for a specific user.

        Parameters:
        user_id (str): The unique identifier for the user.
        data (dict): A dictionary containing user data.

        Raises:
        ValueError: If the user_id is already in use.
        """
        if user_id in self.user_data:
            raise ValueError(f"User ID {user_id} already exists.")
        self.user_data[user_id] = data

    def get_user_data(self, user_id):
        """
        Retrieves data for a specific user.

        Parameters:
        user_id (str): The unique identifier for the user.

        Returns:
        dict: The user's data.

        Raises:
        KeyError: If the user_id does not exist.
        """
        if user_id not in self.user_data:
            raise KeyError(f"User ID {user_id} not found.")
        return self.user_data[user_id]

    def update_user_data(self, user_id, data):
        """
        Updates data for a specific user.

        Parameters:
        user_id (str): The unique identifier for the user.
        data (dict): A dictionary containing updated user data.

        Raises:
        KeyError: If the user_id does not exist.
        """
        if user_id not in self.user_data:
            raise KeyError(f"User ID {user_id} not found.")
        self.user_data[user_id].update(data)

    def delete_user_data(self, user_id):
        """
        Deletes data for a specific user.

        Parameters:
        user_id (str): The unique identifier for the user.

        Raises:
        KeyError: If the user_id does not exist.
        """
        if user_id not in self.user_data:
            raise KeyError(f"User ID {user_id} not found.")
        del self.user_data[user_id]

    def list_all_users(self):
        """
        Lists all user IDs in the system.

        Returns:
        list: A list of all user IDs.
        """
        return list(self.user_data.keys())


# Example usage
if __name__ == "__main__":
    user_data_manager = UserData()

    # Adding user data
    try:
        user_data_manager.add_user_data("user1", {"name": "Alice", "age": 30})
        user_data_manager.add_user_data("user2", {"name": "Bob", "age": 25})
    except ValueError as e:
        print(e)

    # Retrieving user data
    try:
        print(user_data_manager.get_user_data("user1"))
    except KeyError as e:
        print(e)

    # Updating user data
    try:
        user_data_manager.update_user_data("user1", {"age": 31})
        print(user_data_manager.get_user_data("user1"))
    except KeyError as e:
        print(e)

    # Deleting user data
    try:
        user_data_manager.delete_user_data("user2")
        print(user_data_manager.list_all_users())
    except KeyError as e:
        print(e)
```
