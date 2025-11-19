"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-node.pages.dev
Prompt: Write a JavaScript function that tracks the performance of a specific NFT collection, such as Bored Ape Yacht Club, using the data from SearchDapps.
Generated: DETERMINISTIC_73091718a91e0183
Batch ID: 20250612_160804
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.searchdapps.com/nft": {
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
 * @function trackNFTCollectionPerformance
 * @description Tracks the performance of a specific NFT collection using data from SearchDapps.
 * @param {string} collectionName - The name of the NFT collection to track (e.g., "Bored Ape Yacht Club").
 * @param {string} apiKey - The API key for authenticating with SearchDapps.
 * @returns {Promise<Object>} - Returns a promise that resolves with the performance data of the NFT collection.
 * @throws {Error} - Throws an error if the API request fails or returns an invalid response.
 */

async function trackNFTCollectionPerformance(collectionName, apiKey) {
    const baseUrl = 'https://api.searchdapps.com/nft';
    const url = `${baseUrl}/collections/${encodeURIComponent(collectionName)}/performance`;

    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            }
        });

        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
            throw new Error(`Error fetching data from SearchDapps: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        // Validate the response data structure
        if (!data || typeof data !== 'object' || !data.performance) {
            throw new Error('Invalid data structure received from SearchDapps.');
        }

        return data.performance;

    } catch (error) {
        console.error('Failed to track NFT collection performance:', error);
        throw new Error('Could not fetch NFT collection performance data.');
    }
}

// Example usage (uncomment to use):
// (async () => {
//     try {
//         const performanceData = await trackNFTCollectionPerformance('Bored Ape Yacht Club', 'your_api_key_here');
//         console.log(performanceData);
//     } catch (error) {
//         console.error(error.message);
//     }
// })();
```
