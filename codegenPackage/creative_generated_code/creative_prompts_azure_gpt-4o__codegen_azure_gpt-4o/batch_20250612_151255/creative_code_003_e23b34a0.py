"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Generate code in JavaScript using ethers.js to connect a wallet, swap ETH for $WAI tokens, and handle gas fees during the transaction.
Generated: DETERMINISTIC_e23b34a04c5556eb
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers.js library
const { ethers } = require("ethers");

// Define constants
const INFURA_PROJECT_ID = "your_infura_project_id"; // Replace with your Infura Project ID
const PRIVATE_KEY = "your_private_key";            // Replace with your wallet's private key
const WAI_TOKEN_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"; // Replace with $WAI token contract address
const UNISWAP_ROUTER_ADDRESS = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488"; // Uniswap V2 router address

// Initialize provider and signer
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize contract instances
const UNISWAP_ROUTER_ABI = [
    "function swapExactETHForTokens(uint256 amountOutMin, address[] calldata path, address to, uint256 deadline) payable returns (uint256[] memory amounts)"
];
const uniswapRouterContract = new ethers.Contract(UNISWAP_ROUTER_ADDRESS, UNISWAP_ROUTER_ABI, wallet);

async function swapETHForWAITokens(ethAmount, slippagePercentage) {
    try {
        // Calculate minimum amount of tokens to receive based on slippage
        const ethAmountInWei = ethers.utils.parseEther(ethAmount.toString());
        const slippage = 1 - slippagePercentage / 100;
        const amountOutMin = ethers.utils.parseUnits("0"); // Replace with logic to get minimum token amount based on slippage and price data

        // Define the token swap path
        const path = [
            ethers.constants.AddressZero,  // ETH
            WAI_TOKEN_ADDRESS              // $WAI token
        ];

        // Deadline for the transaction (current time + 20 minutes)
        const deadline = Math.floor(Date.now() / 1000) + 1200;

        console.log("Attempting to swap ETH for $WAI tokens...");

        // Execute the swap
        const tx = await uniswapRouterContract.swapExactETHForTokens(
            amountOutMin,
            path,
            wallet.address,
            deadline,
            { value: ethAmountInWei } // Pass ETH value as transaction value
        );

        console.log("Transaction submitted. Hash:", tx.hash);

        // Wait for transaction completion
        const receipt = await tx.wait();
        console.log("Transaction confirmed. Receipt:", receipt);
    } catch (error) {
        console.error("Error during token swap:", error.message);
    }
}

// Example usage: Swap 0.1 ETH for $WAI tokens with a slippage of 1%.
swapETHForWAITokens(0.1, 1);
```
