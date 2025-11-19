"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.info
Prompt: Can you provide a code snippet to create a custom index.html file for a website after the default page has been generated?
Generated: DETERMINISTIC_445ceb73169731ff
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def generate_custom_index_html():
    """
    Generates a custom index.html file for a website.
    Ensures the default page exists before overwriting it with the custom page.
    """
    try:
        # Define file paths
        default_file_path = "index.html"
        custom_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Custom Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    color: #333;
                }
                h1 {
                    color: #4CAF50;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to My Custom Page!</h1>
            <p>This is a custom index.html file created programmatically.</p>
        </body>
        </html>
        """

        # Check if the default index.html file exists
        if os.path.exists(default_file_path):
            print(f"Default '{default_file_path}' exists. Overwriting with custom content...")
        else:
            print(f"'{default_file_path}' does not exist. Creating a new file...")

        # Write custom content to index.html
        with open(default_file_path, 'w') as file:
            file.write(custom_content)

        print(f"Custom '{default_file_path}' created successfully.")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while creating the custom index.html: {e}")

# Call the function to generate the custom index.html
generate_custom_index_html()
```
