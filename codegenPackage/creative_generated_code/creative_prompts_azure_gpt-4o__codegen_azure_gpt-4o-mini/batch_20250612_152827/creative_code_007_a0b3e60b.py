"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Generate a script using web3.js to integrate with a rarity tools provider API, enabling listing of NFTs for rarity evaluation, as mentioned in KevinLand's FAQ section.
Generated: DETERMINISTIC_a0b3e60bdb91402a
Batch ID: 20250612_152827
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.rarity.tools/v1/nft/list": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://link-to-nft-image.com/image.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import required libraries
const Web3 = require('web3');
const axios = require('axios');

// Set up web3 instance with an Ethereum provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'));

// Rarity Tools API endpoint
const RARITY_TOOLS_API_URL = 'https://api.rarity.tools/v1/nft/list';

// Replace with your own contract address and NFT metadata
const CONTRACT_ADDRESS = '0xYourContractAddress';
const NFT_METADATA = {
    name: "NFT Name",
    description: "Description of the NFT",
    image: "https://link-to-nft-image.com/image.png"
};

// Function to list NFT for rarity evaluation
async function listNFTForRarity() {
    try {
        // Prepare the data for the API request
        const requestData = {
            contractAddress: CONTRACT_ADDRESS,
            tokenId: '1', // Replace with the actual token ID
            metadata: NFT_METADATA
        };

        // Make POST request to Rarity Tools API
        const response = await axios.post(RARITY_TOOLS_API_URL, requestData);
        
        // Check if the response is successful
        if (response.status === 200) {
            console.log("Successfully listed NFT for rarity evaluation:", response.data);
        } else {
            console.error("Failed to list NFT. Status code:", response.status);
        }
    } catch (error) {
        // Handle errors such as network issues or API errors
        console.error("An error occurred while listing the NFT:", error.message);
    }
}

// Call the function to list NFT for rarity evaluation
listNFTForRarity();
```

**Note:** Make sure to replace `YOUR_INFURA_PROJECT_ID`, `0xYourContractAddress`, and the `tokenId` with appropriate values for your application. Additionally, ensure you have the necessary permissions and API key to access the Rarity Tools API.
