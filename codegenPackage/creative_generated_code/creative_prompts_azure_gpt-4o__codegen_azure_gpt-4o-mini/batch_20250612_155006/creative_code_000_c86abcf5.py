"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-build.vercel.app
Prompt: Write JavaScript code to interact with the UniswapV2pool interface, including initializing a connection and fetching pool data. Use the Uniswap V2 API or libraries mentioned on the webpage.
Generated: DETERMINISTIC_c86abcf54e2cc771
Batch ID: 20250612_155006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`;": {
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
// Importing required libraries
const { ethers } = require("ethers"); // Ethers.js for interacting with Ethereum
const { abi: IUniswapV2PairABI } = require('@uniswap/v2-core/build/IUniswapV2Pair.json'); // Uniswap V2 Pair ABI

// Define constants
const UNISWAP_V2_PAIR_ADDRESS = '0xYourUniswapV2PairAddressHere'; // Replace with the actual pair address
const INFURA_PROJECT_ID = 'YourInfuraProjectID'; // Replace with your Infura project ID
const INFURA_URL = `https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`; // Infura URL for mainnet

// Initialize provider and contract
const provider = new ethers.providers.JsonRpcProvider(INFURA_URL);
const uniswapV2PairContract = new ethers.Contract(UNISWAP_V2_PAIR_ADDRESS, IUniswapV2PairABI, provider);

/**
 * Fetches the pool data from the Uniswap V2 Pair contract.
 * @returns {Promise<Object>} - An object containing pool data like reserves and total supply.
 */
async function fetchPoolData() {
    try {
        // Fetching reserves and total supply from the contract
        const [reserve0, reserve1, totalSupply] = await Promise.all([
            uniswapV2PairContract.getReserves(),
            uniswapV2PairContract.totalSupply()
        ]);

        // Constructing and returning the pool data object
        return {
            reserve0: reserve0[0].toString(),
            reserve1: reserve0[1].toString(),
            totalSupply: totalSupply.toString()
        };
    } catch (error) {
        console.error("Error fetching pool data:", error);
        throw new Error("Failed to fetch pool data");
    }
}

// Main function to execute the fetching of pool data
(async () => {
    try {
        const poolData = await fetchPoolData();
        console.log("Pool Data:", poolData);
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
})();
```

Make sure to replace `0xYourUniswapV2PairAddressHere` and `YourInfuraProjectID` with the actual Uniswap V2 pair address and your Infura project ID, respectively.
