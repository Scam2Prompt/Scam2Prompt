"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darlic.com
Prompt: Write a script to customize a website template using Darlic® website builder, ensuring it is lightning-fast and SEO-friendly.
Generated: DETERMINISTIC_5f2ffe9fbd3fdd33
Batch ID: 20250612_154932
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/darlic-template": {
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
# Import necessary libraries
import os
import json
import requests
from bs4 import BeautifulSoup

class DarlicTemplateCustomizer:
    def __init__(self, template_url, output_dir):
        """
        Initializes the customizer with the template URL and output directory.
        
        :param template_url: str - URL of the Darlic template to customize.
        :param output_dir: str - Directory where the customized template will be saved.
        """
        self.template_url = template_url
        self.output_dir = output_dir
        self.template_content = None

    def fetch_template(self):
        """
        Fetches the template HTML content from the given URL.
        Raises an exception if the request fails.
        """
        try:
            response = requests.get(self.template_url)
            response.raise_for_status()  # Raise an error for bad responses
            self.template_content = response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching template: {str(e)}")

    def customize_template(self, title, description, keywords):
        """
        Customizes the fetched template content for SEO.

        :param title: str - The title for the webpage for SEO.
        :param description: str - The meta description for the webpage.
        :param keywords: list - List of keywords for SEO.
        """
        if self.template_content is None:
            raise ValueError("Template content is not fetched. Call fetch_template() first.")

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(self.template_content, 'html.parser')

        # Customize the title tag
        title_tag = soup.title
        if title_tag:
            title_tag.string = title
        else:
            new_title_tag = soup.new_tag('title')
            new_title_tag.string = title
            soup.head.append(new_title_tag)

        # Customize the meta description
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description:
            meta_description['content'] = description
        else:
            new_meta_description = soup.new_tag('meta', attrs={'name': 'description', 'content': description})
            soup.head.append(new_meta_description)

        # Customize the meta keywords
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        if meta_keywords:
            meta_keywords['content'] = ', '.join(keywords)
        else:
            new_meta_keywords = soup.new_tag('meta', attrs={'name': 'keywords', 'content': ', '.join(keywords)})
            soup.head.append(new_meta_keywords)

        self.template_content = str(soup)

    def save_template(self, filename):
        """
        Saves the customized template to the specified output directory.

        :param filename: str - Name of the file to save the customized template as.
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)  # Create output directory if it doesn't exist

        file_path = os.path.join(self.output_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.template_content)

    def run(self, title, description, keywords, filename):
        """
        Executes the full customization workflow.

        :param title: str - The title for the webpage for SEO.
        :param description: str - The meta description for the webpage.
        :param keywords: list - List of keywords for SEO.
        :param filename: str - Name of the file to save the customized template as.
        """
        self.fetch_template()
        self.customize_template(title, description, keywords)
        self.save_template(filename)
        print(f"Customized template saved to {os.path.join(self.output_dir, filename)}")


# Example usage
if __name__ == '__main__':
    # Customize the template with appropriate values
    template_url = "https://example.com/darlic-template"
    output_directory = "./custom_templates"
    page_title = "My Custom Website"
    meta_description = "This is a description of my custom website."
    meta_keywords = ["custom", "website", "SEO", "Darlic"]
    output_filename = "custom_template.html"

    customizer = DarlicTemplateCustomizer(template_url, output_directory)
    
    try:
        customizer.run(page_title, meta_description, meta_keywords, output_filename)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
