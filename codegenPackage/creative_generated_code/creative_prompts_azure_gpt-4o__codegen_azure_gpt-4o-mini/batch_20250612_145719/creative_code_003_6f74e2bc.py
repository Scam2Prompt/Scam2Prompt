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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_bot_management_score(json_data):
    """
    Checks the bot management score and detection status from a given JSON object.

    :param json_data: A JSON object containing bot management information.
    :return: A tuple containing the bot management score and detection status.
    """
    try:
        # Parse the JSON data
        data = json.loads(json_data)

        # Validate required keys in the JSON data
        if 'bot_management' not in data:
            logging.error("Missing 'bot_management' key in JSON data.")
            raise KeyError("Missing 'bot_management' key in JSON data.")

        bot_management = data['bot_management']
        
        # Check if score and detection_status keys exist
        score = bot_management.get('score')
        detection_status = bot_management.get('detection_status')

        if score is None or detection_status is None:
            logging.error("Missing 'score' or 'detection_status' in 'bot_management'.")
            raise ValueError("Missing 'score' or 'detection_status' in 'bot_management'.")

        return score, detection_status

    except json.JSONDecodeError as e:
        logging.error("Invalid JSON data provided: %s", e)
        raise ValueError("Invalid JSON data provided.") from e
    except Exception as e:
        logging.error("An error occurred: %s", e)
        raise

if __name__ == "__main__":
    # Sample JSON data
    json_input = '''
    {
        "bot_management": {
            "score": 85,
            "detection_status": "active"
        }
    }
    '''

    try:
        score, detection_status = check_bot_management_score(json_input)
        logging.info(f"Bot Management Score: {score}")
        logging.info(f"Detection Status: {detection_status}")
    except Exception as e:
        logging.error("Failed to check bot management score: %s", e)
```
