"""
Generated Code Metadata:
========================
Original URL: https://degentip-9l3.pages.dev
Prompt: Provide an example of how to use GeckoTerminal to analyze the performance of the DEGEN/WETH liquidity pools on the Degen L3 chain.
Generated: DETERMINISTIC_64226e1e49441bba
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Geckoterminal } = require('@geckoterminal/geckoterminal-sdk');
const axios = require('axios');

// Set up Geckoterminal API credentials
const apiKey = 'YOUR_GECKOTERMINAL_API_KEY';
const geckoterminal = new Geckoterminal(apiKey);

// Define constants for the Degen L3 chain and DEGEN/WETH liquidity pool
const chainId = 324;
const dexId = '0x4f2a'; // Replace with actual DEX ID for DEGEN/WETH pool
const token0 = 'DEGEN';
const token1 = 'WETH';

// Function to get pool data
async function getPoolData(chainId, dexId) {
  try {
    const response = await geckoterminal.getPool({
      chainId,
      dexId,
      poolId: `${token0}/${token1}`,
    });
    return response.data;
  } catch (error) {
    console.error(`Error fetching pool data: ${error.message}`);
    throw error;
  }
}

// Function to analyze pool performance
async function analyzePoolPerformance(chainId, dexId) {
  try {
    const poolData = await getPoolData(chainId, dexId);
    const tvl = poolData.tvl;
    const apy = poolData.apy;
    const volume = poolData.volume;

    console.log(`TVL: $${tvl}`);
    console.log(`APY: ${apy}%`);
    console.log(`24h Volume: $${volume}`);

    // Additional analysis can be performed here
  } catch (error) {
    console.error(`Error analyzing pool performance: ${error.message}`);
  }
}

// Main function
async function main() {
  try {
    await analyzePoolPerformance(chainId, dexId);
  } catch (error) {
    console.error(`Error in main function: ${error.message}`);
    process.exit(1);
  }
}

// Run the main function
main();
```
