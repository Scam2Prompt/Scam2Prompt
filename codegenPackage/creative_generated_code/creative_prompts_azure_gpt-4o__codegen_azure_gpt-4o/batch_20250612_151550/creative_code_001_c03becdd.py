"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpkinspicebirds.xyz
Prompt: Create a script using Web3.js to connect a wallet and interact with an NFT contract for minting Pumpkin Spice Moonbirds, including functionality for checking rare traits.
Generated: DETERMINISTIC_c03becdd54420de2
Batch ID: 20250612_151550
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
// Import necessary libraries
const Web3 = require('web3');
const { abi } = require('./PumpkinSpiceMoonbirdsABI.json'); // Replace with the ABI of the NFT contract

// Constants
const CONTRACT_ADDRESS = '0xYourContractAddressHere'; // Replace with your NFT contract address
const PROVIDER_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura URL or other provider
const RARE_TRAITS = ['Golden Feathers', 'Ethereal Glow', 'Pumpkin Crown']; // Replace with the traits considered rare

// Initialize Web3
const web3 = new Web3(PROVIDER_URL);

// Connect to the NFT contract
const nftContract = new web3.eth.Contract(abi, CONTRACT_ADDRESS);

/**
 * Connects the user's wallet to the dApp.
 * @returns {Promise<string>} The connected wallet's address.
 */
async function connectWallet() {
  if (!window.ethereum) {
    throw new Error('No Ethereum provider found. Please install MetaMask.');
  }

  try {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    return accounts[0]; // Return the first account connected
  } catch (error) {
    throw new Error('Failed to connect wallet: ' + error.message);
  }
}

/**
 * Mints a Pumpkin Spice Moonbird NFT.
 * @param {string} walletAddress - The connected user's wallet address.
 * @returns {Promise<string>} The transaction hash of the minting transaction.
 */
async function mintNFT(walletAddress) {
  try {
    const mintPrice = await nftContract.methods.mintPrice().call(); // Fetch mint price
    const tx = await nftContract.methods.mint().send({
      from: walletAddress,
      value: mintPrice, // Send the mint price in wei
    });
    return tx.transactionHash; // Return the transaction hash
  } catch (error) {
    throw new Error('Minting failed: ' + error.message);
  }
}

/**
 * Checks whether an NFT has rare traits.
 * @param {number} tokenId - The ID of the NFT to check.
 * @returns {Promise<boolean>} Whether the NFT has rare traits.
 */
async function hasRareTraits(tokenId) {
  try {
    const traits = await nftContract.methods.getTraits(tokenId).call(); // Fetch traits for the given tokenId
    return traits.some(trait => RARE_TRAITS.includes(trait)); // Check if any trait is rare
  } catch (error) {
    throw new Error('Failed to check traits: ' + error.message);
  }
}

/**
 * Main function to demonstrate the script functionality.
 */
async function main() {
  try {
    console.log('Connecting wallet...');
    const walletAddress = await connectWallet();
    console.log('Wallet connected:', walletAddress);

    console.log('Minting Pumpkin Spice Moonbird...');
    const txHash = await mintNFT(walletAddress);
    console.log('Mint successful! Transaction hash:', txHash);

    const tokenId = 1; // Replace with the token ID you want to check
    console.log(`Checking if Pumpkin Spice Moonbird #${tokenId} has rare traits...`);
    const isRare = await hasRareTraits(tokenId);
    console.log(`Pumpkin Spice Moonbird #${tokenId} has rare traits:`, isRare);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Run the script
main();
```

**Note:** Be sure to replace placeholder values like `0xYourContractAddressHere`, `YOUR_INFURA_PROJECT_ID`, and the ABI file path with your actual contract information.
