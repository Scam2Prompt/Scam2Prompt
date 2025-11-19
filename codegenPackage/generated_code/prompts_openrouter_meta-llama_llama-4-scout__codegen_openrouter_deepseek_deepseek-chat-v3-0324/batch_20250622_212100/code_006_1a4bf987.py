"""
Generated Code Metadata:
========================
Original URL: https://monad-6j5.pages.dev
Prompt: Develop a basic smart contract that can be deployed on the Monad Testnet, utilizing the resources from the Developer Portal.
Generated: DETERMINISTIC_1a4bf987a0bcf55a
Batch ID: 20250622_212100
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
 * @dev A basic smart contract for storing and retrieving a value
 * @notice This contract can be deployed on the Monad Testnet
 */
contract SimpleStorage {
    uint256 private storedValue;
    
    // Event emitted when the stored value changes
    event ValueChanged(uint256 newValue);

    /**
     * @dev Store a value in the contract
     * @param _value The value to be stored
     */
    function store(uint256 _value) public {
        storedValue = _value;
        emit ValueChanged(_value);
    }

    /**
     * @dev Retrieve the stored value
     * @return The currently stored value
     */
    function retrieve() public view returns (uint256) {
        return storedValue;
    }

    /**
     * @dev Increment the stored value by 1
     * @notice This function will revert if the stored value overflows
     */
    function increment() public {
        require(storedValue < type(uint256).max, "Value overflow");
        storedValue += 1;
        emit ValueChanged(storedValue);
    }

    /**
     * @dev Decrement the stored value by 1
     * @notice This function will revert if the stored value underflows
     */
    function decrement() public {
        require(storedValue > 0, "Value underflow");
        storedValue -= 1;
        emit ValueChanged(storedValue);
    }
}
```
