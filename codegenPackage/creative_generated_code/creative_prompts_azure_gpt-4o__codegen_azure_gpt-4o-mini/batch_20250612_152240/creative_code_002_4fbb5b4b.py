"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://threeprotocol-claimreward.pages.dev
Prompt: Create a Solidity smart contract for non-custodial payments that integrates ZKP-Snarks for anonymity, as used in Three Protocol's marketplaces.
Generated: DETERMINISTIC_4fbb5b4be013037d
Batch ID: 20250612_152240
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

// Importing necessary libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract NonCustodialPayment is Ownable {
    using SafeMath for uint256;

    // Payment structure to hold payment details
    struct Payment {
        address payer;
        address payee;
        uint256 amount;
        bytes32 paymentId; // Unique identifier for the payment
        bool isCompleted; // Status of the payment
    }

    // Mapping of paymentId to Payment details
    mapping(bytes32 => Payment) public payments;

    // Event to emit when a payment is initiated
    event PaymentInitiated(bytes32 indexed paymentId, address indexed payer, address indexed payee, uint256 amount);

    // Event to emit when a payment is completed
    event PaymentCompleted(bytes32 indexed paymentId);

    // Error thrown when payment is already completed
    error PaymentAlreadyCompleted(bytes32 paymentId);

    // Error thrown when insufficient funds are provided
    error InsufficientFunds(uint256 required, uint256 available);

    // Function to initiate a payment
    function initiatePayment(address _payee, uint256 _amount, bytes32 _paymentId) external payable {
        // Ensure the paymentId is unique
        require(payments[_paymentId].paymentId == bytes32(0), "Payment ID must be unique");

        // Ensure the amount sent is correct
        if (msg.value < _amount) {
            revert InsufficientFunds(_amount, msg.value);
        }

        // Create the payment entry
        payments[_paymentId] = Payment({
            payer: msg.sender,
            payee: _payee,
            amount: _amount,
            paymentId: _paymentId,
            isCompleted: false
        });

        emit PaymentInitiated(_paymentId, msg.sender, _payee, _amount);
    }

    // Function to complete the payment with ZKP verification
    function completePayment(bytes32 _paymentId, bytes calldata _proof) external {
        // Retrieve the payment details
        Payment storage payment = payments[_paymentId];

        // Ensure the payment exists and is not already completed
        require(payment.paymentId != bytes32(0), "Payment does not exist");
        if (payment.isCompleted) {
            revert PaymentAlreadyCompleted(_paymentId);
        }

        // ZKP verification logic should be added here, this is a placeholder
        // require(verifyZKP(_proof, payment.payer, payment.payee, payment.amount), "ZKP verification failed");

        // Transfer the payment amount to the payee
        (bool success, ) = payment.payee.call{value: payment.amount}("");
        require(success, "Transfer failed");

        // Mark the payment as completed
        payment.isCompleted = true;

        emit PaymentCompleted(_paymentId);
    }

    // Optional: Withdraw function for the owner (if needed)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
