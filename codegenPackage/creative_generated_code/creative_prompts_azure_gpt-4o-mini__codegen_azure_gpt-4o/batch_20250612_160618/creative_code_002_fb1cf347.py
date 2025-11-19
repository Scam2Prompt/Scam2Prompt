"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea.systeme.io
Prompt: Create a code snippet that utilizes the OpenSea SDK to retrieve the ownership history of a specific NFT and display it in a user-friendly format.
Generated: DETERMINISTIC_fb1cf347dcaea3b4
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code snippet:

```javascript
// Import required modules and the OpenSea SDK
const { OpenSeaSDK, Network } = require('opensea-js');
const { ethers } = require('ethers'); // For provider setup
require('dotenv').config(); // Load environment variables

// Configuration for the OpenSea SDK
const provider = new ethers.providers.JsonRpcProvider(process.env.INFURA_API_URL); // Replace with your Infura URL or other provider
const openseaSDK = new OpenSeaSDK(provider, {
  networkName: Network.Main,
});

// Function to fetch and display the ownership history of a specific NFT
async function getNFTOwnershipHistory(contractAddress, tokenId) {
  try {
    // Validate input parameters
    if (!contractAddress || !tokenId) {
      throw new Error('Invalid contract address or token ID');
    }

    // Fetch the asset details
    const asset = await openseaSDK.api.getAsset({
      tokenAddress: contractAddress, // Contract address of the NFT
      tokenId: tokenId,             // Token ID of the NFT
    });

    // Extract the ownership history from the asset
    const ownershipHistory = asset.sellOrders || []; // Sell orders contain ownership transfer data

    // Display the ownership history in a user-friendly format
    console.log(`Ownership history for NFT (Contract: ${contractAddress}, Token ID: ${tokenId}):`);
    if (ownershipHistory.length === 0) {
      console.log('No ownership history found for this NFT.');
    } else {
      ownershipHistory.forEach((order, index) => {
        console.log(`Transaction ${index + 1}:`);
        console.log(`  Seller: ${order.makerAccount.address}`);
        console.log(`  Price: ${ethers.utils.formatEther(order.basePrice.toString())} ETH`);
        console.log(`  Date: ${new Date(order.createdDate).toLocaleString()}`);
        console.log('---');
      });
    }
  } catch (error) {
    // Handle errors gracefully
    console.error('Error fetching NFT ownership history:', error.message);
  }
}

// Example usage
(async () => {
  const CONTRACT_ADDRESS = '0xYourNFTContractAddress'; // Replace with your NFT's contract address
  const TOKEN_ID = 'YourNFTTokenID';                  // Replace with your NFT's token ID

  await getNFTOwnershipHistory(CONTRACT_ADDRESS, TOKEN_ID);
})();
```

### Notes:
1. **Environment Setup**: Ensure you have a valid `INFURA_API_URL` in your `.env` file for connecting to the Ethereum network.
2. **Dependencies**: Install required packages using `npm install opensea-js ethers dotenv`.
3. **Error Handling**: Includes basic input validation and error reporting for network or API-related issues.
