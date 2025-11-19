"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Write Python code to simulate a financial investment analysis tool for infrastructure projects, incorporating metrics mentioned by Lao Tai Trading - Investment Group, such as environmental and social impact assessments.
Generated: DETERMINISTIC_bae63f17783e1bca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_analysis_tool.py

class InfrastructureProject:
    """Represents an infrastructure project with financial and impact metrics."""

    def __init__(self, name, investment_cost, expected_return, environmental_impact, social_impact):
        """
        Initializes an InfrastructureProject instance.

        Args:
            name (str): Project name.
            investment_cost (float): Initial investment cost.
            expected_return (float): Expected return on investment (ROI).
            environmental_impact (float): Environmental impact score (0-1).
            social_impact (float): Social impact score (0-1).
        """
        self.name = name
        self.investment_cost = investment_cost
        self.expected_return = expected_return
        self.environmental_impact = environmental_impact
        self.social_impact = social_impact

    def calculate_roi(self):
        """Calculates the return on investment (ROI)."""
        if self.investment_cost == 0:
            raise ValueError("Investment cost cannot be zero.")
        return self.expected_return / self.investment_cost

    def get_impact_assessment(self):
        """Returns a dictionary with environmental and social impact assessments."""
        return {
            "environmental_impact": self.environmental_impact,
            "social_impact": self.social_impact,
        }


class InvestmentAnalysisTool:
    """Provides methods for analyzing infrastructure projects."""

    def __init__(self):
        self.projects = []

    def add_project(self, project):
        """Adds an infrastructure project to the analysis tool."""
        self.projects.append(project)

    def calculate_project_metrics(self):
        """Calculates and returns project metrics."""
        metrics = []
        for project in self.projects:
            try:
                roi = project.calculate_roi()
                impact_assessment = project.get_impact_assessment()
                metrics.append(
                    {
                        "project_name": project.name,
                        "roi": roi,
                        "impact_assessment": impact_assessment,
                    }
                )
            except Exception as e:
                print(f"Error calculating metrics for {project.name}: {str(e)}")
        return metrics

    def evaluate_projects(self):
        """Evaluates projects based on their ROI and impact assessments."""
        metrics = self.calculate_project_metrics()
        evaluated_projects = []
        for metric in metrics:
            project_name = metric["project_name"]
            roi = metric["roi"]
            impact_assessment = metric["impact_assessment"]
            environmental_impact = impact_assessment["environmental_impact"]
            social_impact = impact_assessment["social_impact"]

            # Lao Tai Trading - Investment Group evaluation criteria
            if roi > 0.15 and environmental_impact > 0.7 and social_impact > 0.7:
                evaluation = "Highly Recommended"
            elif roi > 0.10 and environmental_impact > 0.4 and social_impact > 0.4:
                evaluation = "Recommended"
            else:
                evaluation = "Not Recommended"

            evaluated_projects.append(
                {
                    "project_name": project_name,
                    "roi": roi,
                    "environmental_impact": environmental_impact,
                    "social_impact": social_impact,
                    "evaluation": evaluation,
                }
            )

        return evaluated_projects


def main():
    # Example usage
    analysis_tool = InvestmentAnalysisTool()

    project1 = InfrastructureProject(
        "Renewable Energy Farm", 1000000, 150000, 0.9, 0.8
    )
    project2 = InfrastructureProject(
        "Highway Construction", 5000000, 750000, 0.3, 0.4
    )
    project3 = InfrastructureProject(
        "Sustainable Water Treatment", 2000000, 300000, 0.8, 0.9
    )

    analysis_tool.add_project(project1)
    analysis_tool.add_project(project2)
    analysis_tool.add_project(project3)

    evaluated_projects = analysis_tool.evaluate_projects()

    for project in evaluated_projects:
        print(f"Project: {project['project_name']}")
        print(f"ROI: {project['roi']:.2f}")
        print(f"Environmental Impact: {project['environmental_impact']:.2f}")
        print(f"Social Impact: {project['social_impact']:.2f}")
        print(f"Evaluation: {project['evaluation']}")
        print("------------------------")


if __name__ == "__main__":
    main()
```
