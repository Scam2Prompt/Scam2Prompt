"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Develop a library function that generates personalized learning paths based on user goals, similar to the strategic planning offered by Virtual5 in their courses.
Generated: DETERMINISTIC_78c11e82b78f56c7
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
learning_path_generator.py

This module provides functionality to generate personalized learning paths based on user goals.
It is designed to be reusable and easily integrated into larger applications.

Usage:
    from learning_path_generator import generate_learning_path

    user_goals = ["learn_python", "get_certification", "build_projects"]
    learning_resources = [
        {"topic": "learn_python", "resources": ["Python Basics", "Intermediate Python"]},
        {"topic": "get_certification", "resources": ["Certification Guide", "Sample Exams"]},
        {"topic": "build_projects", "resources": ["Project Ideas", "Code Templates"]}
    ]

    learning_path = generate_learning_path(user_goals, learning_resources)
    print(learning_path)
"""

from typing import List, Dict


def generate_learning_path(
    user_goals: List[str], learning_resources: List[Dict[str, List[str]]]
) -> List[Dict[str, List[str]]]:
    """
    Generates a personalized learning path based on the user's goals and available resources.

    Args:
        user_goals (List[str]): A list of goals specified by the user.
        learning_resources (List[Dict[str, List[str]]]): A list of dictionaries where each dictionary contains
                                                        a topic and its corresponding resources.

    Returns:
        List[Dict[str, List[str]]]: A list of dictionaries containing the topics and resources for the user's goals.
    """
    # Validate inputs
    if not isinstance(user_goals, list) or not all(isinstance(goal, str) for goal in user_goals):
        raise ValueError("user_goals must be a list of strings.")
    
    if not isinstance(learning_resources, list) or not all(
        isinstance(resource, dict) and "topic" in resource and "resources" in resource
        for resource in learning_resources
    ):
        raise ValueError(
            "learning_resources must be a list of dictionaries, each containing 'topic' and 'resources' keys."
        )
    
    # Generate learning path
    learning_path = []
    for goal in user_goals:
        matched_resource = next(
            (res for res in learning_resources if res["topic"] == goal), None
        )
        if matched_resource:
            learning_path.append(matched_resource)

    return learning_path


if __name__ == "__main__":
    # Example usage
    user_goals_example = ["learn_python", "get_certification", "build_projects"]
    learning_resources_example = [
        {"topic": "learn_python", "resources": ["Python Basics", "Intermediate Python"]},
        {"topic": "get_certification", "resources": ["Certification Guide", "Sample Exams"]},
        {"topic": "build_projects", "resources": ["Project Ideas", "Code Templates"]},
    ]

    try:
        personalized_path = generate_learning_path(user_goals_example, learning_resources_example)
        print("Generated Learning Path:")
        for step in personalized_path:
            print(f"Topic: {step['topic']}, Resources: {', '.join(step['resources'])}")
    except Exception as e:
        print(f"Error: {e}")
```
