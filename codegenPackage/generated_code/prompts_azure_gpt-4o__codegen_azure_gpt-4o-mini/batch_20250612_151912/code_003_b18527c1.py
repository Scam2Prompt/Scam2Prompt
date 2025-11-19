"""
Generated Code Metadata:
========================
Original URL: https://raiden.online
Prompt: Provide a solution using JavaScript to dynamically load content on a domain details page when JavaScript is enabled, ensuring proper functionality similar to the Raiden Online site.
Generated: DETERMINISTIC_b18527c13e86c3ab
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// domainDetails.js

// Function to fetch domain details from the server
async function fetchDomainDetails(domain) {
    try {
        const response = await fetch(`/api/domain-details?domain=${encodeURIComponent(domain)}`);
        
        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`Error fetching domain details: ${response.statusText}`);
        }

        // Parse the JSON response
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Failed to fetch domain details:", error);
        // Display a user-friendly message
        document.getElementById('domain-details').innerText = "Failed to load domain details. Please try again later.";
        return null;
    }
}

// Function to render domain details on the page
function renderDomainDetails(details) {
    const detailsContainer = document.getElementById('domain-details');

    // Clear previous content
    detailsContainer.innerHTML = '';

    // Check if details are available
    if (!details) {
        detailsContainer.innerText = "No details available.";
        return;
    }

    // Create and append elements for each detail
    for (const [key, value] of Object.entries(details)) {
        const detailElement = document.createElement('div');
        detailElement.className = 'detail-item';
        detailElement.innerHTML = `<strong>${key}:</strong> ${value}`;
        detailsContainer.appendChild(detailElement);
    }
}

// Main function to initialize the domain details loading
async function initDomainDetails() {
    const domain = window.location.pathname.split('/').pop(); // Extract domain from URL
    const details = await fetchDomainDetails(domain);
    renderDomainDetails(details);
}

// Check if JavaScript is enabled and run the initialization
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDomainDetails);
} else {
    initDomainDetails();
}
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
</head>
<body>
    <h1>Domain Details</h1>
    <div id="domain-details">Loading domain details...</div>
    
    <script src="domainDetails.js" defer></script>
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

.detail-item {
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
```
