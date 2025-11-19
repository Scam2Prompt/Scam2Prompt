"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rademilos.com
Prompt: Create a code snippet that formats a biography based on the unique life experiences of Rade Milosavljevic, including his work in radio and literature.
Generated: DETERMINISTIC_5c20fc4003d58f46
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Biography Formatter for Rade Milosavljevic

This script formats a biography based on Rade Milosavljevic's unique life experiences
including his work in radio and literature.
"""

def format_biography(name, experiences):
    """
    Formats a biography for the given individual based on their unique experiences.

    Args:
        name (str): The name of the person.
        experiences (list of dict): List of experiences. Each experience is a dictionary
                                    containing 'title', 'description', and 'years'.

    Returns:
        str: A formatted biography.
    """
    try:
        # Validate input
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(experiences, list) or not all(isinstance(exp, dict) for exp in experiences):
            raise ValueError("Experiences must be a list of dictionaries.")

        # Create the biography header
        biography = f"Biography of {name}\n"
        biography += "=" * (len(biography) - 1) + "\n\n"

        # Add each experience
        for i, exp in enumerate(experiences):
            title = exp.get("title", "Untitled Experience")
            description = exp.get("description", "No description provided.")
            years = exp.get("years", "Unknown")

            biography += f"{i + 1}. {title} ({years})\n"
            biography += f"{description}\n\n"

        return biography

    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    experiences = [
        {
            "title": "Radio Host",
            "description": "Hosted a popular radio show, engaging listeners with insightful commentary.",
            "years": "1995-2005",
        },
        {
            "title": "Author",
            "description": "Published multiple works of literature, blending storytelling with cultural themes.",
            "years": "2006-present",
        },
    ]

    biography = format_biography("Rade Milosavljevic", experiences)
    print(biography)
```
