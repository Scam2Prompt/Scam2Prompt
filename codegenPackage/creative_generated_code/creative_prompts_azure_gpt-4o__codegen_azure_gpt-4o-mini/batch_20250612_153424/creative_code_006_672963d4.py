"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: Write a Solidity contract that demonstrates how Open Ocean can be used for censorship-resistant external calls by passing a call data hash.
Generated: DETERMINISTIC_672963d4258deed3
Batch ID: 20250612_153424
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

/// @title Open Ocean Censorship-Resistant Contract
/// @notice This contract demonstrates how to use Open Ocean for making external calls
///         in a censorship-resistant manner by passing a call data hash.
contract OpenOceanCensorshipResistant {

    // Event emitted when a successful external call is made
    event ExternalCallSuccess(address indexed target, bytes data);
    
    // Event emitted when an external call fails
    event ExternalCallFailure(address indexed target, bytes data, string reason);

    /// @notice Function to make an external call with a given call data hash.
    /// @param target The target address to call.
    /// @param callData The call data to send, encoded as bytes.
    /// @param callDataHash The hash of the call data for validation.
    function makeExternalCall(
        address target,
        bytes memory callData,
        bytes32 callDataHash
    ) public returns (bool) {
        // Validate the call data hash to ensure data integrity
        require(keccak256(callData) == callDataHash, "Invalid call data hash");

        // Attempt to make the external call
        (bool success, bytes memory returnData) = target.call(callData);
        
        // Emit event based on success or failure of the call
        if (success) {
            emit ExternalCallSuccess(target, callData);
            return true;
        } else {
            // Decode the revert reason if available
            string memory reason = _getRevertReason(returnData);
            emit ExternalCallFailure(target, callData, reason);
            return false;
        }
    }

    /// @notice Internal function to extract revert reason from returned data.
    /// @param returnData The data returned from the failed call.
    /// @return reason The revert reason as a string.
    function _getRevertReason(bytes memory returnData) internal pure returns (string memory reason) {
        // If the return data is empty, return a generic reason
        if (returnData.length == 0) {
            return "Unknown error";
        }
        
        // Extract the revert reason (first 68 bytes)
        assembly {
            // Check if the length is at least 68 bytes (0x08 for the function selector)
            // If true, return the revert reason
            if lt(mload(returnData), 68) {
                reason := "Unknown error"
            } else {
                reason := add(returnData, 0x04) // Skip the function selector
            }
        }
    }
}
```
