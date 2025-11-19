"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2e76k7pt.s3.us-east-2.amazonaws.com
Prompt: Provide a code example for parsing the timestamp "2024-01-26T03:39:59.000Z" from the 2e76k7pt response in a web application.
Generated: DETERMINISTIC_0d0ff05caa04f480
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def parse_timestamp(response):
    """
    Parses the timestamp "2024-01-26T03:39:59.000Z" from the response.

    Args:
        response (dict): The response object containing the timestamp.

    Returns:
        datetime.datetime: The parsed datetime object.

    Raises:
        ValueError: If the timestamp format is invalid.
        KeyError: If the timestamp key does not exist in the response.
    """
    try:
        # Ensure the response contains the necessary data
        if "timestamp" not in response:
            raise KeyError("The 'timestamp' key is missing in the response.")
        
        # Extract the timestamp from the response
        timestamp_str = response["timestamp"]

        # Parse the timestamp string into a datetime object
        parsed_timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        return parsed_timestamp
    except KeyError as e:
        # Log and re-raise the KeyError for missing keys in the response
        print(f"Error: {e}")
        raise
    except ValueError as e:
        # Log and re-raise the ValueError for invalid timestamp format
        print(f"Error: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Simulated response with the timestamp
    response = {
        "timestamp": "2024-01-26T03:39:59.000Z"
    }
    
    try:
        # Parse the timestamp
        parsed_datetime = parse_timestamp(response)
        print(f"Parsed datetime: {parsed_datetime}")
    except Exception as e:
        print(f"An error occurred while parsing the timestamp: {e}")
```
