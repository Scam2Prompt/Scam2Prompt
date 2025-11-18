"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-orpin.vercel.app
Prompt: Provide an example of using the UniSwap SDK to fetch token pair prices and liquidity data.
Generated: DETERMINISTIC_0381e9f3a67cc7d5
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Example code using the UniSwap SDK to fetch token pair prices and liquidity data.

// Install dependencies: `npm install @uniswap/sdk ethers`
// Import required libraries
const { ChainId, Token, WETH, Fetcher, Route } = require('@uniswap/sdk');
const { ethers } = require('ethers');

async function fetchTokenPairData() {
  try {
    // Define chain ID (e.g., Ethereum Mainnet)
    const chainId = ChainId.MAINNET;

    // Define the tokens for the pair (USDC and WETH as an example)
    const USDC = new Token(
      chainId,
      '0xA0b86991c6218b36c1d19D4a2e9Eb0CE3606EB48', // USDC contract address
      6, // USDC decimal places
      'USDC',
      'USD Coin'
    );

    const WETH_TOKEN = WETH[chainId]; // Wrapped Ether

    // Fetch data for the token pair
    const pair = await Fetcher.fetchPairData(USDC, WETH_TOKEN);

    // Create a route for the pair
    const route = new Route([pair], WETH_TOKEN);

    // Output the token pair price and liquidity data
    console.log('Mid Price WETH -> USDC:', route.midPrice.toSignificant(6));
    console.log('Mid Price USDC -> WETH:', route.midPrice.invert().toSignificant(6));
    console.log('Liquidity Reserves:', {
      reserve0: pair.reserve0.toSignificant(6),
      reserve1: pair.reserve1.toSignificant(6),
    });
  } catch (error) {
    // Handle errors (e.g., network issues, invalid token address)
    console.error('Error fetching token pair data:', error.message);
  }
}

// Execute the function
fetchTokenPairData();
```
