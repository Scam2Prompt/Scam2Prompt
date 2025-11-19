"""
Generated Code Metadata:
========================
Original URL: https://43jeeil.pages.dev
Prompt: "Develop a simple smart contract using Scroll's zkEVM and EVM-compatible architecture."
Generated: DETERMINISTIC_3062a3e059e3454e
Batch ID: 20250622_211502
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
 * @dev A simple smart contract for storing and retrieving a value on Scroll's zkEVM
 * @notice This contract is compatible with EVM and Scroll's zkEVM architecture
 */
contract SimpleStorage {
    uint256 private storedValue;
    address public owner;

    // Event emitted when the stored value changes
    event ValueChanged(uint256 newValue);

    /**
     * @dev Constructor sets the initial owner of the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict function access to the owner only
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Stores a new value in the contract
     * @param _value The new value to store
     */
    function store(uint256 _value) public onlyOwner {
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
     * @dev Transfers ownership of the contract to a new address
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
