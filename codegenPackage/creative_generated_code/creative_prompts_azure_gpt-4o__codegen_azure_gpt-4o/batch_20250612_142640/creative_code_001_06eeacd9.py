"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Provide an example of how ParaSwap can be used to implement a library function that modifies the caller contract's storage securely.
Generated: DETERMINISTIC_06eeacd9dd8d46bb
Batch ID: 20250612_142640
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
 * @title ParaSwapLibrary
 * @dev A library to securely interact with ParaSwap and modify caller contract's storage.
 *      This library assumes that the ParaSwap contract is deployed and accessible.
 */
library ParaSwapLibrary {
    // Define the interface for the ParaSwap contract
    interface IParaSwap {
        function swap(
            address fromToken,
            address toToken,
            uint256 fromAmount,
            uint256 toAmountMin,
            address beneficiary,
            bytes calldata swapData
        ) external returns (uint256);
    }

    /**
     * @dev Performs a token swap via ParaSwap and updates caller contract storage securely.
     * @param paraSwap The address of the ParaSwap contract.
     * @param fromToken The address of the token to swap from.
     * @param toToken The address of the token to swap to.
     * @param fromAmount The amount of `fromToken` to swap.
     * @param toAmountMin The minimum amount of `toToken` expected from the swap.
     * @param swapData The encoded swap parameters for ParaSwap.
     * @param storageSlot The storage slot in the caller contract to update.
     * @param newValue The value to securely store after the swap.
     * @return swappedAmount The actual amount of `toToken` received after the swap.
     */
    function swapAndModifyStorage(
        address paraSwap,
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 toAmountMin,
        bytes calldata swapData,
        uint256 storageSlot,
        bytes32 newValue
    ) external returns (uint256 swappedAmount) {
        require(paraSwap != address(0), "Invalid ParaSwap address");
        require(fromToken != address(0), "Invalid fromToken address");
        require(toToken != address(0), "Invalid toToken address");
        require(storageSlot > 0, "Invalid storageSlot");

        // Interact with ParaSwap for the token swap
        IParaSwap paraSwapContract = IParaSwap(paraSwap);
        swappedAmount = paraSwapContract.swap(
            fromToken,
            toToken,
            fromAmount,
            toAmountMin,
            address(this),
            swapData
        );

        require(swappedAmount >= toAmountMin, "Swap failed: insufficient output");

        // Update the caller contract's storage securely
        // Note: This uses inline assembly to modify storage at the specified slot
        assembly {
            sstore(storageSlot, newValue)
        }
    }
}
```
