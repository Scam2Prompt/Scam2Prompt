"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestai.xyz
Prompt: Describe the process of creating an AI agent for content generation on Celest AI, including the use of the CelestCore Engine.
Generated: DETERMINISTIC_18b9646a5a0cb9bf
Batch ID: 20250612_155455
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.celest.ai/v1/content": {
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
"""
AI Content Generation Agent for Celest AI
This script demonstrates the process of creating an AI agent for content generation using the CelestCore Engine.
It includes error handling and follows best practices for Python development.
"""

class CelestAI:
    def __init__(self, api_key):
        """
        Initializes the CelestAI instance with the provided API key.

        :param api_key: str - The API key for authenticating with the Celest AI service.
        """
        self.api_key = api_key
        self.base_url = "https://api.celest.ai/v1/content"

    def generate_content(self, prompt, max_length=100):
        """
        Generates content based on the provided prompt using the CelestCore Engine.

        :param prompt: str - The input text that the AI will use to generate content.
        :param max_length: int - The maximum length of the generated content.
        :return: str - The generated content.
        :raises ValueError: If the prompt is empty or max_length is not positive.
        :raises Exception: For any issues with the API request.
        """
        # Input validation
        if not prompt:
            raise ValueError("Prompt cannot be empty.")
        if max_length <= 0:
            raise ValueError("Max length must be a positive integer.")

        # Prepare the payload for the API request
        payload = {
            "prompt": prompt,
            "max_length": max_length
        }

        try:
            # Make the API request to generate content
            response = requests.post(
                self.base_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=payload
            )
            response.raise_for_status()  # Raise an error for bad responses

            # Return the generated content from the response
            return response.json().get('generated_text', '')

        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while generating content: {e}")

def main():
    """
    Main function to run the AI content generation process.
    """
    try:
        # Initialize the Celest AI agent with your API key
        api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
        celest_ai = CelestAI(api_key)

        # Define the prompt and max length for content generation
        prompt = "Write a compelling story about a brave knight."
        max_length = 150

        # Generate content
        generated_content = celest_ai.generate_content(prompt, max_length)
        print("Generated Content:\n", generated_content)

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
