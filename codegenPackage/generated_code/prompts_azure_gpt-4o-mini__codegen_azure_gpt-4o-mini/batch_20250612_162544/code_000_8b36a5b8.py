"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: Generate a Python script to calculate the total cost for a family visiting Playland Kenya, including entry fees for the trampoline park, bowling, and virtual reality sessions.
Generated: DETERMINISTIC_8b36a5b8d016e388
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# playland_cost_calculator.py

class PlaylandCostCalculator:
    """
    A class to calculate the total cost for a family visiting Playland Kenya.
    """

    def __init__(self, entry_fee, trampoline_fee, bowling_fee, vr_fee):
        """
        Initializes the cost calculator with the fees for each activity.

        :param entry_fee: Entry fee for the trampoline park
        :param trampoline_fee: Fee for trampoline sessions
        :param bowling_fee: Fee for bowling sessions
        :param vr_fee: Fee for virtual reality sessions
        """
        self.entry_fee = entry_fee
        self.trampoline_fee = trampoline_fee
        self.bowling_fee = bowling_fee
        self.vr_fee = vr_fee

    def calculate_total_cost(self, num_people, num_trampoline_sessions, num_bowling_sessions, num_vr_sessions):
        """
        Calculates the total cost for the family visit.

        :param num_people: Number of people in the family
        :param num_trampoline_sessions: Number of trampoline sessions
        :param num_bowling_sessions: Number of bowling sessions
        :param num_vr_sessions: Number of virtual reality sessions
        :return: Total cost for the visit
        """
        try:
            # Validate input parameters
            if num_people < 1 or num_trampoline_sessions < 0 or num_bowling_sessions < 0 or num_vr_sessions < 0:
                raise ValueError("Number of people must be at least 1 and session counts cannot be negative.")

            # Calculate total cost
            total_cost = (self.entry_fee * num_people +
                           self.trampoline_fee * num_trampoline_sessions * num_people +
                           self.bowling_fee * num_bowling_sessions * num_people +
                           self.vr_fee * num_vr_sessions * num_people)

            return total_cost

        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    # Define the fees for each activity
    ENTRY_FEE = 500  # Entry fee per person
    TRAMPOLINE_FEE = 300  # Fee per trampoline session per person
    BOWLING_FEE = 400  # Fee per bowling session per person
    VR_FEE = 600  # Fee per VR session per person

    # Create an instance of the cost calculator
    calculator = PlaylandCostCalculator(ENTRY_FEE, TRAMPOLINE_FEE, BOWLING_FEE, VR_FEE)

    # Example input
    num_people = 4
    num_trampoline_sessions = 2
    num_bowling_sessions = 1
    num_vr_sessions = 1

    # Calculate total cost
    total_cost = calculator.calculate_total_cost(num_people, num_trampoline_sessions, num_bowling_sessions, num_vr_sessions)

    if total_cost is not None:
        print(f"The total cost for the family visit is: Ksh {total_cost}")

if __name__ == "__main__":
    main()
```
