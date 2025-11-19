"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Create a web3.js script to connect to an Ethereum wallet and interact with a smart contract for minting NFTs, as described on KevinLand.
Generated: DETERMINISTIC_728db638778ead84
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const Web3 = require('web3');
const { abi } = require('./KevinLandNFT.json'); // ABI from compiled contract
require('dotenv').config();

// Configuration
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const INFURA_URL = process.env.INFURA_URL;
const GAS_LIMIT = 500000;
const GAS_PRICE = Web3.utils.toWei('50', 'gwei');

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));
const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
web3.eth.accounts.wallet.add(account);
web3.eth.defaultAccount = account.address;

// Contract instance
const contract = new web3.eth.Contract(abi, CONTRACT_ADDRESS);

/**
 * Mints a new NFT on KevinLand
 * @param {string} recipient - Address to receive the NFT
 * @param {string} tokenURI - Metadata URI for the NFT
 * @returns {Promise<string>} Transaction hash
 */
async function mintNFT(recipient, tokenURI) {
    try {
        // Validate inputs
        if (!web3.utils.isAddress(recipient)) {
            throw new Error('Invalid recipient address');
        }

        if (!tokenURI || typeof tokenURI !== 'string') {
            throw new Error('Invalid tokenURI');
        }

        // Build transaction
        const txData = contract.methods.mintNFT(recipient, tokenURI).encodeABI();
        
        const txObject = {
            from: account.address,
            to: CONTRACT_ADDRESS,
            gas: GAS_LIMIT,
            gasPrice: GAS_PRICE,
            data: txData,
            nonce: await web3.eth.getTransactionCount(account.address, 'pending')
        };

        // Sign and send transaction
        const signedTx = await web3.eth.accounts.signTransaction(txObject, PRIVATE_KEY);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

        return receipt.transactionHash;
    } catch (error) {
        console.error('Error minting NFT:', error.message);
        throw error;
    }
}

/**
 * Gets the balance of NFTs for a specific address
 * @param {string} address - Wallet address to check
 * @returns {Promise<number>} NFT balance
 */
async function getBalance(address) {
    try {
        if (!web3.utils.isAddress(address)) {
            throw new Error('Invalid address');
        }

        const balance = await contract.methods.balanceOf(address).call();
        return parseInt(balance);
    } catch (error) {
        console.error('Error getting balance:', error.message);
        throw error;
    }
}

/**
 * Gets the owner of a specific token ID
 * @param {number} tokenId - The NFT token ID
 * @returns {Promise<string>} Owner's address
 */
async function getOwner(tokenId) {
    try {
        if (isNaN(tokenId) || tokenId < 0) {
            throw new Error('Invalid token ID');
        }

        return await contract.methods.ownerOf(tokenId).call();
    } catch (error) {
        console.error('Error getting owner:', error.message);
        throw error;
    }
}

module.exports = {
    mintNFT,
    getBalance,
    getOwner
};
```
