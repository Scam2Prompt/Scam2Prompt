"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wiener.pages.dev
Prompt: Write a script using ethers.js to calculate the gas fees required for swapping tokens for $WAI during the presale.
Generated: DETERMINISTIC_35729115e808ae49
Batch ID: 20250612_152240
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

// Define the main function to calculate gas fees for swapping tokens for $WAI
async function calculateGasFees() {
    // Provider and wallet setup
    const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");
    const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

    // Token addresses (example addresses, replace with actual ones)
    const tokenAddress = "0xYourTokenAddress"; // The token you are swapping from
    const WAIAddress = "0xYourWAIAddress"; // The $WAI token address

    // Uniswap Router Contract Address (example address, replace with actual one)
    const uniswapRouterAddress = "0xYourUniswapRouterAddress";
    const routerABI = [
        // Simplified ABI to fetch estimates, include only required methods
        "function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts)",
        "function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory amounts)"
    ];
    
    // Create the Uniswap Router contract instance
    const uniswapRouterContract = new ethers.Contract(uniswapRouterAddress, routerABI, wallet);

    // Define the amount of tokens to swap (in wei)
    const amountIn = ethers.utils.parseUnits("1.0", 18); // Example: 1 token with 18 decimals

    // Define the path for the swap (Token to WAI)
    const path = [tokenAddress, WAIAddress];

    try {
        // Estimate gas for the swap
        const gasEstimate = await uniswapRouterContract.estimateGas.swapExactTokensForTokens(
            amountIn,
            0, // Setting amountOutMin to 0 for gas estimation; adjust as needed in production
            path,
            wallet.address,
            Math.floor(Date.now() / 1000) + 60 * 20 // Set deadline for 20 minutes
        );

        // Fetch current gas price
        const gasPrice = await provider.getGasPrice();

        // Calculate total gas fee
        const totalGasFee = gasEstimate.mul(gasPrice);

        console.log(`Estimated Gas Fee: ${ethers.utils.formatEther(totalGasFee)} ETH`);
    } catch (error) {
        console.error("Error estimating gas fees:", error);
    }
}

// Call the main function
calculateGasFees();
```

**Note:** Remember to replace `"YOUR_INFURA_PROJECT_ID"`, `"YOUR_PRIVATE_KEY"`, `"0xYourTokenAddress"`, `"0xYourWAIAddress"`, and `"0xYourUniswapRouterAddress"` with your actual values before running the script. This code assumes you have the necessary permissions and that the token contract allows for token swaps.
