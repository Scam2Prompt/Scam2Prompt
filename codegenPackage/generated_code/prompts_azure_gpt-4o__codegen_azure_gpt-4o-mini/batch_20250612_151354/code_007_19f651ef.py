"""
Generated Code Metadata:
========================
Original URL: https://web-5moo1kdt8-uniswap.vercel.app
Prompt: Provide an example of using Web3.js or ethers.js to interact with Uniswap's smart contracts for token swaps.
Generated: DETERMINISTIC_19f651efdb3742b4
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// Define constants
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura project ID
const WALLET_PRIVATE_KEY = "YOUR_WALLET_PRIVATE_KEY"; // Replace with your wallet's private key
const UNISWAP_ROUTER_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"; // Uniswap V2 Router address
const TOKEN_A_ADDRESS = "0xTOKEN_A_ADDRESS"; // Replace with the address of Token A
const TOKEN_B_ADDRESS = "0xTOKEN_B_ADDRESS"; // Replace with the address of Token B
const AMOUNT_IN = ethers.utils.parseUnits("1.0", 18); // Amount of Token A to swap (1.0 Token A)

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(WALLET_PRIVATE_KEY, provider);

// Create Uniswap Router contract instance
const uniswapRouterABI = [
    "function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory amounts)",
    "function approve(address spender, uint value) external returns (bool)"
];
const uniswapRouter = new ethers.Contract(UNISWAP_ROUTER_ADDRESS, uniswapRouterABI, wallet);

// Function to swap tokens
async function swapTokens() {
    try {
        // Approve the Uniswap Router to spend Token A
        const tokenAContract = new ethers.Contract(TOKEN_A_ADDRESS, ["function approve(address spender, uint value) external returns (bool)"], wallet);
        const approvalTx = await tokenAContract.approve(UNISWAP_ROUTER_ADDRESS, AMOUNT_IN);
        await approvalTx.wait(); // Wait for the transaction to be mined
        console.log("Token A approved for Uniswap Router");

        // Define the path for the swap (Token A -> Token B)
        const path = [TOKEN_A_ADDRESS, TOKEN_B_ADDRESS];
        const amountOutMin = 0; // Set minimum amount of Token B to receive (0 for simplicity)
        const to = wallet.address; // Address to receive Token B
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // Transaction deadline (20 minutes from now)

        // Execute the swap
        const swapTx = await uniswapRouter.swapExactTokensForTokens(AMOUNT_IN, amountOutMin, path, to, deadline);
        await swapTx.wait(); // Wait for the transaction to be mined
        console.log("Swap executed successfully:", swapTx.hash);
    } catch (error) {
        console.error("Error during token swap:", error);
    }
}

// Execute the swap function
swapTokens();
```

**Note:** Make sure to replace `YOUR_INFURA_PROJECT_ID`, `YOUR_WALLET_PRIVATE_KEY`, `0xTOKEN_A_ADDRESS`, and `0xTOKEN_B_ADDRESS` with actual values before running the code.
