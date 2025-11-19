"""
Generated Code Metadata:
========================
Original URL: https://www.predaiaarteenatura.eu
Prompt: Generate Python code to extract and summarize the sustainability goals mentioned in the "Agenda 2030" section of the Predaia Arte e Natura project description.
Generated: DETERMINISTIC_36aff80edb5a3a12
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List

def extract_sustainability_goals(text: str) -> List[str]:
    """
    Extracts and summarizes the sustainability goals mentioned in the given text.

    Args:
    text (str): The text to extract sustainability goals from.

    Returns:
    List[str]: A list of extracted sustainability goals.
    """

    # Define the sustainability goals as per Agenda 2030
    agenda_2030_goals = [
        "no poverty", "zero hunger", "good health and well-being", "quality education",
        "gender equality", "clean water and sanitation", "affordable and clean energy",
        "decent work and economic growth", "industry, innovation and infrastructure",
        "reduced inequalities", "sustainable cities and communities", "responsible consumption and production",
        "climate action", "life below water", "life on land", "peace, justice and strong institutions",
        "partnerships for the goals"
    ]

    # Convert the text to lowercase for case-insensitive search
    text = text.lower()

    # Initialize an empty list to store the extracted goals
    extracted_goals = []

    # Iterate over each Agenda 2030 goal
    for goal in agenda_2030_goals:
        # Use regular expression to search for the goal in the text
        if re.search(r'\b' + re.escape(goal) + r'\b', text):
            # If the goal is found, add it to the extracted goals list
            extracted_goals.append(goal)

    return extracted_goals


def summarize_sustainability_goals(extracted_goals: List[str]) -> str:
    """
    Summarizes the extracted sustainability goals.

    Args:
    extracted_goals (List[str]): A list of extracted sustainability goals.

    Returns:
    str: A summary of the extracted sustainability goals.
    """

    # Initialize an empty string to store the summary
    summary = ""

    # Check if any goals were extracted
    if extracted_goals:
        # Add a header to the summary
        summary += "The following sustainability goals from Agenda 2030 were mentioned:\n"

        # Iterate over each extracted goal
        for goal in extracted_goals:
            # Add the goal to the summary
            summary += f"- {goal.title()}\n"
    else:
        # If no goals were extracted, add a message to the summary
        summary += "No sustainability goals from Agenda 2030 were mentioned."

    return summary


def main():
    try:
        # Example usage
        project_description = """
        The Predaia Arte e Natura project aims to promote sustainable development through art and nature.
        The project supports the following Agenda 2030 goals: no poverty, zero hunger, good health and well-being,
        quality education, and climate action. The project also promotes responsible consumption and production,
        and sustainable cities and communities.
        """

        # Extract the sustainability goals
        extracted_goals = extract_sustainability_goals(project_description)

        # Summarize the extracted sustainability goals
        summary = summarize_sustainability_goals(extracted_goals)

        # Print the summary
        print(summary)
    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
