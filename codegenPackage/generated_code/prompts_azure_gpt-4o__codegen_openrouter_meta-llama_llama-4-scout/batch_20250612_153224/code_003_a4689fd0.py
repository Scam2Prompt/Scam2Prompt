"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Write a script to calculate the estimated budget for an interior design project, including architectural, structural, and MEP (Mechanical, Electrical, Plumbing) technical drawings, as outlined in Nyiku Design's pricing plans.
Generated: DETERMINISTIC_a4689fd0151fbb3b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# interior_design_budget_calculator.py

class InteriorDesignProject:
    def __init__(self, project_name, location, project_size_sqft):
        """
        Initialize an interior design project.

        Args:
            project_name (str): Name of the project.
            location (str): Location of the project.
            project_size_sqft (float): Size of the project in square feet.
        """
        self.project_name = project_name
        self.location = location
        self.project_size_sqft = project_size_sqft

    def calculate_architectural_drawing_cost(self, rate_per_sqft):
        """
        Calculate the cost of architectural technical drawings.

        Args:
            rate_per_sqft (float): Rate per square foot.

        Returns:
            float: Cost of architectural technical drawings.
        """
        return self.project_size_sqft * rate_per_sqft

    def calculate_structural_drawing_cost(self, rate_per_sqft):
        """
        Calculate the cost of structural technical drawings.

        Args:
            rate_per_sqft (float): Rate per square foot.

        Returns:
            float: Cost of structural technical drawings.
        """
        return self.project_size_sqft * rate_per_sqft

    def calculate_mep_drawing_cost(self, rate_per_sqft):
        """
        Calculate the cost of MEP (Mechanical, Electrical, Plumbing) technical drawings.

        Args:
            rate_per_sqft (float): Rate per square foot.

        Returns:
            float: Cost of MEP technical drawings.
        """
        return self.project_size_sqft * rate_per_sqft


class NyikuDesignPricing:
    def __init__(self):
        """
        Initialize Nyiku Design's pricing plans.
        """
        self.pricing_plans = {
            "residential": {
                "architectural": 2.50,
                "structural": 1.50,
                "mep": 2.00
            },
            "commercial": {
                "architectural": 3.00,
                "structural": 2.00,
                "mep": 2.50
            }
        }

    def get_rate(self, project_type, drawing_type):
        """
        Get the rate for a specific project type and drawing type.

        Args:
            project_type (str): Type of project (residential or commercial).
            drawing_type (str): Type of drawing (architectural, structural, or mep).

        Returns:
            float: Rate per square foot.

        Raises:
            ValueError: If project type or drawing type is not found.
        """
        try:
            return self.pricing_plans[project_type][drawing_type]
        except KeyError:
            raise ValueError("Invalid project type or drawing type")


def calculate_budget(project_name, location, project_size_sqft, project_type):
    """
    Calculate the estimated budget for an interior design project.

    Args:
        project_name (str): Name of the project.
        location (str): Location of the project.
        project_size_sqft (float): Size of the project in square feet.
        project_type (str): Type of project (residential or commercial).

    Returns:
        dict: Estimated budget for the project.

    Raises:
        ValueError: If project type is not found.
    """
    nyiku_design_pricing = NyikuDesignPricing()
    project = InteriorDesignProject(project_name, location, project_size_sqft)

    try:
        architectural_rate = nyiku_design_pricing.get_rate(project_type, "architectural")
        structural_rate = nyiku_design_pricing.get_rate(project_type, "structural")
        mep_rate = nyiku_design_pricing.get_rate(project_type, "mep")

        architectural_cost = project.calculate_architectural_drawing_cost(architectural_rate)
        structural_cost = project.calculate_structural_drawing_cost(structural_rate)
        mep_cost = project.calculate_mep_drawing_cost(mep_rate)

        total_cost = architectural_cost + structural_cost + mep_cost

        return {
            "project_name": project_name,
            "project_type": project_type,
            "architectural_cost": architectural_cost,
            "structural_cost": structural_cost,
            "mep_cost": mep_cost,
            "total_cost": total_cost
        }
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    project_name = "Example Project"
    location = "New York"
    project_size_sqft = 1000
    project_type = "residential"

    budget = calculate_budget(project_name, location, project_size_sqft, project_type)

    if budget:
        print("Estimated Budget:")
        print(f"Project Name: {budget['project_name']}")
        print(f"Project Type: {budget['project_type']}")
        print(f"Architectural Cost: ${budget['architectural_cost']:.2f}")
        print(f"Structural Cost: ${budget['structural_cost']:.2f}")
        print(f"MEP Cost: ${budget['mep_cost']:.2f}")
        print(f"Total Cost: ${budget['total_cost']:.2f}")


if __name__ == "__main__":
    main()
```
