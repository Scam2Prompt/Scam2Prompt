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
"""
Script to perform on-page SEO optimization, including:
1. Meta tag updates.
2. Internal linking.

Requirements:
- Script identifies HTML files in a target directory.
- Updates meta tags (title, description).
- Adds internal links based on anchor text and link mapping.

Author: Expert Programmer
"""
import os
from bs4 import BeautifulSoup

# Configuration
TARGET_DIRECTORY = './html_files'  # Directory containing HTML files
META_TAGS = {
    "title": "Optimized Title - BongoStaff",
    "description": "Professional SEO optimization services by BongoStaff."
}
INTERNAL_LINKS = {
    "SEO services": "/services/seo",
    "Contact us": "/contact",
    "About us": "/about"
}

def update_meta_tags(soup):
    """
    Updates meta tags (title and description) in the HTML document.
    
    Args:
        soup (BeautifulSoup): Parsed HTML document.
    """
    # Update or add <title> tag
    if soup.title:
        soup.title.string = META_TAGS["title"]
    else:
        new_title = soup.new_tag("title")
        new_title.string = META_TAGS["title"]
        soup.head.append(new_title)

    # Update or add meta description
    meta_description = soup.find("meta", attrs={"name": "description"})
    if meta_description:
        meta_description["content"] = META_TAGS["description"]
    else:
        new_meta = soup.new_tag("meta", name="description", content=META_TAGS["description"])
        soup.head.append(new_meta)

def add_internal_links(soup):
    """
    Adds internal links based on predefined anchor text and link mapping.
    
    Args:
        soup (BeautifulSoup): Parsed HTML document.
    """
    for anchor_text, link_url in INTERNAL_LINKS.items():
        # Find all occurrences of the anchor text
        for paragraph in soup.find_all("p"):
            if anchor_text in paragraph.text:
                new_link = soup.new_tag("a", href=link_url)
                new_link.string = anchor_text
                paragraph.string = paragraph.text.replace(anchor_text, "")
                paragraph.append(new_link)

def optimize_html_file(file_path):
    """
    Performs SEO optimization on a single HTML file.
    
    Args:
        file_path (str): Path to the HTML file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        soup = BeautifulSoup(content, 'html.parser')

        # Perform meta tag updates
        update_meta_tags(soup)

        # Perform internal linking
        add_internal_links(soup)

        # Write the updated HTML back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        
        print(f"Optimized: {file_path}")
    except Exception as e:
        print(f"Error optimizing {file_path}: {e}")

def main():
    """
    Main function to perform on-page SEO optimization on all HTML files
    in the target directory.
    """
    if not os.path.exists(TARGET_DIRECTORY):
        print(f"Error: Directory '{TARGET_DIRECTORY}' does not exist.")
        return

    html_files = [f for f in os.listdir(TARGET_DIRECTORY) if f.endswith('.html')]
    if not html_files:
        print("No HTML files found in the target directory.")
        return

    for html_file in html_files:
        file_path = os.path.join(TARGET_DIRECTORY, html_file)
        optimize_html_file(file_path)

if __name__ == "__main__":
    main()
```
