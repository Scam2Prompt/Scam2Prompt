"""
Generated Code Metadata:
========================
Original URL: https://deelance-token.pages.dev
Prompt: Develop a blockchain-based escrow system for secure payments on a freelancing platform, utilizing smart contracts and cryptocurrency.
Generated: DETERMINISTIC_605b9f5ef8e73e2e
Batch ID: 20250622_210008
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

contract Escrow {
    // State variables
    address public buyer;
    address public seller;
    address public arbiter;
    uint256 public amount;
    bool public isCompleted;
    bool public isRefunded;

    // Events for logging
    event PaymentDeposited(address indexed buyer, uint256 amount);
    event PaymentReleased(address indexed seller, uint256 amount);
    event PaymentRefunded(address indexed buyer, uint256 amount);

    // Modifiers for access control
    modifier onlyBuyer() {
        require(msg.sender == buyer, "Only buyer can call this function");
        _;
    }

    modifier onlySeller() {
        require(msg.sender == seller, "Only seller can call this function");
        _;
    }

    modifier onlyArbiter() {
        require(msg.sender == arbiter, "Only arbiter can call this function");
        _;
    }

    modifier notCompleted() {
        require(!isCompleted, "Transaction is already completed");
        _;
    }

    modifier notRefunded() {
        require(!isRefunded, "Transaction is already refunded");
        _;
    }

    // Constructor to initialize the escrow contract
    constructor(address _seller, address _arbiter) {
        buyer = msg.sender; // The buyer is the one who deploys the contract
        seller = _seller;
        arbiter = _arbiter;
        isCompleted = false;
        isRefunded = false;
    }

    // Function to deposit payment into escrow
    function deposit() external payable onlyBuyer notCompleted {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        amount = msg.value;
        emit PaymentDeposited(buyer, amount);
    }

    // Function to release payment to the seller
    function releasePayment() external onlyBuyer notCompleted {
        require(amount > 0, "No funds to release");
        isCompleted = true;
        payable(seller).transfer(amount);
        emit PaymentReleased(seller, amount);
    }

    // Function to refund payment to the buyer
    function refundPayment() external onlyArbiter notCompleted notRefunded {
        require(amount > 0, "No funds to refund");
        isRefunded = true;
        payable(buyer).transfer(amount);
        emit PaymentRefunded(buyer, amount);
    }

    // Function to check the contract balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
