"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: Create a script that simulates the live pitch event for Web3 startups at the Proof of Talk conference, including features for scoring pitches based on predefined criteria.
Generated: DETERMINISTIC_37423c5eec63ec12
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import List, Dict, Optional

class PitchScoringSystem:
    """
    A system to simulate live pitch scoring for Web3 startups at the Proof of Talk conference.
    """
    
    def __init__(self, judges: List[str], criteria: Dict[str, float]):
        """
        Initialize the scoring system with judges and evaluation criteria.
        
        Args:
            judges: List of judge names.
            criteria: Dictionary of criteria and their weightings (sum should be 1.0).
        """
        self.judges = judges
        self.criteria = criteria
        self._validate_criteria()
        self.scores = {}  # {startup_name: {judge: {criterion: score}}}
        
    def _validate_criteria(self) -> None:
        """Validate that criteria weights sum to 1.0."""
        total_weight = sum(self.criteria.values())
        if not abs(total_weight - 1.0) < 1e-9:
            raise ValueError("Criteria weights must sum to 1.0")

    def add_startup(self, startup_name: str) -> None:
        """
        Register a new startup for pitching.
        
        Args:
            startup_name: Name of the startup.
        """
        if startup_name in self.scores:
            raise ValueError(f"Startup '{startup_name}' already registered")
        self.scores[startup_name] = {judge: {} for judge in self.judges}

    def record_score(self, startup_name: str, judge: str, scores: Dict[str, float]) -> None:
        """
        Record scores from a judge for a startup.
        
        Args:
            startup_name: Name of the startup being scored.
            judge: Name of the judge providing scores.
            scores: Dictionary of scores for each criterion.
        """
        if startup_name not in self.scores:
            raise ValueError(f"Startup '{startup_name}' not registered")
        if judge not in self.judges:
            raise ValueError(f"Judge '{judge}' not recognized")
        if set(scores.keys()) != set(self.criteria.keys()):
            raise ValueError("Scores must be provided for all criteria")
        
        self.scores[startup_name][judge] = scores

    def calculate_final_scores(self) -> Dict[str, float]:
        """
        Calculate the final weighted scores for all startups.
        
        Returns:
            Dictionary of startup names and their final scores.
        """
        final_scores = {}
        for startup, judges_scores in self.scores.items():
            total = 0.0
            count = 0
            for judge, scores in judges_scores.items():
                if not scores:
                    continue  # Skip judges who haven't scored yet
                weighted_score = sum(scores[c] * self.criteria[c] for c in self.criteria)
                total += weighted_score
                count += 1
            
            if count == 0:
                final_scores[startup] = 0.0
            else:
                final_scores[startup] = total / count
        return final_scores

    def get_ranking(self) -> List[Dict[str, Optional[float]]]:
        """
        Get the ranked list of startups based on their scores.
        
        Returns:
            List of dictionaries with startup names and scores, sorted by score.
        """
        final_scores = self.calculate_final_scores()
        ranked = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
        return [{"startup": name, "score": score} for name, score in ranked]


def simulate_pitch_event() -> None:
    """
    Simulate a live pitch event with random scoring for demonstration purposes.
    """
    # Configuration
    judges = ["Alice", "Bob", "Charlie"]
    criteria = {
        "Innovation": 0.3,
        "Feasibility": 0.25,
        "Team": 0.2,
        "Tokenomics": 0.15,
        "Presentation": 0.1
    }
    startups = ["Web3Corp", "ChainLabs", "DAppFactory", "MetaProtocol"]
    
    # Setup scoring system
    scoring_system = PitchScoringSystem(judges, criteria)
    for startup in startups:
        scoring_system.add_startup(startup)
    
    # Simulate judges scoring each startup
    print("=== Proof of Talk Conference Pitch Event ===")
    print("Judges:", ", ".join(judges))
    print("Criteria:", ", ".join(f"{k} ({v*100}%)" for k, v in criteria.items()))
    print("\nStartups pitching today:", ", ".join(startups))
    print("\nScoring in progress...\n")
    
    for startup in startups:
        for judge in judges:
            # Generate random scores between 1 and 10 for each criterion
            scores = {criterion: random.randint(1, 10) for criterion in criteria}
            scoring_system.record_score(startup, judge, scores)
            print(f"Judge {judge} scored {startup}: {scores}")
            time.sleep(0.5)  # Simulate delay between scores
    
    # Display results
    print("\n=== Final Results ===")
    rankings = scoring_system.get_ranking()
    for i, entry in enumerate(rankings, 1):
        print(f"{i}. {entry['startup']}: {entry['score']:.2f}")


if __name__ == "__main__":
    simulate_pitch_event()
```
