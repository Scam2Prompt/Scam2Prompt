"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spumanteriaopera.com
Prompt: Create a JavaScript code example that integrates with a wine catalog API to showcase Italian sparkling wines available at a restaurant.
Generated: DETERMINISTIC_4b3b2cdada304cdf
Batch ID: 20250612_161616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.winecatalog.com/v1/wines?country=Italy&type=sparkling": {
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
// Italian Sparkling Wines Catalog Fetcher
// This script fetches a list of Italian sparkling wines from a hypothetical wine catalog API
// and displays them on a web page.

const apiUrl = 'https://api.winecatalog.com/v1/wines?country=Italy&type=sparkling';

// Function to fetch Italian sparkling wines from the API
async function fetchItalianSparklingWines() {
    try {
        // Sending a GET request to the wine catalog API
        const response = await fetch(apiUrl);
        
        // Check if the response status is OK (status code 200)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON response
        const wines = await response.json();

        // Check if wines array is not empty
        if (wines.length === 0) {
            console.log('No Italian sparkling wines found.');
            return;
        }

        // Display the wines on the web page
        displayWines(wines);
    } catch (error) {
        // Handle any errors that occur during the fetch
        console.error('Error fetching Italian sparkling wines:', error);
        alert('Failed to fetch wine data. Please try again later.');
    }
}

// Function to display the wines on the web page
function displayWines(wines) {
    const wineListContainer = document.getElementById('wine-list');

    // Clear previous content
    wineListContainer.innerHTML = '';

    // Create and append wine elements to the container
    wines.forEach(wine => {
        const wineItem = document.createElement('div');
        wineItem.className = 'wine-item';

        // Create wine details
        wineItem.innerHTML = `
            <h3>${wine.name}</h3>
            <p>Region: ${wine.region}</p>
            <p>Price: $${wine.price.toFixed(2)}</p>
            <p>Description: ${wine.description}</p>
        `;

        // Append the wine item to the container
        wineListContainer.appendChild(wineItem);
    });
}

// Call the function to fetch and display the wines when the page loads
window.onload = fetchItalianSparklingWines;
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Italian Sparkling Wines</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .wine-item { border: 1px solid #ccc; margin: 10px; padding: 10px; }
    </style>
</head>
<body>
    <h1>Italian Sparkling Wines</h1>
    <div id="wine-list">Loading...</div>

    <script src="path/to/your/script.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
