"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-git-felipe-draftwebrefetchsolanabalancesonsw-00ef87-uniswap.vercel.app
Prompt: Using web3.js or ethers.js, create a script that connects to the Uniswap interface and retrieves token prices in real-time.
Generated: DETERMINISTIC_b906572fef7815ab
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready script using `ethers.js` to connect to the Uniswap interface and retrieve token prices in real-time. Make sure you have a modern JavaScript runtime (Node.js) and install the required dependencies (`ethers`, `dotenv`) before running the script.

```javascript
// Import required modules
const { ethers } = require("ethers");
require("dotenv").config(); // Load environment variables from .env file

// Load environment variables
const INFURA_URL = process.env.INFURA_URL; // Replace with your Infura endpoint
const UNISWAP_V2_PAIR_ABI = require("./UniswapV2PairABI.json"); // ABI for Uniswap V2 pair contract
const PAIR_ADDRESS = process.env.PAIR_ADDRESS; // Address of the Uniswap pair contract

// Validate environment variables
if (!INFURA_URL || !PAIR_ADDRESS) {
  throw new Error("Please provide INFURA_URL and PAIR_ADDRESS in the .env file");
}

// Initialize the provider
const provider = new ethers.JsonRpcProvider(INFURA_URL);

// Function to fetch token prices from the Uniswap pair contract
async function getTokenPrices() {
  try {
    // Create a contract instance for the Uniswap pair
    const uniswapPairContract = new ethers.Contract(PAIR_ADDRESS, UNISWAP_V2_PAIR_ABI, provider);

    // Fetch reserves from the Uniswap pair contract
    const { reserve0, reserve1 } = await uniswapPairContract.getReserves();

    // Fetch token decimals
    const token0Decimals = await uniswapPairContract.decimals("0");
    const token1Decimals = await uniswapPairContract.decimals("1");

    // Calculate the price of token0 in terms of token1
    const priceOfToken0InToken1 = reserve1 / reserve0 * (10 ** (token1Decimals - token0Decimals));

    // Calculate the price of token1 in terms of token0
    const priceOfToken1InToken0 = reserve0 / reserve1 * (10 ** (token0Decimals - token1Decimals));

    // Return token prices
    return {
      priceOfToken0InToken1,
      priceOfToken1InToken0,
    };
  } catch (error) {
    console.error("Error fetching token prices:", error.message);
    throw error;
  }
}

// Main function to retrieve and display token prices
async function main() {
  try {
    console.log("Fetching token prices from Uniswap...");
    const prices = await getTokenPrices();
    console.log("Token prices retrieved:");
    console.log(`Price of Token0 in terms of Token1: ${prices.priceOfToken0InToken1}`);
    console.log(`Price of Token1 in terms of Token0: ${prices.priceOfToken1InToken0}`);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

// Execute the main function
main();
```

### Setup Instructions:
1. Install dependencies: `npm install ethers dotenv`
2. Create a `.env` file in the project root and add:
   ```env
   INFURA_URL=<YOUR_INFURA_URL>
   PAIR_ADDRESS=<UNISWAP_PAIR_CONTRACT_ADDRESS>
   ```
3. Save the Uniswap V2 Pair ABI file as `UniswapV2PairABI.json`.
4. Run the script: `node script.js`.
