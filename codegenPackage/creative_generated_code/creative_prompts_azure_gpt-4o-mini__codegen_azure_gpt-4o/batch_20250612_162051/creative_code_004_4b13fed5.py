"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venoms-1zv.pages.dev
Prompt: How do I implement the judging criteria for the TokenForge hackathon, specifically focusing on trading volumes and technical implementation?
Generated: DETERMINISTIC_4b13fed5edc9ad4e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the clean, production-ready Python code for implementing judging criteria for the TokenForge hackathon based on trading volumes and technical implementation:

```python
import json


class HackathonJudging:
    """
    Class to evaluate TokenForge hackathon projects based on specified criteria:
    - Trading Volume
    - Technical Implementation
    """

    def __init__(self):
        """
        Initialize the judging system with an empty list of projects.
        Each project will be a dictionary containing its relevant data.
        """
        self.projects = []

    def add_project(self, name, trading_volume, technical_score):
        """
        Add a project to the hackathon judging system.

        :param name: Name of the project (string)
        :param trading_volume: Trading volume of the project (float, higher is better)
        :param technical_score: Technical implementation score (int, scale of 1-100)
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Project name must be a non-empty string.")
        if not isinstance(trading_volume, (int, float)) or trading_volume < 0:
            raise ValueError("Trading volume must be a non-negative number.")
        if not isinstance(technical_score, int) or not (0 <= technical_score <= 100):
            raise ValueError("Technical score must be an integer between 0 and 100.")

        self.projects.append({
            "name": name,
            "trading_volume": trading_volume,
            "technical_score": technical_score
        })

    def evaluate_projects(self):
        """
        Evaluate and rank projects based on trading volume and technical implementation.

        :return: List of projects sorted by their total score (descending order).
        """
        if not self.projects:
            raise ValueError("No projects available for evaluation.")

        # Compute total score (weighted) for each project
        for project in self.projects:
            # 70% weight for trading volume, 30% weight for technical implementation
            project['total_score'] = (
                0.7 * project['trading_volume'] + 0.3 * project['technical_score']
            )

        # Sort projects by total score in descending order
        ranked_projects = sorted(self.projects, key=lambda p: p['total_score'], reverse=True)
        return ranked_projects

    def display_results(self, ranked_projects):
        """
        Display the results of the evaluation in a human-readable format.

        :param ranked_projects: List of ranked projects.
        """
        print("Hackathon Judging Results:")
        print("=" * 30)
        for rank, project in enumerate(ranked_projects, start=1):
            print(f"Rank {rank}: {project['name']}")
            print(f"  Trading Volume: {project['trading_volume']}")
            print(f"  Technical Score: {project['technical_score']}")
            print(f"  Total Score: {project['total_score']:.2f}")
            print("-" * 30)

    def save_results_to_file(self, ranked_projects, file_name="judging_results.json"):
        """
        Save the ranked project results to a JSON file.

        :param ranked_projects: List of ranked projects.
        :param file_name: Name of the file to save results (default: judging_results.json)
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(ranked_projects, file, indent=4)
            print(f"Results have been saved to {file_name}")
        except Exception as e:
            print(f"Error saving results to file: {e}")


# Example usage (Uncomment to run):
if __name__ == "__main__":
    judging = HackathonJudging()

    # Add projects (name, trading volume, technical score)
    judging.add_project("Project Alpha", 1500.75, 85)
    judging.add_project("Project Beta", 3000.50, 90)
    judging.add_project("Project Gamma", 1200.30, 95)

    # Evaluate and rank projects
    ranked_projects = judging.evaluate_projects()

    # Display results
    judging.display_results(ranked_projects)

    # Save results to a file
    judging.save_results_to_file(ranked_projects)
```

This code satisfies all the criteria mentioned and is ready for use in a production environment.
