"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Generate code to simulate the impact of third-party candidates on election outcomes in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_ba0cfa0e2aea32e3
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from collections import defaultdict

class ElectionSimulation:
    def __init__(self, total_voters, candidates):
        """
        Initialize the election simulation.
        
        :param total_voters: Total number of voters participating in the election.
        :param candidates: List of candidate names including third-party candidates.
        """
        self.total_voters = total_voters
        self.candidates = candidates
        self.votes = defaultdict(int)
    
    def simulate_voting(self):
        """
        Simulates the voting process by randomly distributing votes among candidates.
        """
        for _ in range(self.total_voters):
            # Simulate a voter randomly choosing a candidate
            chosen_candidate = random.choice(self.candidates)
            self.votes[chosen_candidate] += 1

    def calculate_results(self):
        """
        Calculate election results as percentages.
        
        :return: Dictionary with candidates and their percentage of votes.
        """
        results = {}
        for candidate, vote_count in self.votes.items():
            # Calculate percentage of votes for each candidate
            results[candidate] = (vote_count / self.total_voters) * 100
        return results

    def display_results(self):
        """
        Display the election results in a sorted manner.
        """
        print("Election Results:")
        for candidate, percentage in sorted(self.calculate_results().items(), key=lambda x: x[1], reverse=True):
            print(f"{candidate}: {percentage:.2f}%")

# Error handling for invalid user inputs
def get_simulation_inputs():
    """
    Collect inputs from the user for total voters and candidate names.
    
    :return: Total voters and list of candidates.
    """
    try:
        total_voters = int(input("Enter the total number of voters: "))
        if total_voters <= 0:
            raise ValueError("Total voters must be a positive integer.")
        
        # Collect candidate names
        print("Enter candidate names (including third-party candidates), separated by commas:")
        candidates = input().split(',')
        candidates = [candidate.strip() for candidate in candidates if candidate.strip()]
        
        if len(candidates) < 2:
            raise ValueError("There must be at least two candidates.")
        
        return total_voters, candidates
    except ValueError as e:
        print(f"Error: {e}")
        return get_simulation_inputs()

def main():
    """
    Main function to run the election simulation.
    """
    print("McHenry County Election Simulation - Impact of Third-Party Candidates")
    
    # Get inputs from the user
    total_voters, candidates = get_simulation_inputs()
    
    # Initialize the simulation
    simulation = ElectionSimulation(total_voters, candidates)
    
    # Run the simulation
    simulation.simulate_voting()
    
    # Display results
    simulation.display_results()

if __name__ == "__main__":
    main()
```
