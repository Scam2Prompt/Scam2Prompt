"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineanfts.xyz
Prompt: Create a JavaScript-based solution for integrating Linea blockchain NFT data into a decentralized application (dApp).
Generated: DETERMINISTIC_be007d7ebf5a1eb8
Batch ID: 20250612_145427
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://linea-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import necessary libraries
import Web3 from 'web3';
import axios from 'axios';

// Define constants for the Linea RPC endpoint and NFT contract address
const LINEA_RPC_URL = 'https://linea-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID';
const NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddress';

// Initialize Web3 with the Linea RPC URL
const web3 = new Web3(new Web3.providers.HttpProvider(LINEA_RPC_URL));

// ABI of the NFT contract (simplified for demonstration purposes)
const nftContractABI = [
    // Add the relevant ABI components here
    {
        "constant": true,
        "inputs": [{ "name": "_tokenId", "type": "uint256" }],
        "name": "tokenURI",
        "outputs": [{ "name": "", "type": "string" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{ "name": "", "type": "uint256" }],
        "name": "ownerOf",
        "outputs": [{ "name": "", "type": "address" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
];

// Create a contract instance
const nftContract = new web3.eth.Contract(nftContractABI, NFT_CONTRACT_ADDRESS);

/**
 * Fetch NFT metadata for a given token ID
 * @param {number} tokenId - The ID of the NFT
 * @returns {Promise<Object>} - The NFT metadata
 */
async function fetchNFTMetadata(tokenId) {
    try {
        // Get the token URI from the contract
        const tokenURI = await nftContract.methods.tokenURI(tokenId).call();
        
        // Fetch the metadata from the token URI
        const response = await axios.get(tokenURI);
        
        return response.data; // Return the metadata
    } catch (error) {
        console.error(`Error fetching NFT metadata for token ID ${tokenId}:`, error);
        throw new Error('Failed to fetch NFT metadata');
    }
}

/**
 * Fetch the owner of a given token ID
 * @param {number} tokenId - The ID of the NFT
 * @returns {Promise<string>} - The owner address
 */
async function fetchNFTOwner(tokenId) {
    try {
        // Get the owner address from the contract
        const ownerAddress = await nftContract.methods.ownerOf(tokenId).call();
        
        return ownerAddress; // Return the owner address
    } catch (error) {
        console.error(`Error fetching NFT owner for token ID ${tokenId}:`, error);
        throw new Error('Failed to fetch NFT owner');
    }
}

/**
 * Main function to demonstrate fetching NFT data
 * @async
 */
async function main() {
    const tokenId = 1; // Example token ID

    try {
        // Fetch NFT metadata
        const metadata = await fetchNFTMetadata(tokenId);
        console.log('NFT Metadata:', metadata);

        // Fetch NFT owner
        const owner = await fetchNFTOwner(tokenId);
        console.log('NFT Owner Address:', owner);
    } catch (error) {
        console.error('An error occurred in the main function:', error);
    }
}

// Run the main function
main();
```
