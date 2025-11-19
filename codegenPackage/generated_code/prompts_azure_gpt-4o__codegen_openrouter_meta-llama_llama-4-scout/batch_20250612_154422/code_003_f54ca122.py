"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Provide code for a "矩阵制直销软件" (matrix-based direct selling system) that incorporates multi-layer bonuses and addresses the limitations of traditional hierarchical systems, following JieyaSoft's specifications.
Generated: DETERMINISTIC_f54ca122ea408e9b
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm ready to provide the code. However, I need to clarify that I'll be using Python as the programming language. Here's the code:

```python
# matrix_direct_selling_system.py

class User:
    """Represents a user in the matrix-based direct selling system."""
    
    def __init__(self, user_id, name):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): Name of the user.
        """
        self.user_id = user_id
        self.name = name
        self.downline_users = []  # List of users directly under this user
        self.sponsor = None  # User who sponsored this user

    def add_downline_user(self, user):
        """Adds a user to this user's downline."""
        self.downline_users.append(user)
        user.sponsor = self

    def __repr__(self):
        return f"User(user_id={self.user_id}, name='{self.name}')"


class Matrix:
    """Represents a matrix in the matrix-based direct selling system."""
    
    def __init__(self, width, height):
        """
        Initializes a Matrix object.

        Args:
            width (int): Width of the matrix.
            height (int): Height of the matrix.
        """
        self.width = width
        self.height = height
        self.users = {}  # Dictionary of user_id to User objects

    def add_user(self, user, parent_user_id=None):
        """
        Adds a user to the matrix.

        Args:
            user (User): User to add.
            parent_user_id (int, optional): ID of the parent user. Defaults to None.

        Raises:
            ValueError: If parent_user_id is not provided for a user who is not the root user.
        """
        if parent_user_id is not None:
            parent_user = self.users.get(parent_user_id)
            if parent_user:
                parent_user.add_downline_user(user)
            else:
                raise ValueError("Parent user not found")
        self.users[user.user_id] = user

    def get_user(self, user_id):
        """Gets a user by their ID."""
        return self.users.get(user_id)

    def calculate_bonuses(self, user_id):
        """
        Calculates the bonuses for a user.

        Args:
            user_id (int): ID of the user.

        Returns:
            dict: Dictionary of bonus amounts for each level.
        """
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        bonuses = {}
        level = 0
        queue = [(user, level)]

        while queue:
            current_user, level = queue.pop(0)
            bonus_amount = self.calculate_bonus(current_user, level)
            bonuses[level] = bonuses.get(level, 0) + bonus_amount

            for downline_user in current_user.downline_users:
                queue.append((downline_user, level + 1))

        return bonuses

    def calculate_bonus(self, user, level):
        """
        Calculates the bonus for a user at a given level.

        Args:
            user (User): User to calculate bonus for.
            level (int): Level of the user.

        Returns:
            float: Bonus amount.
        """
        # Implement bonus calculation logic here
        # For example:
        if level == 0:
            return 10.0
        elif level == 1:
            return 5.0
        else:
            return 0.0


class DirectSellingSystem:
    """Represents the matrix-based direct selling system."""
    
    def __init__(self, matrix_width, matrix_height):
        """
        Initializes a DirectSellingSystem object.

        Args:
            matrix_width (int): Width of the matrix.
            matrix_height (int): Height of the matrix.
        """
        self.matrix = Matrix(matrix_width, matrix_height)

    def create_user(self, user_id, name, parent_user_id=None):
        """
        Creates a new user.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): Name of the user.
            parent_user_id (int, optional): ID of the parent user. Defaults to None.

        Returns:
            User: Created user.
        """
        user = User(user_id, name)
        self.matrix.add_user(user, parent_user_id)
        return user

    def get_user(self, user_id):
        """Gets a user by their ID."""
        return self.matrix.get_user(user_id)

    def calculate_bonuses(self, user_id):
        """
        Calculates the bonuses for a user.

        Args:
            user_id (int): ID of the user.

        Returns:
            dict: Dictionary of bonus amounts for each level.
        """
        return self.matrix.calculate_bonuses(user_id)


# Example usage:
if __name__ == "__main__":
    system = DirectSellingSystem(10, 10)

    user1 = system.create_user(1, "John")
    user2 = system.create_user(2, "Jane", 1)
    user3 = system.create_user(3, "Bob", 1)
    user4 = system.create_user(4, "Alice", 2)

    bonuses = system.calculate_bonuses(1)
    print(bonuses)
```

Please let me know if you need any modifications or have further requests!
