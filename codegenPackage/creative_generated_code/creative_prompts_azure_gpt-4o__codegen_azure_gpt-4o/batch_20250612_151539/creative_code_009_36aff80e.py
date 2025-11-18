"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.predaiaarteenatura.eu
Prompt: Generate Python code to extract and summarize the sustainability goals mentioned in the "Agenda 2030" section of the Predaia Arte e Natura project description.
Generated: DETERMINISTIC_36aff80edb5a3a12
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def extract_sustainability_goals(project_description):
    """
    Extract and summarize sustainability goals from the "Agenda 2030" section
    of the project description.

    Args:
        project_description (str): The full text of the project description.

    Returns:
        list: A list of extracted sustainability goals as strings.
    """
    try:
        # Check if the input is valid
        if not isinstance(project_description, str):
            raise ValueError("Input must be a string containing the project description.")

        # Extract the "Agenda 2030" section using a regular expression
        agenda_2030_pattern = r"Agenda 2030 section:(.*?)(?:Section|End of Description|$)"
        match = re.search(agenda_2030_pattern, project_description, re.IGNORECASE | re.DOTALL)
        
        if not match:
            raise ValueError("Could not find 'Agenda 2030' section in the provided description.")

        agenda_2030_text = match.group(1).strip()  # Extract the text of the Agenda 2030 section

        # Split the section into individual goals using bullet points, numbers, or other delimiters
        goals = re.split(r'\n\s*(?:-|\d+\.)\s*', agenda_2030_text)
        goals = [goal.strip() for goal in goals if goal.strip()]  # Clean up whitespace and empty lines

        return goals

    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    # Simulated project description containing the "Agenda 2030" section
    project_description = """
    Predaia Arte e Natura Project Description

    Agenda 2030 section:
    - Promote sustainable agriculture practices to preserve biodiversity.
    - Ensure access to clean water for all communities in the region.
    - Reduce greenhouse gas emissions by adopting renewable energy sources.
    - Foster education and awareness about environmental conservation.
    Section: Next Steps

    End of Description
    """

    # Extract and summarize goals
    sustainability_goals = extract_sustainability_goals(project_description)
    print("Sustainability Goals from Agenda 2030:")
    for i, goal in enumerate(sustainability_goals, start=1):
        print(f"{i}. {goal}")
```
