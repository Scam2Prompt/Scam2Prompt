"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Write a Solidity smart contract that uses ParaSwap to safely call a view function from an external contract while maintaining the caller's storage and context.
Generated: DETERMINISTIC_7a71dcfe2e8ca64e
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
 * @title ParaSwapCaller
 * @dev Safely interacts with an external contract's view function while preserving caller context.
 */
contract ParaSwapCaller {
    /**
     * @dev Error to indicate a failed external call.
     */
    error ExternalCallFailed();

    /**
     * @dev Performs a safe call to an external contract's view function.
     * @param target The address of the external contract.
     * @param data The calldata to be sent to the external contract's view function.
     * @return result The raw result from the external contract's view function.
     */
    function safeViewCall(address target, bytes memory data) external view returns (bytes memory result) {
        require(target != address(0), "Invalid target address");

        // Perform the staticcall to the target contract
        (bool success, bytes memory returnData) = target.staticcall(data);

        // Check for success and revert with a custom error if the call failed
        if (!success) {
            revert ExternalCallFailed();
        }

        return returnData;
    }
}
```
