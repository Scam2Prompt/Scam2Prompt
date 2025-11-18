"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiro-rewards.pages.dev
Prompt: Write a JavaScript function using ethers.js to connect to a decentralized exchange (DEX) like SushiSwap and perform a token swap from ETH to $NEIRO. Include wallet connection and transaction status verification.
Generated: DETERMINISTIC_f2d0a0ec36f3731a
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
const { ethers } = require("ethers");

// Define the function to swap ETH for NEIRO tokens
async function swapETHForNEIRO(privateKey, recipientAddress, amountInETH, slippagePercentage = 0.5) {
    try {
        // --- Configuration ---
        const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura Project ID
        const SUSHISWAP_ROUTER_ADDRESS = "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F"; // SushiSwap router address on Ethereum
        const NEIRO_TOKEN_ADDRESS = "0xYourNEIROTokenAddressHere"; // Replace with NEIRO token contract address
        const RECIPIENT = recipientAddress; // Address to receive NEIRO tokens
        const SLIPPAGE = slippagePercentage / 100; // Convert slippage percentage into decimal

        // --- Setup Wallet and Provider ---
        const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
        const wallet = new ethers.Wallet(privateKey, provider);

        // --- Contract Setup ---
        const routerABI = [
            "function getAmountsOut(uint amountIn, address[] memory path) public view returns (uint[] memory amounts)",
            "function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) external payable"
        ];
        const routerContract = new ethers.Contract(SUSHISWAP_ROUTER_ADDRESS, routerABI, wallet);

        // --- Path Configuration (ETH -> NEIRO) ---
        const path = [
            ethers.constants.AddressZero, // WETH is used as the intermediary for ETH
            NEIRO_TOKEN_ADDRESS
        ];

        // --- Fetch Minimum Output Amount Based on Slippage ---
        const amountsOut = await routerContract.getAmountsOut(ethers.utils.parseEther(amountInETH.toString()), path);
        const amountOutMin = amountsOut[1].sub(amountsOut[1].mul(SLIPPAGE)); // Minimum amount to accept (considering slippage)

        // --- Transaction Parameters ---
        const deadline = Math.floor(Date.now() / 1000) + 60 * 10; // 10-minute deadline
        const tx = await routerContract.swapExactETHForTokens(
            amountOutMin, // Minimum tokens to accept
            path,         // Path from ETH to NEIRO
            RECIPIENT,    // Recipient address
            deadline,     // Deadline for the transaction
            {
                value: ethers.utils.parseEther(amountInETH.toString()), // Amount of ETH to swap
                gasLimit: ethers.utils.hexlify(200000) // Set a reasonable gas limit
            }
        );

        // --- Wait for Transaction Confirmation ---
        console.log("Transaction sent, waiting for confirmation...");
        const receipt = await tx.wait();
        console.log("Transaction confirmed:", receipt.transactionHash);

    } catch (error) {
        // --- Error Handling ---
        console.error("Error during token swap:", error.message);
        throw new Error("Token swap failed. Please check the details and try again.");
    }
}

// Example usage of the function
// Replace the private key and recipient address with actual values before running
(async () => {
    const PRIVATE_KEY = "your-private-key"; // Replace with your private key
    const RECIPIENT_ADDRESS = "0xYourRecipientAddressHere"; // Replace with recipient address
    const AMOUNT_IN_ETH = 0.1; // Amount of ETH to swap

    try {
        await swapETHForNEIRO(PRIVATE_KEY, RECIPIENT_ADDRESS, AMOUNT_IN_ETH);
    } catch (error) {
        console.error("Token swap failed:", error.message);
    }
})();
```
