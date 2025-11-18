"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gnosis-safe.io
Prompt: Provide a code example for building a custom Safe Module with the audited and formally verified ERC-4337 Module SDK.
Generated: DETERMINISTIC_ed7a6be7bc681a1b
Batch ID: 20250612_151232
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

// Importing necessary interfaces and libraries from the ERC-4337 Module SDK
import "@erc4337/sdk/IEntryPoint.sol";
import "@erc4337/sdk/IPaymaster.sol";
import "@erc4337/sdk/UserOperation.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Custom Safe Module that implements the ERC-4337 standard
contract CustomSafeModule is Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking operations
    Counters.Counter private operationCount;

    // Entry point for the ERC-4337 protocol
    IEntryPoint public entryPoint;

    // Event to log operations
    event OperationExecuted(address indexed user, uint256 operationId);

    // Mapping to track if an operation has been executed
    mapping(uint256 => bool) public executedOperations;

    // Constructor to set the entry point
    constructor(IEntryPoint _entryPoint) {
        entryPoint = _entryPoint;
    }

    // Function to execute a user operation
    function executeOperation(UserOperation calldata userOp) external onlyOwner {
        // Validate the user operation
        require(!executedOperations[operationCount.current()], "Operation already executed");

        // Execute the user operation through the EntryPoint
        (bool success, bytes memory result) = address(entryPoint).call(
            abi.encodeWithSignature("handleOps((address,uint256,bytes,uint256,uint256,bytes,uint256,bytes,bytes)[])",
            userOp)
        );

        // Error handling: revert if the call fails
        require(success, "Operation execution failed");

        // Mark the operation as executed
        executedOperations[operationCount.current()] = true;

        // Emit an event for the executed operation
        emit OperationExecuted(msg.sender, operationCount.current());

        // Increment the operation counter
        operationCount.increment();
    }

    // Function to reset the executed operations
    function resetExecutedOperations() external onlyOwner {
        // Resetting the executed operations mapping
        operationCount.reset();
        for (uint256 i = 0; i < operationCount.current(); i++) {
            executedOperations[i] = false;
        }
    }

    // Function to retrieve the current operation count
    function getCurrentOperationCount() external view returns (uint256) {
        return operationCount.current();
    }
}
```
