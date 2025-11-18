"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accessnodeapp.com
Prompt: Create a JavaScript function to enable multichain asset tracking in a Web3 application, using concepts similar to those described on AccessNodeApp.com.
Generated: DETERMINISTIC_8537fb751328f2ee
Batch ID: 20250612_154603
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.polygonscan.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.bscscan.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.ethereum.org": {
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
 * Multichain Asset Tracker for Web3 Applications
 * This function enables tracking of assets across multiple blockchain networks.
 *
 * @param {Array} chains - An array of blockchain network configurations.
 * @param {string} assetId - The identifier of the asset to track.
 * @returns {Promise<Object>} - A promise that resolves to an object containing the asset's tracking data across chains.
 */
async function trackAssetAcrossChains(chains, assetId) {
    // Validate input parameters
    if (!Array.isArray(chains) || chains.length === 0) {
        throw new Error("Invalid 'chains' parameter: must be a non-empty array.");
    }
    if (typeof assetId !== 'string' || assetId.trim() === '') {
        throw new Error("Invalid 'assetId' parameter: must be a non-empty string.");
    }

    // Function to fetch asset data from a specific chain
    const fetchAssetData = async (chain) => {
        try {
            // Simulate fetching asset data from the blockchain
            // This should be replaced with actual Web3 calls using libraries like ethers.js or web3.js
            const response = await fetch(`${chain.apiUrl}/assets/${assetId}`);
            if (!response.ok) {
                throw new Error(`Failed to fetch data from ${chain.name}: ${response.statusText}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error fetching data from ${chain.name}:`, error);
            return null; // Return null for failed fetches to allow other chains to be processed
        }
    };

    // Create an array of promises to fetch asset data from all chains
    const fetchPromises = chains.map(chain => fetchAssetData(chain));

    // Wait for all fetch operations to complete
    const results = await Promise.all(fetchPromises);

    // Filter out any null results (failed fetches)
    const validResults = results.filter(result => result !== null);
    
    // Return tracking data for the asset across the valid chains
    return {
        assetId,
        trackingData: validResults
    };
}

// Example usage
(async () => {
    const chains = [
        { name: 'Ethereum', apiUrl: 'https://api.ethereum.org' },
        { name: 'Binance Smart Chain', apiUrl: 'https://api.bscscan.com' },
        { name: 'Polygon', apiUrl: 'https://api.polygonscan.com' }
    ];
    
    try {
        const assetId = '0x123456789abcdef'; // Replace with actual asset ID
        const trackingInfo = await trackAssetAcrossChains(chains, assetId);
        console.log('Asset Tracking Information:', trackingInfo);
    } catch (error) {
        console.error('Error tracking asset:', error.message);
    }
})();
```
