"""
Generated Code Metadata:
========================
Original URL: https://pooleth.net
Prompt: Generate a code snippet that demonstrates how to create a blog post using the Hatena Blog API, including features like tagging and scheduling.
Generated: DETERMINISTIC_040746dfc7c3db31
Batch ID: 20250612_155144
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://blog.hatena.ne.jp/{username}/{blog_id}/atom/entry": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/2005/Atom": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from datetime import datetime, timedelta
from xml.etree.ElementTree import Element, SubElement, tostring

# Hatena Blog API credentials
API_BASE_URL = "https://blog.hatena.ne.jp/{username}/{blog_id}/atom/entry"
USERNAME = "your_username"
BLOG_ID = "your_blog_id"
API_KEY = "your_api_key"

# Function to create a blog post
def create_blog_post(title, content, tags, publish_date=None):
    """
    Create a blog post on Hatena Blog using the API.

    Args:
        title (str): Title of the blog post.
        content (str): Content of the blog post (HTML format).
        tags (list): List of tags for the blog post.
        publish_date (datetime, optional): Scheduled publish date. If None, publish immediately.

    Returns:
        dict: Response from the Hatena Blog API.
    """
    try:
        # Construct the XML payload for the blog post
        entry = Element("entry", xmlns="http://www.w3.org/2005/Atom")
        
        # Add title
        title_element = SubElement(entry, "title")
        title_element.text = title
        
        # Add content
        content_element = SubElement(entry, "content", type="text/html")
        content_element.text = content
        
        # Add tags (categories)
        for tag in tags:
            category_element = SubElement(entry, "category", term=tag)
        
        # Add publish date if provided
        if publish_date:
            published_element = SubElement(entry, "published")
            published_element.text = publish_date.isoformat()
        
        # Convert XML tree to string
        xml_payload = tostring(entry, encoding="utf-8").decode("utf-8")
        
        # Make the API request
        headers = {
            "Content-Type": "application/xml",
            "Authorization": f"Basic {API_KEY}"
        }
        response = requests.post(API_BASE_URL.format(username=USERNAME, blog_id=BLOG_ID), 
                                 headers=headers, 
                                 data=xml_payload)
        
        # Check for errors
        response.raise_for_status()
        
        # Return the API response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Handle HTTP errors
        print(f"An error occurred while making the API request: {e}")
        return {"error": str(e)}
    except Exception as e:
        # Handle other errors
        print(f"An unexpected error occurred: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Blog post details
    post_title = "My First Blog Post"
    post_content = "<p>This is the content of my first blog post!</p>"
    post_tags = ["Programming", "Python", "API"]
    post_publish_date = datetime.now() + timedelta(days=1)  # Schedule for tomorrow
    
    # Create the blog post
    response = create_blog_post(post_title, post_content, post_tags, post_publish_date)
    
    # Print the response
    print(response)
```
