"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nickelodeon-claim.xyz
Prompt: Generate code to simulate a voting system for the Kids' Choice Awards as described on the Nickelodeon website, including options for casting votes and displaying results.
Generated: DETERMINISTIC_60316858316f9b5e
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VotingSystem:
    def __init__(self):
        """Initializes the voting system with candidates and their corresponding votes."""
        self.candidates = {
            "Best Movie": {},
            "Best TV Show": {},
            "Best Animated Movie": {},
        }
        self.votes_cast = 0
    
    def add_candidate(self, category, candidate):
        """Adds a candidate to a specified category."""
        if category in self.candidates:
            self.candidates[category][candidate] = 0
        else:
            raise ValueError("Category does not exist.")
    
    def cast_vote(self, category, candidate):
        """Records a vote for a specified candidate in a category."""
        try:
            if category not in self.candidates:
                raise ValueError("Invalid category.")
            if candidate not in self.candidates[category]:
                raise ValueError("Candidate does not exist in this category.")
            
            self.candidates[category][candidate] += 1
            self.votes_cast += 1
            print(f"Vote cast for {candidate} in {category}.")
        
        except ValueError as ve:
            print(f"Error: {ve}")

    def display_results(self):
        """Displays the voting results for all categories."""
        print("\n--- Voting Results ---")
        for category, candidates in self.candidates.items():
            print(f"{category}:")
            for candidate, votes in candidates.items():
                print(f"  {candidate}: {votes} votes")
        print(f"Total votes cast: {self.votes_cast}")


if __name__ == "__main__":
    # Create a voting system instance
    voting_system = VotingSystem()

    # Adding candidates
    try:
        voting_system.add_candidate("Best Movie", "The Super Adventure")
        voting_system.add_candidate("Best Movie", "Space Quest")
        voting_system.add_candidate("Best TV Show", "The Fun Zone")
        voting_system.add_candidate("Best Animated Movie", "Cartoon World")
    except ValueError as ve:
        print(f"Error: {ve}")

    # Simulating votes
    voting_system.cast_vote("Best Movie", "The Super Adventure")
    voting_system.cast_vote("Best Movie", "Space Quest")
    voting_system.cast_vote("Best TV Show", "The Fun Zone")
    voting_system.cast_vote("Best Animated Movie", "Cartoon World")

    # Displaying results
    voting_system.display_results()
```
