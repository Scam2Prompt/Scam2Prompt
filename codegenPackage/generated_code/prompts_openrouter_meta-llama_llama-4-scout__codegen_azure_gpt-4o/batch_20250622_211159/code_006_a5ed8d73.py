"""
Generated Code Metadata:
========================
Original URL: https://nft-curve.com
Prompt: Develop a MetaMask Snap that enables users to purchase and manage NFTs directly within their wallet, using the MetaMask SDK and Web3 Services.
Generated: DETERMINISTIC_a5ed8d73c65d39a6
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: nftSnap.js

/**
 * MetaMask Snap for purchasing and managing NFTs directly within the wallet.
 * This Snap uses MetaMask SDK and Web3 services to interact with the blockchain.
 */

// Import required dependencies
const { ethers } = require("ethers");
const { SnapProvider } = require("@metamask/snap-types");

// Constants
const NFT_CONTRACT_ADDRESS = "0xYourNFTContractAddress"; // Replace with your NFT contract address
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura project ID
const NETWORK = "mainnet"; // Change to "rinkeby", "goerli", etc., for test networks

// Initialize Web3 provider
const provider = new ethers.providers.InfuraProvider(NETWORK, INFURA_PROJECT_ID);

// ABI for the NFT contract (simplified example, replace with your contract's ABI)
const nftContractABI = [
  "function purchaseNFT(uint256 tokenId) public payable",
  "function ownerOf(uint256 tokenId) public view returns (address)",
  "function balanceOf(address owner) public view returns (uint256)",
];

// Initialize NFT contract instance
const nftContract = new ethers.Contract(NFT_CONTRACT_ADDRESS, nftContractABI, provider);

/**
 * Function to purchase an NFT.
 * @param {SnapProvider} snapProvider - MetaMask Snap provider.
 * @param {number} tokenId - The ID of the NFT to purchase.
 * @param {string} value - The amount of Ether to send for the purchase.
 */
async function purchaseNFT(snapProvider, tokenId, value) {
  try {
    // Get user's wallet address
    const accounts = await snapProvider.request({ method: "eth_accounts" });
    const userAddress = accounts[0];

    // Connect user's wallet to the contract
    const signer = provider.getSigner(userAddress);
    const contractWithSigner = nftContract.connect(signer);

    // Execute the purchase transaction
    const tx = await contractWithSigner.purchaseNFT(tokenId, { value: ethers.utils.parseEther(value) });
    console.log("Transaction sent:", tx.hash);

    // Wait for transaction confirmation
    const receipt = await tx.wait();
    console.log("Transaction confirmed:", receipt);
    return receipt;
  } catch (error) {
    console.error("Error purchasing NFT:", error);
    throw new Error("Failed to purchase NFT. Please try again.");
  }
}

/**
 * Function to get the balance of NFTs owned by the user.
 * @param {SnapProvider} snapProvider - MetaMask Snap provider.
 * @returns {Promise<number>} - The number of NFTs owned by the user.
 */
async function getNFTBalance(snapProvider) {
  try {
    // Get user's wallet address
    const accounts = await snapProvider.request({ method: "eth_accounts" });
    const userAddress = accounts[0];

    // Query the balance of NFTs
    const balance = await nftContract.balanceOf(userAddress);
    console.log("NFT balance:", balance.toString());
    return balance.toNumber();
  } catch (error) {
    console.error("Error fetching NFT balance:", error);
    throw new Error("Failed to fetch NFT balance. Please try again.");
  }
}

/**
 * Function to check the owner of a specific NFT.
 * @param {number} tokenId - The ID of the NFT to check ownership for.
 * @returns {Promise<string>} - The address of the owner.
 */
async function getNFTOwner(tokenId) {
  try {
    // Query the owner of the NFT
    const owner = await nftContract.ownerOf(tokenId);
    console.log(`Owner of token ${tokenId}:`, owner);
    return owner;
  } catch (error) {
    console.error("Error fetching NFT owner:", error);
    throw new Error("Failed to fetch NFT owner. Please try again.");
  }
}

// Export functions for use in the Snap
module.exports = {
  purchaseNFT,
  getNFTBalance,
  getNFTOwner,
};
```
