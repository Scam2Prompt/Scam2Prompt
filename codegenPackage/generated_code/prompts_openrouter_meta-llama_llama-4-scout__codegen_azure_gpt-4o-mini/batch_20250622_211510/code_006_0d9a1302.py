"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: "Compare and recommend software tools for designing and simulating sanitary infrastructure systems."
Generated: DETERMINISTIC_0d9a1302c30defe8
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class SoftwareTool:
    """
    A class to represent a software tool for designing and simulating sanitary infrastructure systems.
    """

    def __init__(self, name, features, cost, user_rating):
        """
        Initializes a new SoftwareTool instance.

        :param name: str - The name of the software tool.
        :param features: list - A list of features offered by the software.
        :param cost: float - The cost of the software tool.
        :param user_rating: float - The user rating of the software tool (1 to 5).
        """
        self.name = name
        self.features = features
        self.cost = cost
        self.user_rating = user_rating

    def __repr__(self):
        return f"{self.name} (Rating: {self.user_rating}, Cost: ${self.cost})"


def compare_tools(tools):
    """
    Compares a list of software tools and recommends the best one based on user rating and cost.

    :param tools: list - A list of SoftwareTool instances to compare.
    :return: SoftwareTool - The recommended software tool.
    """
    if not tools:
        raise ValueError("The tools list cannot be empty.")

    # Sort tools by user rating (descending) and then by cost (ascending)
    sorted_tools = sorted(tools, key=lambda x: (-x.user_rating, x.cost))

    # Return the top recommended tool
    return sorted_tools[0]


def main():
    """
    Main function to execute the comparison of software tools.
    """
    # List of software tools with their features, cost, and user ratings
    tools = [
        SoftwareTool("Tool A", ["3D Modeling", "Simulation", "Reporting"], 1500, 4.5),
        SoftwareTool("Tool B", ["2D Design", "Cost Estimation"], 1200, 4.0),
        SoftwareTool("Tool C", ["Simulation", "Data Analysis"], 1800, 4.8),
        SoftwareTool("Tool D", ["3D Modeling", "Cost Estimation", "Reporting"], 900, 4.2),
    ]

    try:
        recommended_tool = compare_tools(tools)
        print(f"Recommended Software Tool: {recommended_tool}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
