"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botcodesrc.pages.dev
Prompt: Write a Solidity function that uses assembly to copy memory slices efficiently, as shown in the `copy` function from the Oneinch Slippage Bot contract.
Generated: DETERMINISTIC_2e1955f96cef1c7e
Batch ID: 20250612_151343
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
 * @title MemoryCopy
 * @dev Provides an efficient assembly-based function to copy memory slices.
 */
contract MemoryCopy {
    /**
     * @notice Copies a memory slice from one location to another.
     * @param dest Destination memory pointer where data will be copied.
     * @param src Source memory pointer from where data will be copied.
     * @param length Number of bytes to be copied.
     */
    function copyMemory(uint256 dest, uint256 src, uint256 length) external pure {
        assembly {
            // Ensure length is not zero before proceeding
            if iszero(length) {
                revert(0, 0)
            }

            // Set work pointers
            let end := add(src, length)

            // Copy word by word (32 bytes at a time)
            for { } lt(src, end) { } {
                mstore(dest, mload(src)) // Write 32 bytes from src to dest
                dest := add(dest, 0x20) // Increment dest pointer by 32 bytes
                src := add(src, 0x20)   // Increment src pointer by 32 bytes
            }
        }
    }
}
```
