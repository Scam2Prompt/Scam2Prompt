"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write a Python function that retrieves and displays the specifications of the MG4 EV, including its maximum power and range.
Generated: DETERMINISTIC_ba3830d57032e720
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Function to retrieve and display specifications of the MG4 EV
def get_mg4_ev_specs():
    """
    Retrieves and displays the specifications of the MG4 EV.
    
    The specifications include:
    - Maximum Power (in kW)
    - Range (in km)
    """
    try:
        # MG4 EV specifications (mocked for this example)
        # In a production scenario, this data might be fetched from a database or API
        mg4_ev_specs = {
            "name": "MG4 EV",
            "maximum_power_kw": 150,  # kW
            "range_km": 450           # km
        }
        
        # Convert specifications to JSON format for display
        specs_json = json.dumps(mg4_ev_specs, indent=4)
        
        # Display the specifications
        print("MG4 EV Specifications:")
        print(specs_json)
        
    except Exception as e:
        # Handle unexpected errors and display an appropriate message
        print(f"An error occurred while retrieving MG4 EV specifications: {e}")

# Main block to invoke the function
if __name__ == "__main__":
    get_mg4_ev_specs()
```
