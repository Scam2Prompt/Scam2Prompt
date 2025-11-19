"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Write a JavaScript function that retrieves the number of peers and queue length from the Arweave network's API, based on the provided network details.
Generated: DETERMINISTIC_7944d9511b3b8860
Batch ID: 20250612_160306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net": {
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
 * Function to retrieve the number of peers and queue length from the Arweave network's API.
 * 
 * @param {string} apiUrl - The base URL of the Arweave network's API.
 * @returns {Promise<Object>} - A promise that resolves to an object containing the number of peers and queue length.
 * @throws {Error} - Throws an error if the API request fails or the response is invalid.
 */
async function getArweaveNetworkStats(apiUrl) {
  // Validate the API URL
  if (typeof apiUrl !== 'string' || !apiUrl.trim()) {
    throw new Error('Invalid API URL provided.');
  }

  try {
    // Fetch network details from the API
    const response = await fetch(`${apiUrl}/network`);
    
    // Check if the response status is OK
    if (!response.ok) {
      throw new Error(`Failed to fetch network stats: ${response.status} ${response.statusText}`);
    }

    // Parse the JSON response
    const networkData = await response.json();

    // Validate the presence of required data
    if (
      typeof networkData.peers !== 'number' ||
      typeof networkData.queue_length !== 'number'
    ) {
      throw new Error('Invalid data format received from the API.');
    }

    // Return the peers and queue length
    return {
      peers: networkData.peers,
      queueLength: networkData.queue_length
    };
  } catch (error) {
    // Handle errors gracefully and provide meaningful feedback
    console.error('Error retrieving network stats:', error.message);
    throw error;
  }
}

// Example usage:
// Replace 'https://arweave.net' with the appropriate API URL for your use case.
getArweaveNetworkStats('https://arweave.net')
  .then(stats => {
    console.log('Network Stats:', stats);
  })
  .catch(error => {
    console.error('Failed to retrieve network stats:', error.message);
  });
```
