"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-defiant.com
Prompt: Draft a community petition advocating for better protection and support for citizens in a city facing law enforcement challenges.
Generated: DETERMINISTIC_858c06a9f4ca6a3a
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# petition_generator.py
# This script generates a community petition advocating for better protection and support for citizens
# in a city facing law enforcement challenges.

import datetime

def generate_petition(city_name, issue_description, proposed_solutions):
    """
    Generates a petition advocating for better protection and support for citizens.

    Args:
        city_name (str): Name of the city facing law enforcement challenges.
        issue_description (str): Description of the challenges faced by the citizens.
        proposed_solutions (list): List of proposed solutions for improving the situation.

    Returns:
        str: The formatted petition text.
    """

    # Validate inputs
    if not city_name or not isinstance(city_name, str):
        raise ValueError("City name must be a non-empty string.")
    if not issue_description or not isinstance(issue_description, str):
        raise ValueError("Issue description must be a non-empty string.")
    if not proposed_solutions or not isinstance(proposed_solutions, list):
        raise ValueError("Proposed solutions must be a non-empty list.")

    # Get current date
    current_date = datetime.datetime.now().strftime("%B %d, %Y")

    # Create petition text
    petition = f"""
Community Petition
Date: {current_date}

To the leadership of {city_name},

We, the undersigned, are writing to express our growing concern about the challenges faced by the residents of {city_name}.
Our community is in urgent need of better protection and support due to the following issue(s):

{issue_description}

We believe that immediate action is required to ensure the safety and well-being of our citizens. As a community, 
we propose the following solutions to address these challenges effectively:

"""
    for idx, solution in enumerate(proposed_solutions, start=1):
        petition += f"{idx}. {solution}\n"

    petition += """
We urge the relevant authorities to take these suggestions into consideration and work collaboratively with the community 
to implement the proposed changes. Our goal is to create a safe, equitable, and thriving environment for all residents of {city_name}.

Sincerely,
The Citizens of {city_name}
    """

    return petition

def save_petition_to_file(petition_text, file_name):
    """
    Saves the petition text to a file.

    Args:
        petition_text (str): The petition text to be saved.
        file_name (str): Name of the file where the petition will be saved.

    Raises:
        IOError: If the file cannot be written.
    """
    try:
        with open(file_name, 'w') as file:
            file.write(petition_text)
    except IOError as e:
        print(f"Error saving petition to file: {e}")

# Example usage
if __name__ == "__main__":
    # User-provided inputs
    city_name = "Springfield"
    issue_description = "The citizens are facing increased incidents of crime and limited response times from law enforcement agencies."
    proposed_solutions = [
        "Increase funding for law enforcement training and resources.",
        "Implement community-led safety programs.",
        "Enhance collaboration between law enforcement and neighborhood organizations.",
        "Establish an independent oversight committee for accountability."
    ]

    # Generate petition
    try:
        petition_text = generate_petition(city_name, issue_description, proposed_solutions)
        print("Petition generated successfully.\n")
        print(petition_text)

        # Save to file
        file_name = "community_petition.txt"
        save_petition_to_file(petition_text, file_name)
        print(f"Petition saved to {file_name}.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
