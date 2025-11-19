"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: Write a Solidity smart contract that is optimized for deployment on Linea's zkEVM ecosystem, ensuring compatibility with its EVM bytecode and leveraging low gas fees.
Generated: DETERMINISTIC_e7f9bf41837c9986
Batch ID: 20250612_152249
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

/// @title SimpleStorage
/// @notice A simple smart contract to store and retrieve a value
/// @dev This contract is optimized for deployment on Linea's zkEVM ecosystem
contract SimpleStorage {
    // State variable to store a value
    uint256 private storedValue;

    /// @notice Event emitted when the stored value is updated
    /// @param oldValue The previous value stored
    /// @param newValue The new value stored
    event ValueUpdated(uint256 oldValue, uint256 newValue);

    /// @notice Stores a new value
    /// @param newValue The new value to store
    /// @dev Emits a ValueUpdated event
    function store(uint256 newValue) external {
        uint256 oldValue = storedValue; // Store the old value for the event
        storedValue = newValue; // Update the stored value
        emit ValueUpdated(oldValue, newValue); // Emit the event
    }

    /// @notice Retrieves the currently stored value
    /// @return The currently stored value
    function retrieve() external view returns (uint256) {
        return storedValue; // Return the stored value
    }

    /// @notice Deletes the stored value
    /// @dev Resets the stored value to zero
    function clear() external {
        storedValue = 0; // Reset the stored value
        emit ValueUpdated(storedValue, 0); // Emit event for clarity
    }
}
```
