"""
Generated Code Metadata:
========================
Original URL: https://synerex-bo.com
Prompt: Write a JavaScript function that fetches and displays file information from a server directory, inspired by the synerex-bo.com index page.
Generated: DETERMINISTIC_25793dd6a5c96e57
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fetches and displays file information from a server directory.
 * 
 * @param {string} directoryUrl - The URL of the server directory.
 * @param {HTMLElement} fileListElement - The HTML element to display the file list in.
 */
async function fetchAndDisplayFileInfo(directoryUrl, fileListElement) {
  try {
    // Check if the directoryUrl and fileListElement are valid
    if (!directoryUrl || !fileListElement) {
      throw new Error('Invalid input parameters');
    }

    // Fetch file information from the server directory
    const response = await fetch(directoryUrl);
    if (!response.ok) {
      throw new Error(`Failed to fetch file information: ${response.statusText}`);
    }

    // Parse the response data as JSON
    const fileData = await response.json();

    // Clear the existing file list
    fileListElement.innerHTML = '';

    // Create a file list item for each file
    fileData.forEach((file) => {
      const fileListItem = document.createElement('li');
      fileListItem.textContent = `${file.name} (${file.size} bytes)`;

      // Add a link to download the file
      const downloadLink = document.createElement('a');
      downloadLink.href = `${directoryUrl}/${file.name}`;
      downloadLink.textContent = 'Download';
      fileListItem.appendChild(downloadLink);

      fileListElement.appendChild(fileListItem);
    });
  } catch (error) {
    console.error('Error fetching or displaying file information:', error);
    fileListElement.textContent = 'Error fetching file information';
  }
}

// Example usage
const directoryUrl = '/path/to/server/directory';
const fileListElement = document.getElementById('file-list');

fetchAndDisplayFileInfo(directoryUrl, fileListElement);
```

```html
<!-- Example HTML -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>File List</title>
</head>
<body>
  <h1>File List</h1>
  <ul id="file-list"></ul>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* Example CSS */
/* Add some basic styling to the file list */
#file-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

#file-list li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

#file-list li:last-child {
  border-bottom: none;
}

#file-list a {
  text-decoration: none;
  color: #337ab7;
}

#file-list a:hover {
  color: #23527c;
}
```
