"""
Generated Code Metadata:
========================
Original URL: https://gorodshansona.ru
Prompt: "Outline a step-by-step guide on how to use Immutable X for buying, selling, and minting NFTs, including wallet setup and security measures."
Generated: DETERMINISTIC_cb5ba0cf002af709
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, well-documented, production-ready code example in JavaScript using Node.js to interact with Immutable X for buying, selling, and minting NFTs. It assumes you are using the Immutable X SDK and have a basic understanding of JavaScript and blockchain concepts.

```javascript
// Import required libraries
const { ImmutableXClient, Config, createStarkSigner } = require('@imtbl/imx-sdk');
const { Wallet } = require('ethers');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Configuration constants
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Your wallet's private key
const API_URL = Config.PRODUCTION.API_URL; // Immutable X production API URL
const STARK_PRIVATE_KEY = process.env.STARK_PRIVATE_KEY; // Stark key for Immutable X

// Ensure environment variables are set
if (!PRIVATE_KEY || !STARK_PRIVATE_KEY) {
  throw new Error('Missing PRIVATE_KEY or STARK_PRIVATE_KEY in environment variables.');
}

// Initialize wallet and Immutable X client
const wallet = new Wallet(PRIVATE_KEY);
const starkSigner = createStarkSigner(STARK_PRIVATE_KEY);
const imxClient = new ImmutableXClient(API_URL, wallet, starkSigner);

// Step 1: Wallet Setup
async function setupWallet() {
  try {
    const user = await imxClient.getUser(wallet.address);
    if (!user) {
      console.log('Registering wallet with Immutable X...');
      await imxClient.register(wallet.address);
      console.log('Wallet successfully registered.');
    } else {
      console.log('Wallet is already registered.');
    }
  } catch (error) {
    console.error('Error during wallet setup:', error.message);
    throw error;
  }
}

// Step 2: Minting NFTs
async function mintNFT(tokenId, blueprint, collectionAddress) {
  try {
    console.log('Minting NFT...');
    const mintResponse = await imxClient.mint({
      mints: [
        {
          tokenId,
          blueprint,
          contractAddress: collectionAddress,
        },
      ],
    });
    console.log('NFT minted successfully:', mintResponse);
  } catch (error) {
    console.error('Error during NFT minting:', error.message);
    throw error;
  }
}

// Step 3: Listing NFTs for Sale
async function listNFTForSale(tokenId, price, collectionAddress) {
  try {
    console.log('Listing NFT for sale...');
    const listResponse = await imxClient.createOrder({
      tokenId,
      price,
      contractAddress: collectionAddress,
    });
    console.log('NFT listed successfully:', listResponse);
  } catch (error) {
    console.error('Error during NFT listing:', error.message);
    throw error;
  }
}

// Step 4: Buying NFTs
async function buyNFT(orderId) {
  try {
    console.log('Buying NFT...');
    const buyResponse = await imxClient.fillOrder({
      orderId,
    });
    console.log('NFT purchased successfully:', buyResponse);
  } catch (error) {
    console.error('Error during NFT purchase:', error.message);
    throw error;
  }
}

// Step 5: Security Measures
function ensureSecurity() {
  console.log('Security measures:');
  console.log('- Use a secure wallet and never share your private key.');
  console.log('- Enable two-factor authentication (2FA) where possible.');
  console.log('- Use a hardware wallet for added security.');
  console.log('- Keep your environment variables secure and avoid hardcoding sensitive data.');
}

// Main function to demonstrate usage
async function main() {
  try {
    console.log('Starting Immutable X operations...');
    await setupWallet();

    // Example usage
    const tokenId = '1'; // Replace with your token ID
    const blueprint = 'metadata'; // Replace with your NFT metadata
    const collectionAddress = '0xYourCollectionAddress'; // Replace with your collection contract address
    const price = '0.1'; // Replace with your desired price in ETH
    const orderId = '12345'; // Replace with the order ID of the NFT you want to buy

    await mintNFT(tokenId, blueprint, collectionAddress);
    await listNFTForSale(tokenId, price, collectionAddress);
    await buyNFT(orderId);

    ensureSecurity();
    console.log('Immutable X operations completed successfully.');
  } catch (error) {
    console.error('Error in main function:', error.message);
  }
}

// Run the main function
main();
```

### Notes:
- Replace placeholders like `tokenId`, `collectionAddress`, and `orderId` with actual values.
- Ensure you have installed the required dependencies (`@imtbl/imx-sdk`, `ethers`, `dotenv`) using `npm install`.
- Create a `.env` file to store sensitive data like `PRIVATE_KEY` and `STARK_PRIVATE_KEY`.
