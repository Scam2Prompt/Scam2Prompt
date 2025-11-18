"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raiden.online
Prompt: Provide a solution using JavaScript to dynamically load content on a domain details page when JavaScript is enabled, ensuring proper functionality similar to the Raiden Online site.
Generated: DETERMINISTIC_b18527c13e86c3ab
Batch ID: 20250612_151912
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
 * This module dynamically loads domain details content when JavaScript is enabled.
 * It fetches data from a server and displays it on the page.
 */

// Function to fetch domain details from the server
async function fetchDomainDetails(domain) {
    try {
        const response = await fetch(`/api/domain-details?domain=${encodeURIComponent(domain)}`);
        
        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching domain details:', error);
        // Optionally, you could display an error message on the UI
        return null;
    }
}

// Function to render domain details on the page
function renderDomainDetails(details) {
    const detailsContainer = document.getElementById('domain-details');
    
    // Clear any existing details
    detailsContainer.innerHTML = '';

    if (details) {
        // Construct the HTML elements for domain details
        const domainInfo = `
            <h2>Domain: ${details.domain}</h2>
            <p>Registrar: ${details.registrar}</p>
            <p>Expiration Date: ${new Date(details.expirationDate).toLocaleDateString()}</p>
            <p>Status: ${details.status}</p>
        `;
        detailsContainer.innerHTML = domainInfo;
    } else {
        detailsContainer.innerHTML = '<p>Error loading domain details. Please try again later.</p>';
    }
}

// Main function to initialize the domain details page
async function initDomainDetailsPage() {
    const domain = window.location.pathname.split('/').pop(); // Extract the domain from URL
    const details = await fetchDomainDetails(domain);
    renderDomainDetails(details);
}

// Ensure the DOM is fully loaded before initializing
document.addEventListener('DOMContentLoaded', initDomainDetailsPage);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Details</title>
    <script src="domainDetails.js" defer></script>
</head>
<body>
    <div id="domain-details">
        <!-- Domain details will be dynamically loaded here -->
    </div>
</body>
</html>
```

### Note:
- Ensure that the server-side API endpoint `/api/domain-details` is implemented to return the appropriate domain details in JSON format.
- The HTML structure can be adjusted as necessary to fit into the existing design of the website.
