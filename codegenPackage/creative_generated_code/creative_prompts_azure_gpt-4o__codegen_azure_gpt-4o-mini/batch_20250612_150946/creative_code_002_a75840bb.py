"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless.pages.dev
Prompt: Generate code in JavaScript using ethers.js to send a transaction on Base that redeems multiple Base, Introduced NFTs (up to 30) for $BASED tokens.
Generated: DETERMINISTIC_a75840bbf2eed9e5
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from ethers.js
const { ethers } = require("ethers");

// Define constants for the network and wallet details
const BASE_RPC_URL = "YOUR_BASE_RPC_URL"; // Replace with your Base RPC URL
const WALLET_PRIVATE_KEY = "YOUR_WALLET_PRIVATE_KEY"; // Replace with your wallet private key
const NFT_CONTRACT_ADDRESS = "YOUR_NFT_CONTRACT_ADDRESS"; // Replace with your NFT contract address
const TOKEN_CONTRACT_ADDRESS = "YOUR_TOKEN_CONTRACT_ADDRESS"; // Replace with your $BASED token contract address

// Define the number of NFTs to redeem
const MAX_NFTS_TO_REDEEM = 30;

// Function to send a transaction for redeeming NFTs
async function redeemNFTs(nftIds) {
    // Validate the input
    if (!Array.isArray(nftIds) || nftIds.length === 0 || nftIds.length > MAX_NFTS_TO_REDEEM) {
        throw new Error(`Invalid input: You can redeem between 1 and ${MAX_NFTS_TO_REDEEM} NFTs.`);
    }

    // Setup provider and wallet
    const provider = new ethers.providers.JsonRpcProvider(BASE_RPC_URL);
    const wallet = new ethers.Wallet(WALLET_PRIVATE_KEY, provider);

    // Create a contract instance for the NFT contract
    const nftContract = new ethers.Contract(NFT_CONTRACT_ADDRESS, [
        // Replace with the actual ABI of the NFT contract
        "function redeemNFTs(uint256[] calldata nftIds) external",
    ], wallet);

    // Attempt to send the transaction
    try {
        const tx = await nftContract.redeemNFTs(nftIds);
        console.log(`Transaction sent! Hash: ${tx.hash}`);

        // Wait for the transaction to be mined
        const receipt = await tx.wait();
        console.log("Transaction mined!", receipt);
    } catch (error) {
        console.error("Error sending transaction:", error);
        throw new Error("Transaction failed.");
    }
}

// Example usage of the redeemNFTs function
(async () => {
    // Replace with actual NFT IDs you want to redeem
    const nftIdsToRedeem = [1, 2, 3]; // Example NFT IDs

    try {
        await redeemNFTs(nftIdsToRedeem);
    } catch (error) {
        console.error("Redemption error:", error.message);
    }
})();
```

Make sure to replace placeholders such as `YOUR_BASE_RPC_URL`, `YOUR_WALLET_PRIVATE_KEY`, `YOUR_NFT_CONTRACT_ADDRESS`, and `YOUR_TOKEN_CONTRACT_ADDRESS` with the appropriate values before running the code.
