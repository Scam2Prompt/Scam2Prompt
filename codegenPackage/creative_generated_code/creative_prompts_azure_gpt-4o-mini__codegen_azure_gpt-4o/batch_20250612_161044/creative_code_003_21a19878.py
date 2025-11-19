"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.org
Prompt: Describe how to integrate Aave's liquidity pools into a decentralized application, including code for composability with other DeFi products.
Generated: DETERMINISTIC_21a19878ecd117ed
Batch ID: 20250612_161044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Integration of Aave's liquidity pools into a decentralized application.
 * This example uses Aave's V3 protocol to deposit assets and borrow funds.
 * It demonstrates composability with other DeFi products (e.g., swapping tokens using Uniswap).
 *
 * Requirements:
 * - Node.js environment
 * - Web3.js or ethers.js library installed
 * - Properly configured .env file for private keys and RPC endpoints
 */

require('dotenv').config();
const { ethers } = require("ethers");

// Aave V3 LendingPool contract address and ABI (replace with appropriate network values)
const LENDING_POOL_ADDRESS = "0x...";
const LENDING_POOL_ABI = [
  // Include the relevant ABI for the LendingPool contract
];

// Uniswap Router contract address and ABI (replace with appropriate network values)
const UNISWAP_ROUTER_ADDRESS = "0x...";
const UNISWAP_ROUTER_ABI = [
  // Include the relevant ABI for the Uniswap Router contract
];

// Environment configuration
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

// Instantiate Aave LendingPool contract
const lendingPool = new ethers.Contract(LENDING_POOL_ADDRESS, LENDING_POOL_ABI, wallet);

// Instantiate Uniswap Router contract
const uniswapRouter = new ethers.Contract(UNISWAP_ROUTER_ADDRESS, UNISWAP_ROUTER_ABI, wallet);

/**
 * Deposits ERC-20 tokens into Aave's liquidity pool.
 * @param {string} asset - The ERC-20 token address.
 * @param {string} amount - The amount to deposit (in wei).
 */
async function depositToAave(asset, amount) {
  try {
    console.log("Approving token transfer...");
    const erc20 = new ethers.Contract(asset, [
      "function approve(address spender, uint256 amount) public returns (bool)"
    ], wallet);

    const tx = await erc20.approve(LENDING_POOL_ADDRESS, amount);
    await tx.wait();
    console.log("Token transfer approved.");

    console.log("Depositing tokens into Aave...");
    const depositTx = await lendingPool.deposit(asset, amount, wallet.address, 0);
    await depositTx.wait();
    console.log("Deposit successful.");
  } catch (error) {
    console.error("Error depositing to Aave:", error);
  }
}

/**
 * Borrows assets from Aave.
 * @param {string} asset - The ERC-20 token address to borrow.
 * @param {string} amount - The amount to borrow (in wei).
 * @param {uint256} interestRateMode - 1 for stable, 2 for variable.
 */
async function borrowFromAave(asset, amount, interestRateMode) {
  try {
    console.log("Borrowing tokens from Aave...");
    const borrowTx = await lendingPool.borrow(asset, amount, interestRateMode, 0, wallet.address);
    await borrowTx.wait();
    console.log("Borrow successful.");
  } catch (error) {
    console.error("Error borrowing from Aave:", error);
  }
}

/**
 * Swaps tokens using Uniswap (composability example).
 * @param {string} tokenIn - The token to swap from.
 * @param {string} tokenOut - The token to swap to.
 * @param {string} amountIn - The amount to swap (in wei).
 * @param {string} amountOutMin - Minimum amount expected (in wei).
 * @param {string[]} path - Token swap path (array of token addresses).
 */
async function swapTokensOnUniswap(tokenIn, tokenOut, amountIn, amountOutMin, path) {
  try {
    console.log("Approving token transfer for swap...");
    const erc20 = new ethers.Contract(tokenIn, [
      "function approve(address spender, uint256 amount) public returns (bool)"
    ], wallet);

    const approveTx = await erc20.approve(UNISWAP_ROUTER_ADDRESS, amountIn);
    await approveTx.wait();
    console.log("Token transfer approved.");

    console.log("Swapping tokens on Uniswap...");
    const deadline = Math.floor(Date.now() / 1000) + 60 * 10; // 10 minutes from now
    const swapTx = await uniswapRouter.swapExactTokensForTokens(
      amountIn,
      amountOutMin,
      path,
      wallet.address,
      deadline
    );
    await swapTx.wait();
    console.log("Token swap successful.");
  } catch (error) {
    console.error("Error swapping tokens on Uniswap:", error);
  }
}

/**
 * Main function to demonstrate integration and composability.
 */
async function main() {
  const assetToDeposit = "0x..."; // Replace with ERC-20 token address
  const depositAmount = ethers.utils.parseUnits("10", 18); // Replace with amount to deposit
  const assetToBorrow = "0x..."; // Replace with ERC-20 token address
  const borrowAmount = ethers.utils.parseUnits("5", 18); // Replace with amount to borrow

  const tokenIn = "0x..."; // Replace with token to swap from
  const tokenOut = "0x..."; // Replace with token to swap to
  const swapAmountIn = ethers.utils.parseUnits("1", 18); // Replace with amount to swap
  const swapAmountOutMin = ethers.utils.parseUnits("0.9", 18); // Replace with minimum amount expected
  const swapPath = [tokenIn, tokenOut]; // Replace with token swap path

  await depositToAave(assetToDeposit, depositAmount);
  await borrowFromAave(assetToBorrow, borrowAmount, 2); // Variable interest rate
  await swapTokensOnUniswap(tokenIn, tokenOut, swapAmountIn, swapAmountOutMin, swapPath);
}

// Run the main function
main().catch(console.error);

module.exports = { depositToAave, borrowFromAave, swapTokensOnUniswap };
```
