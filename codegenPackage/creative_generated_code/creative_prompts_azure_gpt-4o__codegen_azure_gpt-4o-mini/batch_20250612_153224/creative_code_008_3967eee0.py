"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: Create a script to automate the process of promoting advertisements on Ifesty, including banner creation and ad boosting.
Generated: DETERMINISTIC_3967eee0f9a91b3f
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifesty.com/v1": {
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
import os
from PIL import Image, ImageDraw, ImageFont

class IfestyAdPromoter:
    """
    A class to automate advertisement promotion on Ifesty, including 
    banner creation and ad boosting functionality.
    """

    def __init__(self, api_key, api_url):
        """
        Initializes the IfestyAdPromoter with API credentials.

        Args:
            api_key (str): API key for authenticating with Ifesty.
            api_url (str): Base URL for Ifesty API.
        """
        self.api_key = api_key
        self.api_url = api_url

    def create_banner(self, text, output_path):
        """
        Creates a banner image with the specified text.

        Args:
            text (str): The text to display on the banner.
            output_path (str): The file path where the banner will be saved.

        Returns:
            str: The file path of the saved banner.
        """
        try:
            # Create a blank image with white background
            width, height = 800, 400
            banner = Image.new('RGB', (width, height), 'white')
            draw = ImageDraw.Draw(banner)

            # Load a font
            font = ImageFont.load_default()

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font)
            position = ((width - text_width) // 2, (height - text_height) // 2)

            # Draw text on the banner
            draw.text(position, text, fill='black', font=font)

            # Save the banner image
            banner.save(output_path)
            return output_path
        except Exception as e:
            print(f"Error creating banner: {e}")
            raise

    def boost_ad(self, ad_id, budget, duration):
        """
        Boosts an existing advertisement.

        Args:
            ad_id (str): The ID of the advertisement to boost.
            budget (float): The budget to allocate for boosting.
            duration (int): Duration in days for the boost.

        Returns:
            dict: Response from the Ifesty API.
        """
        try:
            endpoint = f"{self.api_url}/ads/{ad_id}/boost"
            payload = {
                "budget": budget,
                "duration": duration
            }
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as e:
            print(f"Error boosting ad: {e}")
            raise

if __name__ == "__main__":
    # Configuration
    API_KEY = os.getenv("IFESTY_API_KEY")
    API_URL = "https://api.ifesty.com/v1"

    # Create an instance of IfestyAdPromoter
    ifesty_promoter = IfestyAdPromoter(API_KEY, API_URL)

    # Create a banner
    banner_path = "banner.png"
    ifesty_promoter.create_banner("Promote Your Business!", banner_path)

    # Boost an ad (example values)
    AD_ID = "123456"
    BUDGET = 100.0
    DURATION = 7  # 7 days

    try:
        boost_response = ifesty_promoter.boost_ad(AD_ID, BUDGET, DURATION)
        print("Ad boosted successfully:", boost_response)
    except Exception as e:
        print("Failed to boost ad:", e)
```

Make sure to replace `AD_ID`, `BUDGET`, and `DURATION` with your actual values before running the script. Additionally, set the `IFESTY_API_KEY` environment variable for proper authentication with the Ifesty API.
