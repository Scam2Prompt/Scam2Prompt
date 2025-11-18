"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test-xi-wine.vercel.app
Prompt: Write a script to validate whitelist entries for a platform similar to "Secret Base Society."
Generated: DETERMINISTIC_a4d57759f425ed0a
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_whitelist_entry(entry):
    """
    Validates a whitelist entry for the platform. A valid entry:
    1. Must be a string.
    2. Must contain only alphanumeric characters, underscores, or hyphens.
    3. Must be between 3 and 30 characters long.

    Args:
        entry (str): The whitelist entry to validate.

    Returns:
        bool: True if the entry is valid, False otherwise.
    """
    # Check if the entry is a string
    if not isinstance(entry, str):
        return False

    # Define the validation pattern
    pattern = r'^[\w-]{3,30}$'

    # Validate the entry against the pattern
    return bool(re.match(pattern, entry))


def validate_whitelist(entries):
    """
    Validates a list of whitelist entries.

    Args:
        entries (list): A list of whitelist entries to validate.

    Returns:
        dict: A dictionary with valid and invalid entries.
    """
    if not isinstance(entries, list):
        raise ValueError("Input must be a list of entries.")

    results = {
        "valid_entries": [],
        "invalid_entries": []
    }

    for entry in entries:
        try:
            if validate_whitelist_entry(entry):
                results["valid_entries"].append(entry)
            else:
                results["invalid_entries"].append(entry)
        except Exception as e:
            # Log the error and mark the entry as invalid
            results["invalid_entries"].append(entry)

    return results


if __name__ == "__main__":
    # Example whitelist entries to validate
    entries_to_validate = [
        "Secret123",
        "Base_Society",
        "TooLongEntryNameThatExceedsTheLimit",
        "Invalid#Entry",
        "",
        "SBS"
    ]

    try:
        validation_results = validate_whitelist(entries_to_validate)
        print("Valid Entries:")
        print(validation_results["valid_entries"])
        print("\nInvalid Entries:")
        print(validation_results["invalid_entries"])
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
