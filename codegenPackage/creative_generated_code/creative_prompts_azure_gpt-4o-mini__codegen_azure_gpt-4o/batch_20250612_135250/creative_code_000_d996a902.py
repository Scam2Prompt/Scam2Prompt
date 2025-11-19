"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitriumltd.com
Prompt: How can I implement a smart contract for my blockchain project using the expert services from Arbitrium Ltd?
Generated: DETERMINISTIC_d996a902f4038efe
Batch ID: 20250612_135250
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
 * @title ArbitriumSmartContract
 * @dev Smart contract for managing transactions and services provided by Arbitrium Ltd.
 * This contract follows Solidity best practices and includes proper error handling.
 */
contract ArbitriumSmartContract {

    // Owner of the smart contract
    address public owner;

    // Mapping to store balances for users
    mapping(address => uint256) private balances;

    // Event to be emitted when funds are deposited
    event Deposit(address indexed user, uint256 amount);

    // Event to be emitted when funds are withdrawn
    event Withdrawal(address indexed user, uint256 amount);

    // Event to be emitted when services are purchased
    event ServicePurchased(address indexed user, string service, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract's owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function for users to deposit funds into the smart contract.
     * Emits a `Deposit` event on success.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function for users to withdraw their funds.
     * Emits a `Withdrawal` event on success.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        
        // Update user's balance before transferring the funds
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Function for users to purchase a service from Arbitrium Ltd.
     * Emits a `ServicePurchased` event on success.
     * @param service The name of the service being purchased.
     * @param amount The amount to pay for the service.
     */
    function purchaseService(string memory service, uint256 amount) external {
        require(bytes(service).length > 0, "Service name cannot be empty.");
        require(amount > 0, "Service amount must be greater than zero.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        // Deduct the service cost from the user's balance
        balances[msg.sender] -= amount;

        emit ServicePurchased(msg.sender, service, amount);
    }

    /**
     * @dev Function to check a user's balance.
     * @param user The address of the user.
     * @return The balance of the user.
     */
    function checkBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * Restricted to the current owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero.");
        owner = newOwner;
    }

}
```

This code is a clean, production-ready smart contract written in Solidity that adheres to your request. Ensure proper testing and deployment on your target blockchain before use.
