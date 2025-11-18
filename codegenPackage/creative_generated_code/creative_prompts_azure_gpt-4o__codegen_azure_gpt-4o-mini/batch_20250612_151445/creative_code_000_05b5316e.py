"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-crypto.com
Prompt: Write JavaScript code to interact with the "Cryptonames World" application, ensuring JavaScript is enabled for full functionality.
Generated: DETERMINISTIC_05b5316e979034f8
Batch ID: 20250612_151445
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cryptonames.com/": {
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
 * Cryptonames API Interaction Module
 * This module provides functions to interact with the Cryptonames World application.
 * Ensure that JavaScript is enabled for full functionality.
 */

// Base URL for the Cryptonames API
const BASE_URL = 'https://api.cryptonames.com/';

// Function to fetch cryptocurrency data from the API
/**
 * Fetches cryptocurrency data based on the specified currency code.
 * @param {string} currencyCode - The code of the cryptocurrency to fetch (e.g., 'BTC').
 * @returns {Promise<Object>} - A promise that resolves to the cryptocurrency data.
 * @throws {Error} - Throws an error if the fetch operation fails.
 */
async function fetchCryptoData(currencyCode) {
    try {
        const response = await fetch(`${BASE_URL}data/${currencyCode}`);
        
        // Check if the response is OK (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Failed to fetch cryptocurrency data:', error);
        throw error; // Rethrow the error for further handling
    }
}

// Function to display cryptocurrency data on the webpage
/**
 * Displays cryptocurrency data on the specified HTML element.
 * @param {Object} data - The cryptocurrency data to display.
 * @param {HTMLElement} displayElement - The HTML element where the data will be displayed.
 */
function displayCryptoData(data, displayElement) {
    if (!data || !displayElement) {
        console.error('Invalid data or display element.');
        return;
    }

    // Clear previous content
    displayElement.innerHTML = '';

    // Create and append new content
    const title = document.createElement('h2');
    title.textContent = `Cryptocurrency: ${data.name} (${data.code})`;
    displayElement.appendChild(title);

    const price = document.createElement('p');
    price.textContent = `Current Price: $${data.price}`;
    displayElement.appendChild(price);
}

// Event listener for fetching and displaying data on button click
document.getElementById('fetchButton').addEventListener('click', async () => {
    const currencyCode = document.getElementById('currencyInput').value.trim().toUpperCase();
    const displayElement = document.getElementById('cryptoDisplay');

    try {
        const cryptoData = await fetchCryptoData(currencyCode);
        displayCryptoData(cryptoData, displayElement);
    } catch (error) {
        displayElement.innerHTML = '<p>Error fetching cryptocurrency data. Please try again later.</p>';
    }
});
```

### HTML Structure (for context)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cryptonames World</title>
</head>
<body>
    <input type="text" id="currencyInput" placeholder="Enter cryptocurrency code (e.g., BTC)">
    <button id="fetchButton">Fetch Crypto Data</button>
    <div id="cryptoDisplay"></div>

    <script src="path/to/your/script.js"></script>
</body>
</html>
```

Make sure to replace `path/to/your/script.js` with the actual path where you save the JavaScript code.
