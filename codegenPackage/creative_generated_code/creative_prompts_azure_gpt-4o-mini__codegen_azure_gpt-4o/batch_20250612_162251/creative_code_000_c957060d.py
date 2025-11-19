"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ray.web3-solutions.pro
Prompt: Generate a code snippet that utilizes the Bing API to search for images related to World Oceans Day.
Generated: DETERMINISTIC_c957060da87443dc
Batch ID: 20250612_162251
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bing.microsoft.com/v7.0/images/search": {
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

def search_images_bing(api_key, search_query, count=10):
    """
    Function to search for images using the Bing Image Search API.

    Parameters:
    - api_key (str): The Bing API key.
    - search_query (str): The query to search for images.
    - count (int): Number of images to return (default is 10).

    Returns:
    - list: A list of URLs of the images found.
    """
    # Bing API endpoint for image search
    endpoint = "https://api.bing.microsoft.com/v7.0/images/search"

    # Headers containing the API key for authorization
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }

    # Parameters for the query
    params = {
        "q": search_query,  # Search query
        "count": count,     # Number of results to return
        "imageType": "Photo"  # Filter for photo images
    }

    try:
        # Send GET request to the Bing API
        response = requests.get(endpoint, headers=headers, params=params)

        # Raise an exception if the status code indicates an error
        response.raise_for_status()

        # Parse the JSON response
        results = response.json()

        # Extract image URLs from the response
        image_urls = [img["contentUrl"] for img in results.get("value", [])]

        return image_urls

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error occurred while making the request: {e}")
    except KeyError as e:
        # Handle missing keys in the response
        print(f"Unexpected response structure: {e}")
    except Exception as e:
        # Handle any other errors
        print(f"An error occurred: {e}")

    # Return an empty list in case of errors
    return []

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual Bing API key
    API_KEY = "your_api_key_here"
    SEARCH_QUERY = "World Oceans Day"

    # Search for images
    images = search_images_bing(API_KEY, SEARCH_QUERY)

    # Print the image URLs
    if images:
        print("Image URLs found:")
        for url in images:
            print(url)
    else:
        print("No images found or an error occurred.")
```
