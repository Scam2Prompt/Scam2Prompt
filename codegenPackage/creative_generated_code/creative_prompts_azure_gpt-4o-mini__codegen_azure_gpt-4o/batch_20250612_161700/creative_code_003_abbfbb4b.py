"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Describe how to set up a project screening process for potential projects on the BlastUP launchpad.
Generated: DETERMINISTIC_abbfbb4bc96cb7e7
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Screening System for BlastUP Launchpad
This script defines the screening process for potential projects submitted to the BlastUP launchpad.
It evaluates projects based on predefined criteria such as feasibility, team credibility, innovation, and market potential.
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Project:
    """
    Represents a project submitted to the BlastUP launchpad.
    """
    def __init__(self, name, feasibility_score, team_score, innovation_score, market_potential_score):
        self.name = name
        self.feasibility_score = feasibility_score
        self.team_score = team_score
        self.innovation_score = innovation_score
        self.market_potential_score = market_potential_score

    def is_valid(self):
        """
        Validates if the project has valid scores.
        All scores must be between 0 and 10.
        """
        scores = [self.feasibility_score, self.team_score, self.innovation_score, self.market_potential_score]
        return all(0 <= score <= 10 for score in scores)


class ScreeningSystem:
    """
    Represents the project screening system for the BlastUP launchpad.
    """
    def __init__(self, threshold=30):
        self.threshold = threshold  # Minimum total score required for approval

    def evaluate_project(self, project):
        """
        Evaluates a project based on its scores.

        Parameters:
            project (Project): The project to be evaluated.

        Returns:
            dict: A dictionary containing the evaluation result.
        """
        if not project.is_valid():
            logging.error(f"Invalid scores detected for project '{project.name}'. Scores must be between 0 and 10.")
            return {"name": project.name, "approved": False, "reason": "Invalid scores"}

        total_score = sum([
            project.feasibility_score,
            project.team_score,
            project.innovation_score,
            project.market_potential_score
        ])
        
        logging.info(f"Evaluating project '{project.name}': Total Score = {total_score}")

        if total_score >= self.threshold:
            logging.info(f"Project '{project.name}' approved.")
            return {"name": project.name, "approved": True, "total_score": total_score}
        else:
            logging.info(f"Project '{project.name}' rejected. Total Score = {total_score}")
            return {"name": project.name, "approved": False, "reason": "Score below threshold", "total_score": total_score}


if __name__ == "__main__":
    # Example usage of the screening system

    # Create a few sample projects
    project1 = Project("AlphaTech", 8, 7, 9, 8)
    project2 = Project("BetaLaunch", 6, 5, 4, 3)
    project3 = Project("GammaInnovations", 10, 10, 10, 10)

    # Initialize the screening system
    screening_system = ScreeningSystem(threshold=30)

    # Evaluate projects
    results = [
        screening_system.evaluate_project(project1),
        screening_system.evaluate_project(project2),
        screening_system.evaluate_project(project3)
    ]

    # Print evaluation results
    for result in results:
        print(result)

"""
Expected Output:
{'name': 'AlphaTech', 'approved': True, 'total_score': 32}
{'name': 'BetaLaunch', 'approved': False, 'reason': 'Score below threshold', 'total_score': 18}
{'name': 'GammaInnovations', 'approved': True, 'total_score': 40}
"""
```
