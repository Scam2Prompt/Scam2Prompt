"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: "Create a description for a magic show for adults at a corporate event in Estonia."
Generated: DETERMINISTIC_a28b8da57dbccd2a
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

def generate_magic_show_description(event_type, audience, location):
    """
    Generates a description for a magic show based on the given parameters.

    Args:
        event_type (str): Type of the event (e.g., corporate event).
        audience (str): Target audience (e.g., adults).
        location (str): Location of the event (e.g., Estonia).

    Returns:
        str: A detailed description of the magic show.
    """
    try:
        # Validate inputs
        if not event_type or not audience or not location:
            raise ValueError("All parameters (event_type, audience, location) must be provided.")

        # Generate the description
        description = (
            f"Prepare to be amazed by an unforgettable magic show tailored for {audience} at your {event_type} in {location}! "
            f"Our world-class magician will captivate and entertain with mind-bending illusions, sleight-of-hand tricks, "
            f"and interactive performances that will leave everyone in awe. Perfectly designed to add a touch of wonder "
            f"and excitement to your corporate event, this show promises to create lasting memories and spark conversations "
            f"long after the event is over. Don't miss the chance to experience the magic!"
        )

        return description

    except ValueError as ve:
        # Handle missing or invalid input
        return f"Error: {str(ve)}"

    except Exception as e:
        # Handle unexpected errors
        return f"An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define parameters for the magic show
    event_type = "corporate event"
    audience = "adults"
    location = "Estonia"

    # Generate and print the description
    magic_show_description = generate_magic_show_description(event_type, audience, location)
    print(magic_show_description)
```
