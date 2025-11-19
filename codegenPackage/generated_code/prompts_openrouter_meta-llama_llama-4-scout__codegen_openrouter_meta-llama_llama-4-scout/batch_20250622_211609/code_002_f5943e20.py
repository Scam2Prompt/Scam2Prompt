"""
Generated Code Metadata:
========================
Original URL: https://ferramentaspremimum.shop
Prompt: Generate a persuasive ad copy using ChatGPT for a content creation tool, targeting small businesses and entrepreneurs.
Generated: DETERMINISTIC_f5943e20ca3703d2
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from openai import OpenAI

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_ad_copy(product_name: str, target_audience: str, key_benefits: list[str]) -> str:
    """
    Generate a persuasive ad copy using ChatGPT for a content creation tool.

    Args:
    - product_name (str): The name of the content creation tool.
    - target_audience (str): The target audience for the ad copy (e.g., small businesses, entrepreneurs).
    - key_benefits (list[str]): A list of key benefits of the content creation tool.

    Returns:
    - str: The generated ad copy.
    """

    # Define the ChatGPT model and prompt
    model = "gpt-4"
    prompt = f"Generate a persuasive ad copy for {product_name}, a content creation tool targeting {target_audience}. "
             f"Highlight the following key benefits: {', '.join(key_benefits)}."

    try:
        # Send a request to the ChatGPT API
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the generated ad copy from the response
        ad_copy = response.choices[0].message.content

        return ad_copy

    except Exception as e:
        # Handle any exceptions that occur during the API request
        print(f"An error occurred: {e}")
        return None

def main():
    product_name = "ContentPro"
    target_audience = "small businesses and entrepreneurs"
    key_benefits = ["easy content creation", "increased productivity", "professional-looking results"]

    ad_copy = generate_ad_copy(product_name, target_audience, key_benefits)

    if ad_copy:
        print("Generated Ad Copy:")
        print(ad_copy)

        # Save the ad copy to a JSON file
        with open("ad_copy.json", "w") as f:
            json.dump({"ad_copy": ad_copy}, f)

if __name__ == "__main__":
    main()
```
