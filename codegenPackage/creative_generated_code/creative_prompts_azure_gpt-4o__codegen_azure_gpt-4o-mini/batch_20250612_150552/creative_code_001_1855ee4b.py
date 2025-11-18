"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-ai.pages.dev
Prompt: Create a code example that uses the `audio-ldm` model from Multi AI to generate music based on a text description. Ensure the code includes steps for connecting to the Multi AI API.
Generated: DETERMINISTIC_1855ee4bcf4199d6
Batch ID: 20250612_150552
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multi.ai/v1/audio-ldm": {
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

class MultiAI:
    """
    A class to interact with the Multi AI API for generating music using the audio-ldm model.
    """
    def __init__(self, api_key: str):
        """
        Initializes the Multi AI client with the provided API key.

        Args:
            api_key (str): Your API key for authenticating with the Multi AI API.
        """
        self.api_key = api_key
        self.base_url = "https://api.multi.ai/v1/audio-ldm"

    def generate_music(self, description: str):
        """
        Generates music based on a given text description using the audio-ldm model.

        Args:
            description (str): A textual description of the desired music.

        Returns:
            dict: The response from the API containing the generated music data.

        Raises:
            ValueError: If the description is empty.
            Exception: If the API request fails.
        """
        if not description:
            raise ValueError("Description must not be empty.")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "description": description
        }

        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            return response.json()  # Return the JSON response from the API
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # For HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # For other errors
            raise


if __name__ == "__main__":
    # Example usage of the MultiAI class
    API_KEY = "your_api_key_here"  # Replace with your Multi AI API key
    music_description = "A calming piano piece with nature sounds."

    multi_ai = MultiAI(API_KEY)
    
    try:
        music_data = multi_ai.generate_music(music_description)
        print("Generated music data:", music_data)  # Output the generated music data
    except Exception as e:
        print("Failed to generate music:", e)
```
