"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapdefi.org
Prompt: Write a Solidity smart contract that interacts with PancakeSwap's liquidity pools to calculate impermanent loss for a given token pair.
Generated: DETERMINISTIC_13a2cd1e3c85f532
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ImpermanentLossCalculator
 * @dev A smart contract to calculate impermanent loss for liquidity providers in PancakeSwap pools.
 */
contract ImpermanentLossCalculator {

    // Address of PancakeSwap's Router
    address public immutable pancakeRouter;

    // Interface for PancakeSwap Router
    IPancakeRouter private router;

    /**
     * @dev Constructor initializes the router address.
     * @param _pancakeRouter Address of PancakeSwap's Router
     */
    constructor(address _pancakeRouter) {
        require(_pancakeRouter != address(0), "Invalid router address");
        pancakeRouter = _pancakeRouter;
        router = IPancakeRouter(_pancakeRouter);
    }

    /**
     * @dev Calculates impermanent loss given the token prices and percentage changes.
     * @param initialPriceA Initial price of token A
     * @param initialPriceB Initial price of token B
     * @param updatedPriceA Updated price of token A (after market movement)
     * @param updatedPriceB Updated price of token B (after market movement)
     * @return impermanentLossPercentage Percentage loss due to impermanent loss
     */
    function calculateImpermanentLoss(
        uint256 initialPriceA,
        uint256 initialPriceB,
        uint256 updatedPriceA,
        uint256 updatedPriceB
    ) public pure returns (uint256 impermanentLossPercentage) {
        require(initialPriceA > 0 && initialPriceB > 0, "Initial prices must be greater than zero");
        require(updatedPriceA > 0 && updatedPriceB > 0, "Updated prices must be greater than zero");

        // Ratio of price changes
        uint256 ratioA = (updatedPriceA * 1e18) / initialPriceA;
        uint256 ratioB = (updatedPriceB * 1e18) / initialPriceB;

        // Geometric mean of the ratios
        uint256 geometricMean = sqrt(ratioA * ratioB);

        // Impermanent loss formula
        impermanentLossPercentage = ((2 * 1e18 - (2 * geometricMean)) * 100) / 1e18;
    }

    /**
     * @dev Utility function to calculate square root using Babylonian method.
     * @param x The input number
     * @return y The square root of the input
     */
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
    }
}

/**
 * @dev PancakeSwap Router interface (partial)
 */
interface IPancakeRouter {
    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory);
    function getAmountsIn(uint256 amountOut, address[] calldata path) external view returns (uint256[] memory);
}
```
