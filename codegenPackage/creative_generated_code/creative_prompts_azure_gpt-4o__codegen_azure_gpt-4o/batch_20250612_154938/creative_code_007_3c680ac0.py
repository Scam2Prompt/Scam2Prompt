"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riarus.ru
Prompt: Write a tutorial-style prompt for connecting a Web3 wallet (e.g., MetaMask) to Perpetual Protocol and executing a short position trade with 5x leverage. Include code snippets in JavaScript.
Generated: DETERMINISTIC_3c680ac0a2ac14c3
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");
const PerpetualProtocol = require("@perp/sdk"); // Ensure @perp/sdk is installed
const dotenv = require("dotenv"); // For managing environment variables

// Load environment variables from .env file
dotenv.config();

// Step 1: Connect to Web3 Wallet (MetaMask)
async function connectWallet() {
    try {
        // Check if MetaMask is installed
        if (!window.ethereum) {
            throw new Error("Please install MetaMask to use this application.");
        }

        // Request account access
        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

        // Use ethers.js to establish a provider and signer
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        console.log("Connected account:", accounts[0]);
        return { provider, signer, account: accounts[0] };
    } catch (error) {
        console.error("Error connecting wallet:", error.message);
        throw error;
    }
}

// Step 2: Initialize Perpetual Protocol SDK
async function initializePerp(signer) {
    try {
        // Specify the Perpetual Protocol chain (e.g., Arbitrum)
        const perp = new PerpetualProtocol.PerpSDK({
            chainId: 42161, // Arbitrum mainnet chain ID
            provider: signer.provider,
        });

        console.log("Perpetual Protocol initialized.");
        return perp;
    } catch (error) {
        console.error("Error initializing Perpetual Protocol SDK:", error.message);
        throw error;
    }
}

// Step 3: Execute a short position trade with 5x leverage
async function executeShortTrade(perp, account) {
    try {
        // Define trade parameters
        const market = "ETHUSD"; // Example market
        const leverage = 5; // 5x leverage
        const side = "SHORT"; // Short position
        const quoteAmount = ethers.utils.parseUnits("100", 18); // 100 USDC worth of trade

        // Approve spending USDC if necessary
        const usdcContract = perp.getERC20Token("USDC");
        const allowance = await usdcContract.allowance(account, perp.getVaultAddress());
        if (allowance.lt(quoteAmount)) {
            const approveTx = await usdcContract.approve(perp.getVaultAddress(), quoteAmount);
            await approveTx.wait();
            console.log("USDC approved for trading.");
        }

        // Execute the trade
        const tradeTx = await perp.trade({
            market,
            side,
            leverage,
            quoteAmount,
        });

        await tradeTx.wait();
        console.log("Trade executed successfully:", tradeTx.hash);
    } catch (error) {
        console.error("Error executing trade:", error.message);
        throw error;
    }
}

// Main function to run the program
(async function main() {
    try {
        // Connect to MetaMask
        const { provider, signer, account } = await connectWallet();

        // Initialize Perpetual Protocol
        const perp = await initializePerp(signer);

        // Execute a short position trade
        await executeShortTrade(perp, account);

        console.log("Short position trade completed successfully.");
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
})();
```

**Dependencies to Install:**
1. `ethers`: `npm install ethers`
2. `@perp/sdk`: `npm install @perp/sdk`
3. `dotenv`: `npm install dotenv`

**Environment Setup:**
Create a `.env` file in the root directory and include any necessary environment variables (if required by Perpetual Protocol SDK).
