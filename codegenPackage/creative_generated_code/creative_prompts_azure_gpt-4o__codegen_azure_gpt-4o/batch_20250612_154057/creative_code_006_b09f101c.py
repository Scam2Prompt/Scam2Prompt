"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-coinbase-com.kagiproxy.com
Prompt: Create a smart contract on Ethereum L2 (Base) using Coinbase's developer tools to facilitate onchain payments.
Generated: DETERMINISTIC_b09f101c624254c6
Batch ID: 20250612_154057
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
 * @title PaymentProcessor
 * @dev A smart contract for handling on-chain payments on Ethereum L2 (Base).
 */
contract PaymentProcessor {
    // Event emitted when a payment is successfully processed
    event PaymentReceived(address indexed payer, address indexed payee, uint256 amount);

    // Event emitted when funds are withdrawn by the owner
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Contract constructor that sets the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to make payments to a specific payee.
     * @param payee The address of the recipient.
     */
    function makePayment(address payee) external payable {
        require(payee != address(0), "Invalid payee address");
        require(msg.value > 0, "Payment amount must be greater than zero");

        // Transfer the payment to the payee
        (bool success, ) = payee.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        // Emit the PaymentReceived event
        emit PaymentReceived(msg.sender, payee, msg.value);
    }

    /**
     * @dev Allows the contract owner to withdraw any remaining funds in the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the funds to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw transfer failed");

        // Emit the FundsWithdrawn event
        emit FundsWithdrawn(owner, balance);
    }

    /**
     * @dev Fallback function to handle incoming ether.
     */
    receive() external payable {
        // Accept any ether sent to the contract
    }

    /**
     * @dev Fallback function to handle unexpected calls.
     */
    fallback() external payable {
        // Accept any ether sent to the contract
    }
}
```

This code implements a simple payment processing smart contract that allows users to send payments to specific payees and ensures that the owner can withdraw remaining funds securely. It adheres to Solidity best practices, includes proper error handling, and is fully commented for clarity.
