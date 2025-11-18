"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defie.me
Prompt: Provide code to query the balance of an Ethereum wallet using the Ethers.js library in a DeFi context.
Generated: DETERMINISTIC_8f0367a75ef138ea
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { ethers } = require("ethers");

// Define configuration constants
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura project ID
const WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"; // Replace with the wallet address you want to query

// Create a provider using Infura
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);

/**
 * Function to get the balance of an Ethereum wallet
 * @param {string} walletAddress - The Ethereum wallet address
 * @returns {Promise<string>} - The wallet balance in Ether
 */
async function getWalletBalance(walletAddress) {
    try {
        // Validate the wallet address
        if (!ethers.utils.isAddress(walletAddress)) {
            throw new Error("Invalid wallet address");
        }

        // Fetch the balance in Wei (smallest unit of Ether)
        const balanceWei = await provider.getBalance(walletAddress);

        // Convert balance from Wei to Ether
        const balanceEther = ethers.utils.formatEther(balanceWei);

        return balanceEther;
    } catch (error) {
        console.error("Error fetching wallet balance:", error.message);
        throw error; // Re-throw error for further handling if necessary
    }
}

// Main function to execute the balance query
(async () => {
    try {
        const balance = await getWalletBalance(WALLET_ADDRESS);
        console.log(`Balance of wallet ${WALLET_ADDRESS}: ${balance} ETH`);
    } catch (error) {
        console.error("Failed to get wallet balance:", error.message);
    }
})();
```

Make sure to replace `YOUR_INFURA_PROJECT_ID` and `YOUR_WALLET_ADDRESS` with the actual values before running the code.
