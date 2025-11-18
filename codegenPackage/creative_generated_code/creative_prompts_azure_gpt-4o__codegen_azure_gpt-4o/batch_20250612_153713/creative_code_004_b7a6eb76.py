"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tendaoio.web.app
Prompt: Create a script using Web3.js to display the top 5 Solana NFT collections on Tensor based on 24-hour trading volume.
Generated: DETERMINISTIC_b7a6eb768f24bd79
Batch ID: 20250612_153713
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.trade/v1/nft/collections": {
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
// Import dependencies
const axios = require('axios');

// Tensor API Endpoint
const TENSOR_API_ENDPOINT = "https://api.tensor.trade/v1/nft/collections";

// Helper function to fetch top NFT collections
async function fetchTopCollections() {
    try {
        // Make a GET request to the Tensor API
        const response = await axios.get(TENSOR_API_ENDPOINT);

        // Check if the response data exists and is valid
        if (response.data && Array.isArray(response.data.collections)) {
            // Sort collections based on 24-hour trading volume in descending order
            const sortedCollections = response.data.collections.sort((a, b) => b.volume24h - a.volume24h);

            // Slice the top 5 collections
            const topCollections = sortedCollections.slice(0, 5);

            // Display the top collections
            console.log("Top 5 Solana NFT Collections by 24-Hour Trading Volume:");
            topCollections.forEach((collection, index) => {
                console.log(`${index + 1}. Collection Name: ${collection.name}`);
                console.log(`   24h Volume: ${collection.volume24h} SOL`);
                console.log(`   Floor Price: ${collection.floorPrice} SOL`);
                console.log(`   Total Supply: ${collection.totalSupply}`);
                console.log(`   URL: ${collection.url}`);
                console.log("---------------------------");
            });
        } else {
            console.error("Invalid data received from Tensor API.");
        }
    } catch (error) {
        // Handle errors (network or API-related issues)
        console.error("Error fetching NFT collections from Tensor API:", error.message);
    }
}

// Execute the function to display the top collections
fetchTopCollections();
```

#### Requirements
1. Install `axios`:
   ```bash
   npm install axios
   ```

#### Notes
- Ensure you have access to Tensor's API endpoint as it may require authentication or have rate limits.
