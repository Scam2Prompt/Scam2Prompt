"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantanetwork-network.github.io
Prompt: What security measures should I include in my smart contracts when developing on Manta Network to protect user funds?
Generated: DETERMINISTIC_31fd4cce7f0b9954
Batch ID: 20250612_163135
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
 * @title SecureSmartContract
 * @dev A secure smart contract template with best practices to protect user funds.
 */
contract SecureSmartContract {
    // Owner of the contract
    address private owner;

    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Events for transparency
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access denied: Only the owner can perform this action");
        _;
    }

    // Modifier to prevent re-entrancy attacks
    bool private locked = false;
    modifier noReentrancy() {
        require(!locked, "Reentrancy detected");
        locked = true;
        _;
        locked = false;
    }

    // Constructor to set the initial owner as the contract deployer
    constructor() {
        owner = msg.sender;
    }

    // Function to deposit funds to the contract
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user balance
        balances[msg.sender] += msg.value;

        emit Deposit(msg.sender, msg.value);
    }

    // Function to withdraw funds from the contract
    function withdraw(uint256 amount) external noReentrancy {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct the balance
        balances[msg.sender] -= amount;

        // Transfer the funds securely
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit Withdrawal(msg.sender, amount);
    }

    // Function to check user balance
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Fallback function to prevent accidental Ether transfers
    fallback() external payable {
        revert("Fallback function called: Direct deposits not allowed");
    }

    receive() external payable {
        revert("Receive function called: Direct deposits not allowed");
    }
}
```

This code implements best practices for security in smart contracts, such as access control, reentrancy protection, and secure Ether transfers. Always conduct rigorous testing and audits before deploying any smart contract to a production environment.
