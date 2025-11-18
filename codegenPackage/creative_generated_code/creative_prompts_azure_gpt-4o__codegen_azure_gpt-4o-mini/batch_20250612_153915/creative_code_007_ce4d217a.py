"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-foundation.com
Prompt: Recommend best practices for securing smart contracts on The Open Network and provide code examples.
Generated: DETERMINISTIC_ce4d217a68fadb50
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

// Smart contract for demonstration of best practices in securing smart contracts
contract SecureContract {
    // Mapping to store balances of users
    mapping(address => uint256) private balances;

    // Event to log deposit actions
    event Deposited(address indexed user, uint256 amount);

    // Event to log withdrawal actions
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to check if the caller has sufficient balance
    modifier hasSufficientBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        _;
    }

    // Function to deposit Ether into the contract
    function deposit() external payable {
        require(msg.value > 0, "Deposit must be greater than 0");

        // Update the balance of the sender
        balances[msg.sender] += msg.value;

        // Emit an event for the deposit
        emit Deposited(msg.sender, msg.value);
    }

    // Function to withdraw Ether from the contract
    function withdraw(uint256 amount) external hasSufficientBalance(amount) {
        // Update the balance before transferring to prevent re-entrancy
        balances[msg.sender] -= amount;

        // Use call to transfer Ether, which forwards gas and is considered safer
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit an event for the withdrawal
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of a specific user
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
