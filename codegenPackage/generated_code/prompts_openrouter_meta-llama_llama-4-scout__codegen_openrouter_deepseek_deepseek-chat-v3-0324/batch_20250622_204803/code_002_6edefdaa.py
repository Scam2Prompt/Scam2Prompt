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

contract LiquidityOrdering {
    IUniswapV2Factory public immutable uniswapFactory;

    constructor(address _factory) {
        uniswapFactory = IUniswapV2Factory(_factory);
    }

    struct PairLiquidity {
        address pairAddress;
        uint256 liquidity;
    }

    /**
     * @dev Orders pairs by their available liquidity in descending order
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @param pairs Array of pair addresses to evaluate
     * @return Ordered array of PairLiquidity structs
     */
    function orderPairsByLiquidity(
        address tokenA,
        address tokenB,
        address[] memory pairs
    ) public view returns (PairLiquidity[] memory) {
        require(pairs.length > 0, "No pairs provided");
        
        PairLiquidity[] memory pairLiquidity = new PairLiquidity[](pairs.length);
        
        for (uint256 i = 0; i < pairs.length; i++) {
            IUniswapV2Pair pair = IUniswapV2Pair(pairs[i]);
            
            // Verify the pair contains the specified tokens
            address token0 = pair.token0();
            address token1 = pair.token1();
            require(
                (token0 == tokenA && token1 == tokenB) || 
                (token0 == tokenB && token1 == tokenA),
                "Invalid token pair"
            );
            
            // Get reserves
            (uint112 reserve0, uint112 reserve1,) = pair.getReserves();
            uint256 liquidity = uint256(reserve0) * uint256(reserve1);
            
            pairLiquidity[i] = PairLiquidity({
                pairAddress: pairs[i],
                liquidity: liquidity
            });
        }
        
        // Sort pairs by liquidity in descending order
        _quickSort(pairLiquidity, 0, pairLiquidity.length - 1);
        
        return pairLiquidity;
    }

    /**
     * @dev QuickSort implementation for PairLiquidity array
     * @param arr Array to sort
     * @param left Left index
     * @param right Right index
     */
    function _quickSort(
        PairLiquidity[] memory arr,
        int256 left,
        int256 right
    ) internal pure {
        int256 i = left;
        int256 j = right;
        if (i == j) return;
        
        uint256 pivot = arr[uint256(left + (right - left) / 2)].liquidity;
        
        while (i <= j) {
            while (arr[uint256(i)].liquidity > pivot) i++;
            while (pivot > arr[uint256(j)].liquidity) j--;
            if (i <= j) {
                (arr[uint256(i)], arr[uint256(j)]) = (arr[uint256(j)], arr[uint256(i)]);
                i++;
                j--;
            }
        }
        
        if (left < j) _quickSort(arr, left, j);
        if (i < right) _quickSort(arr, i, right);
    }
}
```
