"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsc-info.mdex.com
Prompt: What libraries can I use to interact with the Mdex Info API once JavaScript is enabled?
Generated: DETERMINISTIC_c0f6fb6c6fbfb667
Batch ID: 20250612_164310
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com": {
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
// Importing necessary libraries for making HTTP requests and handling promises
const axios = require('axios');

/**
 * Class to interact with the Mdex Info API
 */
class MdexInfoAPI {
    constructor(baseUrl) {
        this.baseUrl = baseUrl; // Base URL for the Mdex Info API
    }

    /**
     * Fetches data from a specified endpoint of the Mdex Info API.
     * @param {string} endpoint - The API endpoint to fetch data from.
     * @param {object} params - An object representing query parameters.
     * @returns {Promise<object>} - A promise that resolves to the API response data.
     */
    async fetchData(endpoint, params = {}) {
        try {
            const response = await axios.get(`${this.baseUrl}/${endpoint}`, { params });
            return response.data; // Return the response data
        } catch (error) {
            // Handle errors appropriately
            this.handleError(error);
            throw new Error('Failed to fetch data from Mdex Info API');
        }
    }

    /**
     * Handles errors encountered during API requests.
     * @param {Error} error - The error object to handle.
     */
    handleError(error) {
        if (error.response) {
            // The request was made and the server responded with a status code
            console.error(`Error: ${error.response.status} - ${error.response.data}`);
        } else if (error.request) {
            // The request was made but no response was received
            console.error('Error: No response received from Mdex Info API', error.request);
        } else {
            // Something happened in setting up the request that triggered an error
            console.error('Error:', error.message);
        }
    }
}

// Example usage of the MdexInfoAPI class
(async () => {
    const mdexApi = new MdexInfoAPI('https://api.mdex.com'); // Initialize with the Mdex Info API base URL

    try {
        const data = await mdexApi.fetchData('your-endpoint', { param1: 'value1', param2: 'value2' });
        console.log(data); // Log the fetched data
    } catch (error) {
        console.error(error.message); // Log any errors encountered during the API request
    }
})();
```
