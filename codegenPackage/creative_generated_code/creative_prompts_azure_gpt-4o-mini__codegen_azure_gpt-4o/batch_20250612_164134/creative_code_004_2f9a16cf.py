"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: Provide an example of an API call that could be used to check if a web server is returning a default page due to no content.
Generated: DETERMINISTIC_2f9a16cf91591779
Batch ID: 20250612_164134
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
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

def check_default_page(url):
    """
    Function to check if the web server is returning a default page due to no content.

    Parameters:
        url (str): The URL of the web server to check.

    Returns:
        dict: A dictionary containing the status of the check and additional information.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url, timeout=10)

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Check if the response content is potentially a default page
            # This can be customized based on known default page patterns
            if "default" in response.text.lower() or "index.html" in response.text.lower():
                return {
                    "status": "default_page_detected",
                    "message": "The server is returning a default page.",
                    "content_preview": response.text[:200]  # Return a preview of the content
                }
            else:
                return {
                    "status": "content_found",
                    "message": "The server is returning valid content.",
                    "content_preview": response.text[:200]  # Return a preview of the content
                }
        else:
            return {
                "status": "error",
                "message": f"Received non-200 status code: {response.status_code}",
                "content_preview": None
            }
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return {
            "status": "error",
            "message": f"Request failed: {str(e)}",
            "content_preview": None
        }


# Example usage:
if __name__ == "__main__":
    url_to_check = "http://example.com"  # Replace with the actual URL
    result = check_default_page(url_to_check)
    print(result)
```
