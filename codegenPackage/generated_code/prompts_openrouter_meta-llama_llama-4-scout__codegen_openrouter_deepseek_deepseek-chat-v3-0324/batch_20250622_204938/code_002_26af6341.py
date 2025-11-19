"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Generate a Solidity smart contract that interacts with Uniswap V2 to find contracts with a specific liquidity and order them by liquidity.
Generated: DETERMINISTIC_26af6341a6b7b6d6
Batch ID: 20250622_204938
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract UniswapV2LiquidityFinder {
    IUniswapV2Factory public immutable uniswapFactory;
    
    struct PairInfo {
        address pairAddress;
        uint256 liquidity;
    }

    /**
     * @dev Initialize contract with Uniswap V2 Factory address
     * @param _factoryAddress Address of Uniswap V2 Factory
     */
    constructor(address _factoryAddress) {
        require(_factoryAddress != address(0), "Invalid factory address");
        uniswapFactory = IUniswapV2Factory(_factoryAddress);
    }

    /**
     * @dev Get all pairs with liquidity greater than minLiquidity
     * @param minLiquidity Minimum liquidity threshold to filter pairs
     * @return PairInfo[] Array of pairs with liquidity above threshold
     */
    function getPairsWithMinLiquidity(uint256 minLiquidity) external view returns (PairInfo[] memory) {
        uint256 pairCount = uniswapFactory.allPairsLength();
        PairInfo[] memory tempPairs = new PairInfo[](pairCount);
        uint256 validPairsCount = 0;

        // First pass: count valid pairs
        for (uint256 i = 0; i < pairCount; i++) {
            address pairAddress = uniswapFactory.allPairs(i);
            uint256 liquidity = getLiquidity(pairAddress);
            if (liquidity >= minLiquidity) {
                tempPairs[validPairsCount] = PairInfo(pairAddress, liquidity);
                validPairsCount++;
            }
        }

        // Second pass: create properly sized array
        PairInfo[] memory result = new PairInfo[](validPairsCount);
        for (uint256 i = 0; i < validPairsCount; i++) {
            result[i] = tempPairs[i];
        }

        return result;
    }

    /**
     * @dev Get pairs sorted by liquidity (descending)
     * @param minLiquidity Minimum liquidity threshold to filter pairs
     * @return PairInfo[] Array of pairs sorted by liquidity
     */
    function getPairsSortedByLiquidity(uint256 minLiquidity) external view returns (PairInfo[] memory) {
        PairInfo[] memory pairs = getPairsWithMinLiquidity(minLiquidity);
        quickSort(pairs, 0, int256(pairs.length - 1));
        return pairs;
    }

    /**
     * @dev Calculate liquidity for a pair
     * @param pairAddress Address of the pair
     * @return uint256 Total liquidity of the pair
     */
    function getLiquidity(address pairAddress) public view returns (uint256) {
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        (uint112 reserve0, uint112 reserve1,) = pair.getReserves();
        return uint256(reserve0) + uint256(reserve1);
    }

    /**
     * @dev QuickSort implementation for sorting PairInfo array by liquidity
     * @param arr Array to sort
     * @param left Left index
     * @param right Right index
     */
    function quickSort(PairInfo[] memory arr, int256 left, int256 right) internal pure {
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
        
        if (left < j) quickSort(arr, left, j);
        if (i < right) quickSort(arr, i, right);
    }
}
```
