"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorchain.pages.dev
Prompt: Create a JavaScript function using the `XChainJS` library to query THORChain liquidity pools and retrieve data about available swap routes for Bitcoin and stablecoins.
Generated: DETERMINISTIC_3f62aef805398727
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the xchain-thorchain library
const { Client } = require('@xchainjs/xchain-thorchain');
const { Network } = require('@xchainjs/xchain-client');

/**
 * Function to retrieve swap routes for Bitcoin and stablecoins from THORChain liquidity pools.
 * @returns {Promise<Object>} Returns an object containing available swap routes or an error message.
 */
async function getSwapRoutes() {
  try {
    // Initialize the THORChain client
    const thorchainClient = new Client({ network: Network.Mainnet });

    // Fetch liquidity pool data
    const pools = await thorchainClient.getPools();

    // Filter pools for Bitcoin and stablecoins
    const bitcoinPools = pools.filter(pool => pool.asset.includes('BTC'));
    const stablecoinPools = pools.filter(
      pool => pool.asset.includes('USDT') || pool.asset.includes('USDC')
    );

    // Generate swap routes between Bitcoin and stablecoin pools
    const swapRoutes = [];
    bitcoinPools.forEach(btcPool => {
      stablecoinPools.forEach(stablecoinPool => {
        swapRoutes.push({
          from: btcPool.asset,
          to: stablecoinPool.asset,
        });
      });
    });

    // Return the generated swap routes
    return swapRoutes;
  } catch (error) {
    // Handle and log errors
    console.error('Error fetching swap routes:', error.message || error);
    return { error: 'Failed to fetch swap routes. Please try again later.' };
  }
}

// Example usage of the function
getSwapRoutes()
  .then(routes => console.log('Available Swap Routes:', routes))
  .catch(err => console.error('Unexpected Error:', err));
```
