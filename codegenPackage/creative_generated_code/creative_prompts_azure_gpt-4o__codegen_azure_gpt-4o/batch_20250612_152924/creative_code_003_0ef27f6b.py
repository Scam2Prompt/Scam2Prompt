"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Create a function to duplicate inspection reports, optionally excluding photos, as described in the BeSoft App Vistoria documentation.
Generated: DETERMINISTIC_0ef27f6b97485667
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import copy

def duplicate_inspection_report(report, exclude_photos=False):
    """
    Duplicates an inspection report.

    Args:
        report (dict): The original inspection report to be duplicated. 
                       Expected to be a dictionary containing inspection details.
        exclude_photos (bool): If True, photos will be excluded from the duplicated report.

    Returns:
        dict: A new inspection report dictionary, duplicated from the original.

    Raises:
        ValueError: If the input report is not a dictionary.
    """
    # Ensure the input is a valid dictionary
    if not isinstance(report, dict):
        raise ValueError("Invalid report format. Expected a dictionary.")
    
    # Create a deep copy of the original report to avoid modifying original data
    duplicated_report = copy.deepcopy(report)
    
    # Exclude photos from the duplicated report if requested
    if exclude_photos:
        duplicated_report.pop("photos", None)  # Remove 'photos' key if present

    # Update metadata for the duplicated report (e.g., set a new unique ID)
    duplicated_report["id"] = generate_unique_report_id()
    duplicated_report["created_at"] = get_current_timestamp()

    return duplicated_report

def generate_unique_report_id():
    """
    Generates a unique ID for a new inspection report.

    Returns:
        str: A unique ID (e.g., using UUID or a custom logic).
    """
    import uuid
    return str(uuid.uuid4())

def get_current_timestamp():
    """
    Gets the current timestamp.

    Returns:
        str: Current date and time in ISO 8601 format.
    """
    from datetime import datetime
    return datetime.now().isoformat()
```

Note: Ensure that the `report` dictionary structure matches your application's format, particularly the presence of a `photos` key if relevant.
