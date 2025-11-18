"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Write a Python script to generate a sitemap for a WordPress blog to improve SEO.
Generated: DETERMINISTIC_40b07812e77070bd
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://www.sitemaps.org/schemas/sitemap-image/1.1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourwordpressblog.com": {
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
import os
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urljoin

# Configuration
BASE_URL = 'https://yourwordpressblog.com'  # Replace with your blog's base URL
POSTS_DIRECTORY = './posts'  # Replace with the directory containing your blog posts

def create_sitemap(posts):
    """
    Create an XML sitemap for the given list of posts.

    Args:
        posts (list of dict): A list of dictionaries containing post information.

    Returns:
        str: A string representation of the XML sitemap.
    """
    # Create the root element for the XML sitemap
    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap-image/1.1")

    for post in posts:
        # Create a URL entry for each post
        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = urljoin(BASE_URL, post['slug'])
        ET.SubElement(url, 'lastmod').text = post['last_modified'].isoformat()
        ET.SubElement(url, 'changefreq').text = 'monthly'
        ET.SubElement(url, 'priority').text = '0.5'
    
    # Convert the XML tree to a string
    xml_str = ET.tostring(urlset, encoding='utf-8', method='xml').decode('utf-8')
    return xml_str

def fetch_posts(directory):
    """
    Fetch posts from the specified directory.

    Args:
        directory (str): The directory containing the blog posts.

    Returns:
        list of dict: A list of dictionaries with post slugs and last modified dates.
    """
    posts = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.md'):  # Assuming markdown files for blog posts
                # Generate post info
                slug = filename[:-3]  # Remove .md extension
                last_modified = datetime.fromtimestamp(os.path.getmtime(os.path.join(directory, filename)))
                posts.append({'slug': slug, 'last_modified': last_modified})
    except Exception as e:
        print(f"Error reading posts: {e}")
        raise

    return posts

def save_sitemap(sitemap, output_file='sitemap.xml'):
    """
    Save the generated sitemap to an XML file.

    Args:
        sitemap (str): The XML string representation of the sitemap.
        output_file (str): The output file path for the sitemap.
    """
    try:
        with open(output_file, 'w') as f:
            f.write(sitemap)
        print(f"Sitemap saved to {output_file}")
    except IOError as e:
        print(f"Error saving sitemap: {e}")
        raise

def main():
    """
    Main function to generate the sitemap for the WordPress blog.
    """
    try:
        # Fetch posts from the specified directory
        posts = fetch_posts(POSTS_DIRECTORY)

        # Create a sitemap from the posts
        sitemap = create_sitemap(posts)

        # Save the sitemap to an XML file
        save_sitemap(sitemap)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
