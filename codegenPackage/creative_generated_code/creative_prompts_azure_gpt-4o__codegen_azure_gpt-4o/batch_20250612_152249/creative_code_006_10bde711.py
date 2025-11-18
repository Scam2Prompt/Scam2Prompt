"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feg-chain.pages.dev
Prompt: Provide code examples for integrating the FEG Aggregator/Router functionality into a decentralized application (dApp) to source the most affordable token trading rates across multiple DEXs.
Generated: DETERMINISTIC_10bde711643e9f67
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
// Ensure you have installed ethers.js and axios via npm
const { ethers } = require("ethers");
const axios = require("axios");

// Define constants for FEG Aggregator/Router
const FEG_ROUTER_ADDRESS = "0xYourFEGRouterAddressHere"; // Replace this with the actual FEG Router contract address
const FEG_ROUTER_ABI = [ /* Fill in the FEG Router ABI here */ ]; // Replace with the actual ABI of the FEG Router

// Set up the ethers.js provider (e.g., Infura or Alchemy)
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL); // Set your RPC URL in environment variables

// Wallet details (must handle private keys securely in production, do not hard-code them)
const privateKey = process.env.PRIVATE_KEY; // Set your private key in environment variables
const wallet = new ethers.Wallet(privateKey, provider);

// Instantiate FEG Router contract
const fegRouter = new ethers.Contract(FEG_ROUTER_ADDRESS, FEG_ROUTER_ABI, wallet);

// Function to get the best trading rate via FEG Aggregator
async function getBestTradingRate(inputToken, outputToken, inputAmount) {
    try {
        // Call the FEG Router's function to get the best DEX trade rate
        const bestRate = await fegRouter.getBestRate(inputToken, outputToken, inputAmount);
        
        // Log the result for debugging purposes (optional)
        console.log(`Best rate fetched: ${ethers.utils.formatUnits(bestRate, 18)}`);

        // Return the rate details
        return bestRate;
    } catch (error) {
        console.error("Error fetching the best trading rate:", error);
        throw new Error("Failed to fetch the best trading rate. Please try again.");
    }
}

// Function to execute a trade using the FEG Router
async function executeTrade(inputToken, outputToken, inputAmount, slippageTolerance) {
    try {
        // Fetch the current best rate
        const bestRate = await getBestTradingRate(inputToken, outputToken, inputAmount);

        // Compute the minimum amount of output tokens to accept (accounting for slippage tolerance)
        const minOutputAmount = bestRate - (bestRate * slippageTolerance) / 100;

        // Approve the router to spend input tokens (if using ERC-20 tokens)
        const inputTokenContract = new ethers.Contract(inputToken, ERC20_ABI, wallet); // Replace ERC20_ABI with the standard ERC-20 ABI
        const approvalTx = await inputTokenContract.approve(FEG_ROUTER_ADDRESS, inputAmount);
        await approvalTx.wait(); // Wait for the approval transaction to be mined

        // Execute the trade via FEG Router
        const tradeTx = await fegRouter.swapTokens(
            inputToken,
            outputToken,
            inputAmount,
            minOutputAmount,
            wallet.address
        );

        // Wait for the transaction to be mined
        const receipt = await tradeTx.wait();

        // Log the receipt for debugging purposes (optional)
        console.log("Trade executed successfully:", receipt);

        // Return the transaction receipt
        return receipt;
    } catch (error) {
        console.error("Error executing the trade:", error);
        throw new Error("Failed to execute the trade. Please try again.");
    }
}

// Example usage of the functions
(async () => {
    const inputToken = "0xInputTokenAddressHere"; // Replace with the actual input token address
    const outputToken = "0xOutputTokenAddressHere"; // Replace with the actual output token address
    const inputAmount = ethers.utils.parseUnits("1.0", 18); // Replace "1.0" with the amount of tokens to trade
    const slippageTolerance = 1; // Set slippage tolerance (e.g., 1%)

    try {
        // Execute the trade
        const receipt = await executeTrade(inputToken, outputToken, inputAmount, slippageTolerance);
        console.log("Trade completed successfully! Transaction hash:", receipt.transactionHash);
    } catch (error) {
        console.error("An error occurred while executing the trade:", error.message);
    }
})();
```
