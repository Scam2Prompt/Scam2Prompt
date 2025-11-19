"""
Generated Code Metadata:
========================
Original URL: https://walrusnft.com
Prompt: Illustrate how to use Web3.js to interact with the Walrus NFT collection, focusing on fetching ownership details and transaction history.
Generated: DETERMINISTIC_f937231a43b082f3
Batch ID: 20250612_155544
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=${config.walrusNFTContractAddress}&tokenid=${tokenId}&sort=desc&apikey=${config.etherscanApiKey}`": {
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

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const axios = require('axios');

// Configuration
const config = {
  rpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID', // Replace with your Infura project ID
  walrusNFTContractAddress: '0x...', // Replace with Walrus NFT contract address
  etherscanApiKey: 'YOUR_ETHERSCAN_API_KEY', // Replace with your Etherscan API key
  abi: [/* Walrus NFT contract ABI */] // Replace with actual ABI
};

// Initialize Web3
const web3 = new Web3(config.rpcUrl);

// Create contract instance
const walrusNFTContract = new web3.eth.Contract(config.abi, config.walrusNFTContractAddress);

/**
 * Fetches the owner of a specific Walrus NFT
 * @param {number} tokenId - The token ID to check
 * @returns {Promise<string>} - Address of the owner
 */
async function getNFTOwner(tokenId) {
  try {
    const owner = await walrusNFTContract.methods.ownerOf(tokenId).call();
    return owner;
  } catch (error) {
    console.error(`Error fetching owner for token ${tokenId}:`, error);
    throw new Error('Failed to fetch NFT owner');
  }
}

/**
 * Fetches the transaction history for a specific Walrus NFT
 * @param {number} tokenId - The token ID to check
 * @returns {Promise<Array>} - Array of transactions
 */
async function getNFTTransactionHistory(tokenId) {
  try {
    const response = await axios.get(
      `https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=${config.walrusNFTContractAddress}&tokenid=${tokenId}&sort=desc&apikey=${config.etherscanApiKey}`
    );
    
    if (response.data.status !== '1') {
      throw new Error(response.data.message || 'Failed to fetch transaction history');
    }
    
    return response.data.result;
  } catch (error) {
    console.error(`Error fetching transaction history for token ${tokenId}:`, error);
    throw new Error('Failed to fetch transaction history');
  }
}

/**
 * Fetches all NFTs owned by a specific address
 * @param {string} address - The wallet address to check
 * @returns {Promise<Array>} - Array of owned token IDs
 */
async function getOwnedNFTs(address) {
  try {
    // Get total supply first
    const totalSupply = await walrusNFTContract.methods.totalSupply().call();
    
    const ownedTokens = [];
    
    // Check ownership for each token (this can be optimized with balanceOf and tokenOfOwnerByIndex if available)
    for (let i = 1; i <= totalSupply; i++) {
      try {
        const owner = await walrusNFTContract.methods.ownerOf(i).call();
        if (owner.toLowerCase() === address.toLowerCase()) {
          ownedTokens.push(i);
        }
      } catch (error) {
        // Skip if token doesn't exist or other error occurs
        continue;
      }
    }
    
    return ownedTokens;
  } catch (error) {
    console.error(`Error fetching owned NFTs for address ${address}:`, error);
    throw new Error('Failed to fetch owned NFTs');
  }
}

// Example usage
(async () => {
  try {
    const tokenId = 123; // Example token ID
    const walletAddress = '0x...'; // Example wallet address
    
    // Get owner of a specific NFT
    const owner = await getNFTOwner(tokenId);
    console.log(`Owner of token ${tokenId}:`, owner);
    
    // Get transaction history for an NFT
    const txHistory = await getNFTTransactionHistory(tokenId);
    console.log(`Transaction history for token ${tokenId}:`, txHistory);
    
    // Get all NFTs owned by an address
    const ownedNFTs = await getOwnedNFTs(walletAddress);
    console.log(`NFTs owned by ${walletAddress}:`, ownedNFTs);
    
  } catch (error) {
    console.error('Error in example usage:', error);
  }
})();
```
