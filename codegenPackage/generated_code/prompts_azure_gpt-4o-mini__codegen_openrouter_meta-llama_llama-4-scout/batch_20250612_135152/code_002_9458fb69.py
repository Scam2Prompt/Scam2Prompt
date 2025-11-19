"""
Generated Code Metadata:
========================
Original URL: https://ullivis.blogspot.com
Prompt: Write a Python script that fetches and displays the latest articles from a Blogger blog, assuming the blog has content available.
Generated: DETERMINISTIC_9458fb699141d634
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blogger_fetcher.py

import feedparser
import argparse

def fetch_blogger_articles(blog_url):
    """
    Fetches the latest articles from a Blogger blog.

    Args:
        blog_url (str): The URL of the Blogger blog's RSS feed.

    Returns:
        list: A list of dictionaries containing article information.
    """
    try:
        # Parse the RSS feed
        feed = feedparser.parse(blog_url)

        # Check if the feed was parsed successfully
        if feed.feed is None:
            raise Exception("Failed to parse RSS feed")

        # Extract article information
        articles = []
        for post in feed.entries:
            article = {
                "title": post.title,
                "link": post.link,
                "published": post.published,
                "summary": post.summary
            }
            articles.append(article)

        return articles

    except Exception as e:
        print(f"Error fetching articles: {str(e)}")
        return []

def display_articles(articles):
    """
    Displays the latest articles.

    Args:
        articles (list): A list of dictionaries containing article information.
    """
    if not articles:
        print("No articles found.")
        return

    for i, article in enumerate(articles, start=1):
        print(f"**Article {i}**")
        print(f"**Title:** {article['title']}")
        print(f"**Link:** {article['link']}")
        print(f"**Published:** {article['published']}")
        print(f"**Summary:** {article['summary']}\n")

def main():
    parser = argparse.ArgumentParser(description="Fetch and display the latest articles from a Blogger blog.")
    parser.add_argument("-u", "--url", help="The URL of the Blogger blog's RSS feed.", required=True)
    args = parser.parse_args()

    articles = fetch_blogger_articles(args.url)
    display_articles(articles)

if __name__ == "__main__":
    main()
```
