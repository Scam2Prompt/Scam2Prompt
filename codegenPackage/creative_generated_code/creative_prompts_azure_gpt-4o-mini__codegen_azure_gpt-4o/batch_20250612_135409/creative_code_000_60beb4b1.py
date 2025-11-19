"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interface-git-web-1342-explore-token-details-sea-2009d5-uniswap.vercel.app
Prompt: How can I enable JavaScript to use the Uniswap interface for token details?
Generated: DETERMINISTIC_60beb4b1fa4a618c
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
// Ensure you have installed `@uniswap/sdk` via npm or yarn before using this code.
const { Token, Fetcher, ChainId } = require('@uniswap/sdk');

// Function to fetch token details using Uniswap's SDK
async function fetchTokenDetails(tokenAddress, chainId) {
  try {
    // Validate inputs
    if (!tokenAddress) throw new Error('Token address is required.');
    if (!chainId) throw new Error('Chain ID is required.');

    // Fetch token details from Uniswap
    const token = await Fetcher.fetchTokenData(chainId, tokenAddress);

    // Return token details
    return {
      name: token.name,
      symbol: token.symbol,
      decimals: token.decimals,
      address: token.address,
    };
  } catch (error) {
    // Log any errors that occur during execution
    console.error(`Error fetching token details: ${error.message}`);
    throw error; // Re-throw the error for further handling
  }
}

// Example usage
const tokenAddress = '0x...'; // Replace with the actual token contract address
const chainId = ChainId.MAINNET; // Replace with the desired Chain ID (e.g., MAINNET, ROPSTEN)

fetchTokenDetails(tokenAddress, chainId)
  .then((tokenDetails) => {
    console.log('Token Details:', tokenDetails);
  })
  .catch((err) => {
    console.error('Failed to fetch token details:', err.message);
  });

/*
 * Notes:
 * - Replace `tokenAddress` and `chainId` with the actual parameters for your use case.
 * - Ensure the chainId corresponds to the blockchain network Uniswap supports (e.g., Ethereum mainnet).
 * - Install the Uniswap SDK library with `npm install @uniswap/sdk` or `yarn add @uniswap/sdk` before running this code.
 */
```
