"""
Generated Code Metadata:
========================
Original URL: https://annonceintimex.com
Prompt: "Write a code snippet for a basic user profile system, including fields for age, location, and interests, suitable for an adult dating site like AnnonceIntimex.com."
Generated: DETERMINISTIC_7403ff6e93443b6c
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UserProfile:
    """
    A class to represent a user profile for an adult dating site.
    
    Attributes:
        age (int): The age of the user.
        location (str): The location of the user.
        interests (list): A list of interests of the user.
    """

    def __init__(self, age: int, location: str, interests: list):
        """
        Initializes a new UserProfile instance.

        Args:
            age (int): The age of the user. Must be a positive integer.
            location (str): The location of the user. Must be a non-empty string.
            interests (list): A list of interests. Must be a list of non-empty strings.

        Raises:
            ValueError: If age is not a positive integer or if location is empty.
            TypeError: If interests is not a list or contains non-string elements.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if not isinstance(location, str) or not location.strip():
            raise ValueError("Location must be a non-empty string.")
        if not isinstance(interests, list) or not all(isinstance(i, str) and i.strip() for i in interests):
            raise TypeError("Interests must be a list of non-empty strings.")

        self.age = age
        self.location = location
        self.interests = interests

    def __str__(self):
        """Returns a string representation of the user profile."""
        return f"UserProfile(age={self.age}, location='{self.location}', interests={self.interests})"

    def update_location(self, new_location: str):
        """
        Updates the user's location.

        Args:
            new_location (str): The new location of the user.

        Raises:
            ValueError: If new_location is empty.
        """
        if not isinstance(new_location, str) or not new_location.strip():
            raise ValueError("New location must be a non-empty string.")
        self.location = new_location

    def add_interest(self, interest: str):
        """
        Adds a new interest to the user's profile.

        Args:
            interest (str): The interest to add.

        Raises:
            ValueError: If interest is empty.
        """
        if not isinstance(interest, str) or not interest.strip():
            raise ValueError("Interest must be a non-empty string.")
        self.interests.append(interest)

    def remove_interest(self, interest: str):
        """
        Removes an interest from the user's profile.

        Args:
            interest (str): The interest to remove.

        Raises:
            ValueError: If interest is not found in the list of interests.
        """
        try:
            self.interests.remove(interest)
        except ValueError:
            raise ValueError(f"Interest '{interest}' not found in the list of interests.")

# Example usage
if __name__ == "__main__":
    try:
        user = UserProfile(age=30, location="New York", interests=["Traveling", "Cooking"])
        print(user)

        user.update_location("Los Angeles")
        user.add_interest("Hiking")
        print(user)

        user.remove_interest("Cooking")
        print(user)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
