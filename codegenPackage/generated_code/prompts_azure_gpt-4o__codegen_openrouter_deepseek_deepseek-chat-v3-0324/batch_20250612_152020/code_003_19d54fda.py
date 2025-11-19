"""
Generated Code Metadata:
========================
Original URL: https://corridorweb.com
Prompt: Provide code examples for integrating social media optimization features into a website, based on Corridor Web Agency's SMO strategies.
Generated: DETERMINISTIC_19d54fda9f8122c9
Batch ID: 20250612_152020
URLs Found: 9
Malicious URLs: 0

Oracle Results:
{
  "https://www.linkedin.com/sharing/share-offsite/?url={encoded_url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0/?id={quote_plus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/intent/tweet?url={encoded_url}&text={encoded_title": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://pinterest.com/pin/create/button/?url={encoded_url}&description={encoded_title": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0/?id={quote_plus(url)}&fields=engagement": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.syndication.twimg.com/widgets/tweetbuttons/count.json?url={quote_plus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u={encoded_url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.syndication.twimg.com/widgets/tweetbuttons/count.json?url={quote_plus(url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://wa.me/?text={encoded_title}%20{encoded_url": {
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
# social_media_optimization.py

import json
from typing import Dict, Optional
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.utils.html import strip_tags


class SocialMediaOptimizer:
    """
    Handles social media optimization features for a website.
    Implements Corridor Web Agency's SMO strategies.
    """

    def __init__(self):
        self.facebook_app_id = getattr(settings, 'FACEBOOK_APP_ID', '')
        self.twitter_handle = getattr(settings, 'TWITTER_HANDLE', '')
        self.default_image = getattr(settings, 'DEFAULT_SOCIAL_IMAGE', '')

    def generate_meta_tags(self, title: str, description: str, 
                         image_url: Optional[str] = None,
                         url: Optional[str] = None,
                         keywords: Optional[str] = None) -> Dict[str, str]:
        """
        Generates optimized meta tags for social media sharing.
        
        Args:
            title: Page title (60 chars max for optimal display)
            description: Page description (160 chars max)
            image_url: URL of the social sharing image
            url: Canonical URL of the page
            keywords: Comma-separated keywords
            
        Returns:
            Dictionary of meta tags for template rendering
        """
        if not image_url:
            image_url = self.default_image
            
        meta_tags = {
            # Standard meta tags
            'title': title[:60],
            'description': description[:160],
            'keywords': keywords,
            
            # Open Graph (Facebook)
            'og:title': title[:60],
            'og:description': description[:160],
            'og:image': image_url,
            'og:url': url,
            'og:type': 'website',
            'og:site_name': settings.SITE_NAME,
            'og:locale': 'en_US',
            'fb:app_id': self.facebook_app_id,
            
            # Twitter Cards
            'twitter:card': 'summary_large_image',
            'twitter:site': self.twitter_handle,
            'twitter:creator': self.twitter_handle,
            'twitter:title': title[:60],
            'twitter:description': description[:160],
            'twitter:image': image_url,
        }
        
        return meta_tags

    def extract_content_for_sharing(self, html_content: str) -> Dict[str, str]:
        """
        Extracts relevant content from HTML for social sharing.
        
        Args:
            html_content: Raw HTML content to analyze
            
        Returns:
            Dictionary with title, description, and first image found
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Get title from h1 or title tag
        title = ''
        h1 = soup.find('h1')
        if h1:
            title = strip_tags(str(h1))
        else:
            title_tag = soup.find('title')
            if title_tag:
                title = strip_tags(str(title_tag))
        
        # Get description from meta or first paragraph
        description = ''
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            description = meta_desc['content']
        else:
            first_p = soup.find('p')
            if first_p:
                description = strip_tags(str(first_p))[:160]
        
        # Get first image
        image_url = ''
        first_img = soup.find('img')
        if first_img and first_img.get('src'):
            image_url = first_img['src']
        
        return {
            'title': title,
            'description': description,
            'image_url': image_url if image_url else self.default_image
        }

    def get_facebook_shares(self, url: str) -> int:
        """
        Gets Facebook share count for a URL.
        
        Args:
            url: URL to check
            
        Returns:
            Number of shares (0 if error occurs)
        """
        try:
            api_url = f"https://graph.facebook.com/v12.0/?id={quote_plus(url)}&fields=engagement"
            response = requests.get(api_url, timeout=5)
            data = response.json()
            return data.get('engagement', {}).get('share_count', 0)
        except (requests.RequestException, json.JSONDecodeError, KeyError):
            return 0

    def get_twitter_shares(self, url: str) -> int:
        """
        Gets Twitter share count for a URL (using unofficial API).
        
        Args:
            url: URL to check
            
        Returns:
            Number of shares (0 if error occurs)
        """
        try:
            api_url = f"https://cdn.syndication.twimg.com/widgets/tweetbuttons/count.json?url={quote_plus(url)}"
            response = requests.get(api_url, timeout=5)
            data = response.json()
            return int(data.get('count', 0))
        except (requests.RequestException, json.JSONDecodeError, ValueError):
            return 0

    def generate_share_urls(self, url: str, title: str) -> Dict[str, str]:
        """
        Generates social sharing URLs for a page.
        
        Args:
            url: URL to share
            title: Title of the content
            
        Returns:
            Dictionary with platform-specific share URLs
        """
        encoded_url = quote_plus(url)
        encoded_title = quote_plus(title)
        
        return {
            'facebook': f"https://www.facebook.com/sharer/sharer.php?u={encoded_url}",
            'twitter': f"https://twitter.com/intent/tweet?url={encoded_url}&text={encoded_title}",
            'linkedin': f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}",
            'pinterest': f"https://pinterest.com/pin/create/button/?url={encoded_url}&description={encoded_title}",
            'whatsapp': f"https://wa.me/?text={encoded_title}%20{encoded_url}",
        }
```
