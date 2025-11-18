"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-v3-exchange.vercel.app
Prompt: Provide an example of how to use Uniswap V3's SDK to fetch current token prices and liquidity pool data.
Generated: DETERMINISTIC_98d389c7225754dd
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from the Uniswap V3 SDK and ethers.js
import { ChainId, Token, TokenAmount, Pair, Fetcher } from '@uniswap/v3-sdk';
import { ethers } from 'ethers';

/**
 * Function to fetch current token prices and liquidity pool data for a given pair of tokens.
 * @param {string} tokenAddressA - The address of the first token.
 * @param {string} tokenAddressB - The address of the second token.
 * @param {number} chainId - The chain ID for the network (e.g., 1 for Ethereum mainnet).
 */
async function fetchTokenPricesAndLiquidity(tokenAddressA, tokenAddressB, chainId = ChainId.Mainnet) {
    try {
        // Initialize provider (using ethers.js to connect to Ethereum network)
        const provider = new ethers.providers.InfuraProvider(chainId, 'YOUR_INFURA_PROJECT_ID');

        // Fetch the token data for the given addresses
        const tokenA = await Fetcher.fetchTokenData(chainId, tokenAddressA);
        const tokenB = await Fetcher.fetchTokenData(chainId, tokenAddressB);

        // Fetch the pair details (liquidity pool data) for the token pair
        const pair = await Fetcher.fetchPairData(tokenA, tokenB, provider);
        
        // Calculate price and liquidity
        const price = pair.token0Price.toSignificant(6); // Price of token A in terms of token B
        const liquidity = pair.getLiquidityAmount().toFixed(); // Total liquidity in the pool

        // Output the results
        console.log(`Current price of ${tokenA.symbol} in terms of ${tokenB.symbol}: ${price}`);
        console.log(`Total liquidity in the ${tokenA.symbol}/${tokenB.symbol} pool: ${liquidity}`);
    } catch (error) {
        // Handle errors gracefully
        console.error('Error fetching token prices and liquidity:', error);
    }
}

// Replace with actual token addresses and call the function to fetch data
const TOKEN_ADDRESS_A = '0x...'; // Replace with the first token address
const TOKEN_ADDRESS_B = '0x...'; // Replace with the second token address
fetchTokenPricesAndLiquidity(TOKEN_ADDRESS_A, TOKEN_ADDRESS_B);
```

Make sure to replace `'YOUR_INFURA_PROJECT_ID'`, `TOKEN_ADDRESS_A`, and `TOKEN_ADDRESS_B` with actual values before running the code.
