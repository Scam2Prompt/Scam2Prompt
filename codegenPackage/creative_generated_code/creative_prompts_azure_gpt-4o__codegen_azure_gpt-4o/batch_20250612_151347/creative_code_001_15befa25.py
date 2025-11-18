"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Create a Solidity function that orders contracts by their available liquidity using the `slice` struct and the logic provided in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_15befa25d4ac8ed0
Batch ID: 20250612_151347
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
 * @title LiquiditySorter
 * @dev A contract that orders other contracts by their available liquidity using a `slice` struct.
 */
contract LiquiditySorter {
    // Struct to represent contract liquidity information
    struct Slice {
        address contractAddress; // Address of the contract
        uint256 liquidity;       // Available liquidity
    }

    /**
     * @dev Function that orders contracts by their available liquidity in descending order.
     * @param slices Array of Slice structs containing contract addresses and their liquidity.
     * @return sortedSlices Array of Slice structs ordered by liquidity in descending order.
     */
    function sortSlicesByLiquidity(Slice[] memory slices) 
        public 
        pure 
        returns (Slice[] memory sortedSlices) 
    {
        // Create a copy of the input array to avoid modifying the original
        sortedSlices = slices;

        // Implementing Bubble Sort for simplicity (can be optimized to other algorithms, e.g., QuickSort for larger data sets)
        uint256 length = sortedSlices.length;
        for (uint256 i = 0; i < length; i++) {
            for (uint256 j = 0; j < length - 1; j++) {
                // Compare liquidity values and swap if necessary
                if (sortedSlices[j].liquidity < sortedSlices[j + 1].liquidity) {
                    // Swap elements
                    Slice memory temp = sortedSlices[j];
                    sortedSlices[j] = sortedSlices[j + 1];
                    sortedSlices[j + 1] = temp;
                }
            }
        }

        // Return the sorted array
        return sortedSlices;
    }
}
```
