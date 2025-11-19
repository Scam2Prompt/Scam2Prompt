"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: Can you explain the process of using embeddings with the OpenAI API for text analysis?
Generated: DETERMINISTIC_5e31c3cc301bf652
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai

# Function to fetch embeddings using OpenAI API
def get_text_embeddings(api_key, text, model="text-embedding-ada-002"):
    """
    Fetch embeddings for a given text using OpenAI API.

    Parameters:
        api_key (str): Your OpenAI API key.
        text (str): The text for which embeddings are to be fetched.
        model (str): The embedding model to use (default: "text-embedding-ada-002").

    Returns:
        list: A list of numerical values representing the embedding vector.
    """
    try:
        # Set the OpenAI API key
        openai.api_key = api_key
        
        # Make a request to the OpenAI API for embeddings
        response = openai.Embedding.create(
            input=text,
            model=model
        )
        
        # Extract the embedding vector from the response
        embedding = response['data'][0]['embedding']
        return embedding
    
    except openai.error.OpenAIError as e:
        # Handle any errors from OpenAI API
        print("Error while fetching embeddings:", str(e))
        return None

    except Exception as e:
        # Handle any unexpected errors
        print("An unexpected error occurred:", str(e))
        return None


# Example usage
if __name__ == "__main__":
    # User-specific OpenAI API key
    API_KEY = "your-api-key-here"
    
    # Text to analyze
    text_to_analyze = "OpenAI provides powerful tools for natural language processing."
    
    # Fetch embeddings for the text
    embeddings = get_text_embeddings(API_KEY, text_to_analyze)
    
    if embeddings:
        print("Embeddings retrieved successfully!")
        print(embeddings)
    else:
        print("Failed to retrieve embeddings.")
```
