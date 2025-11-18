"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-protocol.net
Prompt: Create a program that uses the Wattpad API to identify stories with high engagement metrics and suggest them for adaptation into books via Wattpad Books.
Generated: DETERMINISTIC_bec5d60f61a15550
Batch ID: 20250612_152018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wattpad.com/v4/stories": {
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

# Constants
API_BASE_URL = "https://api.wattpad.com/v4/stories"
API_KEY = "your_api_key_here"  # Replace with your Wattpad API key
MINIMUM_VOTES = 5000  # Minimum number of votes to consider a story highly engaging
MINIMUM_READS = 100000  # Minimum number of reads to consider a story highly engaging

def fetch_trending_stories(api_key):
    """
    Fetch trending stories from the Wattpad API.

    Args:
        api_key (str): The API key for Wattpad.

    Returns:
        list: A list of stories returned by the API.
    """
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(f"{API_BASE_URL}/hot", headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json().get("stories", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trending stories: {e}")
        return []

def filter_high_engagement_stories(stories, min_votes, min_reads):
    """
    Filter stories based on high engagement metrics.

    Args:
        stories (list): A list of stories.
        min_votes (int): Minimum number of votes to qualify as high engagement.
        min_reads (int): Minimum number of reads to qualify as high engagement.

    Returns:
        list: A list of stories with high engagement.
    """
    return [
        story for story in stories
        if story.get("voteCount", 0) >= min_votes and story.get("readCount", 0) >= min_reads
    ]

def suggest_books_for_adaptation(stories):
    """
    Suggest stories for adaptation into books.

    Args:
        stories (list): High engagement stories.

    Returns:
        None
    """
    print("Suggested Stories for Book Adaptation:")
    for story in stories:
        print(f"- Title: {story.get('title')}, Author: {story.get('user', {}).get('name')}")
        print(f"  Reads: {story.get('readCount')}, Votes: {story.get('voteCount')}")
        print(f"  URL: {story.get('url')}\n")

def main():
    """
    Main function to orchestrate the program workflow.
    """
    print("Fetching trending stories from Wattpad...")
    stories = fetch_trending_stories(API_KEY)

    if not stories:
        print("No stories found or an error occurred.")
        return

    print("Filtering stories with high engagement...")
    high_engagement_stories = filter_high_engagement_stories(stories, MINIMUM_VOTES, MINIMUM_READS)

    if not high_engagement_stories:
        print("No stories meet the engagement criteria.")
        return

    suggest_books_for_adaptation(high_engagement_stories)

if __name__ == "__main__":
    main()
```
