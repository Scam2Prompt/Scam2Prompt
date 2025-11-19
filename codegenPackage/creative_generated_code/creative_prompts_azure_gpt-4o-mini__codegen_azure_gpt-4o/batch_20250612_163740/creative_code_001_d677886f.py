"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tcs-campaigns.com
Prompt: Write a code snippet that demonstrates the integration of generative AI in the software development lifecycle using TCS AI Catapult Forward.
Generated: DETERMINISTIC_d677886fe3c5f552
Batch ID: 20250612_163740
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.tcsai.catapultforward.com`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.tcsai.catapultforward.com": {
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

class TCSAIIntegration:
    """
    A class to demonstrate the integration of TCS AI Catapult Forward in 
    the software development lifecycle for generative AI capabilities.
    """

    def __init__(self, api_key, base_url):
        """
        Initialize the integration with necessary credentials.

        :param api_key: The API key for authenticating with TCS AI Catapult Forward
        :param base_url: The base URL for the API endpoint
        """
        self.api_key = api_key
        self.base_url = base_url

    def generate_code_snippet(self, prompt):
        """
        Generate a code snippet using TCS AI Catapult Forward based on the provided prompt.

        :param prompt: A textual description of the desired code functionality
        :return: Generated code snippet as a string
        """
        try:
            # Prepare the request payload
            payload = {"prompt": prompt}
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # Send the request to the generative AI API
            response = requests.post(f"{self.base_url}/generate", json=payload, headers=headers)

            # Check for successful response
            if response.status_code == 200:
                data = response.json()
                # Extract and return the generated code snippet
                return data.get("generated_code", "")
            else:
                raise Exception(f"API Error: {response.status_code} - {response.text}")
        
        except requests.exceptions.RequestException as e:
            # Handle networking-related errors
            print(f"Networking Error: {e}")
            return None
        
        except Exception as e:
            # Handle other errors
            print(f"Error: {e}")
            return None

    def integrate_into_sdlc(self, prompt):
        """
        Demonstrate how generative AI can be integrated within the software development lifecycle.

        :param prompt: A textual description of the desired functionality
        """
        print("Generating code snippet based on the provided prompt...")
        generated_code = self.generate_code_snippet(prompt)

        if generated_code:
            print("Generated Code Snippet:")
            print(generated_code)
        else:
            print("Failed to generate code snippet. Please check errors above.")


# Main function to demonstrate the integration
if __name__ == "__main__":
    # Configuration details (replace with actual API key and endpoint)
    API_KEY = "your-tcs-ai-api-key"
    BASE_URL = "https://api.tcsai.catapultforward.com"

    # Create an instance of the TCS AI Integration class
    tcs_ai = TCSAIIntegration(api_key=API_KEY, base_url=BASE_URL)

    # Prompt for generative AI to create a code snippet
    user_prompt = "Write a Python function to calculate the factorial of a number using recursion."

    # Demonstrate integration
    tcs_ai.integrate_into_sdlc(prompt=user_prompt)
```

Make sure to replace `your-tcs-ai-api-key` and `https://api.tcsai.catapultforward.com` with your actual credentials and endpoint information from TCS AI Catapult Forward.
