"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Generate Python code to automate the creation of work plan templates based on the structure provided in "电子工作计划集合7篇" from the website xxcw51.com.
Generated: DETERMINISTIC_1d486e97e4a852ad
Batch ID: 20250612_154536
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://xxcw51.com/\u7535\u5b50\u5de5\u4f5c\u8ba1\u5212\u96c6\u54087\u7bc7": {
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
import os
import requests
from bs4 import BeautifulSoup
from docx import Document

class WorkPlanTemplateGenerator:
    def __init__(self, url):
        """
        Initialize the WorkPlanTemplateGenerator with the URL of the work plan collection.
        
        :param url: str - The URL to fetch the work plan templates from.
        """
        self.url = url
        self.templates = []

    def fetch_templates(self):
        """
        Fetch the work plan templates from the specified URL.
        This method retrieves the HTML content and parses it to extract template data.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Assuming the templates are in <div class="template"> elements
            for template_div in soup.find_all('div', class_='template'):
                title = template_div.find('h2').text.strip()
                content = template_div.find('p').text.strip()
                self.templates.append({'title': title, 'content': content})
        except requests.RequestException as e:
            print(f"Error fetching templates: {e}")

    def create_word_documents(self):
        """
        Create Word documents for each template fetched.
        Each document will be named after the template title.
        """
        for template in self.templates:
            self._create_word_document(template['title'], template['content'])

    def _create_word_document(self, title, content):
        """
        Create a Word document for a single template.
        
        :param title: str - The title of the template.
        :param content: str - The content of the template.
        """
        try:
            doc = Document()
            doc.add_heading(title, level=1)
            doc.add_paragraph(content)
            
            # Save the document with a sanitized title
            sanitized_title = self._sanitize_filename(title)
            doc.save(f"{sanitized_title}.docx")
            print(f"Document '{sanitized_title}.docx' created successfully.")
        except Exception as e:
            print(f"Error creating document for '{title}': {e}")

    @staticmethod
    def _sanitize_filename(filename):
        """
        Sanitize the filename to ensure it is valid for the filesystem.
        
        :param filename: str - The original filename.
        :return: str - The sanitized filename.
        """
        return "".join(c for c in filename if c.isalnum() or c in (' ', '_')).rstrip()

def main():
    url = "http://xxcw51.com/电子工作计划集合7篇"  # Replace with the actual URL
    generator = WorkPlanTemplateGenerator(url)
    
    generator.fetch_templates()
    if generator.templates:
        generator.create_word_documents()
    else:
        print("No templates found.")

if __name__ == "__main__":
    main()
```
