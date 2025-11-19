"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purelywealth.com
Prompt: Write a JavaScript function that fetches data from a finance API, inspired by the vision and partnerships highlighted on Purely Wealth.
Generated: DETERMINISTIC_cd42bda258e3c149
Batch ID: 20250612_140250
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/finance-data": {
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
 * Fetches financial data from a specified finance API.
 * This function demonstrates how to handle API calls with error handling
 * and returns the data in a structured format.
 * 
 * @async
 * @function fetchFinanceData
 * @param {string} apiUrl - The URL of the finance API to fetch data from.
 * @returns {Promise<Object>} - A promise that resolves to the fetched data.
 * @throws {Error} - Throws an error if the API call fails or returns an invalid response.
 */
async function fetchFinanceData(apiUrl) {
    try {
        // Validate the input URL
        if (typeof apiUrl !== 'string' || !apiUrl) {
            throw new Error('Invalid API URL provided.');
        }

        // Perform the API call
        const response = await fetch(apiUrl);

        // Check if the response is OK (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`API call failed with status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Validate the structure of the returned data (optional)
        if (!data || typeof data !== 'object') {
            throw new Error('Invalid data structure returned from API.');
        }

        // Return the fetched data
        return data;

    } catch (error) {
        // Log the error for debugging
        console.error('Error fetching finance data:', error.message);
        // Rethrow the error for further handling
        throw new Error(`Failed to fetch finance data: ${error.message}`);
    }
}

// Example usage (replace with actual API URL)
const apiUrl = 'https://api.example.com/finance-data';

fetchFinanceData(apiUrl)
    .then(data => {
        console.log('Fetched finance data:', data);
    })
    .catch(error => {
        console.error('Error occurred:', error.message);
    });
```
