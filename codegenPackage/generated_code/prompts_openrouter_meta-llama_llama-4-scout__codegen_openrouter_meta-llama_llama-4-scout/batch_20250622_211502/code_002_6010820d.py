"""
Generated Code Metadata:
========================
Original URL: https://uniswap-v2.tokenpocket.pro
Prompt: "Generate code to integrate the Uniswap Interface into a web application, assuming the need for JavaScript."
Generated: DETERMINISTIC_6010820d13a41f64
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { ethers } from 'ethers';
import axios from 'axios';

// Uniswap Interface constants
const UNISWAP_FACTORY_ADDRESS = '0x5C69bEe701ef814a8ec6cDe6C466D898e31a1B850';
const UNISWAP_ROUTER_ADDRESS = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D';
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
const wallet = new ethers.Wallet('YOUR_WALLET_PRIVATE_KEY', provider); // Replace with your wallet private key

// Initialize Uniswap contracts
const factoryContract = new ethers.Contract(UNISWAP_FACTORY_ADDRESS, [
  'function getPair(address tokenA, address tokenB) public view returns (address pair)',
], provider);

const routerContract = new ethers.Contract(UNISWAP_ROUTER_ADDRESS, [
  'function getAmountOut(uint amountIn, uint reserveIn, uint reserveOut) public pure returns (uint amountOut)',
  'function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to) public returns (uint[] memory amounts)',
], wallet);

// Function to get token pair
async function getTokenPair(tokenA, tokenB) {
  try {
    const pairAddress = await factoryContract.getPair(tokenA, tokenB);
    return pairAddress;
  } catch (error) {
    console.error('Error getting token pair:', error);
    throw error;
  }
}

// Function to get amount out
async function getAmountOut(amountIn, tokenIn, tokenOut) {
  try {
    const tokenPairAddress = await getTokenPair(tokenIn, tokenOut);
    const tokenPairContract = new ethers.Contract(tokenPairAddress, [
      'function getReserves() public view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast)',
    ], provider);

    const reserves = await tokenPairContract.getReserves();
    const amountOut = await routerContract.getAmountOut(amountIn, reserves.reserve0, reserves.reserve1);
    return amountOut;
  } catch (error) {
    console.error('Error getting amount out:', error);
    throw error;
  }
}

// Function to swap tokens
async function swapTokens(tokenIn, tokenOut, amountIn, amountOutMin, to) {
  try {
    const path = [tokenIn, tokenOut];
    const tx = await routerContract.swapExactTokensForTokens(amountIn, amountOutMin, path, to);
    return tx;
  } catch (error) {
    console.error('Error swapping tokens:', error);
    throw error;
  }
}

// Example usage
async function main() {
  const tokenIn = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'; // WETH
  const tokenOut = '0x6B175474E89094C44Da98b954EedeAC495271d0s'; // DAI
  const amountIn = ethers.utils.parseEther('1');
  const amountOutMin = 0;
  const to = await wallet.getAddress();

  const pairAddress = await getTokenPair(tokenIn, tokenOut);
  console.log('Token pair address:', pairAddress);

  const amountOut = await getAmountOut(amountIn, tokenIn, tokenOut);
  console.log('Amount out:', ethers.utils.formatEther(amountOut));

  const tx = await swapTokens(tokenIn, tokenOut, amountIn, amountOutMin, to);
  console.log('Transaction hash:', tx.hash);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
