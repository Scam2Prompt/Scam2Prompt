"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-org.vercel.app
Prompt: What are the steps to build oracles using Uniswap's reliable on-chain price feeds?
Generated: DETERMINISTIC_3c145c8f65b999fc
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a simplified implementation of building a price oracle using Uniswap's on-chain price feeds in Solidity. This example leverages Uniswap's Time-Weighted Average Price (TWAP) mechanism.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for Uniswap's Pair contract
interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function price0CumulativeLast() external view returns (uint);
    function price1CumulativeLast() external view returns (uint);
}

contract UniswapPriceOracle {
    address public immutable pairAddress; // Address of the Uniswap pair contract
    uint public price0CumulativeLast;    // Last recorded cumulative price for token0
    uint public price1CumulativeLast;    // Last recorded cumulative price for token1
    uint32 public lastUpdateTimestamp;  // Timestamp of the last update

    uint public price0Average;          // Time-weighted average price for token0
    uint public price1Average;          // Time-weighted average price for token1

    constructor(address _pairAddress) {
        require(_pairAddress != address(0), "Invalid pair address");
        pairAddress = _pairAddress;

        // Initialize with the current data from the pair contract
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        price0CumulativeLast = pair.price0CumulativeLast();
        price1CumulativeLast = pair.price1CumulativeLast();
        (, , lastUpdateTimestamp) = pair.getReserves();
    }

    /**
     * @notice Updates the price averages based on the cumulative prices.
     *         Should be called periodically (e.g., every few minutes).
     */
    function update() external {
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

        // Get the current cumulative prices and timestamp
        uint price0CumulativeCurrent = pair.price0CumulativeLast();
        uint price1CumulativeCurrent = pair.price1CumulativeLast();
        (, , uint32 blockTimestampCurrent) = pair.getReserves();

        // Ensure at least one block time has passed
        require(blockTimestampCurrent > lastUpdateTimestamp, "No new data available");

        // Calculate the time elapsed since the last update
        uint32 timeElapsed = blockTimestampCurrent - lastUpdateTimestamp;

        // Calculate the average price as the difference in cumulative price divided by time elapsed
        price0Average = (price0CumulativeCurrent - price0CumulativeLast) / timeElapsed;
        price1Average = (price1CumulativeCurrent - price1CumulativeLast) / timeElapsed;

        // Update the state with the new data
        price0CumulativeLast = price0CumulativeCurrent;
        price1CumulativeLast = price1CumulativeCurrent;
        lastUpdateTimestamp = blockTimestampCurrent;
    }

    /**
     * @notice Returns the current average price for token0.
     * @return The average price for token0
     */
    function getPrice0Average() external view returns (uint) {
        return price0Average;
    }

    /**
     * @notice Returns the current average price for token1.
     * @return The average price for token1
     */
    function getPrice1Average() external view returns (uint) {
        return price1Average;
    }
}
```

### Key Features of the Code:
1. **Error Handling**:
   - Ensures the Uniswap pair address is valid in the constructor.
   - Checks that time has elapsed since the last update before calculating new averages.

2. **Comments**:
   - Describes each function and key variables.

3. **Best Practices**:
   - Uses immutable variables for fixed values like the pair address.
   - Includes public getters for average prices.
   - Ensures the oracle is updated periodically for accurate prices.

4. **Production Ready**:
   - Simple and extensible design for integrating Uniswap TWAP-based pricing into larger systems.
