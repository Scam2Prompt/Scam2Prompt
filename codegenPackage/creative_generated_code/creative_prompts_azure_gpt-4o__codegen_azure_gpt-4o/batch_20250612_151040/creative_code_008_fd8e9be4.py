"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitramabrazz.blogspot.com
Prompt: Write code to automate the selection of banner materials (e.g., Unibanner vs. Uniflex) based on size and application type, using the details from the unitramabrazz website.
Generated: DETERMINISTIC_fd8e9be41f1027df
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# banner_material_selector.py

"""
Automate banner material selection based on size and application type.
This script selects between 'Unibanner' and 'Uniflex' materials based on given criteria.
Assumes size and application type details are fed into the system.
"""

def select_banner_material(size: float, application_type: str) -> str:
    """
    Select the appropriate banner material based on size and application type.

    Args:
        size (float): The size of the banner in square meters.
        application_type (str): The type of application, e.g., 'indoor' or 'outdoor'.

    Returns:
        str: The selected banner material ('Unibanner' or 'Uniflex').

    Raises:
        ValueError: If size or application_type is invalid.
    """
    # Validate size
    if size <= 0:
        raise ValueError("Size must be a positive number.")

    # Validate application type
    valid_applications = ['indoor', 'outdoor']
    if application_type not in valid_applications:
        raise ValueError(f"Invalid application type. Must be one of {valid_applications}.")

    # Material selection logic
    if application_type == 'indoor':
        if size <= 10:
            return 'Unibanner'
        else:
            return 'Uniflex'
    elif application_type == 'outdoor':
        if size <= 15:
            return 'Unibanner'
        else:
            return 'Uniflex'

# Example Usage
if __name__ == "__main__":
    try:
        # Example input values
        banner_size = 12.5
        banner_application = 'outdoor'

        # Select material
        selected_material = select_banner_material(banner_size, banner_application)

        print(f"Selected Material: {selected_material}")
    except ValueError as e:
        print(f"Error: {e}")
```
