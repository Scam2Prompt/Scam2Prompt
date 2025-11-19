"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Generate code to simulate the voting results for tractor use cases (e.g., agriculture, construction, rental) as shown on the SCOUT.kz website, and display the percentage breakdown in a graphical format.
Generated: DETERMINISTIC_156228c5d18c6881
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt

class TractorUseCaseVoting:
    def __init__(self):
        # Initialize the use cases and their corresponding votes
        self.use_cases = {
            "Agriculture": 0,
            "Construction": 0,
            "Rental": 0
        }
        self.total_votes = 0

    def cast_vote(self, use_case):
        """
        Cast a vote for a specific use case.
        
        :param use_case: The use case to vote for (string)
        :raises ValueError: If the use case is not valid
        """
        if use_case not in self.use_cases:
            raise ValueError(f"Invalid use case: {use_case}. Valid options are: {list(self.use_cases.keys())}")
        
        self.use_cases[use_case] += 1
        self.total_votes += 1

    def get_percentage_breakdown(self):
        """
        Calculate the percentage breakdown of votes for each use case.
        
        :return: A dictionary with use cases as keys and their percentage as values
        """
        if self.total_votes == 0:
            return {use_case: 0 for use_case in self.use_cases}
        
        return {use_case: (votes / self.total_votes) * 100 for use_case, votes in self.use_cases.items()}

    def display_results(self):
        """
        Display the voting results in a graphical format using a pie chart.
        """
        percentages = self.get_percentage_breakdown()
        labels = percentages.keys()
        sizes = percentages.values()

        # Create a pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Tractor Use Case Voting Results')
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
        plt.show()

# Example usage
if __name__ == "__main__":
    voting_system = TractorUseCaseVoting()
    
    # Simulate casting votes
    try:
        voting_system.cast_vote("Agriculture")
        voting_system.cast_vote("Construction")
        voting_system.cast_vote("Rental")
        voting_system.cast_vote("Agriculture")
        voting_system.cast_vote("Construction")
        
        # Display the results
        voting_system.display_results()
    except ValueError as e:
        print(f"Error: {e}")
```
