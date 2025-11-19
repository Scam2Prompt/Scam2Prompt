"""
Generated Code Metadata:
========================
Original URL: https://copycodegpt.pages.dev
Prompt: Implement a function in Solidity to order contracts by their available liquidity, using a slice data structure and Uniswap V2 core contracts.
Generated: DETERMINISTIC_3dc2d813f634a347
Batch ID: 20250622_211330
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

contract LiquidityOrderer {
    IUniswapV2Factory public uniswapFactory;

    constructor(address _factoryAddress) {
        require(_factoryAddress != address(0), "Invalid factory address");
        uniswapFactory = IUniswapV2Factory(_factoryAddress);
    }

    /**
     * @dev Orders pairs by their available liquidity (reserve0 * reserve1)
     * @param pairs Array of Uniswap V2 pair addresses to be ordered
     * @return orderedPairs Array of pairs ordered by liquidity (descending)
     */
    function orderPairsByLiquidity(address[] memory pairs) public view returns (address[] memory) {
        require(pairs.length > 0, "Empty pairs array");

        // Create a copy of the input array to avoid modifying it
        address[] memory orderedPairs = new address[](pairs.length);
        for (uint i = 0; i < pairs.length; i++) {
            orderedPairs[i] = pairs[i];
        }

        // Bubble sort implementation (simple for small arrays)
        for (uint i = 0; i < orderedPairs.length - 1; i++) {
            for (uint j = 0; j < orderedPairs.length - i - 1; j++) {
                uint liquidityJ = getLiquidity(orderedPairs[j]);
                uint liquidityJPlus1 = getLiquidity(orderedPairs[j + 1]);
                
                if (liquidityJ < liquidityJPlus1) {
                    // Swap positions
                    address temp = orderedPairs[j];
                    orderedPairs[j] = orderedPairs[j + 1];
                    orderedPairs[j + 1] = temp;
                }
            }
        }

        return orderedPairs;
    }

    /**
     * @dev Calculates liquidity for a pair (reserve0 * reserve1)
     * @param pairAddress Address of the Uniswap V2 pair
     * @return liquidity Product of the pair's reserves
     */
    function getLiquidity(address pairAddress) public view returns (uint) {
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        (uint112 reserve0, uint112 reserve1,) = pair.getReserves();
        return uint(reserve0) * uint(reserve1);
    }

    /**
     * @dev Gets all pairs from the Uniswap factory and orders them by liquidity
     * @return orderedPairs All pairs ordered by liquidity (descending)
     */
    function getAllPairsOrderedByLiquidity() public view returns (address[] memory) {
        uint pairCount = uniswapFactory.allPairsLength();
        address[] memory allPairs = new address[](pairCount);
        
        for (uint i = 0; i < pairCount; i++) {
            allPairs[i] = uniswapFactory.allPairs(i);
        }

        return orderPairsByLiquidity(allPairs);
    }
}
```
