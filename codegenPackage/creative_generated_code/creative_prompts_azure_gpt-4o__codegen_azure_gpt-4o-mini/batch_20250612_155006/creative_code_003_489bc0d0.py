"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-build.vercel.app
Prompt: Provide an example of JavaScript code to fetch token reserves from a Uniswap V2 liquidity pool, referencing the UniswapV2pool interface.
Generated: DETERMINISTIC_489bc0d00722d1ec
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// Uniswap V2 Pool Interface ABI
const UNISWAP_V2_POOL_ABI = [
    "function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast)"
];

// Function to fetch token reserves from a Uniswap V2 liquidity pool
async function fetchTokenReserves(poolAddress) {
    try {
        // Validate the pool address
        if (!ethers.utils.isAddress(poolAddress)) {
            throw new Error("Invalid pool address provided.");
        }

        // Initialize ethers provider (using default provider)
        const provider = ethers.getDefaultProvider();

        // Create a contract instance for the Uniswap V2 Pool
        const poolContract = new ethers.Contract(poolAddress, UNISWAP_V2_POOL_ABI, provider);

        // Fetch reserves from the pool
        const [reserve0, reserve1] = await poolContract.getReserves();

        // Log the reserves
        console.log(`Reserve 0: ${reserve0.toString()}`);
        console.log(`Reserve 1: ${reserve1.toString()}`);

        // Return reserves as an object
        return {
            reserve0: reserve0.toString(),
            reserve1: reserve1.toString()
        };
    } catch (error) {
        // Handle errors and log them
        console.error("Error fetching token reserves:", error);
        throw new Error("Failed to fetch token reserves. See console for details.");
    }
}

// Example usage (replace with a valid Uniswap V2 pool address)
const poolAddress = "0x..."; // Enter a valid Uniswap V2 pool address here

fetchTokenReserves(poolAddress)
    .then(reserves => {
        console.log("Fetched reserves:", reserves);
    })
    .catch(error => {
        console.error("Error:", error.message);
    });
```
