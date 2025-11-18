"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.tech
Prompt: Provide code to modify the default `index.html` file in a hosting setup to display a custom "Site Under Construction" message.
Generated: DETERMINISTIC_4f6a7a56e7418636
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def modify_index_html(directory_path):
    """
    Modifies the default `index.html` file in the given directory to display
    a "Site Under Construction" message. If the file doesn't exist, it creates it.

    Args:
        directory_path (str): Path to the directory containing `index.html`.
    """
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")

        # Path to the index.html file
        index_file_path = os.path.join(directory_path, 'index.html')

        # HTML content for "Site Under Construction"
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Site Under Construction</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #f4f4f9;
                    color: #333;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }

                h1 {
                    font-size: 2.5em;
                }

                p {
                    font-size: 1.2em;
                }
            </style>
        </head>
        <body>
            <div>
                <h1>Site Under Construction</h1>
                <p>We are working hard to bring you a better experience. Check back soon!</p>
            </div>
        </body>
        </html>
        """

        # Write or overwrite the index.html file with the custom message
        with open(index_file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f"'index.html' successfully modified in directory: {directory_path}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError:
        print("Permission denied: Unable to write to the specified directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    # Replace with the actual path where your hosting setup stores 'index.html'
    hosting_directory = "/path/to/hosting/directory"
    
    modify_index_html(hosting_directory)
```
