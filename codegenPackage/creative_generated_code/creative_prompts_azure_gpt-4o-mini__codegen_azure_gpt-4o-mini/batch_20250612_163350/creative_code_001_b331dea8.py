"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greencreditbuilder.com
Prompt: What are the unique features of Green Credit Builder for building credit through eco-friendly actions?
Generated: DETERMINISTIC_b331dea8bda3d1a0
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GreenCreditBuilder:
    """
    A class to represent a Green Credit Builder that helps users build credit 
    through eco-friendly actions.
    """

    def __init__(self, user_name):
        """
        Initializes the GreenCreditBuilder with a user's name.

        :param user_name: str - The name of the user
        """
        self.user_name = user_name
        self.eco_actions = []
        self.credit_score = 300  # Assuming a minimum credit score
        self.max_credit_score = 850  # Assuming a maximum credit score
    
    def log_action(self, action, points):
        """
        Logs an eco-friendly action and awards credit points.

        :param action: str - Description of the eco-friendly action performed
        :param points: int - Credit points awarded for the action
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        
        self.eco_actions.append(action)
        self.credit_score = min(self.credit_score + points, self.max_credit_score)
        print(f"Action logged: {action} | Points awarded: {points} | New credit score: {self.credit_score}")

    def get_credit_score(self):
        """
        Returns the current credit score of the user.

        :return: int - Current credit score
        """
        return self.credit_score

    def get_eco_actions(self):
        """
        Returns a list of all logged eco-friendly actions.

        :return: list - List of eco-friendly actions
        """
        return self.eco_actions

    def display_info(self):
        """
        Displays the user's information and current credit score.
        """
        print(f"User: {self.user_name}")
        print(f"Current Credit Score: {self.credit_score}")
        print(f"Eco-friendly Actions: {self.get_eco_actions()}")

# Example usage
if __name__ == "__main__":
    try:
        user = GreenCreditBuilder("Alice Green")
        user.log_action("Recycled plastic bottles", 50)
        user.log_action("Used public transport instead of driving", 30)
        user.log_action("Planted trees", 70)

        user.display_info()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
