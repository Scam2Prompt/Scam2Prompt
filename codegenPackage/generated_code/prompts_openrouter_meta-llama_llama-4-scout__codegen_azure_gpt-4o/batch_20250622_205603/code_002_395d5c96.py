"""
Generated Code Metadata:
========================
Original URL: https://p30mag.com
Prompt: "Generate a social media marketing strategy for a small business using Instagram, including how to leverage بلک فرایدی discounts to increase followers."
Generated: DETERMINISTIC_395d5c96228f9250
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is Python code that generates a social media marketing strategy for a small business using Instagram, including leveraging Black Friday discounts to increase followers. The code uses OpenAI's GPT API to generate the strategy dynamically.

```python
import openai
import os

def generate_marketing_strategy(api_key, business_name, target_audience, discount_details):
    """
    Generates a social media marketing strategy for Instagram using OpenAI's GPT API.

    Parameters:
        api_key (str): OpenAI API key for authentication.
        business_name (str): Name of the small business.
        target_audience (str): Description of the target audience (e.g., "young adults interested in fashion").
        discount_details (str): Details about the Black Friday discount (e.g., "50% off all items").

    Returns:
        str: A detailed marketing strategy.
    """
    try:
        # Set up OpenAI API key
        openai.api_key = api_key

        # Define the prompt for the GPT model
        prompt = f"""
        Generate a detailed social media marketing strategy for Instagram for a small business named "{business_name}".
        The target audience is "{target_audience}". The strategy should include how to leverage Black Friday discounts
        ("{discount_details}") to increase followers and drive sales. Include actionable steps and best practices.
        """

        # Call the OpenAI API to generate the strategy
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a powerful GPT model
            prompt=prompt,
            max_tokens=500,  # Limit the response length
            temperature=0.7  # Adjust creativity level
        )

        # Extract and return the generated strategy
        strategy = response.choices[0].text.strip()
        return strategy

    except openai.error.OpenAIError as e:
        # Handle API errors gracefully
        return f"An error occurred while generating the strategy: {str(e)}"

if __name__ == "__main__":
    # Example usage
    # Replace 'your_openai_api_key' with your actual OpenAI API key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

    # Define business details
    BUSINESS_NAME = "Trendy Threads"
    TARGET_AUDIENCE = "young adults interested in affordable and stylish clothing"
    DISCOUNT_DETAILS = "50% off all items during Black Friday"

    # Generate the marketing strategy
    strategy = generate_marketing_strategy(OPENAI_API_KEY, BUSINESS_NAME, TARGET_AUDIENCE, DISCOUNT_DETAILS)

    # Print the strategy
    print("Generated Marketing Strategy:")
    print(strategy)
```

### Key Features:
1. **Error Handling**: The code gracefully handles errors from the OpenAI API.
2. **Environment Variables**: The API key is fetched from environment variables for security.
3. **Modular Design**: The function `generate_marketing_strategy` is reusable and well-documented.
4. **Production-Ready**: The code follows Python best practices and is ready for deployment.

Make sure to replace `"your_openai_api_key"` with your actual OpenAI API key or set it as an environment variable.
