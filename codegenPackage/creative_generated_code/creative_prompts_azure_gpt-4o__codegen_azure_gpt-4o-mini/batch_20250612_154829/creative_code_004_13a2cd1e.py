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

// Import PancakeSwap interfaces
import "@pancakeswap/pancake-swap-core/contracts/interfaces/IPancakePair.sol";
import "@pancakeswap/pancake-swap-core/contracts/interfaces/IPancakeFactory.sol";
import "@pancakeswap/pancake-swap-core/contracts/interfaces/IPancakeRouter02.sol";

contract ImpermanentLossCalculator {
    IPancakeRouter02 public pancakeRouter;
    IPancakeFactory public pancakeFactory;

    // Event for logging impermanent loss calculation
    event ImpermanentLossCalculated(uint256 impermanentLoss);

    // Constructor to initialize PancakeSwap router and factory
    constructor(address _router, address _factory) {
        pancakeRouter = IPancakeRouter02(_router);
        pancakeFactory = IPancakeFactory(_factory);
    }

    // Function to calculate impermanent loss between two token addresses
    function calculateImpermanentLoss(address tokenA, address tokenB, uint256 initialPriceA, uint256 initialPriceB) 
        external 
        view 
        returns (uint256) 
    {
        // Get the pair address for the token pair
        address pairAddress = pancakeFactory.getPair(tokenA, tokenB);
        require(pairAddress != address(0), "Pair does not exist");

        // Get reserves from the pair
        (uint256 reserveA, uint256 reserveB, ) = IPancakePair(pairAddress).getReserves();

        // Calculate prices from reserves
        uint256 currentPriceA = reserveA * 1e18 / reserveB; // Using 1e18 for precision
        uint256 currentPriceB = reserveB * 1e18 / reserveA;

        // Calculate impermanent loss 
        uint256 impermanentLoss = calculateLoss(initialPriceA, initialPriceB, currentPriceA, currentPriceB);

        // Emit event for logging
        emit ImpermanentLossCalculated(impermanentLoss);

        return impermanentLoss;
    }

    // Internal function to calculate impermanent loss percentage
    function calculateLoss(uint256 initialPriceA, uint256 initialPriceB, uint256 currentPriceA, uint256 currentPriceB) 
        internal 
        pure 
        returns (uint256) 
    {
        // Calculate the change ratio for each token
        uint256 changeA = (currentPriceA * 100) / initialPriceA;
        uint256 changeB = (currentPriceB * 100) / initialPriceB;

        // Determine impermanent loss based on the changes
        uint256 impermanentLoss = (changeA + changeB) / 2; // Simplistic average for loss calculation
        return impermanentLoss > 100 ? 0 : (100 - impermanentLoss); // Cap maximum loss at 100%
    }
}
```
