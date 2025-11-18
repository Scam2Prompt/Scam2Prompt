"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Develop a program to check the bot management score and detection status from a JSON object similar to the one on netsecurity.pages.dev.
Generated: DETERMINISTIC_6f74e2bcb2ccee4d
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def check_bot_management_status(json_data):
    """
    Function to check the bot management score and detection status 
    from the provided JSON object.

    Args:
    json_data (str): JSON string containing bot management details.

    Returns:
    dict: A dictionary containing the bot score and detection status.
    """
    try:
        # Parse the JSON string
        data = json.loads(json_data)
        
        # Navigate to the expected fields
        bot_score = data.get("bot_management", {}).get("score", None)
        detection_status = data.get("bot_management", {}).get("detection_status", None)
        
        # Validate presence of required fields
        if bot_score is None:
            raise ValueError("Missing 'score' in bot_management.")
        if detection_status is None:
            raise ValueError("Missing 'detection_status' in bot_management.")
        
        return {
            "bot_score": bot_score,
            "detection_status": detection_status
        }
    
    except json.JSONDecodeError:
        # Handle JSON parsing errors
        raise ValueError("Invalid JSON data provided.")
    except Exception as e:
        # Handle unexpected errors
        raise RuntimeError(f"An error occurred while processing the JSON data: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Example JSON input
    json_input = '''
    {
        "bot_management": {
            "score": 85,
            "detection_status": "low-risk"
        },
        "other_data": {
            "key": "value"
        }
    }
    '''
    try:
        result = check_bot_management_status(json_input)
        print("Bot Management Details:")
        print(f"Score: {result['bot_score']}")
        print(f"Detection Status: {result['detection_status']}")
    except Exception as e:
        print(f"Error: {e}")
```
