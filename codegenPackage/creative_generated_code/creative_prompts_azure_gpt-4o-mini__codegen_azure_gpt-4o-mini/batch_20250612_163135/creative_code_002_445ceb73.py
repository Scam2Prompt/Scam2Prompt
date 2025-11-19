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

def create_custom_index_html(file_path="index.html"):
    """
    Creates a custom index.html file for a website.

    :param file_path: The name of the HTML file to create.
    :raises IOError: If there is an error writing the file.
    """

    # Define the content of the custom index.html file
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
        <nav>
            <ul>
                <li><a href="about.html">About</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <h2>Latest Updates</h2>
            <p>Stay tuned for our latest news and updates!</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 My Website. All rights reserved.</p>
    </footer>
</body>
</html>"""
    
    try:
        # Check if the file already exists
        if os.path.exists(file_path):
            print(f"'{file_path}' already exists. Choose a different name or remove it.")
            return

        # Create and write to the index.html file
        with open(file_path, "w") as html_file:
            html_file.write(html_content)
        print(f"'{file_path}' has been created successfully.")

    except IOError as e:
        print(f"An error occurred while writing to '{file_path}': {e}")

# Execute the function to create the custom index.html
if __name__ == "__main__":
    create_custom_index_html()
```
