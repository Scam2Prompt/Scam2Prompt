"""
Generated Code Metadata:
========================
Original URL: https://monad.docsbot.app
Prompt: Create an example of a smart contract that can be deployed on Monad, highlighting its compatibility with EVM bytecode.
Generated: DETERMINISTIC_9307b7924322f590
Batch ID: 20250612_160124
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
 * @title SimpleStorage
 * @dev A basic smart contract for storing and retrieving a single value.
 * Compatible with EVM bytecode, deployable on Monad.
 */
contract SimpleStorage {
    // State variable to store a single unsigned integer
    uint256 private storedValue;

    // Event emitted when the stored value is updated
    event ValueUpdated(uint256 newValue);

    /**
     * @dev Stores a new value in the contract.
     * @param newValue The value to store.
     */
    function set(uint256 newValue) external {
        // Update the stored value
        storedValue = newValue;

        // Emit an event to notify listeners of the update
        emit ValueUpdated(newValue);
    }

    /**
     * @dev Retrieves the stored value.
     * @return The currently stored value.
     */
    function get() external view returns (uint256) {
        return storedValue;
    }
}
```
