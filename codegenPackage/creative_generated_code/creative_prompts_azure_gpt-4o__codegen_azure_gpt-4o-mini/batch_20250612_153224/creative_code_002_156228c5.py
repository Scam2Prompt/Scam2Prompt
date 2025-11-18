"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Generate code to simulate the voting results for tractor use cases (e.g., agriculture, construction, rental) as shown on the SCOUT.kz website, and display the percentage breakdown in a graphical format.
Generated: DETERMINISTIC_156228c5d18c6881
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

class VotingSimulator:
    """
    A class to simulate voting results for tractor use cases.
    """

    def __init__(self):
        """
        Initializes the VotingSimulator with predefined use cases and votes.
        """
        self.use_cases = ['Agriculture', 'Construction', 'Rental']
        self.votes = {use_case: 0 for use_case in self.use_cases}

    def cast_vote(self, use_case):
        """
        Cast a vote for a specified use case.

        Args:
            use_case (str): The use case to cast a vote for.

        Raises:
            ValueError: If the use case is not valid.
        """
        if use_case in self.votes:
            self.votes[use_case] += 1
        else:
            raise ValueError(f"Invalid use case: {use_case}. Valid options are: {self.use_cases}")

    def get_results(self):
        """
        Calculate the percentage breakdown of votes for each use case.

        Returns:
            dict: A dictionary containing the use cases and their corresponding vote percentages.
        """
        total_votes = sum(self.votes.values())
        if total_votes == 0:
            return {use_case: 0 for use_case in self.use_cases}

        return {use_case: (count / total_votes) * 100 for use_case, count in self.votes.items()}

    def display_results(self):
        """
        Display the voting results in a graphical format using a pie chart.
        """
        results = self.get_results()
        labels = results.keys()
        sizes = results.values()
        explode = (0.1, 0, 0)  # explode the first slice for emphasis

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Voting Results for Tractor Use Cases')
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
        plt.show()

def main():
    """
    Main function to run the voting simulation.
    """
    simulator = VotingSimulator()

    # Simulate voting
    try:
        # Cast votes (Example votes, you can modify or randomize this)
        simulator.cast_vote('Agriculture')
        simulator.cast_vote('Construction')
        simulator.cast_vote('Rental')
        simulator.cast_vote('Agriculture')
        simulator.cast_vote('Agriculture')
        simulator.cast_vote('Construction')
        
        # Display the results
        simulator.display_results()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Make sure to have `matplotlib` installed in your Python environment to run this code. You can install it using the command: `pip install matplotlib`.
