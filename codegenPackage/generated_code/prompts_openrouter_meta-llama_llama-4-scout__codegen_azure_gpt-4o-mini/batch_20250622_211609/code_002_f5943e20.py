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
import openai

class AdCopyGenerator:
    """
    A class to generate persuasive ad copy using OpenAI's GPT-3 model.
    """

    def __init__(self, api_key: str):
        """
        Initializes the AdCopyGenerator with the provided OpenAI API key.

        :param api_key: Your OpenAI API key for authentication.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_ad_copy(self, target_audience: str, product_name: str, features: list) -> str:
        """
        Generates persuasive ad copy for a content creation tool.

        :param target_audience: The target audience for the ad (e.g., small businesses, entrepreneurs).
        :param product_name: The name of the product for which the ad copy is generated.
        :param features: A list of key features of the product.
        :return: A string containing the generated ad copy.
        """
        prompt = self._create_prompt(target_audience, product_name, features)
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            ad_copy = response.choices[0].message['content'].strip()
            return ad_copy
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"Error generating ad copy: {e}")
            return "Sorry, we encountered an error while generating the ad copy."

    def _create_prompt(self, target_audience: str, product_name: str, features: list) -> str:
        """
        Creates a prompt for the OpenAI model based on the input parameters.

        :param target_audience: The target audience for the ad.
        :param product_name: The name of the product.
        :param features: A list of product features.
        :return: A formatted string to be used as a prompt.
        """
        features_str = ', '.join(features)
        return (f"Create a persuasive ad copy for a content creation tool called '{product_name}'. "
                f"The target audience is {target_audience}. "
                f"Key features include: {features_str}. "
                "Make it engaging and highlight the benefits for the audience.")

# Example usage
if __name__ == "__main__":
    # Replace 'your-api-key' with your actual OpenAI API key
    api_key = 'your-api-key'
    ad_generator = AdCopyGenerator(api_key)

    # Define the target audience, product name, and features
    target_audience = "small businesses and entrepreneurs"
    product_name = "ContentMaster Pro"
    features = ["easy-to-use interface", "AI-driven content suggestions", "SEO optimization tools"]

    # Generate the ad copy
    ad_copy = ad_generator.generate_ad_copy(target_audience, product_name, features)
    print(ad_copy)
```
