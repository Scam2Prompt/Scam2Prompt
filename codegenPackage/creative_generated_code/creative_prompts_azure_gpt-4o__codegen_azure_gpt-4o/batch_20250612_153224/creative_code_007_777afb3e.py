"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npors.net
Prompt: Recommend tools or libraries for managing continuous support and project management tasks, tailored to the services described on npors.net.
Generated: DETERMINISTIC_777afb3eb225a8e7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to recommend tools or libraries for continuous support and project management tasks
based on the services described on npors.net. The script uses a predefined database of tools
and libraries for categorization and selection.

Language: Python
"""

# Import necessary libraries
import json

# Error Handling Definitions
class RecommendationError(Exception):
    """Custom exception for recommendation errors."""
    pass

# Tool Database (Mocked for demonstration)
TOOLS_DATABASE = [
    {
        "name": "Jira",
        "type": "Project Management",
        "features": ["Agile boards", "Scrum", "Kanban", "Reporting"],
        "recommendation_reason": "Great for team collaboration and tracking progress in real-time."
    },
    {
        "name": "Trello",
        "type": "Task Management",
        "features": ["Kanban boards", "Integrations", "Team collaboration"],
        "recommendation_reason": "Simple and intuitive for lightweight project management."
    },
    {
        "name": "Slack",
        "type": "Communication",
        "features": ["Messaging", "Integrations", "File sharing"],
        "recommendation_reason": "Perfect for team communication and integration with other tools."
    },
    {
        "name": "Asana",
        "type": "Project Management",
        "features": ["Task tracking", "Workflows", "Team dashboards"],
        "recommendation_reason": "Well-suited for managing complex projects and tasks."
    },
    {
        "name": "GitHub",
        "type": "Version Control",
        "features": ["Code repository", "Issue tracking", "Team collaboration"],
        "recommendation_reason": "Ideal for managing codebases and issues in software projects."
    }
]

def recommend_tools(service_descriptions):
    """
    Recommend tools based on provided service descriptions.

    Args:
        service_descriptions (list): List of strings describing the services provided.

    Returns:
        list: List of recommended tools.
    """
    try:
        # Validate input
        if not isinstance(service_descriptions, list) or not all(isinstance(desc, str) for desc in service_descriptions):
            raise RecommendationError("Invalid service descriptions provided. Must be a list of strings.")

        # Find matching tools
        recommendations = []
        for tool in TOOLS_DATABASE:
            # Check if the tool's features match the service descriptions
            if any(feature.lower() in desc.lower() for desc in service_descriptions for feature in tool["features"]):
                recommendations.append({
                    "name": tool["name"],
                    "type": tool["type"],
                    "reason": tool["recommendation_reason"]
                })

        # Handle case when no tools are matched
        if not recommendations:
            raise RecommendationError("No matching tools found for the provided service descriptions.")

        return recommendations

    except RecommendationError as re:
        # Log and return error message
        return {"error": str(re)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Mock service descriptions from npors.net (replace with actual descriptions)
    service_descriptions = [
        "Agile project management",
        "Team collaboration",
        "Lightweight task monitoring",
        "Version control for software projects"
    ]

    # Get tool recommendations
    recommendations = recommend_tools(service_descriptions)

    # Output recommendations
    print(json.dumps(recommendations, indent=4))
```
