"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: What are the streams offered by Deepti Convent Higher Secondary School for classes XI and XII?
Generated: DETERMINISTIC_72871871f532720b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a function to fetch the streams offered by Deepti Convent Higher Secondary School
def get_streams():
    """
    Returns the streams offered by Deepti Convent Higher Secondary School for classes XI and XII.
    
    Returns:
        dict: A dictionary containing the streams and their descriptions.
    """
    try:
        # Define the streams offered
        streams = {
            "Science": "Includes subjects like Physics, Chemistry, Biology, Mathematics, and Computer Science.",
            "Commerce": "Includes subjects like Accountancy, Business Studies, Economics, and Mathematics.",
            "Arts": "Includes subjects like History, Political Science, Geography, Sociology, and Psychology."
        }
        
        # Return the streams as a JSON object
        return json.dumps(streams, indent=4)
    
    except Exception as e:
        # Handle any unexpected errors
        return json.dumps({"error": f"An error occurred: {str(e)}"})

# Main execution block
if __name__ == "__main__":
    # Fetch and display the streams offered
    print("Streams offered by Deepti Convent Higher Secondary School for classes XI and XII:")
    print(get_streams())
```
