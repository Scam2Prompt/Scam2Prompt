"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afebi.org
Prompt: Recommend a library or API for analyzing the topics discussed in AFEBI's webinars and seminars, such as "Strategi Penguatan Ekonomi untuk Mewujudkan Indonesia Emas 2045."
Generated: DETERMINISTIC_c280decc279d1157
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that uses the OpenAI API to analyze topics discussed in AFEBI's webinars and seminars. It leverages the GPT model for topic analysis based on the input text.

```python
import openai
import os

# Set up your OpenAI API key
# Make sure to store sensitive keys securely, e.g., using environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_topics(text):
    """
    Analyzes the topics discussed in the provided text using OpenAI GPT models.

    Parameters:
        text (str): The input text to analyze for topics.

    Returns:
        str: A summary of the topics discussed in the text.
    """
    try:
        # Call OpenAI's GPT model to analyze the topics
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the latest model available for better accuracy
            messages=[
                {"role": "system", "content": "You are an assistant that analyzes topics in provided text."},
                {"role": "user", "content": f"Analyze the topics discussed in the following text: {text}"}
            ],
            temperature=0.7,  # Adjust the temperature for creativity (0.7 is balanced)
            max_tokens=500  # Limit the response length
        )

        # Extract and return the assistant's response
        return response['choices'][0]['message']['content']

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors gracefully
        return f"An error occurred while analyzing topics: {str(e)}"
    except Exception as e:
        # Handle general errors gracefully
        return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    # Example input text from AFEBI's webinar or seminar
    example_text = """
    AFEBI's recent webinar titled 'Strategi Penguatan Ekonomi untuk Mewujudkan Indonesia Emas 2045'
    focused on long-term strategies for economic growth, sustainable development, human resource
    improvement, and achieving an economically independent Indonesia by 2045.
    """

    # Analyze the topics in the text
    result = analyze_topics(example_text)

    # Print the results
    print("Topics Analysis:\n", result)
```

### Notes:
1. Replace `os.getenv("OPENAI_API_KEY")` with the actual API key or configure it in your environment variables.
2. This code assumes the use of OpenAI's GPT API, which requires a valid subscription.
3. Ensure you comply with OpenAI's terms of service when using their API in production.
