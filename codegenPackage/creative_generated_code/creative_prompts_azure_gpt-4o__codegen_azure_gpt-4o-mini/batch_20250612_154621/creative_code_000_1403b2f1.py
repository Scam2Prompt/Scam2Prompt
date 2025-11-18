"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfc.com
Prompt: Write a JavaScript script to interact with Ethereum 2.0 staking APIs and retrieve validator performance data.
Generated: DETERMINISTIC_1403b2f117c94b58
Batch ID: 20250612_154621
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://beaconcha.in/api/v1": {
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
// Import necessary libraries
const axios = require('axios');

// Define constants for API endpoints
const BASE_URL = 'https://beaconcha.in/api/v1';
const VALIDATOR_PERFORMANCE_ENDPOINT = `${BASE_URL}/validator/`;

/**
 * Fetches validator performance data from Ethereum 2.0 staking API
 * @param {string} validatorIndex - The unique index of the validator
 * @returns {Promise<Object>} - The validator performance data
 * @throws {Error} - Throws an error if the API call fails
 */
async function fetchValidatorPerformance(validatorIndex) {
    try {
        // Validate the input
        if (!validatorIndex || isNaN(validatorIndex)) {
            throw new Error('Invalid validator index provided.');
        }

        // Make a GET request to the API
        const response = await axios.get(`${VALIDATOR_PERFORMANCE_ENDPOINT}${validatorIndex}/performance`);
        
        // Check for a successful response
        if (response.status !== 200) {
            throw new Error(`Error fetching data: ${response.statusText}`);
        }

        // Return the performance data
        return response.data.data;
    } catch (error) {
        // Log the error and rethrow it for further handling
        console.error(`Failed to fetch validator performance: ${error.message}`);
        throw error;
    }
}

/**
 * Main function to demonstrate the use of the fetchValidatorPerformance function
 * @async
 */
async function main() {
    const validatorIndex = '12345'; // Replace with the desired validator index

    try {
        const performanceData = await fetchValidatorPerformance(validatorIndex);
        console.log('Validator Performance Data:', performanceData);
    } catch (error) {
        console.error('Error in main execution:', error.message);
    }
}

// Execute the main function
main();
```

**Note:** Ensure you have `axios` installed in your project. You can install it using `npm install axios`.
