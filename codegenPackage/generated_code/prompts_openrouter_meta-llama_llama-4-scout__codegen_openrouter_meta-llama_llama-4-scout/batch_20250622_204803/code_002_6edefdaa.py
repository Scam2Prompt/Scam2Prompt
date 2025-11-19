"""
Generated Code Metadata:
========================
Original URL: https://codesource.pages.dev
Prompt: "Generate a function in Solidity to order contracts by their available liquidity using Uniswap V2."
Generated: DETERMINISTIC_6edefdaa19474f41
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

/**
 * @title UniswapV2LiquiditySorter
 * @author [Your Name]
 * @notice A contract to sort Uniswap V2 pairs by their available liquidity.
 */
contract UniswapV2LiquiditySorter {
    // Uniswap V2 Factory contract instance
    IUniswapV2Factory public immutable factory;

    /**
     * @param _factory Address of the Uniswap V2 Factory contract.
     */
    constructor(address _factory) {
        require(_factory != address(0), "UniswapV2LiquiditySorter: Factory address cannot be zero");
        factory = IUniswapV2Factory(_factory);
    }

    /**
     * @notice Sorts Uniswap V2 pairs by their available liquidity in descending order.
     * @param _tokenA Address of the first token.
     * @param _tokenB Address of the second token.
     * @return A list of Uniswap V2 pairs sorted by liquidity.
     */
    function sortPairsByLiquidity(address _tokenA, address _tokenB) public view returns (IUniswapV2Pair[] memory) {
        // Get all pairs from the factory
        address[] memory allPairs = factory.allPairs();

        // Filter pairs that contain both tokens
        IUniswapV2Pair[] memory pairs = new IUniswapV2Pair[](allPairs.length);
        uint256 pairCount = 0;
        for (uint256 i = 0; i < allPairs.length; i++) {
            IUniswapV2Pair pair = IUniswapV2Pair(allPairs[i]);
            if (pair.token0() == _tokenA && pair.token1() == _tokenB) {
                pairs[pairCount] = pair;
                pairCount++;
            } else if (pair.token0() == _tokenB && pair.token1() == _tokenA) {
                pairs[pairCount] = pair;
                pairCount++;
            }
        }

        // Trim the array to the correct size
        IUniswapV2Pair[] memory filteredPairs = new IUniswapV2Pair[](pairCount);
        for (uint256 i = 0; i < pairCount; i++) {
            filteredPairs[i] = pairs[i];
        }

        // Sort pairs by liquidity
        for (uint256 i = 0; i < filteredPairs.length; i++) {
            for (uint256 j = i + 1; j < filteredPairs.length; j++) {
                if (filteredPairs[i].getLiquidity() < filteredPairs[j].getLiquidity()) {
                    // Swap pairs
                    IUniswapV2Pair temp = filteredPairs[i];
                    filteredPairs[i] = filteredPairs[j];
                    filteredPairs[j] = temp;
                }
            }
        }

        return filteredPairs;
    }
}

// Helper function to get liquidity (Uniswap V2 doesn't have a direct function for this)
interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 _reserve0, uint112 _reserve1, uint32 _blockTimestampLast);
    function token0() external pure returns (address);
    function token1() external pure returns (address);
}

library UniswapV2Library {
    function getLiquidity(IUniswapV2Pair pair) internal view returns (uint256) {
        (uint112 _reserve0, uint112 _reserve1, ) = pair.getReserves();
        return _reserve0 * _reserve1;
    }
}
```
