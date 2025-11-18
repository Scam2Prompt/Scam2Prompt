"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Create a script that simulates the live pitch event for Web3 startups at the Proof of Talk conference, including features for scoring pitches based on predefined criteria.
Generated: DETERMINISTIC_37423c5eec63ec12
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PitchEvent:
    """
    Class to simulate a live pitch event for Web3 startups.
    """
    def __init__(self, startups, criteria):
        """
        Initializes the event with startups and scoring criteria.
        :param startups: List of startup names participating in the pitch.
        :param criteria: List of criteria for scoring.
        """
        self.startups = startups
        self.criteria = criteria
        self.scores = {startup: {} for startup in startups}

    def simulate_pitch(self):
        """
        Simulates the pitch event and assigns scores based on criteria.
        """
        for startup in self.startups:
            print(f"\nPitching Startup: {startup}")
            print("-" * 30)
            for criterion in self.criteria:
                # Simulate score between 1 to 10 for each criterion
                score = random.randint(1, 10)
                self.scores[startup][criterion] = score
                print(f"{criterion}: {score}")

    def calculate_total_scores(self):
        """
        Calculates the total score for each startup.
        """
        for startup, scores in self.scores.items():
            self.scores[startup]['Total'] = sum(scores.values())

    def display_results(self):
        """
        Displays the pitch results sorted by total scores.
        """
        print("\nFinal Results:")
        print("=" * 30)
        sorted_results = sorted(self.scores.items(), key=lambda x: x[1]['Total'], reverse=True)
        for startup, scores in sorted_results:
            print(f"Startup: {startup}")
            for criterion, score in scores.items():
                print(f"  {criterion}: {score}")
            print("-" * 30)


def main():
    """
    Main function to run the pitch event simulation.
    """
    try:
        # List of startups participating
        startups = [
            "BlockChainX",
            "CryptoLab",
            "NFTopia",
            "Web3Innovators",
            "MetaMarket"
        ]

        # Predefined scoring criteria
        criteria = [
            "Innovation",
            "Market Potential",
            "Team Strength",
            "Presentation"
        ]

        print("Welcome to the Proof of Talk Web3 Startup Pitch Event!")
        print("=" * 50)

        # Initialize and simulate the event
        event = PitchEvent(startups, criteria)
        event.simulate_pitch()
        event.calculate_total_scores()
        event.display_results()

    except Exception as e:
        print(f"An error occurred during the event: {str(e)}")


if __name__ == "__main__":
    main()
```
