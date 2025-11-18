"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doo4k.top
Prompt: Generate code to extract and display BBCode full linked embed codes for images hosted on a Chevereto-based platform.
Generated: DETERMINISTIC_acf55376f79385fe
Batch ID: 20250612_151752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-chevereto-instance/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

def get_image_embed_codes(api_url, api_key):
    """
    Fetches image data from a Chevereto-based platform and extracts BBCode embed codes.

    Args:
        api_url (str): The URL to the Chevereto API endpoint.
        api_key (str): The API key to authenticate requests.

    Returns:
        list: A list of BBCode embed codes for images.
    """
    try:
        # Define the parameters for the API request
        params = {
            'key': api_key,
        }

        # Make a request to the Chevereto API
        response = requests.get(api_url, params=params)

        # Check if the response is successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract images and their embed codes
        embed_codes = []
        for image in data.get('images', []):
            # Construct the BBCode embed code
            bbcode = f"[url={image['url']}][img]{image['url_viewer']}[/img][/url]"
            embed_codes.append(bbcode)

        return embed_codes

    except requests.exceptions.RequestException as e:
        # Handle networking errors
        print(f"Error occurred while making the API request: {e}")
        return []
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        print(f"Error occurred while decoding the JSON response: {e}")
        return []
    except KeyError as e:
        # Handle missing keys in the JSON response
        print(f"Error occurred while extracting image data: Missing key {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace these with your Chevereto API details
    CHEVERETO_API_URL = "https://your-chevereto-instance/api"
    CHEVERETO_API_KEY = "your-api-key"

    # Get the embed codes
    embed_codes = get_image_embed_codes(CHEVERETO_API_URL, CHEVERETO_API_KEY)

    # Display the embed codes
    if embed_codes:
        print("BBCode Embed Codes:")
        for code in embed_codes:
            print(code)
    else:
        print("No embed codes found or an error occurred.")
```
