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
  "https://arweave.net/your-api-endpoint": {
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
 * Retrieves the number of peers and queue length from the Arweave network API.
 * 
 * @param {string} apiUrl - The URL of the Arweave network API.
 * @returns {Promise<Object>} - A promise that resolves to an object containing
 *                              the number of peers and queue length.
 * @throws {Error} - Throws an error if the request to the API fails or if the
 *                   response is not in the expected format.
 */
async function getArweaveNetworkStats(apiUrl) {
    try {
        // Validate the provided API URL
        if (typeof apiUrl !== 'string' || !apiUrl.startsWith('http')) {
            throw new Error('Invalid API URL provided.');
        }

        const response = await fetch(apiUrl);

        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }

        const data = await response.json();

        // Check if the expected properties exist in the response
        if (typeof data !== 'object' || !data.peers || !data.queueLength) {
            throw new Error('Unexpected response format from the API.');
        }

        // Return the relevant network statistics
        return {
            peers: data.peers,
            queueLength: data.queueLength
        };
    } catch (error) {
        // Handle error and log it to console for debugging
        console.error('Error retrieving network stats:', error);
        throw new Error('Failed to retrieve Arweave network statistics.');
    }
}

// Example usage:
// (Uncomment to run the example, ensuring to replace `apiUrl` with a valid URL)
// getArweaveNetworkStats('https://arweave.net/your-api-endpoint')
//     .then(stats => console.log(stats))
//     .catch(err => console.error(err));

```
