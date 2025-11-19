"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walrusnft.com
Prompt: Illustrate how to use Web3.js to interact with the Walrus NFT collection, focusing on fetching ownership details and transaction history.
Generated: DETERMINISTIC_f937231a43b082f3
Batch ID: 20250612_155544
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/assets/${WALRUS_NFT_ADDRESS}/${tokenId}/transfers`": {
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
// Import the required libraries
const Web3 = require('web3');
const axios = require('axios');

// Define the Walrus NFT contract details
const WALRUS_NFT_ADDRESS = '0xYourWalrusNFTContractAddress'; // Replace with actual contract address
const WALRUS_NFT_ABI = [ /* ABI array goes here */ ]; // Replace with actual ABI

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID')); // Replace with your Infura project ID

/**
 * Fetch ownership details of the Walrus NFT collection for a given wallet address
 * @param {string} walletAddress - The Ethereum wallet address to check
 * @returns {Promise<Array>} - A promise that resolves to an array of owned NFT IDs
 */
async function getOwnershipDetails(walletAddress) {
    try {
        // Create a contract instance
        const contract = new web3.eth.Contract(WALRUS_NFT_ABI, WALRUS_NFT_ADDRESS);
        
        // Fetch the number of NFTs owned by the wallet
        const balance = await contract.methods.balanceOf(walletAddress).call();
        
        const ownedNFTs = [];
        
        // Loop through the owned NFTs and fetch their IDs
        for (let i = 0; i < balance; i++) {
            const tokenId = await contract.methods.tokenOfOwnerByIndex(walletAddress, i).call();
            ownedNFTs.push(tokenId);
        }
        
        return ownedNFTs;
    } catch (error) {
        console.error('Error fetching ownership details:', error);
        throw new Error('Could not fetch ownership details.'); // Propagate error
    }
}

/**
 * Fetch the transaction history of a specific NFT by its token ID
 * @param {string} tokenId - The token ID of the NFT
 * @returns {Promise<Array>} - A promise that resolves to an array of transaction details
 */
async function getTransactionHistory(tokenId) {
    try {
        // Placeholder URL for transaction history; replace with actual endpoint
        const response = await axios.get(`https://api.opensea.io/api/v1/assets/${WALRUS_NFT_ADDRESS}/${tokenId}/transfers`);
        
        return response.data.asset_events || [];
    } catch (error) {
        console.error('Error fetching transaction history:', error);
        throw new Error('Could not fetch transaction history.'); // Propagate error
    }
}

// Example Usage
(async () => {
    const walletAddress = '0xYourWalletAddress'; // Replace with actual wallet address
    const tokenId = '1'; // Replace with actual token ID

    try {
        // Fetch and log ownership details
        const ownedNFTs = await getOwnershipDetails(walletAddress);
        console.log('Owned NFTs:', ownedNFTs);

        // Fetch and log transaction history for a specific NFT
        const transactions = await getTransactionHistory(tokenId);
        console.log('Transaction History for token ID', tokenId, ':', transactions);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```
