"""
Generated Code Metadata:
========================
Original URL: https://deviationinfotech.in
Prompt: "Develop a web scraping tool using Python and BeautifulSoup to extract data from social media platforms for a digital marketing project, similar to Deviation Infotech's data-driven marketing approach."
Generated: DETERMINISTIC_08eb32b9e04684ee
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_media_scraper.py

import requests
from bs4 import BeautifulSoup
import logging
from logging.handlers import RotatingFileHandler
import json
import argparse

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
file_handler = RotatingFileHandler('social_media_scraper.log', maxBytes=1024*1024*10, backupCount=5)
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def scrape_facebook_page(url):
    """
    Scrapes a Facebook page and extracts the page's name, description, and posts.

    Args:
        url (str): The URL of the Facebook page to scrape.

    Returns:
        dict: A dictionary containing the page's name, description, and posts.
    """
    try:
        # Send a GET request to the Facebook page
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the page's name and description
        page_name = soup.find('title').text.strip()
        page_description = soup.find('meta', attrs={'name': 'description'})
        if page_description:
            page_description = page_description.get('content')
        else:
            page_description = ''

        # Extract the page's posts
        posts = []
        post_containers = soup.find_all('div', class_='fb-post')
        for post in post_containers:
            post_text = post.find('div', class_='fb-post-inner')
            if post_text:
                posts.append(post_text.text.strip())

        return {
            'name': page_name,
            'description': page_description,
            'posts': posts
        }

    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while scraping the Facebook page: {e}")
        return None

def scrape_twitter_profile(url):
    """
    Scrapes a Twitter profile and extracts the profile's name, bio, and tweets.

    Args:
        url (str): The URL of the Twitter profile to scrape.

    Returns:
        dict: A dictionary containing the profile's name, bio, and tweets.
    """
    try:
        # Send a GET request to the Twitter profile
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the profile's name and bio
        profile_name = soup.find('title').text.strip()
        profile_bio = soup.find('div', class_='bio')
        if profile_bio:
            profile_bio = profile_bio.text.strip()
        else:
            profile_bio = ''

        # Extract the profile's tweets
        tweets = []
        tweet_containers = soup.find_all('div', class_='tweet')
        for tweet in tweet_containers:
            tweet_text = tweet.find('div', class_='tweet-text')
            if tweet_text:
                tweets.append(tweet_text.text.strip())

        return {
            'name': profile_name,
            'bio': profile_bio,
            'tweets': tweets
        }

    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while scraping the Twitter profile: {e}")
        return None

def scrape_instagram_profile(url):
    """
    Scrapes an Instagram profile and extracts the profile's name, bio, and posts.

    Args:
        url (str): The URL of the Instagram profile to scrape.

    Returns:
        dict: A dictionary containing the profile's name, bio, and posts.
    """
    try:
        # Send a GET request to the Instagram profile
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the profile's name and bio
        profile_name = soup.find('title').text.strip()
        profile_bio = soup.find('meta', attrs={'name': 'description'})
        if profile_bio:
            profile_bio = profile_bio.get('content')
        else:
            profile_bio = ''

        # Extract the profile's posts
        posts = []
        post_containers = soup.find_all('div', class_='media')
        for post in post_containers:
            post_text = post.find('div', class_='media-caption')
            if post_text:
                posts.append(post_text.text.strip())

        return {
            'name': profile_name,
            'bio': profile_bio,
            'posts': posts
        }

    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while scraping the Instagram profile: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Social Media Scraper')
    parser.add_argument('--facebook', help='Facebook page URL')
    parser.add_argument('--twitter', help='Twitter profile URL')
    parser.add_argument('--instagram', help='Instagram profile URL')
    parser.add_argument('--output', help='Output file path', default='output.json')
    args = parser.parse_args()

    data = {}

    if args.facebook:
        facebook_data = scrape_facebook_page(args.facebook)
        if facebook_data:
            data['facebook'] = facebook_data

    if args.twitter:
        twitter_data = scrape_twitter_profile(args.twitter)
        if twitter_data:
            data['twitter'] = twitter_data

    if args.instagram:
        instagram_data = scrape_instagram_profile(args.instagram)
        if instagram_data:
            data['instagram'] = instagram_data

    if data:
        with open(args.output, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Data scraped and saved to {args.output}")
    else:
        logger.info("No data scraped")

if __name__ == '__main__':
    main()
```
