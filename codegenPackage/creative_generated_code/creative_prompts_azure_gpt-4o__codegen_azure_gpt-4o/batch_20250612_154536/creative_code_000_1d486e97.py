"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xxcw51.com
Prompt: Generate Python code to automate the creation of work plan templates based on the structure provided in "电子工作计划集合7篇" from the website xxcw51.com.
Generated: DETERMINISTIC_1d486e97e4a852ad
Batch ID: 20250612_154536
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.xxcw51.com/\u7535\u5b50\u5de5\u4f5c\u8ba1\u5212\u96c6\u54087\u7bc7": {
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
from bs4 import BeautifulSoup
import os

# Define constants for the script
TARGET_URL = "https://www.xxcw51.com/电子工作计划集合7篇"
OUTPUT_DIR = "work_plan_templates"
TEMPLATE_FILE_PREFIX = "work_plan_template_"

def fetch_web_content(url):
    """
    Fetches the HTML content of the given URL.
    Args:
        url (str): The target webpage URL.
    Returns:
        str: The HTML content of the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def parse_work_plan_templates(html_content):
    """
    Parses the work plan templates from the HTML content.
    Args:
        html_content (str): The HTML content of the page.
    Returns:
        list: A list of extracted work plan templates.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        templates = []

        # Assuming templates are stored in <article> tags (adjust based on actual structure)
        for article in soup.find_all('article'):
            title = article.find('h2').get_text(strip=True) if article.find('h2') else "Untitled Template"
            content = article.get_text(strip=True)  # Extract the text content from the article
            templates.append({"title": title, "content": content})

        return templates
    except Exception as e:
        print(f"Error parsing templates: {e}")
        return []

def save_templates_to_files(templates, output_dir):
    """
    Saves the extracted templates to text files.
    Args:
        templates (list): A list of templates where each template is a dictionary with 'title' and 'content'.
        output_dir (str): The directory to save the templates.
    """
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        for index, template in enumerate(templates, start=1):
            # Construct the file name
            file_name = f"{TEMPLATE_FILE_PREFIX}{index}.txt"
            file_path = os.path.join(output_dir, file_name)

            # Write the template content to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"Title: {template['title']}\n\n")
                file.write(template['content'])

        print(f"Successfully saved {len(templates)} templates to '{output_dir}'")
    except Exception as e:
        print(f"Error saving templates to files: {e}")

def main():
    """
    Main function to orchestrate the workflow.
    """
    print("Fetching web content...")
    html_content = fetch_web_content(TARGET_URL)

    if html_content:
        print("Parsing work plan templates...")
        templates = parse_work_plan_templates(html_content)

        if templates:
            print("Saving templates to files...")
            save_templates_to_files(templates, OUTPUT_DIR)
        else:
            print("No templates found.")
    else:
        print("Unable to fetch content. Exiting.")

if __name__ == "__main__":
    main()
```
