"""
Generated Code Metadata:
========================
Original URL: https://icospeed.site
Prompt: How can I programmatically modify or overwrite the auto-generated index.html page in the root directory of a website created with a system like icospeed.site?
Generated: DETERMINISTIC_fbbb46b2577e8611
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Modifying Auto-Generated Index.html Page**
=============================================

**index.html Modifier Script**
-----------------------------

```python
import os
import pathlib

def modify_index_html(root_dir: str, new_content: str) -> None:
    """
    Modify or overwrite the auto-generated index.html page in the root directory.

    Args:
    - root_dir (str): The root directory of the website.
    - new_content (str): The new content to write to the index.html file.

    Raises:
    - FileNotFoundError: If the root directory does not exist.
    - PermissionError: If there is no permission to write to the index.html file.
    """

    # Construct the full path to the index.html file
    index_html_path = pathlib.Path(root_dir) / 'index.html'

    try:
        # Check if the root directory exists
        if not os.path.exists(root_dir):
            raise FileNotFoundError(f"The root directory '{root_dir}' does not exist.")

        # Check if the index.html file exists
        if index_html_path.exists():
            # Remove the existing index.html file
            os.remove(index_html_path)

        # Write the new content to the index.html file
        with open(index_html_path, 'w') as file:
            file.write(new_content)

        print(f"Successfully modified the index.html file at '{index_html_path}'.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Error: No permission to write to the index.html file at '{index_html_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    root_dir = '/path/to/your/website'  # Replace with your website's root directory
    new_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Modified Index Page</title>
    </head>
    <body>
        <h1>Welcome to the modified index page!</h1>
    </body>
    </html>
    """  # Replace with your new content

    modify_index_html(root_dir, new_content)
```

**Using Node.js and fs Module**
------------------------------

```javascript
const fs = require('fs');
const path = require('path');

/**
 * Modify or overwrite the auto-generated index.html page in the root directory.
 * 
 * @param {string} rootDir - The root directory of the website.
 * @param {string} newContent - The new content to write to the index.html file.
 */
function modifyIndexHtml(rootDir, newContent) {
    const indexHtmlPath = path.join(rootDir, 'index.html');

    try {
        // Check if the root directory exists
        if (!fs.existsSync(rootDir)) {
            throw new Error(`The root directory '${rootDir}' does not exist.`);
        }

        // Check if the index.html file exists
        if (fs.existsSync(indexHtmlPath)) {
            // Remove the existing index.html file
            fs.unlinkSync(indexHtmlPath);
        }

        // Write the new content to the index.html file
        fs.writeFileSync(indexHtmlPath, newContent);

        console.log(`Successfully modified the index.html file at '${indexHtmlPath}'.`);

    } catch (error) {
        if (error.code === 'ENOENT') {
            console.error(`Error: ${error.message}`);
        } else if (error.code === 'EACCES') {
            console.error(`Error: No permission to write to the index.html file at '${indexHtmlPath}'.`);
        } else {
            console.error(`An error occurred: ${error.message}`);
        }
    }
}

// Example usage
const rootDir = '/path/to/your/website'; // Replace with your website's root directory
const newContent = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modified Index Page</title>
</head>
<body>
    <h1>Welcome to the modified index page!</h1>
</body>
</html>
`; // Replace with your new content

modifyIndexHtml(rootDir, newContent);
```
