"""
Generated Code Metadata:
========================
Original URL: https://jaiosdfojidsijfaaa.web.app
Prompt: Design a smart contract for a Web3 payments platform that enables unverified recipient transactions, using the Solana network and incorporating a first-come-first-served (FCFS) system.
Generated: DETERMINISTIC_6bc47d3ab2f11d6c
Batch ID: 20250622_211113
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

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a Web3 payments platform
contract Web3Payments is Ownable {
    // Event emitted when a payment is made
    event PaymentMade(address indexed sender, address indexed recipient, uint256 amount, uint256 timestamp);

    // Struct to hold payment details
    struct Payment {
        address sender;
        address recipient;
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to store payments by their ID
    mapping(uint256 => Payment) public payments;
    uint256 public paymentCount;

    // Function to make a payment
    function makePayment(address recipient, uint256 amount) external {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the specified amount of tokens from the sender to the recipient
        IERC20 token = IERC20(address(this)); // Assuming the contract itself holds the tokens
        require(token.transferFrom(msg.sender, recipient, amount), "Token transfer failed");

        // Create a new payment record
        payments[paymentCount] = Payment(msg.sender, recipient, amount, block.timestamp);
        paymentCount++;

        // Emit the payment event
        emit PaymentMade(msg.sender, recipient, amount, block.timestamp);
    }

    // Function to retrieve payment details by ID
    function getPayment(uint256 paymentId) external view returns (Payment memory) {
        require(paymentId < paymentCount, "Payment ID does not exist");
        return payments[paymentId];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
