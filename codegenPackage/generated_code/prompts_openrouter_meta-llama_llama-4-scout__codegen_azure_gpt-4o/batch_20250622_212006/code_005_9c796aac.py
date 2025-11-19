"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Design a basic smart contract for managing cannabis investment funds using blockchain technology.
Generated: DETERMINISTIC_9c796aaced9b4bb9
Batch ID: 20250622_212006
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
 * @title CannabisInvestmentFund
 * @dev A smart contract to manage cannabis investment funds.
 * Investors can deposit funds, withdraw funds, and view their balances.
 */
contract CannabisInvestmentFund {
    // Mapping to store balances of each investor
    mapping(address => uint256) private balances;

    // Owner of the contract
    address public owner;

    // Event emitted when funds are deposited
    event FundsDeposited(address indexed investor, uint256 amount);

    // Event emitted when funds are withdrawn
    event FundsWithdrawn(address indexed investor, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows an investor to deposit funds into the contract.
     * Emits a FundsDeposited event.
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Allows an investor to withdraw funds from the contract.
     * Emits a FundsWithdrawn event.
     * @param amount The amount to withdraw.
     */
    function withdrawFunds(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Returns the balance of the caller.
     * @return The balance of the caller.
     */
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    /**
     * @dev Allows the owner to withdraw all funds from the contract.
     * Only callable by the owner.
     */
    function withdrawAllFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available to withdraw");
        
        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to handle Ether sent directly to the contract.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
