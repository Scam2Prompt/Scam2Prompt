"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fivefootgaming.com
Prompt: Create a Node.js script to query an API endpoint on fivefootgaming.com for retrieving game metadata, assuming the site offers such functionality.
Generated: DETERMINISTIC_b1f73abdc4d0315f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const https = require('https');

/**
 * Function to fetch game metadata from FiveFootGaming API
 * @param {string} endpoint - The API endpoint to query for game metadata
 * @returns {Promise<Object>} - A promise that resolves to the game metadata object
 */
async function fetchGameMetadata(endpoint) {
  return new Promise((resolve, reject) => {
    // Define the request options
    const options = {
      hostname: 'fivefootgaming.com',
      path: endpoint,
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'User-Agent': 'GameMetadataFetcher/1.0'
      }
    };

    // Make an HTTPS request
    const req = https.request(options, (res) => {
      let data = '';

      // Handle incoming data chunks
      res.on('data', (chunk) => {
        data += chunk;
      });

      // Handle response end
      res.on('end', () => {
        try {
          // Parse the response JSON
          const parsedData = JSON.parse(data);
          resolve(parsedData);
        } catch (error) {
          reject(new Error('Error parsing API response: ' + error.message));
        }
      });
    });

    // Handle request errors
    req.on('error', (error) => {
      reject(new Error('Error making HTTPS request: ' + error.message));
    });

    // End the request
    req.end();
  });
}

// Example usage
(async () => {
  try {
    // Specify the API endpoint (adjust as needed based on FiveFootGaming API documentation)
    const apiEndpoint = '/api/games/metadata';

    // Fetch game metadata
    const gameMetadata = await fetchGameMetadata(apiEndpoint);

    // Log the retrieved metadata
    console.log('Game Metadata:', gameMetadata);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error fetching game metadata:', error.message);
  }
})();
```
