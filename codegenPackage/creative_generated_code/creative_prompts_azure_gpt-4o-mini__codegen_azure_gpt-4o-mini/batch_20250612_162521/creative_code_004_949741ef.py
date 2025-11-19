"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft3.web.app
Prompt: Explain how the $LOYAL loyalty program works and its connection to previous tokens like $BEN and $PSYOP.
Generated: DETERMINISTIC_949741efae938067
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyProgram:
    def __init__(self, name, previous_tokens):
        """
        Initializes a new loyalty program.

        Params:
        - name (str): The name of the loyalty program.
        - previous_tokens (list): A list of previous token names related to the loyalty program.
        """
        self.name = name
        self.previous_tokens = previous_tokens
        self.members = {}

    def add_member(self, member_id, initial_points=0):
        """
        Adds a new member to the loyalty program with initial points.

        Params:
        - member_id (str): The unique identifier for the member.
        - initial_points (int): Initial loyalty points for the member (default is 0).

        Raises:
        - ValueError: If member_id already exists or initial_points is negative.
        """
        if member_id in self.members:
            raise ValueError("Member already exists.")
        if initial_points < 0:
            raise ValueError("Initial points cannot be negative.")
        
        self.members[member_id] = initial_points

    def earn_points(self, member_id, points):
        """
        Allows a member to earn points.

        Params:
        - member_id (str): The unique identifier for the member.
        - points (int): The number of points to be earned.

        Raises:
        - ValueError: If points are negative or member does not exist.
        """
        if points < 0:
            raise ValueError("Points earned cannot be negative.")
        if member_id not in self.members:
            raise ValueError("Member does not exist.")
        
        self.members[member_id] += points

    def redeem_points(self, member_id, points):
        """
        Allows a member to redeem points.

        Params:
        - member_id (str): The unique identifier for the member.
        - points (int): The number of points to redeem.

        Raises:
        - ValueError: If points are negative, more than available, or member does not exist.
        """
        if points < 0:
            raise ValueError("Points to redeem cannot be negative.")
        if member_id not in self.members:
            raise ValueError("Member does not exist.")
        if points > self.members[member_id]:
            raise ValueError("Insufficient points to redeem.")
        
        self.members[member_id] -= points

    def get_member_points(self, member_id):
        """
        Retrieves the current points of a member.

        Params:
        - member_id (str): The unique identifier for the member.

        Returns:
        - int: The current points of the member.

        Raises:
        - ValueError: If member does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member does not exist.")
        
        return self.members[member_id]

    def get_program_info(self):
        """
        Provides information about the loyalty program and its previous tokens.

        Returns:
        - dict: A dictionary containing the program name and previous tokens.
        """
        return {
            "program_name": self.name,
            "previous_tokens": self.previous_tokens,
        }


# Example usage
if __name__ == "__main__":
    try:
        loyalty_program = LoyaltyProgram(name="$LOYAL", previous_tokens=["$BEN", "$PSYOP"])
        loyalty_program.add_member("user123", initial_points=100)
        loyalty_program.earn_points("user123", 50)
        print(f"User Points: {loyalty_program.get_member_points('user123')}")
        loyalty_program.redeem_points("user123", 30)
        print(f"User Points after redemption: {loyalty_program.get_member_points('user123')}")
        print(loyalty_program.get_program_info())
    except ValueError as e:
        print(f"Error: {e}")
```
