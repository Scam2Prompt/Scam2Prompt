"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Create a code snippet that formats a biography based on the unique life experiences of Rade Milosavljevic, including his work in radio and literature.
Generated: DETERMINISTIC_5c20fc4003d58f46
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import textwrap

def format_biography(name, experiences):
    """
    Formats a biography based on the given name and life experiences.

    Args:
        name (str): The name of the individual.
        experiences (list of str): A list of unique life experiences.

    Returns:
        str: A formatted biography as a string.
    """
    try:
        # Validate inputs
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not experiences or not all(isinstance(exp, str) for exp in experiences):
            raise ValueError("Experiences must be a list of non-empty strings.")

        # Create the biography header
        biography = f"Biography of {name}\n"
        biography += "=" * len(biography.strip()) + "\n\n"

        # Add life experiences
        biography += "Life Experiences:\n"
        for i, experience in enumerate(experiences, start=1):
            biography += f"{i}. {experience}\n"

        # Wrap text for better readability
        return textwrap.fill(biography, width=80)

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while formatting the biography: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define the name and experiences
    name = "Rade Milosavljevic"
    experiences = [
        "Worked as a radio host, captivating audiences with his voice and storytelling.",
        "Authored several literary works that explored the human condition and philosophy.",
        "Contributed to the cultural landscape through his creative endeavors in media and literature."
    ]

    # Generate and print the formatted biography
    formatted_biography = format_biography(name, experiences)
    print(formatted_biography)
```
