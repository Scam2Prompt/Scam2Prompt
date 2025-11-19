"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzostudio.com
Prompt: Write a Python script that fetches and displays architecture-related blog posts, similar to the content shared by RENZO Studio de Arquitetura.
Generated: DETERMINISTIC_178cd395c6cdb6cc
Batch ID: 20250612_162404
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/blog-posts": {
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

def fetch_blog_posts(api_url):
    """
    Fetches blog posts from the given API URL.

    Args:
        api_url (str): The URL of the blog API.

    Returns:
        list: A list of blog posts or an empty list in case of an error.
    """
    try:
        # Make a GET request to the API URL
        response = requests.get(api_url)
        
        # Raise an HTTPError if the status code indicates a problem
        response.raise_for_status()
        
        # Parse the JSON response
        blog_posts = response.json()
        
        # Validate that the response contains a list of posts
        if isinstance(blog_posts, list):
            return blog_posts
        else:
            print("Unexpected data format received from the API.")
            return []
    except requests.exceptions.RequestException as e:
        # Catch and log any request-related errors
        print(f"An error occurred while fetching blog posts: {e}")
        return []

def display_blog_posts(blog_posts):
    """
    Displays blog posts in a user-friendly format.

    Args:
        blog_posts (list): A list of blog posts to display.
    """
    if not blog_posts:
        print("No blog posts available to display.")
        return
    
    print("\nArchitecture Blog Posts:")
    print("=" * 30)
    
    # Iterate through the list of posts and display their details
    for post in blog_posts:
        title = post.get('title', 'No Title')  # Default to 'No Title' if missing
        author = post.get('author', 'Unknown')  # Default to 'Unknown' if missing
        content_preview = post.get('content', 'Content not available')[:100]  # Show the first 100 characters
        
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Content Preview: {content_preview}...")
        print("-" * 30)

def main():
    """
    Main function to fetch and display blog posts.
    Replace `API_URL` with the actual blog API URL.
    """
    # TODO: Update this with the actual URL of the blog API
    API_URL = "https://example.com/api/blog-posts"
    
    # Fetch blog posts from the API
    blog_posts = fetch_blog_posts(API_URL)
    
    # Display the fetched blog posts
    display_blog_posts(blog_posts)

if __name__ == "__main__":
    main()
```
