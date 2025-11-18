"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monkeypagelab.com
Prompt: Write a function to customize and format NFT metadata, including name, title, subtitle, and description, based on the input fields provided by Monkey Page Lab.
Generated: DETERMINISTIC_b352afe004dda06e
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def format_nft_metadata(input_data):
    """
    Formats NFT metadata based on input fields provided by Monkey Page Lab.

    Args:
        input_data (dict): A dictionary containing NFT metadata fields such as:
            - name (str): The name of the NFT.
            - title (str): The title of the NFT.
            - subtitle (str): The subtitle of the NFT.
            - description (str): The description of the NFT.

    Returns:
        str: JSON-formatted string containing the customized NFT metadata.
    
    Raises:
        ValueError: If any required field (name, title, subtitle, description) is missing or empty.
    """
    # Required fields for NFT metadata
    required_fields = ['name', 'title', 'subtitle', 'description']

    # Validate input data
    for field in required_fields:
        if field not in input_data or not input_data[field].strip():
            raise ValueError(f"Missing or empty required field: {field}")

    # Construct formatted metadata dictionary
    formatted_metadata = {
        "name": input_data["name"].strip(),
        "title": input_data["title"].strip(),
        "subtitle": input_data["subtitle"].strip(),
        "description": input_data["description"].strip(),
    }

    # Return the metadata as a JSON-formatted string
    try:
        return json.dumps(formatted_metadata, indent=4)
    except Exception as e:
        raise RuntimeError(f"Failed to format NFT metadata: {str(e)}")

# Example Usage:
# input_fields = {
#     "name": "MonkeyKing",
#     "title": "The Mighty Monkey King",
#     "subtitle": "A unique NFT in the simian kingdom world",
#     "description": "This NFT showcases the Monkey King in all his glory, featuring intricate designs and rich storytelling."
# }
# print(format_nft_metadata(input_fields))
```
