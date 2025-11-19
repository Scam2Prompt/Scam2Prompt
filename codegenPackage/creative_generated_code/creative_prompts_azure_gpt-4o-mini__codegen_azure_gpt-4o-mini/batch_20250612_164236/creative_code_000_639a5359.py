"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-nft.vercel.app
Prompt: How can I connect my wallet to mint NFTs using the Internet Friends Creator on ZKSync?
Generated: DETERMINISTIC_639a53599320b6d8
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import { ethers } from 'ethers';
import { ZkSyncProvider, Wallet } from 'zksync';
import { NFTContract } from './NFTContract'; // Import your NFT contract interface

// Define constants
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const WALLET_PRIVATE_KEY = 'YOUR_WALLET_PRIVATE_KEY'; // Replace with your wallet private key
const NFT_CONTRACT_ADDRESS = 'YOUR_NFT_CONTRACT_ADDRESS'; // Replace with your deployed NFT contract address

// Function to mint NFT
async function mintNFT(tokenURI) {
    try {
        // Setup provider for ZKSync
        const provider = await ZkSyncProvider.newDefaultProvider('mainnet');
        
        // Create wallet instance
        const wallet = new Wallet(WALLET_PRIVATE_KEY, provider);

        // Initialize NFT contract instance
        const contract = new ethers.Contract(NFT_CONTRACT_ADDRESS, NFTContract.abi, wallet);

        // Mint NFT by calling the mint function on the contract
        const tx = await contract.mint(wallet.address, tokenURI);

        // Wait for the transaction to be mined
        const receipt = await tx.wait();

        console.log('NFT minted successfully!', receipt);
    } catch (error) {
        console.error('Error minting NFT:', error);
        
        // Handle specific error cases if needed
        if (error.code === 'INSUFFICIENT_FUNDS') {
            console.error('Please ensure your wallet has enough funds to cover the transaction.');
        } else if (error.code === 'NETWORK_ERROR') {
            console.error('Network error occurred. Please check your connection and try again.');
        } else {
            console.error('An unexpected error occurred:', error.message);
        }
    }
}

// Call mintNFT with the desired token URI
const tokenURI = 'YOUR_TOKEN_URI'; // Replace with your specific token URI
mintNFT(tokenURI);
```

**Note**: Replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_WALLET_PRIVATE_KEY`, `YOUR_NFT_CONTRACT_ADDRESS`, and `YOUR_TOKEN_URI` with actual values to execute the code. Make sure to securely handle your private key and never expose it in public repositories.
