"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapv2-ui.vercel.app
Prompt: Write code to integrate Mantle Swap's token swap functionality into a custom web application using the Uniswap V2 protocol as a reference.
Generated: DETERMINISTIC_6325a628e2cb0ca1
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from "web3"; // Web3.js library for blockchain interactions
import { ethers } from "ethers"; // Ethers.js library for wallet and contract interactions

// Uniswap V2 Router ABI (simplified for demonstration purposes)
const UNISWAP_V2_ROUTER_ABI = [
  {
    "name": "swapExactTokensForTokens",
    "type": "function",
    "inputs": [
      { "type": "uint256", "name": "amountIn" },
      { "type": "uint256", "name": "amountOutMin" },
      { "type": "address[]", "name": "path" },
      { "type": "address", "name": "to" },
      { "type": "uint256", "name": "deadline" },
    ],
    "outputs": [{ "type": "uint256[]", "name": "amounts" }],
  },
];

// Mantle Swap Router Contract Address (replace with actual contract address)
const MANTLE_SWAP_ROUTER_ADDRESS = "0xYourMantleSwapRouterAddress";

// Initialize Web3 Instance
const web3 = new Web3(window.ethereum); // Using MetaMask provider

// Function to perform token swap
async function mantleTokenSwap({
  privateKey,
  inputTokenAddress,
  outputTokenAddress,
  amountIn,
  amountOutMin,
  recipientAddress,
  deadline,
}) {
  try {
    // Validate inputs
    if (
      !privateKey ||
      !inputTokenAddress ||
      !outputTokenAddress ||
      !amountIn ||
      !amountOutMin ||
      !recipientAddress ||
      !deadline
    ) {
      throw new Error("Missing required parameters for token swap.");
    }

    // Initialize wallet instance
    const wallet = new ethers.Wallet(privateKey, new ethers.providers.Web3Provider(window.ethereum));

    // Initialize contract instance
    const mantleSwapRouterContract = new ethers.Contract(
      MANTLE_SWAP_ROUTER_ADDRESS,
      UNISWAP_V2_ROUTER_ABI,
      wallet
    );

    // Approve input token for Mantle Swap Router (ensure token contract supports ERC-20 approve function)
    const tokenContract = new ethers.Contract(
      inputTokenAddress,
      [
        {
          name: "approve",
          type: "function",
          inputs: [
            { type: "address", name: "spender" },
            { type: "uint256", name: "value" },
          ],
          outputs: [{ type: "bool", name: "success" }],
        },
      ],
      wallet
    );
    const approveTx = await tokenContract.approve(MANTLE_SWAP_ROUTER_ADDRESS, amountIn);
    await approveTx.wait();

    // Prepare the token swap path (input token -> output token)
    const path = [inputTokenAddress, outputTokenAddress];

    // Perform the token swap
    const swapTx = await mantleSwapRouterContract.swapExactTokensForTokens(
      amountIn, // Amount of input tokens
      amountOutMin, // Minimum acceptable amount of output tokens
      path, // Token swap path
      recipientAddress, // Recipient's wallet address
      deadline // Transaction deadline (timestamp)
    );

    // Wait for transaction confirmation
    const receipt = await swapTx.wait();

    console.log("Swap successful:", receipt);
    return receipt;
  } catch (error) {
    console.error("Error during token swap:", error.message);
    throw error; // Rethrow error for higher-level handling
  }
}

// Example usage
(async () => {
  try {
    // Replace with actual values
    const privateKey = "0xYourPrivateKey";
    const inputTokenAddress = "0xInputTokenAddress";
    const outputTokenAddress = "0xOutputTokenAddress";
    const amountIn = ethers.utils.parseUnits("1", "18"); // Input token amount (e.g., 1 token, 18 decimals)
    const amountOutMin = ethers.utils.parseUnits("0.9", "18"); // Minimum output token amount (e.g., 0.9 tokens)
    const recipientAddress = "0xRecipientAddress"; // Recipient's wallet address
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now

    const swapReceipt = await mantleTokenSwap({
      privateKey,
      inputTokenAddress,
      outputTokenAddress,
      amountIn,
      amountOutMin,
      recipientAddress,
      deadline,
    });

    console.log("Swap transaction receipt:", swapReceipt);
  } catch (error) {
    console.error("Swap failed:", error.message);
  }
})();
```
