"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Write a function to determine the necessary permits for a healthcare center construction in Spain, based on Pahubel's location and experience."
Generated: DETERMINISTIC_ef35b0ff1d54ac41
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def determine_permits(location, experience_years):
    """
    Determines the necessary permits for constructing a healthcare center in Spain based on location and experience.
    
    Args:
        location (str): The location where the healthcare center will be constructed.
        experience_years (int): Years of experience in healthcare construction.
    
    Returns:
        dict: A dictionary containing required permits and their statuses.
    
    Raises:
        ValueError: If location is empty or experience_years is negative.
    """
    
    if not location or not isinstance(location, str):
        raise ValueError("Location must be a non-empty string")
    
    if not isinstance(experience_years, int) or experience_years < 0:
        raise ValueError("Experience years must be a non-negative integer")
    
    # Base permits required for all healthcare centers
    required_permits = {
        'building_license': True,
        'health_department_approval': True,
        'environmental_impact_assessment': False,
        'urban_planning_permit': False,
        'special_healthcare_facility_permit': False
    }
    
    # Location-specific permits
    if 'madrid' in location.lower():
        required_permits['urban_planning_permit'] = True
    elif 'barcelona' in location.lower():
        required_permits['environmental_impact_assessment'] = True
        required_permits['urban_planning_permit'] = True
    
    # Experience-based permits
    if experience_years < 5:
        required_permits['special_healthcare_facility_permit'] = True
    
    return required_permits
```
