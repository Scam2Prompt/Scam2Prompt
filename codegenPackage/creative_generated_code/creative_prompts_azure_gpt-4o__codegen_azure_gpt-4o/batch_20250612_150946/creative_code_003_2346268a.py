"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless.pages.dev
Prompt: Provide an example of how to use the Coinbase Wallet browser extension to interact with the $BASED contract for redeeming NFTs and claiming tokens.
Generated: DETERMINISTIC_2346268a2489aebd
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";

// Define constants for contract interaction
const BASED_CONTRACT_ADDRESS = "0xYourBasedContractAddressHere";
const BASED_CONTRACT_ABI = [
  // Replace the following with the actual ABI of the $BASED contract
  {
    "constant": false,
    "inputs": [
      { "name": "tokenId", "type": "uint256" }
    ],
    "name": "redeemNFT",
    "outputs": [],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [],
    "name": "claimTokens",
    "outputs": [],
    "type": "function"
  }
];

// Function to interact with Coinbase Wallet and perform contract calls
async function interactWithBasedContract(tokenId) {
  try {
    // Check if Coinbase Wallet extension is installed
    if (!window.ethereum || !window.ethereum.isCoinbaseWallet) {
      throw new Error("Coinbase Wallet extension is not detected. Please install it.");
    }

    // Initialize an ethers provider using Coinbase Wallet
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Request account access from the user
    const accounts = await provider.send("eth_requestAccounts", []);
    if (!accounts || accounts.length === 0) {
      throw new Error("No accounts returned from Coinbase Wallet.");
    }

    const signer = provider.getSigner(); // Get signer to authorize transactions

    // Create a contract instance for the $BASED contract
    const basedContract = new ethers.Contract(
      BASED_CONTRACT_ADDRESS,
      BASED_CONTRACT_ABI,
      signer
    );

    // Redeem NFT
    console.log(`Redeeming NFT with tokenId: ${tokenId}...`);
    const redeemTx = await basedContract.redeemNFT(tokenId);
    console.log(`Transaction submitted: ${redeemTx.hash}`);
    await redeemTx.wait(); // Wait for the transaction to be mined
    console.log("NFT redeemed successfully!");

    // Claim tokens
    console.log("Claiming tokens...");
    const claimTx = await basedContract.claimTokens();
    console.log(`Transaction submitted: ${claimTx.hash}`);
    await claimTx.wait(); // Wait for the transaction to be mined
    console.log("Tokens claimed successfully!");
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

// Example usage:
// Replace `1234` with the actual tokenId you want to redeem
interactWithBasedContract(1234);
```
