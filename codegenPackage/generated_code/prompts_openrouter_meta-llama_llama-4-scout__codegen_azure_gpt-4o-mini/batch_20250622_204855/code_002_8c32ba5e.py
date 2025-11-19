"""
Generated Code Metadata:
========================
Original URL: https://ssly.vip
Prompt: Generate code to programmatically create a default index.html page similar to the one described on this site, using a provided template.
Generated: DETERMINISTIC_8c32ba5eb1acdc28
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os

# Define the template for the index.html file
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Default Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>
    <main>
        <section>
            <h2>About</h2>
            <p>This is a default index.html page created programmatically.</p>
        </section>
        <section>
            <h2>Contact</h2>
            <p>You can reach us at <a href="mailto:info@example.com">info@example.com</a>.</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 My Website</p>
    </footer>
</body>
</html>
"""

def create_index_html(file_path='index.html'):
    """
    Creates an index.html file with a default template.

    Args:
        file_path (str): The path where the index.html file will be created.
    
    Raises:
        IOError: If there is an error writing the file.
    """
    try:
        # Check if the file already exists
        if os.path.exists(file_path):
            print(f"File '{file_path}' already exists. No changes made.")
            return
        
        # Write the HTML template to the file
        with open(file_path, 'w') as file:
            file.write(HTML_TEMPLATE)
        
        print(f"'{file_path}' has been created successfully.")
    
    except IOError as e:
        print(f"An error occurred while creating the file: {e}")

if __name__ == "__main__":
    create_index_html()
```
