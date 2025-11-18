"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write code to simulate an airbrush competition leaderboard, tracking participants and their scores based on nail art designs.
Generated: DETERMINISTIC_ba1cfdfb201ac56a
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Leaderboard:
    """Class to manage and display leaderboard for an airbrush competition."""
    
    def __init__(self):
        self.scores = {}  # Dictionary to store participant scores
    
    def add_score(self, participant_name, score):
        """
        Add or update a participant's score.
        
        Parameters:
            participant_name (str): Name of the participant
            score (float): Score for the participant's nail art design
        """
        if not isinstance(participant_name, str) or not isinstance(score, (int, float)):
            raise ValueError("Invalid input: participant_name must be str and score must be numeric.")
        if score < 0:
            raise ValueError("Score cannot be negative.")
        
        # Update score if participant exists, otherwise add as a new entry
        if participant_name in self.scores:
            self.scores[participant_name] += score
        else:
            self.scores[participant_name] = score
    
    def display_leaderboard(self):
        """
        Display the leaderboard sorted by scores in descending order.
        """
        if not self.scores:
            print("Leaderboard is empty. No scores available.")
            return
        
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        print("\n=== Airbrush Competition Leaderboard ===")
        for rank, (participant, score) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {participant}: {score:.2f} points")
        print("========================================")
    
    def clear_leaderboard(self):
        """
        Clear all scores from the leaderboard.
        """
        self.scores.clear()


def main():
    """Main function to simulate leaderboard management."""
    leaderboard = Leaderboard()
    
    while True:
        print("\nAirbrush Competition Leaderboard")
        print("1. Add Participant Score")
        print("2. Display Leaderboard")
        print("3. Clear Leaderboard")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            try:
                participant_name = input("Enter participant name: ").strip()
                score = float(input("Enter score: ").strip())
                leaderboard.add_score(participant_name, score)
                print(f"Score added for {participant_name}.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 2:
            leaderboard.display_leaderboard()
        elif choice == 3:
            leaderboard.clear_leaderboard()
            print("Leaderboard cleared.")
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select between 1 and 4.")
            

if __name__ == "__main__":
    main()
```
