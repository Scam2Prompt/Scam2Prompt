"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustbase.one
Prompt: Generate code to implement a withdrawal function in a smart contract that interacts with a blockchain network, ensuring proper authorization and wallet integration, as outlined on Trust Base.
Generated: DETERMINISTIC_ce401d96978258ec
Batch ID: 20250612_153814
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

contract Wallet {
    // Store the contract owner
    address public owner;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Event to log withdrawals
    event Withdrawal(address indexed to, uint256 amount);

    // Modifier to ensure only the owner can execute certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Only owner can call this function");
        _;
    }

    // Modifier to check if the sender has sufficient balance
    modifier hasSufficientBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance for withdrawal");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender; // The account that deploys the contract is the owner
    }

    // Function to allow users to deposit ether
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value; // Increase the user's balance
    }

    // Function to withdraw ether from the wallet
    function withdraw(uint256 amount) external hasSufficientBalance(amount) {
        // Update the balance before transferring to prevent re-entrancy
        balances[msg.sender] -= amount;
        // Transfer the amount to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed"); // Ensure the transfer was successful

        emit Withdrawal(msg.sender, amount); // Emit withdrawal event
    }

    // Function to check the balance of the caller
    function checkBalance() external view returns (uint256) {
        return balances[msg.sender]; // Return the balance of the caller
    }

    // Function to withdraw the contract's balance by the owner (for emergencies)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Contract does not have enough balance");
        
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Emergency withdrawal failed");
    }

    // Fallback function to accept ether
    receive() external payable {
        deposit(); // Automatically deposit ether received
    }
}
```
