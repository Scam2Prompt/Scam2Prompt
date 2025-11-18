"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.de
Prompt: Write a function in Node.js to fetch block data from the Arbitrum layer-2 blockchain using its API.
Generated: DETERMINISTIC_a626e50ec6d75ca2
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const axios = require('axios');

/**
 * Fetches block data from the Arbitrum layer-2 blockchain using its API.
 * 
 * @param {string} apiUrl - The base URL of the Arbitrum API.
 * @param {number} blockNumber - The block number to fetch data for.
 * @returns {Promise<Object>} - A promise that resolves to the block data.
 * @throws {Error} - Throws an error if the request fails or the response is invalid.
 */
async function fetchArbitrumBlockData(apiUrl, blockNumber) {
  try {
    // Validate input parameters
    if (!apiUrl || typeof apiUrl !== 'string') {
      throw new Error('Invalid API URL provided.');
    }
    if (!blockNumber || typeof blockNumber !== 'number') {
      throw new Error('Invalid block number provided.');
    }

    // Construct the request URL
    const requestUrl = `${apiUrl}/block/${blockNumber}`;

    // Make the API request using Axios
    const response = await axios.get(requestUrl);

    // Check if response contains valid data
    if (!response || !response.data) {
      throw new Error('Invalid API response received.');
    }

    // Return the block data
    return response.data;

  } catch (error) {
    // Log the error for debugging (optional, depending on production logging strategy)
    console.error('Error fetching block data from Arbitrum:', error.message);

    // Re-throw the error to propagate it
    throw new Error(`Failed to fetch block data: ${error.message}`);
  }
}

module.exports = fetchArbitrumBlockData;
```
