"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetespepe.net
Prompt: Write a JavaScript function that fetches and lists the contents of a server directory, inspired by the index page of wallstreetespepe.net.
Generated: DETERMINISTIC_e9ca0b8991b18053
Batch ID: 20250612_155752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/directory": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Fetch and list the contents of a server directory.
 * This function makes an HTTP request to a given URL and parses the response
 * to display directory contents. Assumes the server returns a JSON response
 * with an array of file names or objects representing the directory contents.
 *
 * @param {string} url - The URL of the server directory to fetch.
 * @returns {Promise<void>} - Resolves when the directory contents are listed.
 */
async function fetchDirectoryContents(url) {
  try {
    // Validate that the input is a non-empty string
    if (typeof url !== 'string' || url.trim() === '') {
      throw new Error('Invalid URL provided. Please provide a valid non-empty string.');
    }

    console.log(`Fetching directory contents from: ${url}`);

    // Make a GET request to fetch the directory contents
    const response = await fetch(url);

    // Check if the response status indicates success
    if (!response.ok) {
      throw new Error(`Failed to fetch directory contents. Server responded with status: ${response.status}`);
    }

    // Parse the JSON response
    const data = await response.json();

    // Validate that the response data is an array
    if (!Array.isArray(data)) {
      throw new Error('Unexpected response format. Expected an array of directory contents.');
    }

    // Log the directory contents to the console
    console.log('Directory Contents:');
    data.forEach((item, index) => {
      if (typeof item === 'object' && item !== null) {
        // If item is an object, log its properties
        console.log(`${index + 1}. ${JSON.stringify(item)}`);
      } else {
        // Otherwise, log the item as a string
        console.log(`${index + 1}. ${item}`);
      }
    });
  } catch (error) {
    // Handle errors gracefully and log them
    console.error('An error occurred while fetching the directory contents:', error.message);
  }
}

// Example usage:
// Replace 'https://example.com/directory' with the actual URL of the server directory
fetchDirectoryContents('https://example.com/directory');
```

Note: Ensure that the server at the provided URL returns a JSON response with an array of contents.
