"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-starknet-project.vercel.app
Prompt: Create a JavaScript demo application that connects to StarkNet and fetches metadata for NFTs stored on the network.
Generated: DETERMINISTIC_4ce15668b26d6418
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://alpha4.starknet.io": {
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
// Importing necessary libraries
import { Provider, Contract } from 'starknet';

// Initialize the StarkNet Provider with your RPC URL
const provider = new Provider({ 
    sequencer: { 
        baseUrl: 'https://alpha4.starknet.io' // Change to the correct RPC URL
    } 
});

// NFT Contract Address and ABI (for example purposes, replace with actual)
const nftContractAddress = '0xYourNFTContractAddress';
const nftContractABI = [
    // Add the NFT contract ABI here
];

// Function to fetch NFT metadata
async function fetchNFTMetadata(tokenId) {
    try {
        // Create a contract instance
        const contract = new Contract(nftContractABI, nftContractAddress, provider);

        // Call the method to get metadata (replace with actual method name)
        const metadata = await contract.call('get_metadata', [tokenId]);

        if (!metadata) {
            console.error(`No metadata found for token ID: ${tokenId}`);
            return null;
        }

        console.log(`NFT Metadata for token ID ${tokenId}:`, metadata);
        return metadata;
    } catch (error) {
        // Handle errors appropriately
        console.error('Error fetching NFT metadata:', error);
    }
}

// Example usage
const exampleTokenId = '1'; // Replace with the actual token ID you wish to query
fetchNFTMetadata(exampleTokenId);
```

Make sure to replace placeholders like `0xYourNFTContractAddress` and `get_metadata` with actual values relevant to your NFT contract. Ensure that the ABI of your NFT contract is correctly defined in the `nftContractABI` array.
