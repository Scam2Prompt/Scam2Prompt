"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Generate a Google Ads campaign strategy for a startup in Jordan, including keyword research and ad copywriting, using IDEX Marketing's services as a reference."
Generated: DETERMINISTIC_a630c57a2af9001f
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import json

# Constants
OPENAI_API_KEY = "your_openai_api_key_here"  # Replace with your OpenAI API key
STARTUP_LOCATION = "Jordan"
SERVICE_PROVIDER = "IDEX Marketing"

def generate_google_ads_strategy(api_key, location, service_provider):
    """
    Generates a Google Ads campaign strategy using OpenAI's GPT model.
    
    Parameters:
        api_key (str): OpenAI API key.
        location (str): Target location for the campaign.
        service_provider (str): Reference service provider for strategy inspiration.
    
    Returns:
        dict: A dictionary containing keyword research and ad copy suggestions.
    """
    try:
        # Initialize OpenAI API
        openai.api_key = api_key

        # Prompt for GPT model
        prompt = f"""
        Generate a Google Ads campaign strategy for a startup in {location}. 
        Include keyword research and ad copywriting, using {service_provider}'s services as a reference. 
        Provide actionable insights and examples.
        """

        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a suitable GPT model
            prompt=prompt,
            max_tokens=1000,  # Adjust token limit based on expected response size
            temperature=0.7  # Adjust creativity level
        )

        # Parse response
        strategy = response.choices[0].text.strip()
        return {"strategy": strategy}

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        return {"error": f"OpenAI API error: {str(e)}"}
    except Exception as e:
        # Handle general errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Main function
if __name__ == "__main__":
    try:
        # Generate strategy
        result = generate_google_ads_strategy(OPENAI_API_KEY, STARTUP_LOCATION, SERVICE_PROVIDER)

        # Output result
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("Google Ads Campaign Strategy:")
            print(json.dumps(result, indent=4))  # Pretty print the strategy

    except Exception as e:
        print(f"An unexpected error occurred in the main function: {str(e)}")
```

**Note:** Replace `"your_openai_api_key_here"` with your actual OpenAI API key. Ensure you have the OpenAI Python library installed (`pip install openai`) before running the code.
