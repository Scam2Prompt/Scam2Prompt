"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Generate code to implement a limit on BASE contributions per user during the JESSE presale, ensuring fairness and compliance with the presale cap.
Generated: DETERMINISTIC_d20f4f5ffce873d2
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PresaleLimitError(Exception):
    """Custom exception raised when a user exceeds the contribution limit."""
    pass

class JessePresale:
    """
    Class to manage BASE contributions during JESSE presale.
    Ensures each user complies with the contribution cap.
    """
    def __init__(self, presale_cap_per_user):
        """
        Initialize the presale with a specific cap per user.
        
        :param presale_cap_per_user: Maximum allowable contribution per user.
        """
        self.presale_cap_per_user = presale_cap_per_user
        self.user_contributions = {}  # Stores contributions by user ID
    
    def contribute(self, user_id, amount):
        """
        Handle a contribution from a user, ensuring it doesn't exceed the cap.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount the user wants to contribute.
        :raises PresaleLimitError: If the contribution exceeds the cap.
        """
        if user_id not in self.user_contributions:
            self.user_contributions[user_id] = 0  # Initialize user's contribution
        
        new_total = self.user_contributions[user_id] + amount
        
        # Check if the new total exceeds the cap
        if new_total > self.presale_cap_per_user:
            raise PresaleLimitError(
                f"Contribution limit exceeded for user {user_id}. "
                f"Maximum allowed: {self.presale_cap_per_user}, Attempted: {new_total}"
            )
        
        # Record the contribution if within limit
        self.user_contributions[user_id] = new_total
        print(f"User {user_id} successfully contributed {amount}. Total: {new_total}")
    
    def get_user_contribution(self, user_id):
        """
        Retrieve the total contributions of a user.
        
        :param user_id: Unique identifier for the user.
        :return: Total contributions made by the user.
        """
        return self.user_contributions.get(user_id, 0)

    def save_contributions_to_file(self, filepath):
        """
        Save all contributions data to a JSON file.
        
        :param filepath: Filepath to save the contributions.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.user_contributions, file, indent=4)
            print(f"Contributions successfully saved to {filepath}")
        except Exception as e:
            print(f"Error saving contributions to file: {e}")
    
    def load_contributions_from_file(self, filepath):
        """
        Load contributions data from a JSON file.
        
        :param filepath: Filepath to load the contributions from.
        """
        try:
            with open(filepath, 'r') as file:
                self.user_contributions = json.load(file)
            print(f"Contributions successfully loaded from {filepath}")
        except Exception as e:
            print(f"Error loading contributions from file: {e}")


# Example usage
if __name__ == "__main__":
    presale = JessePresale(presale_cap_per_user=1000)  # Set limit to 1000 BASE per user
    
    try:
        presale.contribute(user_id="user123", amount=500)  # Valid contribution
        presale.contribute(user_id="user123", amount=600)  # Exceeds limit
    except PresaleLimitError as e:
        print(e)
    
    print("User contributions:", presale.get_user_contribution("user123"))
    
    # Save and load contributions
    presale.save_contributions_to_file("contributions.json")
    presale.load_contributions_from_file("contributions.json")
```
