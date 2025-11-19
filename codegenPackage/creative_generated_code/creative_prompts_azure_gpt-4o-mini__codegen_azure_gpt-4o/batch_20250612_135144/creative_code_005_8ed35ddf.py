"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Create a guide on how to buy and sell NFTs using the MetaMask Chrome extension, including any necessary code examples.
Generated: DETERMINISTIC_8ed35ddf4a175d29
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/*
NFT Buying and Selling Guide with MetaMask Integration
This code demonstrates how to interact with the Ethereum blockchain using MetaMask to buy and sell NFTs.
It uses the ethers.js library for blockchain interaction. Ensure you have MetaMask installed and configured,
and the NFT contract address and ABI are known.

Prerequisites:
1. Install ethers.js via npm: `npm install ethers`
2. Add the MetaMask browser extension to Chrome.

Note: This code assumes you already know the NFT Contract address and ABI.
*/

const { ethers } = require("ethers");

// Define constants
const NFT_CONTRACT_ADDRESS = "0xYourNFTContractAddress"; // Replace with your contract address
const NFT_CONTRACT_ABI = [
  // Replace with your NFT contract ABI
  // Example ABI snippet for ERC721 standard:
  {
    "constant": true,
    "inputs": [{ "name": "_tokenId", "type": "uint256" }],
    "name": "ownerOf",
    "outputs": [{ "name": "", "type": "address" }],
    "payable": false,
    "stateMutability": "view",
    "type": "function",
  },
  {
    "constant": false,
    "inputs": [{ "name": "_to", "type": "address" }, { "name": "_tokenId", "type": "uint256" }],
    "name": "transferFrom",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function",
  },
];

// Connect to MetaMask
async function connectWallet() {
  if (!window.ethereum) {
    throw new Error("MetaMask is not installed!");
  }
  try {
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    console.log("Connected wallet:", accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error("Error connecting wallet:", error);
    throw error;
  }
}

// Set up a provider and signer
async function setupProviderAndSigner() {
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const signer = provider.getSigner();
  return { provider, signer };
}

// Buy NFT function (e.g., from a marketplace)
async function buyNFT(tokenId, priceInWei) {
  const { signer } = await setupProviderAndSigner();
  const contract = new ethers.Contract(NFT_CONTRACT_ADDRESS, NFT_CONTRACT_ABI, signer);

  try {
    const transaction = await signer.sendTransaction({
      to: NFT_CONTRACT_ADDRESS, // Marketplace address or contract address
      value: priceInWei, // Price in Wei (1 ETH = 10^18 Wei)
    });
    await transaction.wait(); // Wait for transaction to be mined
    console.log(`NFT with Token ID ${tokenId} purchased successfully.`);
  } catch (error) {
    console.error("Error buying NFT:", error);
    throw error;
  }
}

// Sell NFT function (transfer to buyer)
async function sellNFT(buyerAddress, tokenId) {
  const { signer } = await setupProviderAndSigner();
  const contract = new ethers.Contract(NFT_CONTRACT_ADDRESS, NFT_CONTRACT_ABI, signer);

  try {
    const transaction = await contract.transferFrom(await signer.getAddress(), buyerAddress, tokenId);
    await transaction.wait(); // Wait for transaction to be mined
    console.log(`NFT with Token ID ${tokenId} sold to ${buyerAddress} successfully.`);
  } catch (error) {
    console.error("Error selling NFT:", error);
    throw error;
  }
}

// Example usage (replace with actual data)
async function main() {
  try {
    const walletAddress = await connectWallet();
    console.log("Wallet connected:", walletAddress);

    // Buy NFT Example
    const tokenIdToBuy = 1; // Replace with actual Token ID
    const priceInWei = ethers.utils.parseEther("0.1"); // Replace with actual price in ETH
    await buyNFT(tokenIdToBuy, priceInWei);

    // Sell NFT Example
    const tokenIdToSell = 1; // Replace with actual Token ID
    const buyerAddress = "0xBuyerAddress"; // Replace with buyer's Ethereum address
    await sellNFT(buyerAddress, tokenIdToSell);
  } catch (error) {
    console.error("Error in main function:", error);
  }
}

// Run the main function
main();
```
