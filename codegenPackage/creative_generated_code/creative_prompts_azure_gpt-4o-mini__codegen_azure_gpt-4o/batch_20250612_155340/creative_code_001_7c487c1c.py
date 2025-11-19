"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getafreehomedelivary.blogspot.com
Prompt: How can I use the Blogger API to create a subscription feature for my blog posts?
Generated: DETERMINISTIC_7c487c1c70054dc0
Batch ID: 20250612_155340
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts": {
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

# Constants for Blogger API
API_KEY = 'your-api-key-here'  # Replace with your Blogger API key
BLOG_ID = 'your-blog-id-here'  # Replace with your blog ID
BLOGGER_API_URL = f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts'

# Subscription management
SUBSCRIBERS_FILE = 'subscribers.txt'  # File to store subscriber email addresses

def add_subscriber(email):
    """
    Adds a subscriber email to the subscribers file.
    """
    try:
        with open(SUBSCRIBERS_FILE, 'a') as file:
            file.write(f'{email}\n')
        print(f'Subscriber {email} added successfully.')
    except IOError as e:
        print(f'Error saving subscriber: {e}')

def get_subscribers():
    """
    Retrieves the list of subscriber emails.
    """
    try:
        with open(SUBSCRIBERS_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except IOError:
        # If the file doesn't exist, return an empty list
        return []

def fetch_latest_post():
    """
    Fetches the latest blog post from the Blogger API.

    Returns:
        dict: The latest blog post details.
    """
    try:
        response = requests.get(BLOGGER_API_URL, params={'key': API_KEY, 'maxResults': 1})
        response.raise_for_status()  # Raise an error for HTTP issues
        posts = response.json().get('items', [])
        return posts[0] if posts else None
    except requests.RequestException as e:
        print(f'Error fetching latest post: {e}')
        return None

def notify_subscribers(post):
    """
    Sends a notification to all subscribers about a new post.

    Args:
        post (dict): The blog post details.
    """
    if not post:
        print('No post to notify subscribers about.')
        return

    subscribers = get_subscribers()
    if not subscribers:
        print('No subscribers to notify.')
        return

    # This is a placeholder for sending notifications (e.g., email).
    # In production, replace this with an actual email sending service.
    for subscriber in subscribers:
        print(f'Sending notification to {subscriber}:')
        print(f'Subject: New Blog Post - {post["title"]}')
        print(f'Link: {post["url"]}\n')

def main():
    """
    Main function to handle subscription feature.
    """
    print("Welcome to the Blogger Subscription Feature!")
    
    while True:
        print("\nMenu:")
        print("1. Add Subscriber")
        print("2. Notify Subscribers of Latest Post")
        print("3. View Subscribers")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            email = input("Enter subscriber email: ")
            add_subscriber(email)
        elif choice == '2':
            latest_post = fetch_latest_post()
            notify_subscribers(latest_post)
        elif choice == '3':
            subscribers = get_subscribers()
            print("Subscribers:")
            for subscriber in subscribers:
                print(subscriber)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```
