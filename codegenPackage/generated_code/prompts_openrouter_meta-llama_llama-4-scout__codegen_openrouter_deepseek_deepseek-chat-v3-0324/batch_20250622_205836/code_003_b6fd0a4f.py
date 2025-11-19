"""
Generated Code Metadata:
========================
Original URL: https://web3-node-82f.pages.dev
Prompt: How can I use Web3.js to connect to a blockchain network and manage NFTs, including minting, transferring, and receiving them?
Generated: DETERMINISTIC_b6fd0a4f7ed695bb
Batch ID: 20250622_205836
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://${NETWORK}.infura.io/v3/${INFURA_PROJECT_ID}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/nft/metadata/1": {
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
const { abi } = require('./NFTContractABI.json'); // Replace with your NFT contract ABI
require('dotenv').config();

// Configuration
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS; // Your NFT contract address
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID; // Your Infura project ID
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Your wallet private key
const NETWORK = process.env.NETWORK || 'ropsten'; // Default to Ropsten testnet

// Initialize Web3 with Infura provider
const web3 = new Web3(`https://${NETWORK}.infura.io/v3/${INFURA_PROJECT_ID}`);

// Create contract instance
const nftContract = new web3.eth.Contract(abi, CONTRACT_ADDRESS);

// Get the account from private key
const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
web3.eth.accounts.wallet.add(account);

/**
 * Mint a new NFT
 * @param {string} toAddress - Recipient address
 * @param {string} tokenURI - Metadata URI for the NFT
 * @returns {Promise<string>} Transaction hash
 */
async function mintNFT(toAddress, tokenURI) {
    try {
        const tx = nftContract.methods.mint(toAddress, tokenURI);
        const gas = await tx.estimateGas({ from: account.address });
        const gasPrice = await web3.eth.getGasPrice();
        
        const txData = {
            from: account.address,
            to: CONTRACT_ADDRESS,
            gas,
            gasPrice,
            data: tx.encodeABI()
        };

        const signedTx = await web3.eth.accounts.signTransaction(txData, PRIVATE_KEY);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        
        return receipt.transactionHash;
    } catch (error) {
        console.error('Error minting NFT:', error);
        throw error;
    }
}

/**
 * Transfer NFT to another address
 * @param {string} fromAddress - Current owner address
 * @param {string} toAddress - New owner address
 * @param {number} tokenId - ID of the NFT to transfer
 * @returns {Promise<string>} Transaction hash
 */
async function transferNFT(fromAddress, toAddress, tokenId) {
    try {
        const tx = nftContract.methods.transferFrom(fromAddress, toAddress, tokenId);
        const gas = await tx.estimateGas({ from: account.address });
        const gasPrice = await web3.eth.getGasPrice();
        
        const txData = {
            from: account.address,
            to: CONTRACT_ADDRESS,
            gas,
            gasPrice,
            data: tx.encodeABI()
        };

        const signedTx = await web3.eth.accounts.signTransaction(txData, PRIVATE_KEY);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        
        return receipt.transactionHash;
    } catch (error) {
        console.error('Error transferring NFT:', error);
        throw error;
    }
}

/**
 * Get NFT owner by token ID
 * @param {number} tokenId - ID of the NFT
 * @returns {Promise<string>} Owner address
 */
async function getNFTOwner(tokenId) {
    try {
        return await nftContract.methods.ownerOf(tokenId).call();
    } catch (error) {
        console.error('Error getting NFT owner:', error);
        throw error;
    }
}

/**
 * Get NFT metadata URI by token ID
 * @param {number} tokenId - ID of the NFT
 * @returns {Promise<string>} Metadata URI
 */
async function getNFTURI(tokenId) {
    try {
        return await nftContract.methods.tokenURI(tokenId).call();
    } catch (error) {
        console.error('Error getting NFT URI:', error);
        throw error;
    }
}

/**
 * Get balance of NFTs for an address
 * @param {string} ownerAddress - Address to check balance for
 * @returns {Promise<number>} Number of NFTs owned
 */
async function getNFTBalance(ownerAddress) {
    try {
        return await nftContract.methods.balanceOf(ownerAddress).call();
    } catch (error) {
        console.error('Error getting NFT balance:', error);
        throw error;
    }
}

// Example usage (commented out)
/*
(async () => {
    try {
        const recipient = '0xRecipientAddress';
        const tokenURI = 'https://example.com/nft/metadata/1';
        
        // Mint NFT
        const mintTx = await mintNFT(recipient, tokenURI);
        console.log('Mint transaction hash:', mintTx);
        
        // Get NFT owner
        const tokenId = 1; // Example token ID
        const owner = await getNFTOwner(tokenId);
        console.log('NFT owner:', owner);
        
        // Transfer NFT
        const newOwner = '0xNewOwnerAddress';
        const transferTx = await transferNFT(recipient, newOwner, tokenId);
        console.log('Transfer transaction hash:', transferTx);
        
        // Check balance
        const balance = await getNFTBalance(newOwner);
        console.log('NFT balance:', balance);
    } catch (error) {
        console.error('Example error:', error);
    }
})();
*/
```
