"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurnft-blur.github.io
Prompt: Provide an example of a JavaScript function that integrates with a blockchain to verify the ownership and transaction history of a specific Blur NFT.
Generated: DETERMINISTIC_71af56ddd9022b55
Batch ID: 20250612_154902
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=${contractAddress}&address=${owner}&page=1&offset=100&sort=desc&apikey=YOUR_ETHERSCAN_API_KEY`;": {
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
const Web3 = require('web3'); // Web3 library to interact with Ethereum blockchain
const axios = require('axios'); // Axios for API calls

// Set up Web3 connection to Ethereum blockchain
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'); // Replace with your Infura project ID

/**
 * Fetches the ownership and transaction history of a specific Blur NFT.
 * @param {string} contractAddress - The smart contract address of the Blur NFT.
 * @param {number} tokenId - The token ID of the NFT to verify.
 * @returns {Promise<object>} - Ownership and transaction history details.
 */
async function verifyBlurNFTOwnership(contractAddress, tokenId) {
    try {
        // Validate inputs
        if (!web3.utils.isAddress(contractAddress)) {
            throw new Error('Invalid contract address');
        }
        if (typeof tokenId !== 'number' || tokenId < 0) {
            throw new Error('Invalid token ID');
        }

        // ABI (Application Binary Interface) for ERC721 NFT standard
        const ERC721_ABI = [
            {
                constant: true,
                inputs: [{ name: '_tokenId', type: 'uint256' }],
                name: 'ownerOf',
                outputs: [{ name: '', type: 'address' }],
                payable: false,
                stateMutability: 'view',
                type: 'function',
            },
        ];

        // Create contract instance for the specific Blur NFT
        const contract = new web3.eth.Contract(ERC721_ABI, contractAddress);

        // Fetch current owner of the NFT
        const owner = await contract.methods.ownerOf(tokenId).call();
        if (!owner) {
            throw new Error('Could not retrieve owner information');
        }

        // Fetch transaction history (using an API like Etherscan or Blur's API)
        // Replace with Blur's API endpoint if available
        const etherscanApiUrl = `https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=${contractAddress}&address=${owner}&page=1&offset=100&sort=desc&apikey=YOUR_ETHERSCAN_API_KEY`; // Replace with your Etherscan API key
        const response = await axios.get(etherscanApiUrl);

        if (response.status !== 200 || !response.data.result) {
            throw new Error('Could not retrieve transaction history');
        }

        // Extract transaction history
        const transactionHistory = response.data.result.map((tx) => ({
            from: tx.from,
            to: tx.to,
            tokenId: tx.tokenID,
            timestamp: tx.timeStamp,
            transactionHash: tx.hash,
        }));

        // Return ownership and transaction details
        return {
            owner,
            transactionHistory,
        };
    } catch (error) {
        // Handle errors and return a friendly message
        console.error('Error verifying Blur NFT ownership:', error.message);
        throw new Error('An error occurred while verifying the NFT ownership and history.');
    }
}

// Example usage:
// Replace with the actual contract address and token ID of the Blur NFT
const contractAddress = '0x1234567890abcdef1234567890abcdef12345678';
const tokenId = 1;

verifyBlurNFTOwnership(contractAddress, tokenId)
    .then((data) => {
        console.log('NFT Ownership and History:', data);
    })
    .catch((error) => {
        console.error('Error:', error.message);
    });

```
