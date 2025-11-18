"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-ai.pages.dev
Prompt: Generate code that uses the `dreamshaper-v8` model from Multi AI to create an animated video from a series of text prompts. Include instructions for accessing the model through the Multi AI API.
Generated: DETERMINISTIC_57ed14b24c6d2e37
Batch ID: 20250612_150552
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multi.ai": {
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

class MultiAI:
    """
    A class to interact with the Multi AI API for generating animated videos using the dreamshaper-v8 model.
    """

    def __init__(self, api_key: str):
        """
        Initializes the MultiAI class with the provided API key.
        
        Args:
            api_key (str): The API key to authenticate with Multi AI.
        """
        self.api_key = api_key
        self.base_url = "https://api.multi.ai"  # The base URL for Multi AI API

    def create_animated_video(self, prompts: list, video_title: str) -> dict:
        """
        Creates an animated video from a series of text prompts.

        Args:
            prompts (list): A list of text prompts for the animated video.
            video_title (str): The title of the video to be created.

        Returns:
            dict: The response from the API containing the video details.
        """
        endpoint = f"{self.base_url}/v1/video/create"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "dreamshaper-v8",
            "prompts": prompts,
            "title": video_title
        }

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Return the response JSON

        except requests.exceptions.RequestException as e:
            raise SystemExit(f"API Request failed: {e}")

def main():
    """
    Main function to execute the video creation process.
    """
    # Ensure the API key is available as an environment variable
    api_key = os.getenv("MULTI_AI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the MULTI_AI_API_KEY environment variable.")

    # Initialize the MultiAI client
    multi_ai = MultiAI(api_key)

    # Define prompts and video title
    prompts = [
        "A serene sunrise over a mountain landscape.",
        "A bustling city with animated people walking around.",
        "A calm beach with waves gently crashing."
    ]
    video_title = "My Animated Journey"

    # Create the animated video
    video_response = multi_ai.create_animated_video(prompts, video_title)
    
    # Output the result
    print("Video creation initiated:")
    print(json.dumps(video_response, indent=4))

if __name__ == "__main__":
    main()
```

**Instructions for Use:**
1. Set up an account with Multi AI and obtain an API key.
2. Store your API key in an environment variable named `MULTI_AI_API_KEY`.
3. Install the `requests` library if not already installed: `pip install requests`.
4. Run the script to create an animated video based on the defined prompts.
