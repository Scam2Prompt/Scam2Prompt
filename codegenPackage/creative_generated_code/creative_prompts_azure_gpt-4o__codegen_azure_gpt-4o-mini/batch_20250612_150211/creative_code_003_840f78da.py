"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cxconnect1-dss.coinbase.co.za
Prompt: Generate JavaScript code to dynamically load content on a webpage, ensuring proper functionality for a domain details page similar to the one described.
Generated: DETERMINISTIC_840f78daa5630b40
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// domainDetails.js

/**
 * Fetches domain details from the server and updates the webpage.
 * 
 * @param {string} domain - The domain name for which to fetch details.
 */
async function loadDomainDetails(domain) {
    try {
        // Validate the domain input
        if (!isValidDomain(domain)) {
            throw new Error("Invalid domain format");
        }

        // Fetch domain details from the API
        const response = await fetch(`/api/domain-details?domain=${encodeURIComponent(domain)}`);
        
        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`Error fetching domain details: ${response.statusText}`);
        }

        // Parse the JSON response
        const domainDetails = await response.json();

        // Update the HTML with the fetched details
        updateDomainDetailsUI(domainDetails);
    } catch (error) {
        console.error("Failed to load domain details:", error);
        displayErrorMessage(error.message);
    }
}

/**
 * Validates the domain format.
 * 
 * @param {string} domain - The domain name to validate.
 * @returns {boolean} - Returns true if valid, otherwise false.
 */
function isValidDomain(domain) {
    // Simple regex for domain validation
    const domainPattern = /^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$/;
    return domainPattern.test(domain);
}

/**
 * Updates the UI with the fetched domain details.
 * 
 * @param {Object} details - The domain details object.
 */
function updateDomainDetailsUI(details) {
    const detailsContainer = document.getElementById('domain-details');

    // Clear previous content
    detailsContainer.innerHTML = '';

    // Create and append new content
    const title = document.createElement('h2');
    title.textContent = `Details for: ${details.domain}`;
    detailsContainer.appendChild(title);

    const infoList = document.createElement('ul');
    Object.keys(details).forEach(key => {
        const listItem = document.createElement('li');
        listItem.textContent = `${key}: ${details[key]}`;
        infoList.appendChild(listItem);
    });
    detailsContainer.appendChild(infoList);
}

/**
 * Displays an error message to the user.
 * 
 * @param {string} message - The error message to display.
 */
function displayErrorMessage(message) {
    const errorContainer = document.getElementById('error-message');
    errorContainer.textContent = message;
    errorContainer.style.display = 'block'; // Show the error message
}

// Example usage: Call this function with the domain name when needed
// loadDomainDetails('example.com');
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Details</title>
    <link rel="stylesheet" href="styles.css">
    <script src="domainDetails.js" defer></script>
</head>
<body>
    <div id="error-message" style="color: red; display: none;"></div>
    <div id="domain-details"></div>
    <input type="text" id="domain-input" placeholder="Enter domain name" />
    <button id="load-details-button">Load Domain Details</button>

    <script>
        // Add event listener to load domain details when button is clicked
        document.getElementById('load-details-button').addEventListener('click', () => {
            const domain = document.getElementById('domain-input').value.trim();
            loadDomainDetails(domain);
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

#domain-details {
    margin-top: 20px;
}

#error-message {
    margin-bottom: 20px;
}
```
