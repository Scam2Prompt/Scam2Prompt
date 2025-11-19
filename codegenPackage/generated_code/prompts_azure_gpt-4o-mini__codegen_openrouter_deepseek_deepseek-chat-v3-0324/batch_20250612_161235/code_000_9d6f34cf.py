"""
Generated Code Metadata:
========================
Original URL: https://monad.at
Prompt: Write a Solidity smart contract that can be deployed on the Monad blockchain, ensuring it takes advantage of the 100% EVM compatibility without requiring code changes.
Generated: DETERMINISTIC_9d6f34cfcd3e1797
Batch ID: 20250612_161235
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
 * @dev A simple smart contract for storing and retrieving a value
 * @notice This contract is fully EVM compatible and can be deployed on Monad blockchain
 */
contract SimpleStorage {
    uint256 private storedValue;
    
    // Event emitted when the stored value changes
    event ValueChanged(uint256 newValue);

    /**
     * @dev Stores a new value in the contract
     * @param _value The new value to store
     */
    function store(uint256 _value) public {
        storedValue = _value;
        emit ValueChanged(_value);
    }

    /**
     * @dev Retrieves the stored value
     * @return The currently stored value
     */
    function retrieve() public view returns (uint256) {
        return storedValue;
    }

    /**
     * @dev Increments the stored value by 1
     */
    function increment() public {
        require(storedValue < type(uint256).max, "Value overflow");
        storedValue += 1;
        emit ValueChanged(storedValue);
    }

    /**
     * @dev Decrements the stored value by 1
     */
    function decrement() public {
        require(storedValue > 0, "Value underflow");
        storedValue -= 1;
        emit ValueChanged(storedValue);
    }
}
```
