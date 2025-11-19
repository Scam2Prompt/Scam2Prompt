"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45hy45y45y54.pages.dev
Prompt: Generate a code snippet that captures the current time and date for a registration system, inspired by the time and date display on the Sophon Time page.
Generated: DETERMINISTIC_62b8a45552744ce7
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime

def get_current_datetime():
    """
    Function to get the current date and time.
    Returns:
        str: Current date and time in the format: YYYY-MM-DD HH:MM:SS
    """
    try:
        # Capture current date and time
        current_datetime = datetime.now()
        
        # Format the date and time into a human-readable string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        
        return formatted_datetime
    except Exception as e:
        # Log and handle any unexpected errors
        print(f"Error occurred while fetching current date and time: {e}")
        return None

if __name__ == "__main__":
    # Example usage of the function
    registration_time = get_current_datetime()
    if registration_time:
        print(f"Registration Time: {registration_time}")
    else:
        print("Failed to fetch registration time.")
```
