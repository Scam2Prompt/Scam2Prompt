"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad.docsbot.app
Prompt: Create an example of a smart contract that can be deployed on Monad, highlighting its compatibility with EVM bytecode.
Generated: DETERMINISTIC_9307b7924322f590
Batch ID: 20250612_160124
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

/// @title Example Smart Contract for Monad
/// @notice This contract serves as an example of a simple storage contract compatible with EVM bytecode
/// @dev The contract allows for storing and retrieving a value
contract SimpleStorage {
    // State variable to hold the stored value
    uint256 private storedValue;

    // Event emitted when the value is set
    event ValueSet(uint256 indexed newValue);

    /// @notice Sets the stored value
    /// @param _value The new value to be stored
    /// @dev Emits a ValueSet event upon successful value setting
    function setValue(uint256 _value) external {
        // Update the stored value
        storedValue = _value;

        // Emit the event indicating the value has been set
        emit ValueSet(_value);
    }

    /// @notice Retrieves the stored value
    /// @return The current stored value
    function getValue() external view returns (uint256) {
        return storedValue;
    }

    /// @notice Reset the stored value to zero
    /// @dev Emits a ValueSet event with a value of zero
    function resetValue() external {
        storedValue = 0;
        emit ValueSet(0);
    }
}
```
