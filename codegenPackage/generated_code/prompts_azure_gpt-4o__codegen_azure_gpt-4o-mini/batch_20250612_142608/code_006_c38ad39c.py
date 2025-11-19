"""
Generated Code Metadata:
========================
Original URL: https://polymarket.gitbook.io
Prompt: Develop a script to convert markdown files into a GitBook site, leveraging the publishing tools mentioned in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_c38ad39c5e3cf3c8
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys
import shutil

class MarkdownToGitBookConverter:
    def __init__(self, markdown_dir, output_dir):
        """
        Initialize the converter with the source markdown directory and output directory.

        :param markdown_dir: Directory containing markdown files.
        :param output_dir: Directory where the GitBook site will be generated.
        """
        self.markdown_dir = markdown_dir
        self.output_dir = output_dir

    def validate_directories(self):
        """Check if the markdown directory exists and is a directory."""
        if not os.path.isdir(self.markdown_dir):
            raise FileNotFoundError(f"Markdown directory '{self.markdown_dir}' does not exist.")
        if not os.path.isdir(self.output_dir):
            os.makedirs(self.output_dir)  # Create output directory if it doesn't exist

    def convert_markdown_to_gitbook(self):
        """Convert markdown files to a GitBook site."""
        self.validate_directories()
        
        # Copy the starter template files to the output directory
        self.copy_gitbook_template()

        # Generate the GitBook site
        self.build_gitbook()

    def copy_gitbook_template(self):
        """Copy the Polymarket GitBook starter template to the output directory."""
        template_dir = os.path.join(os.path.dirname(__file__), 'gitbook_template')
        if not os.path.exists(template_dir):
            raise FileNotFoundError(f"GitBook template directory '{template_dir}' does not exist.")

        # Copy all files from the template directory to the output directory
        for item in os.listdir(template_dir):
            s = os.path.join(template_dir, item)
            d = os.path.join(self.output_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)

    def build_gitbook(self):
        """Build the GitBook site using the GitBook CLI."""
        try:
            # Change to the output directory
            os.chdir(self.output_dir)

            # Run the GitBook build command
            subprocess.run(['gitbook', 'build'], check=True)
            print("GitBook site has been successfully built.")
        except subprocess.CalledProcessError as e:
            print(f"Error during GitBook build: {e}")
            sys.exit(1)

if __name__ == "__main__":
    # Define the source markdown directory and output directory
    markdown_directory = 'path/to/your/markdown/files'  # Update this path
    output_directory = 'path/to/output/gitbook'  # Update this path

    # Create an instance of the converter
    converter = MarkdownToGitBookConverter(markdown_directory, output_directory)

    # Convert markdown files to GitBook site
    try:
        converter.convert_markdown_to_gitbook()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```

**Note:** Ensure that you have the GitBook CLI installed and the `gitbook_template` directory exists in the same directory as this script, containing the necessary starter files for the GitBook site. Update the `markdown_directory` and `output_directory` variables with the appropriate paths before running the script.
