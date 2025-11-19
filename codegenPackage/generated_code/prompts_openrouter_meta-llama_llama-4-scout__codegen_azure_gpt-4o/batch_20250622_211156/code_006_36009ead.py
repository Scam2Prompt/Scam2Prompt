"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Create a sample award nomination for an activity professional in Minnesota, using the criteria outlined by MN SWAP.
Generated: DETERMINISTIC_36009ead5b0f3449
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def create_award_nomination(nominee_name, activity_profession, achievements, nominator_name, contact_info):
    """
    Creates a sample award nomination for an activity professional in Minnesota.

    Args:
        nominee_name (str): Name of the nominee.
        activity_profession (str): Profession or role of the nominee.
        achievements (list): List of achievements or contributions by the nominee.
        nominator_name (str): Name of the person nominating.
        contact_info (dict): Contact information of the nominator (e.g., email, phone).

    Returns:
        str: JSON-formatted award nomination.
    """
    try:
        # Validate input
        if not nominee_name or not activity_profession or not achievements or not nominator_name or not contact_info:
            raise ValueError("All fields are required to create a nomination.")

        if not isinstance(achievements, list) or not all(isinstance(a, str) for a in achievements):
            raise ValueError("Achievements must be a list of strings.")

        if not isinstance(contact_info, dict) or "email" not in contact_info or "phone" not in contact_info:
            raise ValueError("Contact info must be a dictionary containing 'email' and 'phone'.")

        # Create nomination dictionary
        nomination = {
            "nominee_name": nominee_name,
            "activity_profession": activity_profession,
            "achievements": achievements,
            "nominator_name": nominator_name,
            "contact_info": contact_info,
            "state": "Minnesota",
            "organization": "MN SWAP"
        }

        # Convert nomination to JSON format
        nomination_json = json.dumps(nomination, indent=4)
        return nomination_json

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Sample data for the nomination
    nominee_name = "Jane Doe"
    activity_profession = "Recreational Therapist"
    achievements = [
        "Implemented innovative therapy programs for seniors",
        "Organized community outreach events",
        "Mentored new activity professionals"
    ]
    nominator_name = "John Smith"
    contact_info = {
        "email": "john.smith@example.com",
        "phone": "555-123-4567"
    }

    # Generate the nomination
    nomination = create_award_nomination(
        nominee_name, activity_profession, achievements, nominator_name, contact_info
    )

    # Print the nomination
    print(nomination)
```
