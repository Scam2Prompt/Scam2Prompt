"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Implement a Solidity function that orders contracts by their available liquidity, using the slice struct and assembly code patterns provided in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_8c2221213cd8dc47
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
 * @dev Contract to order other contracts by their available liquidity.
 */
contract LiquiditySorter {
    struct Slice {
        address contractAddress; // Address of the contract
        uint256 liquidity;      // Available liquidity of the contract
    }

    /**
     * @dev Orders contracts by their liquidity in descending order using assembly for performance optimization.
     * @param slices Array of Slice structs containing contract addresses and liquidity values.
     * @return sortedSlices Sorted array of Slice structs by liquidity.
     */
    function orderByLiquidity(Slice[] memory slices) public pure returns (Slice[] memory sortedSlices) {
        sortedSlices = slices;

        assembly {
            let n := mload(sortedSlices) // Number of elements in the array

            // Bubble sort implementation (optimized using assembly)
            for { let i := 0 } lt(i, sub(n, 1)) { i := add(i, 1) } {
                for { let j := 0 } lt(j, sub(n, i, 1)) { j := add(j, 1) } {
                    // Get memory pointers for the current and next Slice structs
                    let current := add(add(sortedSlices, mul(j, 0x40)), 0x20)
                    let next := add(add(sortedSlices, mul(add(j, 1), 0x40)), 0x20)

                    // Load liquidity values
                    let currentLiquidity := mload(current)
                    let nextLiquidity := mload(next)

                    // Compare liquidity values
                    if lt(currentLiquidity, nextLiquidity) {
                        // Swap the slices if the next has more liquidity
                        let temp := mload(add(sortedSlices, mul(j, 0x40)))
                        mstore(add(sortedSlices, mul(j, 0x40)), mload(add(sortedSlices, mul(add(j, 1), 0x40))))
                        mstore(add(sortedSlices, mul(add(j, 1), 0x40)), temp)
                    }
                }
            }
        }
    }
}
```
