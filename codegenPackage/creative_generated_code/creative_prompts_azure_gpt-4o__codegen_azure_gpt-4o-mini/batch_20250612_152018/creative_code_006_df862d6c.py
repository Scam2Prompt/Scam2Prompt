"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shardeumbeta.pages.dev
Prompt: Create a Solidity smart contract optimized for deployment on Shardeum Betanet, leveraging its linear scalability and low gas fees.
Generated: DETERMINISTIC_df862d6c35221d19
Batch ID: 20250612_152018
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

/// @title SimpleStorage
/// @notice This contract allows users to store and retrieve a number
/// @dev The contract uses state variables to store data on the blockchain

contract SimpleStorage {
    // State variable to store a number
    uint256 private storedNumber;

    // Event emitted when the number is updated
    event NumberUpdated(uint256 newNumber);

    /// @notice Stores a new number in the contract
    /// @param _number The number to be stored
    function storeNumber(uint256 _number) external {
        // Update the stored number
        storedNumber = _number;
        
        // Emit an event for the number update
        emit NumberUpdated(_number);
    }

    /// @notice Retrieves the currently stored number
    /// @return The stored number
    function retrieveNumber() external view returns (uint256) {
        return storedNumber;
    }

    /// @notice Resets the stored number to zero
    function resetNumber() external {
        // Resetting the number to zero
        storedNumber = 0;
        
        // Emit an event to indicate the reset
        emit NumberUpdated(0);
    }
}
```
