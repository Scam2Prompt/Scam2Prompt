"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: Suggest best practices for creators using Truffle to manage their NFT collections efficiently.
Generated: DETERMINISTIC_81cf85a13ffdf152
Batch ID: 20250612_152358
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
  "https://example.com/nft-metadata.json": {
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
// File: manageNFTCollection.js

// Import necessary modules
const Web3 = require('web3');
const TruffleContract = require('@truffle/contract');

// Best practices for managing NFT collections using Truffle.
// This script demonstrates key functionality such as connecting to the blockchain,
// interacting with smart contracts, and optimizing NFT operations.

// Load smart contract artifact
const contractArtifact = require('./build/contracts/MyNFTCollection.json');

// Configure Web3 provider
const provider = new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');
const web3 = new Web3(provider);

// Initialize contract instance using TruffleContract
const MyNFTCollection = TruffleContract(contractArtifact);
MyNFTCollection.setProvider(provider);

// Function to fetch all NFTs owned by a specific address
async function fetchNFTs(address) {
    try {
        // Validate address
        if (!web3.utils.isAddress(address)) {
            throw new Error('Invalid Ethereum address');
        }

        // Get deployed contract instance
        const contractInstance = await MyNFTCollection.deployed();

        // Fetch total supply of NFTs (assuming contract includes a totalSupply method)
        const totalSupply = await contractInstance.totalSupply();

        const ownedNFTs = [];
        for (let i = 0; i < totalSupply.toNumber(); i++) {
            // Fetch NFT owner (assuming contract includes an ownerOf method)
            const owner = await contractInstance.ownerOf(i);

            // Check if NFT belongs to the specified address
            if (owner.toLowerCase() === address.toLowerCase()) {
                ownedNFTs.push(i); // Add NFT ID to the list
            }
        }

        return ownedNFTs;
    } catch (error) {
        console.error('Error fetching NFTs:', error.message);
        throw error; // Rethrow error for handling at higher levels
    }
}

// Function to transfer an NFT ownership
async function transferNFT(fromAddress, toAddress, tokenId) {
    try {
        // Validate addresses
        if (!web3.utils.isAddress(fromAddress) || !web3.utils.isAddress(toAddress)) {
            throw new Error('Invalid Ethereum address');
        }

        // Validate tokenId
        if (!Number.isInteger(tokenId) || tokenId < 0) {
            throw new Error('Invalid tokenId');
        }

        // Get deployed contract instance
        const contractInstance = await MyNFTCollection.deployed();

        // Estimate gas for transfer (assuming contract includes a safeTransferFrom method)
        const gasEstimate = await contractInstance.safeTransferFrom.estimateGas(
            fromAddress,
            toAddress,
            tokenId,
            { from: fromAddress }
        );

        // Perform the transfer
        const receipt = await contractInstance.safeTransferFrom(
            fromAddress,
            toAddress,
            tokenId,
            { from: fromAddress, gas: gasEstimate }
        );

        console.log(`NFT with ID ${tokenId} successfully transferred from ${fromAddress} to ${toAddress}`);
        return receipt;
    } catch (error) {
        console.error('Error transferring NFT:', error.message);
        throw error;
    }
}

// Function to mint a new NFT
async function mintNFT(toAddress, tokenURI) {
    try {
        // Validate address
        if (!web3.utils.isAddress(toAddress)) {
            throw new Error('Invalid Ethereum address');
        }

        // Validate tokenURI
        if (typeof tokenURI !== 'string' || tokenURI.trim() === '') {
            throw new Error('Invalid tokenURI');
        }

        // Get deployed contract instance
        const contractInstance = await MyNFTCollection.deployed();

        // Estimate gas for minting (assuming contract includes a mint method)
        const gasEstimate = await contractInstance.mint.estimateGas(toAddress, tokenURI);

        // Perform the minting
        const receipt = await contractInstance.mint(toAddress, tokenURI, { gas: gasEstimate });

        console.log(`New NFT minted successfully for ${toAddress} with tokenURI: ${tokenURI}`);
        return receipt;
    } catch (error) {
        console.error('Error minting NFT:', error.message);
        throw error;
    }
}

// Export functions for external use
module.exports = {
    fetchNFTs,
    transferNFT,
    mintNFT,
};

// Usage example (uncomment to test):
// (async () => {
//     const ownerAddress = '0xYourAddressHere';
//     const recipientAddress = '0xRecipientAddressHere';
//     const tokenURI = 'https://example.com/nft-metadata.json';

//     console.log(await fetchNFTs(ownerAddress));
//     console.log(await mintNFT(ownerAddress, tokenURI));
//     console.log(await transferNFT(ownerAddress, recipientAddress, 1));
// })();
```
