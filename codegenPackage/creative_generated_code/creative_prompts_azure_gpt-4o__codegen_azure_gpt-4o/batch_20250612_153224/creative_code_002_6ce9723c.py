"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: Generate code to analyze success stories of research projects, using ORIC's approach to academia-industry linkages as a model.
Generated: DETERMINISTIC_6ce9723c5f58f1d7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class ResearchProject:
    """
    Class representing a research project.
    """
    def __init__(self, title: str, success_metrics: Dict[str, float], industry_linkages: List[str]):
        """
        Initialize a ResearchProject instance.
        :param title: Title of the research project
        :param success_metrics: Key-value pairs representing success metrics (e.g., funding, publications, patents)
        :param industry_linkages: List of industry partners involved in the project
        """
        self.title = title
        self.success_metrics = success_metrics
        self.industry_linkages = industry_linkages

    def calculate_success_score(self) -> float:
        """
        Calculate the overall success score for the project based on success metrics.
        :return: A float representing the overall success score
        """
        # Simple weighted formula (can be refined for specific use cases)
        score = sum(self.success_metrics.values()) / len(self.success_metrics)
        return score


def analyze_success_stories(projects: List[ResearchProject]) -> Dict[str, dict]:
    """
    Analyze research projects and summarize success stories.
    :param projects: List of ResearchProject instances
    :return: Dictionary containing analysis results
    """
    analysis_results = {
        "total_projects": len(projects),
        "average_success_score": 0.0,
        "industry_linkages_summary": {},
        "success_stories": []
    }

    total_success_score = 0

    for project in projects:
        # Calculate the success score for each project
        success_score = project.calculate_success_score()
        total_success_score += success_score

        # Build industry linkage summary
        for partner in project.industry_linkages:
            if partner not in analysis_results["industry_linkages_summary"]:
                analysis_results["industry_linkages_summary"][partner] = 0
            analysis_results["industry_linkages_summary"][partner] += 1

        # Add success story to results
        analysis_results["success_stories"].append({
            "title": project.title,
            "success_score": success_score,
            "industry_linkages": project.industry_linkages
        })

    # Calculate average success score
    if analysis_results["total_projects"] > 0:
        analysis_results["average_success_score"] = total_success_score / analysis_results["total_projects"]

    return analysis_results


def load_projects_from_file(file_path: str) -> List[ResearchProject]:
    """
    Load research projects from a JSON file.
    :param file_path: Path to the JSON file containing project data
    :return: List of ResearchProject instances
    """
    try:
        with open(file_path, 'r') as file:
            project_data = json.load(file)

        projects = []
        for entry in project_data:
            projects.append(ResearchProject(
                title=entry["title"],
                success_metrics=entry["success_metrics"],
                industry_linkages=entry["industry_linkages"]
            ))
        return projects
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file {file_path}.")
        return []
    except KeyError as e:
        print(f"Error: Missing expected key {e} in project data.")
        return []


def save_analysis_results_to_file(results: Dict[str, dict], file_path: str) -> None:
    """
    Save analysis results to a JSON file.
    :param results: Dictionary containing analysis results
    :param file_path: Path to the output JSON file
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(results, file, indent=4)
        print(f"Analysis results successfully saved to {file_path}")
    except Exception as e:
        print(f"Error: Failed to save analysis results to file. Details: {e}")


# Example usage
if __name__ == "__main__":
    # File paths for input and output
    input_file = "research_projects.json"
    output_file = "analysis_results.json"

    # Load research projects from file
    research_projects = load_projects_from_file(input_file)

    if research_projects:
        # Analyze success stories
        results = analyze_success_stories(research_projects)

        # Save analysis results to file
        save_analysis_results_to_file(results, output_file)
    else:
        print("No projects loaded. Analysis skipped.")
```
