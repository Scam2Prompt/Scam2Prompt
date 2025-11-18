"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bongostaff.com
Prompt: Create a script to perform on-page SEO optimization, including meta tag updates and internal linking, as outlined by BongoStaff.
Generated: DETERMINISTIC_e0ad4c4ad49161db
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
from bs4 import BeautifulSoup

class SEOOptimizer:
    """
    A class to perform on-page SEO optimization, including meta tag updates and internal linking.
    """

    def __init__(self, html_file_path):
        """Initialize the optimizer with the path to the HTML file."""
        self.html_file_path = html_file_path
        self.soup = self._load_html()

    def _load_html(self):
        """Load HTML content from the specified file path."""
        try:
            with open(self.html_file_path, 'r', encoding='utf-8') as file:
                return BeautifulSoup(file, 'html.parser')
        except FileNotFoundError:
            raise FileNotFoundError(f"HTML file not found at {self.html_file_path}")
        except Exception as e:
            raise Exception(f"An error occurred while loading the HTML file: {e}")

    def update_meta_tags(self, title=None, description=None, keywords=None):
        """
        Update the meta tags in the HTML document.

        :param title: New title for the page
        :param description: New description for the page
        :param keywords: New keywords for the page
        """
        if title:
            self._set_meta_tag('title', title)
        if description:
            self._set_meta_tag('meta', {'name': 'description', 'content': description})
        if keywords:
            self._set_meta_tag('meta', {'name': 'keywords', 'content': keywords})

    def _set_meta_tag(self, tag_name, attributes):
        """Set a specific meta tag in the HTML document."""
        if tag_name == 'title':
            self.soup.title.string = attributes
        else:
            existing_meta = self.soup.find(tag_name, attrs={'name': attributes['name']})
            if existing_meta:
                existing_meta['content'] = attributes['content']
            else:
                meta_tag = self.soup.new_tag(tag_name, **attributes)
                self.soup.head.append(meta_tag)

    def update_internal_links(self, old_url, new_url):
        """
        Update internal links from old_url to new_url in the HTML document.

        :param old_url: The old URL to be replaced
        :param new_url: The new URL to replace with
        """
        links_updated = 0
        for link in self.soup.find_all('a', href=True):
            if old_url in link['href']:
                link['href'] = re.sub(re.escape(old_url), new_url, link['href'])
                links_updated += 1
        return links_updated

    def save_changes(self, output_file_path):
        """Save the updated HTML content to a new file."""
        try:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(str(self.soup))
        except Exception as e:
            raise Exception(f"An error occurred while saving the HTML file: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        seo_optimizer = SEOOptimizer('example.html')
        seo_optimizer.update_meta_tags(
            title="New Page Title",
            description="This is a new description for SEO optimization.",
            keywords="seo, optimization, example"
        )
        updated_links_count = seo_optimizer.update_internal_links('old-url.com', 'new-url.com')
        print(f"Updated {updated_links_count} internal links.")
        seo_optimizer.save_changes('optimized_example.html')
    except Exception as e:
        print(f"Error: {e}")
```
