"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.eu
Prompt: Generate Solidity code for a smart contract optimized for the Arbitrum Layer 2 network, including gas-efficient functions.
Generated: DETERMINISTIC_b8de8149d1d55434
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// A gas-efficient, production-ready smart contract optimized for the Arbitrum Layer 2 network.
contract ArbitrumOptimizedContract {
    // Owner of the contract
    address public owner;

    // Mapping to store balances for each address
    mapping(address => uint256) private balances;

    // Events for logging critical actions
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to certain functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the deployer as the initial owner
    constructor() {
        owner = msg.sender;
        emit OwnershipTransferred(address(0), msg.sender);
    }

    // Function to deposit ETH into the contract
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;

        // Emit event for deposit
        emit Deposit(msg.sender, msg.value);
    }

    // Function to withdraw ETH from the contract
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balance before transferring to prevent reentrancy attacks
        balances[msg.sender] -= amount;

        // Transfer ETH back to the caller
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        // Emit event for withdrawal
        emit Withdrawal(msg.sender, amount);
    }

    // Function to check the balance of a specific address
    function balanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to transfer ownership of the contract to a new address
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Function to rescue accidentally sent funds (only owner can execute this)
    function rescueFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to rescue");

        // Transfer all contract balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "ETH transfer failed");
    }
}
```
