"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-nft-dapp-frontend.vercel.app
Prompt: How can I retrieve and display a list of NFTs for a connected wallet in a Sui NFT dApp? Include relevant API calls.
Generated: DETERMINISTIC_ef34f5e6236c9b2a
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { JsonRpcProvider, Network } = require('@mysten/sui.js'); // Sui library to interact with the blockchain
const Web3 = require('web3'); // Used for wallet connection (e.g., MetaMask)

// Configuration: Sui RPC Endpoint
const provider = new JsonRpcProvider(Network.DEVNET); // Change Network.DEVNET to your desired network (MAINNET, TESTNET, DEVNET)

// Function to retrieve NFTs for a connected wallet
async function getNFTsForConnectedWallet(walletAddress) {
    try {
        // Validate input
        if (!walletAddress || typeof walletAddress !== 'string') {
            throw new Error('Invalid wallet address.');
        }

        // Fetch owned objects for the wallet address
        const ownedObjects = await provider.getObjectsOwnedByAddress(walletAddress);

        // Filter NFT objects from owned objects
        const nftObjects = ownedObjects.filter(obj => obj.type.includes('NFT'));

        // Return the list of NFTs
        return nftObjects.map(obj => ({
            objectId: obj.objectId,
            type: obj.type,
        }));
    } catch (error) {
        console.error('Error retrieving NFTs:', error.message);
        throw error; // Re-throw the error for further handling
    }
}

// Example usage
async function main() {
    try {
        // Retrieve wallet address from connected Web3 wallet (MetaMask or similar)
        const web3 = new Web3(Web3.givenProvider);
        const accounts = await web3.eth.requestAccounts(); // Request accounts from the connected wallet
        const walletAddress = accounts[0]; // Use the first connected wallet address

        console.log('Connected Wallet Address:', walletAddress);

        // Fetch NFTs for the wallet address
        const nfts = await getNFTsForConnectedWallet(walletAddress);

        // Display the NFTs
        console.log('NFTs owned by the wallet:', nfts);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
}

// Run the main function
main();
```
