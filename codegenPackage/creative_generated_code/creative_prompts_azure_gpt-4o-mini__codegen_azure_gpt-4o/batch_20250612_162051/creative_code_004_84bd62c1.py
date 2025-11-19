"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: What are the best practices for using modern tools and equipment in infrastructure construction, and how can I document these in a project report?
Generated: DETERMINISTIC_84bd62c1f0db31a6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import datetime

def generate_report(best_practices, tools_used, project_name, author_name):
    """
    Generates a formatted project report for documenting best practices in modern infrastructure construction.

    :param best_practices: List of best practices (strings) for using modern tools in construction.
    :param tools_used: List of modern tools and equipment used in the project (strings).
    :param project_name: Name of the infrastructure project (string).
    :param author_name: Name of the person generating the report (string).
    :return: Formatted project report as a string.
    """

    # Validate input parameters
    if not isinstance(best_practices, list) or not all(isinstance(i, str) for i in best_practices):
        raise ValueError("best_practices must be a list of strings.")
    if not isinstance(tools_used, list) or not all(isinstance(i, str) for i in tools_used):
        raise ValueError("tools_used must be a list of strings.")
    if not isinstance(project_name, str):
        raise ValueError("project_name must be a string.")
    if not isinstance(author_name, str):
        raise ValueError("author_name must be a string.")

    # Get the current date and time for the report
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Start building the report
    report = []
    report.append(f"Project Report: {project_name}")
    report.append(f"Author: {author_name}")
    report.append(f"Date: {current_date}")
    report.append("\n--- Best Practices ---")
    for practice in best_practices:
        report.append(f"- {practice}")
    report.append("\n--- Tools and Equipment Used ---")
    for tool in tools_used:
        report.append(f"- {tool}")

    # Join report sections into a single formatted string
    return "\n".join(report)


def main():
    """
    Main function to demonstrate report generation.
    """

    # Example input data
    best_practices = [
        "Ensure proper safety protocols are implemented when using heavy machinery.",
        "Conduct regular maintenance checks on all equipment.",
        "Utilize digital project management tools for tracking progress.",
        "Train personnel on the use of modern construction technologies."
    ]

    tools_used = [
        "Excavators with GPS tracking systems",
        "Automated concrete mixers",
        "Drone-based surveying equipment",
        "3D modeling software"
    ]

    project_name = "Modern Infrastructure Development Project"
    author_name = "John Doe"

    try:
        # Generate the report
        report = generate_report(best_practices, tools_used, project_name, author_name)
        
        # Output the report
        print(report)
    except ValueError as e:
        # Handle input validation errors
        print(f"Error generating report: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
