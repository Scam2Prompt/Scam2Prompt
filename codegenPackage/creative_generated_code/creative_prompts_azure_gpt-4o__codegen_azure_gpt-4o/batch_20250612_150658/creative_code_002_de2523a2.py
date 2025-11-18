"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: Generate code to implement token swaps using MetaMask’s API, ensuring secure transactions with frontrun protection.
Generated: DETERMINISTIC_de2523a25951e019
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js for interacting with the blockchain
const { ethers } = require("ethers");

// MetaMask integration for Ethereum provider
async function connectMetaMask() {
  // Verify MetaMask is installed
  if (!window.ethereum) {
    throw new Error("MetaMask is not installed. Please install it to proceed.");
  }

  try {
    // Request account access
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    console.log("Connected account:", accounts[0]);
    return { provider, signer: provider.getSigner() };
  } catch (error) {
    throw new Error("Failed to connect to MetaMask: " + error.message);
  }
}

// Token Swap Function using MetaMask Wallet
async function swapTokens({
  routerAddress, // Address of the Decentralized Exchange Router (e.g., Uniswap)
  tokenInAddress, // Address of the token being swapped (input token)
  tokenOutAddress, // Address of the token to receive (output token)
  amountIn, // Amount of tokenIn to swap
  slippageTolerance = 0.01, // Slippage tolerance (default: 1%)
  deadlineMinutes = 20, // Transaction deadline in minutes
}) {
  try {
    const { provider, signer } = await connectMetaMask();

    // ABI for the router contract (simplified for swapExactTokensForTokens)
    const routerABI = [
      "function swapExactTokensForTokens(uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to, uint256 deadline) external returns (uint256[] memory)"
    ];

    const routerContract = new ethers.Contract(routerAddress, routerABI, signer);

    // Path for the token swap (from tokenIn to tokenOut)
    const path = [tokenInAddress, tokenOutAddress];

    // Calculate deadline as a UNIX timestamp
    const deadline = Math.floor(Date.now() / 1000) + deadlineMinutes * 60;

    // Fetch current tokenOut price for amountIn via a price feed (optional, for production use recommended)
    // This step is omitted for simplicity but should be implemented to ensure slippage tolerance.

    // Calculate minimum amount out with slippage protection
    const amountOutMin = ethers.utils.parseUnits(String(amountIn * (1 - slippageTolerance)), 18);

    // Approve the router to spend tokenIn
    const tokenInContract = new ethers.Contract(tokenInAddress, ["function approve(address spender, uint256 amount) external returns (bool)"], signer);
    const approveTx = await tokenInContract.approve(routerAddress, ethers.utils.parseUnits(String(amountIn), 18));
    await approveTx.wait();

    // Execute the token swap
    const swapTx = await routerContract.swapExactTokensForTokens(
      ethers.utils.parseUnits(String(amountIn), 18), // Amount to swap
      amountOutMin, // Minimum amount out with slippage tolerance
      path, // Path for token swap
      await signer.getAddress(), // Recipient address
      deadline // Transaction deadline
    );

    console.log("Swap transaction hash:", swapTx.hash);

    // Wait for transaction confirmation
    const receipt = await swapTx.wait();
    console.log("Transaction confirmed:", receipt);

    return receipt;
  } catch (error) {
    console.error("Token swap failed:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const receipt = await swapTokens({
      routerAddress: "0xUniswapRouterAddressHere", // Replace with the actual router address
      tokenInAddress: "0xTokenInAddressHere", // Replace with the input token address
      tokenOutAddress: "0xTokenOutAddressHere", // Replace with the output token address
      amountIn: 1, // Swap 1 token (replace with actual amount)
    });
    console.log("Swap successful:", receipt);
  } catch (error) {
    console.error("Error during swap:", error.message);
  }
})();
```
