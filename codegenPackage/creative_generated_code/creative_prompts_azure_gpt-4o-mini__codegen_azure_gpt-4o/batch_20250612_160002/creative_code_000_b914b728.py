"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Generate a Python script that utilizes SEO best practices for a digital marketing campaign, as outlined in the PDMA Technologies training program.
Generated: DETERMINISTIC_b914b728b56815c1
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
SEO Digital Marketing Script
This script automates the process of optimizing URLs and generating meta tags
for a digital marketing campaign. It follows SEO best practices to enhance website visibility.
"""

import os
import re
import logging
from datetime import datetime


# Configure logging for tracking and debugging
logging.basicConfig(
    filename="seo_script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def generate_meta_tags(title, description, keywords):
    """
    Generate SEO meta tags given a title, description, and keywords.

    Args:
        title (str): The title of the webpage, ideally 50-60 characters.
        description (str): The meta description, ideally 150-160 characters.
        keywords (list): A list of keywords relevant to the webpage.

    Returns:
        dict: A dictionary containing meta tag information.
    """
    # Validate input lengths
    if len(title) > 60:
        logging.warning("Title length exceeds 60 characters. Consider shortening it.")
    if len(description) > 160:
        logging.warning("Description length exceeds 160 characters. Consider shortening it.")

    # Create meta tag information
    meta_tags = {
        "title": title,
        "description": description,
        "keywords": ", ".join(keywords)
    }

    logging.info("Meta tags successfully generated.")
    return meta_tags


def optimize_url(url):
    """
    Optimize a given URL to follow SEO-friendly guidelines.

    Args:
        url (str): The URL to optimize.

    Returns:
        str: The optimized URL.
    """
    # Convert URL to lowercase
    optimized_url = url.lower()

    # Replace spaces with hyphens
    optimized_url = re.sub(r"\s+", "-", optimized_url)

    # Remove special characters (except hyphens)
    optimized_url = re.sub(r"[^a-z0-9\-]", "", optimized_url)

    logging.info(f"URL optimized successfully: {optimized_url}")
    return optimized_url


def save_seo_data(meta_tags, url, output_file="seo_data.txt"):
    """
    Save meta tags and optimized URL into a file.

    Args:
        meta_tags (dict): Dictionary containing meta tag information.
        url (str): Optimized URL.
        output_file (str): Path to the output file.
    """
    try:
        with open(output_file, "a") as file:
            file.write(f"Title: {meta_tags['title']}\n")
            file.write(f"Description: {meta_tags['description']}\n")
            file.write(f"Keywords: {meta_tags['keywords']}\n")
            file.write(f"Optimized URL: {url}\n")
            file.write("-" * 40 + "\n")

        logging.info(f"SEO data successfully saved to {output_file}.")
    except Exception as e:
        logging.error(f"Error saving SEO data: {e}")


def main():
    """
    Main function to execute the SEO optimization process.
    """
    # Example inputs for a webpage
    page_title = "Learn Digital Marketing Strategies"
    page_description = (
        "Explore the best digital marketing tactics to boost your online presence. "
        "Learn SEO, PPC, and social media marketing tips."
    )
    page_keywords = ["digital marketing", "SEO", "PPC", "social media marketing"]
    page_url = "www.example.com/learn digital marketing"

    logging.info("Starting SEO optimization process.")

    # Generate meta tags
    meta_tags = generate_meta_tags(page_title, page_description, page_keywords)

    # Optimize URL
    optimized_url = optimize_url(page_url)

    # Save SEO data to file
    save_seo_data(meta_tags, optimized_url)

    logging.info("SEO optimization process completed.")


if __name__ == "__main__":
    # Check if log file exists and archive it
    if os.path.exists("seo_script.log"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.rename("seo_script.log", f"seo_script_{timestamp}.log")

    # Run the main function
    main()
```
