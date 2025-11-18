"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-v3-exchange.vercel.app
Prompt: Write a script to automate token swaps on Uniswap V3 using ethers.js, including error handling for failed transactions.
Generated: DETERMINISTIC_29ef90828be7d779
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { ethers } = require("ethers");
require("dotenv").config(); // For managing environment variables

// Define constants and configuration
const INFURA_URL = process.env.INFURA_URL; // Infura endpoint URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the wallet
const UNISWAP_ROUTER_ADDRESS = "0xE592427A0AEce92De3Edee1F18E0157C05861564"; // Uniswap V3 Router
const UNISWAP_ROUTER_ABI = require("./uniswapV3RouterAbi.json"); // Import Uniswap V3 Router ABI

const TOKEN_IN = "0xA0b86991c6218b36c1d19d4a2e9Eb0CE3606EB48"; // USDC address
const TOKEN_OUT = "0xC02aaA39b223FE8D0A0E5C4F27eAD9083C756Cc2"; // WETH address
const AMOUNT_IN = ethers.utils.parseUnits("500", 6); // Amount of USDC to swap (500 USDC)
const SLIPPAGE_TOLERANCE = 0.005; // 0.5% slippage tolerance

// Initialize ethers provider and signer
const provider = new ethers.providers.JsonRpcProvider(INFURA_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize Uniswap router contract
const uniswapRouter = new ethers.Contract(
  UNISWAP_ROUTER_ADDRESS,
  UNISWAP_ROUTER_ABI,
  wallet
);

// Main function for the token swap
async function swapTokens() {
  try {
    // Fetch current block timestamp for deadline
    const block = await provider.getBlock("latest");
    const deadline = block.timestamp + 60 * 5; // Set deadline to 5 minutes from now

    // Fetch token pair pool price for calculation (optional step for slippage protection)
    const amountOutMin = await getEstimatedAmountOut(AMOUNT_IN);
    const amountOutMinWithSlippage = amountOutMin.mul(
      ethers.BigNumber.from((1 - SLIPPAGE_TOLERANCE) * 10000).toString()
    ).div(10000); // Adjust for slippage tolerance

    // Build parameters for the swap
    const params = {
      tokenIn: TOKEN_IN,
      tokenOut: TOKEN_OUT,
      fee: 3000, // Uniswap V3 pool fee (0.30%)
      recipient: wallet.address,
      deadline: deadline,
      amountIn: AMOUNT_IN,
      amountOutMinimum: amountOutMinWithSlippage,
      sqrtPriceLimitX96: 0 // No price limit
    };

    // Approve token transfer to Uniswap router
    const tokenInContract = new ethers.Contract(
      TOKEN_IN,
      ["function approve(address spender, uint256 amount) public returns (bool)"],
      wallet
    );
    const approveTx = await tokenInContract.approve(
      UNISWAP_ROUTER_ADDRESS,
      AMOUNT_IN
    );
    console.log("Approving token transfer...");
    await approveTx.wait();

    // Execute the swap
    console.log("Swapping tokens...");
    const swapTx = await uniswapRouter.exactInputSingle(params);
    const receipt = await swapTx.wait();
    console.log("Swap successful:", receipt);

  } catch (error) {
    console.error("Error occurred during token swap:", error.message);
  }
}

// Helper function to estimate amount out
async function getEstimatedAmountOut(amountIn) {
  try {
    const quoteParams = {
      tokenIn: TOKEN_IN,
      tokenOut: TOKEN_OUT,
      fee: 3000,
      amountIn: amountIn,
      sqrtPriceLimitX96: 0
    };
    const amountOut = await uniswapRouter.callStatic.quoteExactInputSingle(
      quoteParams.tokenIn,
      quoteParams.tokenOut,
      quoteParams.fee,
      quoteParams.amountIn,
      quoteParams.sqrtPriceLimitX96
    );
    return amountOut;
  } catch (error) {
    throw new Error("Failed to fetch estimated output amount: " + error.message);
  }
}

// Execute the script
swapTokens();
```

**Note:**  
- Be sure to replace environment variables (`INFURA_URL`, `PRIVATE_KEY`) with your actual values.  
- Ensure the `uniswapV3RouterAbi.json` file contains the ABI for the Uniswap V3 router contract.  
- Tokens and amounts in this script are examples and may need to be adjusted based on your requirements.
