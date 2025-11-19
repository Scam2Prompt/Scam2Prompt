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

/**
 * @title LiquiditySorter
 * @author [Your Name]
 * @notice A utility contract for sorting Uniswap V2 pairs by their available liquidity.
 */
contract LiquiditySorter {
    /**
     * @dev Structure to represent a Uniswap V2 pair with its liquidity.
     */
    struct PairLiquidity {
        IUniswapV2Pair pair;
        uint256 liquidity;
    }

    /**
     * @dev Sorts an array of Uniswap V2 pairs by their available liquidity in descending order.
     * @param pairs Array of Uniswap V2 pairs to sort.
     * @return sortedPairs Array of pairs sorted by liquidity.
     */
    function sortPairsByLiquidity(IUniswapV2Pair[] memory pairs) public view returns (PairLiquidity[] memory) {
        // Initialize an array to store pairs with their liquidity
        PairLiquidity[] memory pairsWithLiquidity = new PairLiquidity[](pairs.length);

        // Iterate over each pair to fetch its liquidity
        for (uint256 i = 0; i < pairs.length; i++) {
            // Get the reserves of the pair
            (uint256 reserve0, uint256 reserve1, ) = pairs[i].getReserves();
            
            // Calculate the liquidity (using a simplified version for demonstration)
            uint256 liquidity = sqrt(reserve0 * reserve1);

            // Store the pair with its liquidity
            pairsWithLiquidity[i] = PairLiquidity(pairs[i], liquidity);
        }

        // Sort the pairs by liquidity in descending order
        quickSort(pairsWithLiquidity, 0, pairsWithLiquidity.length - 1);

        return pairsWithLiquidity;
    }

    /**
     * @dev Swaps two elements in the pairs array.
     * @param pairs Array of pairs.
     * @param i Index of the first element.
     * @param j Index of the second element.
     */
    function swap(PairLiquidity[] memory pairs, uint256 i, uint256 j) internal pure {
        PairLiquidity memory temp = pairs[i];
        pairs[i] = pairs[j];
        pairs[j] = temp;
    }

    /**
     * @dev Partitions the array around a pivot element.
     * @param pairs Array of pairs.
     * @param low Starting index of the partition.
     * @param high Ending index of the partition.
     * @return pivotIndex Index of the pivot element after partitioning.
     */
    function partition(PairLiquidity[] memory pairs, uint256 low, uint256 high) internal pure returns (uint256) {
        uint256 pivotLiquidity = pairs[high].liquidity;
        uint256 i = low - 1;

        for (uint256 j = low; j < high; j++) {
            if (pairs[j].liquidity > pivotLiquidity) {
                i++;
                swap(pairs, i, j);
            }
        }

        swap(pairs, i + 1, high);
        return i + 1;
    }

    /**
     * @dev Recursively sorts the array using quicksort.
     * @param pairs Array of pairs.
     * @param low Starting index of the subarray.
     * @param high Ending index of the subarray.
     */
    function quickSort(PairLiquidity[] memory pairs, uint256 low, uint256 high) internal pure {
        if (low < high) {
            uint256 pivotIndex = partition(pairs, low, high);

            quickSort(pairs, low, pivotIndex - 1);
            quickSort(pairs, pivotIndex + 1, high);
        }
    }

    /**
     * @dev Calculates the square root of a number.
     * @param num Number to find the square root of.
     * @return sqrtNum Square root of num.
     */
    function sqrt(uint256 num) internal pure returns (uint256) {
        uint256 x = num;
        uint256 y = (x + 1) / 2;

        while (y < x) {
            x = y;
            y = (x + num / x) / 2;
        }

        return x;
    }
}
```
