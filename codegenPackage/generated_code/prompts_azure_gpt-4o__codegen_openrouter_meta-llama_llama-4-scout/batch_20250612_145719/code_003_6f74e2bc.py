"""
Generated Code Metadata:
========================
Original URL: https://netsecurity.pages.dev
Prompt: Develop a program to check the bot management score and detection status from a JSON object similar to the one on netsecurity.pages.dev.
Generated: DETERMINISTIC_6f74e2bcb2ccee4d
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def check_bot_management_score(bot_management):
    """
    Checks the bot management score and detection status from a JSON object.

    Args:
        bot_management (dict): A dictionary containing bot management information.

    Returns:
        dict: A dictionary containing the bot management score and detection status.

    Raises:
        ValueError: If the input is not a valid JSON object or if required keys are missing.
    """
    try:
        # Check if input is a dictionary
        if not isinstance(bot_management, dict):
            raise ValueError("Invalid input. Expected a dictionary.")

        # Check if required keys exist
        required_keys = ["score", "detection"]
        if not all(key in bot_management for key in required_keys):
            raise ValueError("Missing required keys in the input dictionary.")

        # Extract bot management score and detection status
        score = bot_management["score"]
        detection = bot_management["detection"]

        # Validate score range
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            raise ValueError("Invalid score. Expected a number between 0 and 100.")

        # Validate detection status
        if not isinstance(detection, str) or detection.lower() not in ["verified", "suspicious", "unknown"]:
            raise ValueError("Invalid detection status. Expected 'verified', 'suspicious', or 'unknown'.")

        # Return bot management score and detection status
        return {
            "bot_management_score": score,
            "detection_status": detection.lower()
        }

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def load_json_data(json_data):
    """
    Loads JSON data from a string.

    Args:
        json_data (str): A string containing JSON data.

    Returns:
        dict: A dictionary representing the JSON data.

    Raises:
        json.JSONDecodeError: If the input string is not a valid JSON.
    """
    try:
        return json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None


def main():
    # Example JSON object
    json_data = '''
    {
        "score": 85,
        "detection": "verified"
    }
    '''

    # Load JSON data
    bot_management = load_json_data(json_data)

    # Check bot management score and detection status
    result = check_bot_management_score(bot_management)

    # Print result
    if result:
        print("Bot Management Score:", result["bot_management_score"])
        print("Detection Status:", result["detection_status"])


if __name__ == "__main__":
    main()
```
