"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-blockchain-webapp.vercel.app
Prompt: Provide an example of interacting with Uniswap's smart contracts to retrieve pool data and display it in a web app.
Generated: DETERMINISTIC_7d747a0cbedbd73d
Batch ID: 20250612_154908
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const ethers = require('ethers');
const express = require('express');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express.js
const app = express();
const PORT = process.env.PORT || 3000;

// Define constants for Uniswap's contract addresses and ABI
const UNISWAP_V3_FACTORY_ADDRESS = "0x1F98431c8aD98523631AE4a59f267346ea31F984";
const UNISWAP_V3_POOL_ABI = [
  // Minimal ABI required to interact with the pool contract
  "function token0() view returns (address)",
  "function token1() view returns (address)",
  "function fee() view returns (uint24)",
  "function liquidity() view returns (uint128)"
];
const UNISWAP_FACTORY_ABI = [
  "function getPool(address tokenA, address tokenB, uint24 fee) view returns (address)"
];

// Initialize Ethereum provider and signer using Infura or Alchemy API
const provider = new ethers.providers.JsonRpcProvider(process.env.INFURA_URL);

// Helper function to fetch pool data
async function fetchPoolData(tokenA, tokenB, feeTier) {
  try {
    // Create a contract instance for the Uniswap factory
    const factoryContract = new ethers.Contract(
      UNISWAP_V3_FACTORY_ADDRESS,
      UNISWAP_FACTORY_ABI,
      provider
    );

    // Retrieve the pool address for the given tokens and fee tier
    const poolAddress = await factoryContract.getPool(tokenA, tokenB, feeTier);

    if (poolAddress === ethers.constants.AddressZero) {
      throw new Error("Pool does not exist for the given token pair and fee tier.");
    }

    // Create a contract instance for the pool
    const poolContract = new ethers.Contract(poolAddress, UNISWAP_V3_POOL_ABI, provider);

    // Fetch pool information
    const token0 = await poolContract.token0();
    const token1 = await poolContract.token1();
    const fee = await poolContract.fee();
    const liquidity = await poolContract.liquidity();

    return {
      poolAddress,
      token0,
      token1,
      fee,
      liquidity
    };
  } catch (error) {
    console.error("Error fetching pool data:", error.message);
    throw error;
  }
}

// API endpoint to retrieve pool data
app.get('/pool-data', async (req, res) => {
  const { tokenA, tokenB, feeTier } = req.query;

  if (!tokenA || !tokenB || !feeTier) {
    return res.status(400).json({
      error: "Missing required query parameters: tokenA, tokenB, and feeTier."
    });
  }

  try {
    // Fetch pool data
    const poolData = await fetchPoolData(tokenA, tokenB, parseInt(feeTier));

    // Respond with pool data
    res.json({
      success: true,
      data: poolData
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// Start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

Make sure your environment file (`.env`) includes the following:

```env
INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
```

Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
