"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robertoabajo.es
Prompt: Develop a JavaScript function that retrieves and displays information about recent art exhibitions, similar to the content found on Roberto Abajo's webpage.
Generated: DETERMINISTIC_5dd5223630d62a4d
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/recent-exhibitions": {
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
 * Fetches and displays recent art exhibitions from a specified API.
 * This function retrieves data asynchronously and updates the DOM with exhibition information.
 * 
 * @async
 * @function fetchArtExhibitions
 * @param {string} apiUrl - The URL of the API endpoint to fetch art exhibitions from.
 */
async function fetchArtExhibitions(apiUrl) {
    try {
        // Make an HTTP GET request to the API URL
        const response = await fetch(apiUrl);

        // Check if the response is okay (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON response
        const exhibitions = await response.json();

        // Call the function to display exhibitions
        displayExhibitions(exhibitions);
    } catch (error) {
        // Log the error to the console and display a user-friendly message
        console.error('Failed to fetch art exhibitions:', error);
        document.getElementById('exhibition-container').innerHTML = `
            <p>Error loading exhibitions. Please try again later.</p>
        `;
    }
}

/**
 * Displays a list of art exhibitions on the webpage.
 * 
 * @function displayExhibitions
 * @param {Array} exhibitions - An array of exhibition objects to display.
 */
function displayExhibitions(exhibitions) {
    const container = document.getElementById('exhibition-container');

    // Clear any existing content
    container.innerHTML = '';

    // Check if there are exhibitions to display
    if (exhibitions.length === 0) {
        container.innerHTML = '<p>No recent exhibitions found.</p>';
        return;
    }

    // Create and append exhibition details to the container
    exhibitions.forEach(exhibition => {
        const exhibitionElement = document.createElement('div');
        exhibitionElement.classList.add('exhibition');

        exhibitionElement.innerHTML = `
            <h3>${exhibition.title}</h3>
            <p><strong>Location:</strong> ${exhibition.location}</p>
            <p><strong>Date:</strong> ${exhibition.date}</p>
            <p>${exhibition.description}</p>
        `;

        container.appendChild(exhibitionElement);
    });
}

// Example usage: Fetch recent exhibitions from a sample API endpoint
const apiUrl = 'https://api.example.com/recent-exhibitions';
fetchArtExhibitions(apiUrl);
```

**HTML Example Structure** (for context, not included in the code):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Art Exhibitions</title>
    <style>
        #exhibition-container { margin: 20px; }
        .exhibition { border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <h1>Recent Art Exhibitions</h1>
    <div id="exhibition-container"></div>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```
