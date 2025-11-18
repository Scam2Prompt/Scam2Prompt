"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnia.pages.dev
Prompt: Generate code to integrate Somnia's interoperability protocols into a decentralized application (dApp) for unified NFT trading across different blockchains.
Generated: DETERMINISTIC_3a06991501592bfb
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and dependencies
const Web3 = require('web3');
const SomniaSDK = require('somnia-sdk'); // Hypothetical SDK for Somnia's interoperability protocols
const dotenv = require('dotenv');
dotenv.config();

// Initialize the environment variables
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key for signing transactions
const RPC_URL = process.env.RPC_URL;        // RPC URL of the blockchain node
const SOMNIA_API_KEY = process.env.SOMNIA_API_KEY; // API key to use Somnia SDK

// Initialize web3 and Somnia SDK
const web3 = new Web3(new Web3.providers.HttpProvider(RPC_URL));
const somnia = new SomniaSDK(SOMNIA_API_KEY);

// Define wallet information
const userWallet = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
web3.eth.accounts.wallet.add(userWallet);

// Contract configuration
const nftMarketplaceContractAddress = '0xYourNFTMarketplaceAddress'; // Replace with actual contract address
const nftMarketplaceABI = [
  /* Replace with the ABI of the NFT marketplace contract */
];

// Initialize the marketplace contract
const nftMarketplaceContract = new web3.eth.Contract(
  nftMarketplaceABI, 
  nftMarketplaceContractAddress
);

/**
 * Function to list an NFT for unified trading across multiple blockchains.
 * 
 * @param {string} nftContractAddress - Address of the NFT contract.
 * @param {number} tokenId - ID of the NFT to be listed.
 * @param {number} price - Price of the NFT in WEI.
 * @returns {Promise<string>} - Transaction hash if successful.
 */
async function listNFT(nftContractAddress, tokenId, price) {
  try {
    // Check if Somnia's protocol supports the NFT contract
    const isSupported = await somnia.isContractSupported(nftContractAddress);
    if (!isSupported) {
      throw new Error("NFT contract is not supported by Somnia's protocol.");
    }

    // Create interoperability metadata using Somnia's SDK
    const interoperabilityMetadata = await somnia.createInteroperabilityMetadata(
      nftContractAddress, 
      tokenId
    );

    // Prepare transaction data for listing the NFT
    const txData = nftMarketplaceContract.methods.listNFT(
      nftContractAddress, 
      tokenId, 
      price, 
      interoperabilityMetadata
    ).encodeABI();

    // Create and sign the transaction
    const tx = {
      from: userWallet.address,
      to: nftMarketplaceContractAddress,
      gas: await web3.eth.estimateGas({
        from: userWallet.address,
        to: nftMarketplaceContractAddress,
        data: txData,
      }),
      data: txData,
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log("NFT listed successfully. Transaction Hash:", receipt.transactionHash);
    return receipt.transactionHash;
  } catch (error) {
    console.error("Error listing NFT:", error.message);
    throw error;
  }
}

/**
 * Function to buy an NFT listed on the marketplace.
 * 
 * @param {string} listingId - ID of the NFT listing to purchase.
 * @returns {Promise<string>} - Transaction hash if successful.
 */
async function buyNFT(listingId) {
  try {
    // Prepare transaction data for buying the NFT
    const txData = nftMarketplaceContract.methods.buyNFT(listingId).encodeABI();

    // Create and sign the transaction
    const tx = {
      from: userWallet.address,
      to: nftMarketplaceContractAddress,
      gas: await web3.eth.estimateGas({
        from: userWallet.address,
        to: nftMarketplaceContractAddress,
        data: txData,
      }),
      data: txData,
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log("NFT purchased successfully. Transaction Hash:", receipt.transactionHash);
    return receipt.transactionHash;
  } catch (error) {
    console.error("Error purchasing NFT:", error.message);
    throw error;
  }
}

// Example Usage
(async () => {
  try {
    const nftContractAddress = '0xYourNFTContractAddress'; // Replace with actual NFT contract address
    const tokenId = 1; // Replace with the ID of the NFT to be listed
    const price = web3.utils.toWei('0.1', 'ether'); // Replace with desired price in ETH

    // List an NFT for unified trading
    const listTransactionHash = await listNFT(nftContractAddress, tokenId, price);
    console.log("Listed NFT Transaction Hash:", listTransactionHash);

    // Buy the listed NFT
    const listingId = '0xListingId'; // Replace with actual listing ID from marketplace
    const buyTransactionHash = await buyNFT(listingId);
    console.log("Purchased NFT Transaction Hash:", buyTransactionHash);
  } catch (error) {
    console.error("Error in dApp execution:", error.message);
  }
})();
```
