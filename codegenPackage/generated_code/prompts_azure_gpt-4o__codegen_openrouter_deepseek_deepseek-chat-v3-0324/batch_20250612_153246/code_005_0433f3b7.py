"""
Generated Code Metadata:
========================
Original URL: https://hildeinox.com
Prompt: Create a function in Python to classify stainless steel grades based on the descriptions provided in the "Paslanmaz Çelik Kaliteleri" section of Hilde Inox.
Generated: DETERMINISTIC_0433f3b7585fcc1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def classify_stainless_steel_grade(description):
    """
    Classifies stainless steel grades based on the provided description.
    
    Args:
        description (str): The description of the stainless steel grade.
        
    Returns:
        str: The classified grade or 'Unknown' if no match found.
    """
    # Dictionary mapping keywords to stainless steel grades
    grade_mapping = {
        '304': ['304', '1.4301', 'aisi 304', '18/8', '18-8'],
        '304L': ['304l', '1.4307', 'aisi 304l', 'low carbon'],
        '316': ['316', '1.4401', 'aisi 316', 'marine grade'],
        '316L': ['316l', '1.4404', 'aisi 316l', 'low carbon'],
        '321': ['321', '1.4541', 'aisi 321', 'titanium stabilized'],
        '430': ['430', '1.4016', 'aisi 430', 'ferritic'],
        '410': ['410', '1.4006', 'aisi 410', 'martensitic'],
        '2205': ['2205', '1.4462', 'duplex', 'uns s32205'],
        '904L': ['904l', '1.4539', 'n08904', 'high alloy']
    }
    
    if not description or not isinstance(description, str):
        return 'Unknown'
    
    description_lower = description.lower()
    
    for grade, keywords in grade_mapping.items():
        for keyword in keywords:
            if keyword in description_lower:
                return grade
    
    return 'Unknown'
```
