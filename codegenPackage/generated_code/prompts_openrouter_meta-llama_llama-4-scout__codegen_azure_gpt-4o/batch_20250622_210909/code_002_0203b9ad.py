"""
Generated Code Metadata:
========================
Original URL: https://shivvedika.com
Prompt: What is the significance of the location of Shiv Vedika Trust near the Manikarnika Ghat in Varanasi, and how does it contribute to the organization's mission?
Generated: DETERMINISTIC_0203b9ad919014e8
Batch ID: 20250622_210909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python script that fetches information about the significance of the location of Shiv Vedika Trust near Manikarnika Ghat in Varanasi and how it contributes to the organization's mission. The script uses the OpenAI API to retrieve relevant information.

```python
import openai
import os

def fetch_significance(api_key, query):
    """
    Fetches information about the significance of a location and its contribution to an organization's mission
    using OpenAI's GPT model.

    Parameters:
        api_key (str): OpenAI API key for authentication.
        query (str): The query to be sent to the GPT model.

    Returns:
        str: The response from the GPT model.
    """
    try:
        # Initialize OpenAI API
        openai.api_key = api_key

        # Make a request to the GPT model
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant."},
                {"role": "user", "content": query}
            ]
        )

        # Extract and return the response content
        return response['choices'][0]['message']['content']

    except openai.error.AuthenticationError:
        return "Error: Invalid API key. Please check your OpenAI API key."
    except openai.error.OpenAIError as e:
        return f"Error: An issue occurred while communicating with the OpenAI API. Details: {str(e)}"
    except Exception as e:
        return f"Error: An unexpected error occurred. Details: {str(e)}"

if __name__ == "__main__":
    # Load OpenAI API key from environment variables for security
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    else:
        # Define the query
        query = ("What is the significance of the location of Shiv Vedika Trust near the Manikarnika Ghat in Varanasi, "
                 "and how does it contribute to the organization's mission?")
        
        # Fetch the information
        result = fetch_significance(api_key, query)
        
        # Print the result
        print(result)
```

### Instructions:
1. Set your OpenAI API key as an environment variable named `OPENAI_API_KEY` before running the script.
2. Install the `openai` Python package if not already installed (`pip install openai`).
3. Run the script to fetch the requested information.

This code adheres to best practices, includes error handling, and is production-ready.
