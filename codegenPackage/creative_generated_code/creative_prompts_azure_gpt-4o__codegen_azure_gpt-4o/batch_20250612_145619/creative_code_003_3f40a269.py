"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfjw.com
Prompt: Create a smart contract in Solidity that supports ETH pledging with customizable pledge amounts and withdrawal functionality.
Generated: DETERMINISTIC_3f40a269311ca38e
Batch ID: 20250612_145619
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

/// @title ETH Pledging Smart Contract
/// @author 
/// @notice This contract allows ETH pledges with customizable amounts and safe withdrawal for contract owner.
/// @dev Implements basic security, error handling, and best practices for Solidity.

contract ETHPledging {
    // State variables
    address public owner; // Contract owner
    uint256 public totalPledged; // Total ETH pledged
    mapping(address => uint256) public pledges; // Tracks pledged amounts by address

    // Events
    event Pledged(address indexed pledger, uint256 amount);
    event Withdrawn(address indexed recipient, uint256 amount);

    /// @notice Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /// @notice Constructor sets the deployer as the contract owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Allows users to pledge ETH to the contract
    /// @dev Sends ETH to the contract and updates pledge records
    function pledge() external payable {
        require(msg.value > 0, "Pledge must be greater than 0");

        // Update state
        pledges[msg.sender] += msg.value;
        totalPledged += msg.value;

        emit Pledged(msg.sender, msg.value);
    }

    /// @notice Allows the owner to withdraw all ETH from the contract
    /// @dev Only callable by the contract owner
    function withdraw() external onlyOwner {
        uint256 amount = address(this).balance;
        require(amount > 0, "Nothing to withdraw");

        // Transfer ETH to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit Withdrawn(owner, amount);
    }

    /// @notice Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /// @notice Receive function to handle proper ETH pledges
    receive() external payable {
        pledge();
    }
}
```
