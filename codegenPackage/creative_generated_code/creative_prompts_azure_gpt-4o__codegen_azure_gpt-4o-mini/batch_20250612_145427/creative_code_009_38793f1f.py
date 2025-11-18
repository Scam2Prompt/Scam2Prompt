"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineanfts.xyz
Prompt: Write code to handle errors and exceptions when querying NFT data from the Linea NFT Finder API in a JavaScript application.
Generated: DETERMINISTIC_38793f1f11c20324
Batch ID: 20250612_145427
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linea.nftfinder.io/nft/${tokenId}`;": {
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
 * NFT Data Fetcher
 * This function queries the Linea NFT Finder API for NFT data and handles errors gracefully.
 */

async function fetchNFTData(tokenId) {
    const apiUrl = `https://api.linea.nftfinder.io/nft/${tokenId}`;
    
    try {
        // Validate the tokenId input
        if (!tokenId || typeof tokenId !== 'string') {
            throw new Error('Invalid tokenId: It must be a non-empty string.');
        }

        // Perform the API request
        const response = await fetch(apiUrl);
        
        // Check if the response is successful
        if (!response.ok) {
            // Handle errors based on the response status
            switch (response.status) {
                case 404:
                    throw new Error('NFT not found: Please check the token ID.');
                case 500:
                    throw new Error('Server error: Please try again later.');
                default:
                    throw new Error(`Error: ${response.statusText}`);
            }
        }

        // Parse and return the JSON data
        const nftData = await response.json();
        return nftData;

    } catch (error) {
        // Log the error to the console for debugging
        console.error('Error fetching NFT data:', error.message);
        // Optionally rethrow the error for further handling
        throw error;
    }
}

// Example usage of the fetchNFTData function
(async () => {
    const tokenId = 'example-token-id'; // Replace with a valid token ID

    try {
        const data = await fetchNFTData(tokenId);
        console.log('NFT Data:', data);
    } catch (error) {
        // Handle the user-facing error message
        console.error('Failed to retrieve NFT data:', error.message);
    }
})();
```
