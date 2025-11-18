"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Write a Python script to calculate the total cost for a family visiting Playland Kenya, including activities like trampoline, bowling, and virtual reality, based on the pricing details provided on the website.
Generated: DETERMINISTIC_6a02932c657aa3f4
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PlaylandKenya:
    def __init__(self):
        """Initialize the pricing for activities."""
        self.prices = {
            'trampoline': 200,  # Price per person for trampoline
            'bowling': 300,     # Price per game of bowling
            'virtual_reality': 400  # Price per session of virtual reality
        }

    def calculate_total_cost(self, num_people, trampoline_sessions, bowling_games, vr_sessions):
        """
        Calculate the total cost for a family visiting Playland Kenya.
        
        Parameters:
            num_people (int): The number of people in the family.
            trampoline_sessions (int): The number of trampoline sessions.
            bowling_games (int): The number of bowling games.
            vr_sessions (int): The number of virtual reality sessions.
        
        Returns:
            float: Total cost of the visit.
        
        Raises:
            ValueError: If any parameter is invalid (non-negative integers).
        """
        # Validate input parameters
        if not isinstance(num_people, int) or not isinstance(trampoline_sessions, int) or \
           not isinstance(bowling_games, int) or not isinstance(vr_sessions, int):
            raise ValueError("All parameters must be integers.")
        if num_people < 0 or trampoline_sessions < 0 or bowling_games < 0 or vr_sessions < 0:
            raise ValueError("All parameters must be non-negative integers.")

        # Calculate costs
        trampoline_cost = self.prices['trampoline'] * num_people * trampoline_sessions
        bowling_cost = self.prices['bowling'] * bowling_games
        vr_cost = self.prices['virtual_reality'] * vr_sessions
        
        # Total cost
        total_cost = trampoline_cost + bowling_cost + vr_cost
        return total_cost


def main():
    """Main function to run the cost calculation."""
    playland = PlaylandKenya()
    
    # Input data
    num_people = 4  # Example: 4 family members
    trampoline_sessions = 2  # Example: 2 sessions
    bowling_games = 1  # Example: 1 game
    vr_sessions = 1  # Example: 1 session
    
    try:
        total_cost = playland.calculate_total_cost(num_people, trampoline_sessions, bowling_games, vr_sessions)
        print(f"The total cost for the visit is: Ksh {total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
