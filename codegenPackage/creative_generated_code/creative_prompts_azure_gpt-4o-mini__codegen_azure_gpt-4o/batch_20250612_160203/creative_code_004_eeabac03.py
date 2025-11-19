"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://susongdcity.cn
Prompt: Generate a code snippet that demonstrates how to swap assets on a decentralized exchange using Coinbase Wallet.
Generated: DETERMINISTIC_eeabac03487a7a87
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script demonstrates how to swap assets on a decentralized exchange using Coinbase Wallet.
 * It uses ethers.js for interacting with Ethereum-based smart contracts and assumes the user has
 * a Coinbase Wallet connected. Update the contract address, token details, and amounts accordingly.
 */

// Import required dependencies
const { ethers } = require("ethers");

// Constants
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura project ID
const UNISWAP_ROUTER_ADDRESS = "0xE592427A0AEce92De3Edee1F18E0157C05861564"; // Example: Uniswap V3 Router address
const TOKEN_IN_ADDRESS = "0x..."; // Replace with the address of the token you want to swap from
const TOKEN_OUT_ADDRESS = "0x..."; // Replace with the address of the token you want to swap to
const AMOUNT_IN = ethers.utils.parseUnits("1", 18); // Replace "1" with the amount of TOKEN_IN you want to swap
const SLIPPAGE = 0.005; // Slippage tolerance (0.5%)

async function swapTokens() {
  try {
    // Connect to Ethereum provider using Coinbase Wallet
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Prompt user to connect their Coinbase Wallet
    await provider.send("eth_requestAccounts", []);

    const signer = provider.getSigner();

    // ABI for Uniswap V3's swapExactInputSingle function
    const uniswapRouterABI = [
      "function exactInputSingle((address,address,uint24,address,uint256,uint256,uint160)) external payable returns (uint256)"
    ];

    const uniswapRouterContract = new ethers.Contract(
      UNISWAP_ROUTER_ADDRESS,
      uniswapRouterABI,
      signer
    );

    // Fetch token decimals for proper calculations
    const tokenInContract = new ethers.Contract(
      TOKEN_IN_ADDRESS,
      ["function decimals() view returns (uint8)"],
      provider
    );

    const tokenOutContract = new ethers.Contract(
      TOKEN_OUT_ADDRESS,
      ["function decimals() view returns (uint8)"],
      provider
    );

    const tokenInDecimals = await tokenInContract.decimals();
    const tokenOutDecimals = await tokenOutContract.decimals();

    // Calculate minimum amount out based on slippage tolerance
    const amountOutMinimum = ethers.utils.parseUnits(
      (1 - SLIPPAGE).toFixed(tokenOutDecimals),
      tokenOutDecimals
    );

    // Approve the router to spend TOKEN_IN
    const tokenInApproveABI = ["function approve(address spender, uint256 amount)"];
    const tokenInContractWithSigner = new ethers.Contract(
      TOKEN_IN_ADDRESS,
      tokenInApproveABI,
      signer
    );

    const approvalTx = await tokenInContractWithSigner.approve(
      UNISWAP_ROUTER_ADDRESS,
      AMOUNT_IN
    );
    await approvalTx.wait();

    console.log("Token approval successful");

    // Define swap parameters
    const swapParams = {
      tokenIn: TOKEN_IN_ADDRESS,
      tokenOut: TOKEN_OUT_ADDRESS,
      fee: 3000, // Pool fee (e.g., 0.3%)
      recipient: await signer.getAddress(),
      deadline: Math.floor(Date.now() / 1000) + 60 * 10, // Deadline (10 minutes from now)
      amountIn: AMOUNT_IN,
      amountOutMinimum: amountOutMinimum,
      sqrtPriceLimitX96: 0 // No price limit
    };

    // Execute the swap
    const swapTx = await uniswapRouterContract.exactInputSingle(swapParams);
    const receipt = await swapTx.wait();

    console.log("Swap successful:", receipt);
  } catch (error) {
    console.error("Error swapping tokens:", error);
  }
}

// Execute the function
swapTokens();
```

**Note**: Replace placeholder values like `INFURA_PROJECT_ID`, token addresses, and amounts with actual values. Ensure the user has sufficient funds and the wallet is connected properly before executing.
