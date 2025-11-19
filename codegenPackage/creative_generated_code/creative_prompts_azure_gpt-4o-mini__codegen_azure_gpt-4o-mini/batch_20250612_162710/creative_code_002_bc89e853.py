"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frontiersistem.ro
Prompt: Create a function in JavaScript that fetches product information from an import service API, reflecting the offerings of FRONTIER SISTEM.
Generated: DETERMINISTIC_bc89e853ac90a040
Batch ID: 20250612_162710
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.frontiersistem.com/products": {
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
 * Fetches product information from the FRONTIER SISTEM API.
 * 
 * This function makes a GET request to the specified API endpoint
 * and retrieves the product offerings. It handles errors gracefully
 * and returns the data in a structured format.
 * 
 * @async
 * @function fetchProductInformation
 * @param {string} apiUrl - The URL of the API endpoint to fetch data from.
 * @returns {Promise<Object>} - A promise that resolves to the product data or an error object.
 * @throws {Error} - Throws an error if the fetch operation fails.
 */
async function fetchProductInformation(apiUrl) {
    try {
        // Check if the provided URL is valid
        if (!apiUrl || typeof apiUrl !== 'string') {
            throw new Error('Invalid API URL provided.');
        }

        // Making a GET request to the API
        const response = await fetch(apiUrl);

        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.status} ${response.statusText}`);
        }

        // Parsing the JSON response
        const data = await response.json();

        // Returning the product data
        return data;
    } catch (error) {
        // Logging the error to the console
        console.error('Error in fetchProductInformation:', error);
        
        // Re-throwing the error for further handling if needed
        throw new Error(`Failed to fetch product information: ${error.message}`);
    }
}

// Example usage (uncomment to use):
// const apiUrl = 'https://api.frontiersistem.com/products';
// fetchProductInformation(apiUrl)
//     .then(data => console.log('Product Data:', data))
//     .catch(error => console.error('Fetch Error:', error));
```
