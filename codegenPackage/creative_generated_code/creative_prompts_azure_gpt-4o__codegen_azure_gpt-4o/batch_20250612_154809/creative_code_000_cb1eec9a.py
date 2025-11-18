"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Write a Solidity contract that uses `IUniswapV2Factory` and `IUniswapV2Pair` to identify new Uniswap liquidity pool contracts, similar to the functionality described in the Uniswap Slippage Bot.
Generated: DETERMINISTIC_cb1eec9a43d12726
Batch ID: 20250612_154809
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

// Import interfaces for Uniswap V2 Factory and Pair contracts
interface IUniswapV2Factory {
    function allPairs(uint) external view returns (address);
    function allPairsLength() external view returns (uint);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

// Contract to monitor new liquidity pools on Uniswap V2
contract UniswapPoolMonitor {
    // Address of the Uniswap V2 Factory
    address public immutable uniswapFactory;

    // Event emitted when a new pool is identified
    event NewPoolDetected(address indexed pair, address token0, address token1);

    // Mapping to track already processed pairs
    mapping(address => bool) private processedPairs;

    // Constructor to set the factory address during deployment
    constructor(address _uniswapFactory) {
        require(_uniswapFactory != address(0), "Factory address cannot be zero");
        uniswapFactory = _uniswapFactory;
    }

    /**
     * @dev Function to scan for new pairs on Uniswap V2.
     * Emits an event for each new pair detected.
     */
    function scanNewPools() external {
        // Reference the factory interface
        IUniswapV2Factory factory = IUniswapV2Factory(uniswapFactory);

        // Get the total number of pairs
        uint totalPairs = factory.allPairsLength();

        for (uint i = 0; i < totalPairs; i++) {
            // Get the address of the pair at the current index
            address pair = factory.allPairs(i);

            // Skip already processed pairs
            if (processedPairs[pair]) {
                continue;
            }

            // Mark the pair as processed
            processedPairs[pair] = true;

            // Reference the pair interface
            IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);

            // Fetch token addresses for the pair
            address token0 = uniswapPair.token0();
            address token1 = uniswapPair.token1();

            // Emit an event for the new pool
            emit NewPoolDetected(pair, token0, token1);
        }
    }

    /**
     * @dev Check if a pool has already been processed.
     * @param pair Address of the pool to check.
     * @return True if the pool has been processed, false otherwise.
     */
    function isPoolProcessed(address pair) external view returns (bool) {
        return processedPairs[pair];
    }
}
```
