"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: Create a JavaScript snippet to detect and handle errors when fetching domain details from an API.
Generated: DETERMINISTIC_9463ea5e21e47138
Batch ID: 20250612_153728
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/domains/${encodeURIComponent": {
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
 * Fetches domain details from a given API endpoint.
 * @param {string} domain - The domain name to fetch details for.
 * @returns {Promise<Object>} - A promise that resolves to the domain details.
 * @throws {Error} - Throws an error if the fetch fails or if the domain is invalid.
 */
async function fetchDomainDetails(domain) {
    // Validate the domain input
    if (typeof domain !== 'string' || domain.trim() === '') {
        throw new Error('Invalid domain: Please provide a non-empty string.');
    }

    const apiUrl = `https://api.example.com/domains/${encodeURIComponent(domain)}`;

    try {
        // Make the API request to fetch domain details
        const response = await fetch(apiUrl);

        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status} - ${response.statusText}`);
        }

        // Parse the JSON response
        const domainDetails = await response.json();

        // Check if the expected data is present in the response
        if (!domainDetails || typeof domainDetails !== 'object') {
            throw new Error('Invalid response format: Expected an object.');
        }

        return domainDetails;

    } catch (error) {
        // Handle fetch errors or processing errors
        console.error('Error fetching domain details:', error.message);
        throw new Error(`Failed to fetch domain details: ${error.message}`);
    }
}

// Example usage (commented out for production):
// fetchDomainDetails('example.com')
//     .then(details => console.log(details))
//     .catch(error => console.error('Error:', error.message));
```
