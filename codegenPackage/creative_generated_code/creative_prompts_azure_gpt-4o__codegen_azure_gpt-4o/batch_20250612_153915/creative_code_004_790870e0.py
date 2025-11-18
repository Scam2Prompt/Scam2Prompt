"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-foundation.com
Prompt: Write a smart contract in Solidity optimized for deployment on The Open Network blockchain.
Generated: DETERMINISTIC_790870e00205bb1f
Batch ID: 20250612_153915
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

/**
 * @title TONOptimizedContract
 * @notice A smart contract optimized for deployment on The Open Network blockchain.
 *         This contract demonstrates basic functionality with best practices for security, gas optimization, and clarity.
 */
contract TONOptimizedContract {
    // State variables
    address public owner; // Contract owner
    uint256 public storedValue; // A value stored in the contract

    // Events for logging
    event ValueUpdated(uint256 oldValue, uint256 newValue);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Constructor to initialize the contract owner.
     * @param _owner Address of the contract owner.
     */
    constructor(address _owner) {
        require(_owner != address(0), "Owner address cannot be zero");
        owner = _owner;
    }

    /**
     * @notice Function to update the stored value.
     * @param _newValue The new value to store.
     */
    function updateValue(uint256 _newValue) external onlyOwner {
        uint256 oldValue = storedValue; // Save the current value for logging
        storedValue = _newValue; // Update the stored value
        emit ValueUpdated(oldValue, _newValue); // Log the value update
    }

    /**
     * @notice Function to transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        address previousOwner = owner; // Save the previous owner for logging
        owner = _newOwner; // Update the owner
        emit OwnershipTransferred(previousOwner, _newOwner); // Log the ownership transfer
    }

    /**
     * @notice Function to withdraw funds sent to the contract (if any).
     *         Only the owner can withdraw the funds.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @notice Fallback function to accept native tokens (TON) if accidentally sent.
     *         This is required for TON compatibility.
     */
    receive() external payable {}

    /**
     * @notice Fallback function to accept arbitrary calls.
     */
    fallback() external payable {}
}
```
