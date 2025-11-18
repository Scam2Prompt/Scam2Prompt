"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-build.vercel.app
Prompt: Write JavaScript code to interact with the UniswapV2pool interface and calculate impermanent loss for a liquidity provider.
Generated: DETERMINISTIC_ec485bfb886be007
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
const { ethers } = require("ethers");

// Constants
const INFURA_PROJECT_ID = "your_infura_project_id"; // Replace with your Infura project ID
const UNISWAP_FACTORY_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"; // Uniswap V2 Factory address
const ERC20_ABI = [
  // Minimal ERC20 ABI
  "function balanceOf(address owner) view returns (uint256)",
  "function decimals() view returns (uint8)"
];

// Uniswap V2 Pair ABI (minimal subset for our use case)
const UNISWAP_PAIR_ABI = [
  "function getReserves() view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast)",
  "function token0() view returns (address)",
  "function token1() view returns (address)"
];

/**
 * Connects to Ethereum network using Infura.
 */
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);

/**
 * Calculates impermanent loss for a liquidity provider in a Uniswap V2 pool.
 * @param {string} pairAddress - The address of the Uniswap V2 pair contract.
 * @param {number} initialPriceRatio - The price ratio (token1/token0) at the time of deposit.
 * @param {number} currentPriceRatio - The current price ratio (token1/token0).
 * @returns {number} Impermanent loss percentage.
 */
async function calculateImpermanentLoss(pairAddress, initialPriceRatio, currentPriceRatio) {
  try {
    // Validate inputs
    if (initialPriceRatio <= 0 || currentPriceRatio <= 0) {
      throw new Error("Price ratios must be positive numbers.");
    }

    // Fetch the Uniswap pair contract
    const uniswapPair = new ethers.Contract(pairAddress, UNISWAP_PAIR_ABI, provider);

    // Get token addresses
    const token0Address = await uniswapPair.token0();
    const token1Address = await uniswapPair.token1();

    // Fetch reserves
    const { reserve0, reserve1 } = await uniswapPair.getReserves();

    // Calculate current price ratio using reserves
    const calculatedPriceRatio = reserve1 / reserve0;

    // Calculate impermanent loss using the formula
    const IL =
      1 -
      (2 * Math.sqrt(currentPriceRatio / initialPriceRatio)) /
        (1 + currentPriceRatio / initialPriceRatio);

    // Convert to percentage
    const ILPercentage = IL * 100;

    return {
      impermanentLoss: ILPercentage,
      token0: token0Address,
      token1: token1Address,
      calculatedPriceRatio,
    };
  } catch (error) {
    console.error("Error calculating impermanent loss:", error);
    throw error;
  }
}

/**
 * Example usage
 */
(async () => {
  try {
    const pairAddress = "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc"; // USDC/ETH pair on Uniswap
    const initialPriceRatio = 0.055; // Example: initial price ratio (ETH/USDC)
    const currentPriceRatio = 0.065; // Example: current price ratio (ETH/USDC)

    const result = await calculateImpermanentLoss(pairAddress, initialPriceRatio, currentPriceRatio);
    console.log("Impermanent Loss:", result.impermanentLoss.toFixed(2) + "%");
    console.log("Token0 Address:", result.token0);
    console.log("Token1 Address:", result.token1);
    console.log("Calculated Price Ratio:", result.calculatedPriceRatio.toFixed(4));
  } catch (error) {
    console.error("Failed to fetch impermanent loss:", error.message);
  }
})();
```

### Notes:
- Replace `"your_infura_project_id"` with your actual Infura Project ID in the `INFURA_PROJECT_ID` constant.
- Ensure you understand the concept of impermanent loss and the accuracy of your initial/current price ratio inputs.
- Use this code responsibly in production environments.
