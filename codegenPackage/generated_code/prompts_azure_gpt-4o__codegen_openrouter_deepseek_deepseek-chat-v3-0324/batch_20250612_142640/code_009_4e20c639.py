"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: Explain and provide code demonstrating how ParaSwap can be used to safely forward call data hash for censorship resistance in Ethereum smart contracts.
Generated: DETERMINISTIC_4e20c639c8bf2b84
Batch ID: 20250612_142640
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

/**
 * @title ParaSwapForwarder
 * @dev A contract that forwards call data to ParaSwap while maintaining censorship resistance
 * by using a hash of the call data for verification.
 */
contract ParaSwapForwarder {
    // Event to log forwarded calls
    event Forwarded(
        address indexed sender,
        bytes32 indexed callDataHash,
        address target,
        uint256 value,
        bytes callData
    );

    // Mapping to store processed call data hashes to prevent replay attacks
    mapping(bytes32 => bool) public processedHashes;

    /**
     * @dev Forwards a call to ParaSwap after verifying the call data hash
     * @param target The address of the ParaSwap contract to call
     * @param value The amount of ETH to send with the call
     * @param callData The call data to forward
     * @param callDataHash The keccak256 hash of the call data for verification
     */
    function forwardCall(
        address target,
        uint256 value,
        bytes calldata callData,
        bytes32 callDataHash
    ) external payable {
        // Verify the call data matches the provided hash
        require(
            keccak256(callData) == callDataHash,
            "ParaSwapForwarder: call data hash mismatch"
        );

        // Ensure this hash hasn't been processed before
        require(
            !processedHashes[callDataHash],
            "ParaSwapForwarder: call data already processed"
        );

        // Mark this hash as processed
        processedHashes[callDataHash] = true;

        // Verify the sent value matches the specified value
        require(
            msg.value == value,
            "ParaSwapForwarder: incorrect ETH value sent"
        );

        // Forward the call to ParaSwap
        (bool success, ) = target.call{value: value}(callData);
        require(
            success,
            "ParaSwapForwarder: call forwarding failed"
        );

        // Emit event for censorship resistance
        emit Forwarded(
            msg.sender,
            callDataHash,
            target,
            value,
            callData
        );
    }

    /**
     * @dev Verifies if a call data hash has been processed
     * @param callDataHash The hash to check
     * @return bool True if the hash has been processed
     */
    function isHashProcessed(bytes32 callDataHash) external view returns (bool) {
        return processedHashes[callDataHash];
    }
}
```
