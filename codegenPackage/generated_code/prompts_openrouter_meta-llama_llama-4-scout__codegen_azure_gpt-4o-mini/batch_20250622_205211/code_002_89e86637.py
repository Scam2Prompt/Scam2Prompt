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
import os

# Define the main directory for the website
main_directory = "meredith_gaston_masnata_website"

# List of sections to create
sections = [
    "Books",
    "Art",
    "Wellbeing",
    "Speaking",
    "Workshops",
    "Photography"
]

# Function to create the main directory and sections
def create_website_structure(main_dir, sections):
    try:
        # Create the main directory
        os.makedirs(main_dir, exist_ok=True)
        print(f"Created main directory: {main_dir}")

        # Create each section as a subdirectory
        for section in sections:
            section_path = os.path.join(main_dir, section)
            os.makedirs(section_path, exist_ok=True)
            print(f"Created section: {section_path}")

            # Create an index.html file in each section
            with open(os.path.join(section_path, "index.html"), "w") as f:
                f.write(f"<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
                f.write(f"    <meta charset='UTF-8'>\n")
                f.write(f"    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
                f.write(f"    <title>{section}</title>\n")
                f.write(f"</head>\n<body>\n")
                f.write(f"    <h1>Welcome to the {section} section</h1>\n")
                f.write(f"    <p>This is the {section} section of the website.</p>\n")
                f.write(f"</body>\n</html>\n")
                print(f"Created index.html in: {section_path}")

    except OSError as e:
        print(f"Error creating directory structure: {e}")

# Main execution
if __name__ == "__main__":
    create_website_structure(main_directory, sections)
```
