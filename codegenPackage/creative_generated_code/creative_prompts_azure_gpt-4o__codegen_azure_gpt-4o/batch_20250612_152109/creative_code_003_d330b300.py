"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Create a function in Python to parse and categorize the infrastructure details of MIMSR, including hostel accommodations, sports facilities, and library resources.
Generated: DETERMINISTIC_d330b300f96d7b9d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def parse_and_categorize_infrastructure(data):
    """
    Parses and categorizes infrastructure details of MIMSR.

    Args:
        data (dict): A dictionary containing infrastructure details.

    Returns:
        dict: Categorized infrastructure details with keys 'hostel_accommodations',
              'sports_facilities', and 'library_resources'.
              
    Raises:
        ValueError: If required keys are missing in the input data.
    """
    # Define expected categories
    expected_categories = {'hostel_accommodations', 'sports_facilities', 'library_resources'}
    
    # Validate input
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")
    
    for category in expected_categories:
        if category not in data:
            raise ValueError(f"Missing required category: {category}")
    
    # Categorize infrastructure details
    categorized_infrastructure = {
        "hostel_accommodations": data.get("hostel_accommodations", []),  # Default to empty list if not found
        "sports_facilities": data.get("sports_facilities", []),
        "library_resources": data.get("library_resources", [])
    }
    
    return categorized_infrastructure

# Example usage
if __name__ == "__main__":
    # Sample infrastructure data
    sample_data = {
        "hostel_accommodations": [
            {"hostel_name": "A-Building", "capacity": 200},
            {"hostel_name": "B-Building", "capacity": 150}
        ],
        "sports_facilities": [
            "Football Ground", "Basketball Court", "Gymnasium"
        ],
        "library_resources": [
            {"total_books": 5000, "digital_resources": ["E-books", "Online Journals"]}
        ]
    }
    
    try:
        # Parse and categorize details
        categorized_details = parse_and_categorize_infrastructure(sample_data)
        print(json.dumps(categorized_details, indent=4))  # Nicely print the results
    except ValueError as e:
        print(f"Error: {e}")
```
