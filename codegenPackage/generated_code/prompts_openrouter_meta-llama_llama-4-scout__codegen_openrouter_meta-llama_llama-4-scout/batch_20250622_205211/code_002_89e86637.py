"""
Generated Code Metadata:
========================
Original URL: https://meredithgastonmasnata.com
Prompt: Generate a Python script to create a basic website structure similar to Meredith Gaston Masnata's, featuring sections for Books, Art, Wellbeing, Speaking, Workshops, and Photography.
Generated: DETERMINISTIC_89e86637bf988a51
Batch ID: 20250622_205211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# website_generator.py

import os

class WebsiteGenerator:
    def __init__(self, website_name):
        """
        Initialize the website generator.

        Args:
            website_name (str): The name of the website.
        """
        self.website_name = website_name
        self.structure = {
            "Books": [],
            "Art": [],
            "Wellbeing": [],
            "Speaking": [],
            "Workshops": [],
            "Photography": []
        }

    def create_website_structure(self):
        """
        Create the basic website structure.
        """
        try:
            # Create the website directory
            os.mkdir(self.website_name)
            print(f"Website directory '{self.website_name}' created.")

            # Create the sections directories
            for section in self.structure:
                section_dir = os.path.join(self.website_name, section.lower())
                os.mkdir(section_dir)
                print(f"Section directory '{section}' created.")

                # Create index.html file for each section
                self.create_index_html(section_dir, section)

            # Create index.html file for the website
            self.create_website_index_html(self.website_name)

        except FileExistsError:
            print(f"Website directory '{self.website_name}' already exists.")

    def create_index_html(self, directory, section):
        """
        Create an index.html file for a section.

        Args:
            directory (str): The directory path.
            section (str): The section name.
        """
        index_html = f"""
        <!-- {section} Section Index -->
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{section}</title>
        </head>
        <body>
            <h1>{section}</h1>
            <p>Welcome to the {section} section.</p>
        </body>
        </html>
        """
        with open(os.path.join(directory, "index.html"), "w") as file:
            file.write(index_html)

    def create_website_index_html(self, website_name):
        """
        Create an index.html file for the website.

        Args:
            website_name (str): The website name.
        """
        index_html = f"""
        <!-- Website Index -->
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{website_name}</title>
        </head>
        <body>
            <h1>{website_name}</h1>
            <ul>
                {"".join([f"<li><a href='{section.lower()}/'>{section}</a></li>" for section in self.structure])}
            </ul>
        </body>
        </html>
        """
        with open(os.path.join(website_name, "index.html"), "w") as file:
            file.write(index_html)


if __name__ == "__main__":
    website_name = "meredith-gaston-masnata"
    generator = WebsiteGenerator(website_name)
    generator.create_website_structure()
```
