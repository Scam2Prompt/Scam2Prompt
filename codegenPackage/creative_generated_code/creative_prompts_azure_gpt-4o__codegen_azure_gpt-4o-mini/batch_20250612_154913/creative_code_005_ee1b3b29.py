"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-ten.vercel.app
Prompt: Create a payment system smart contract for retail payments using Linea's zk rollup, ensuring low transaction costs and compatibility with MetaMask.
Generated: DETERMINISTIC_ee1b3b2970b285a0
Batch ID: 20250612_154913
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

// Importing OpenZeppelin's Ownable contract to manage ownership
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title RetailPayment
 * @dev A smart contract for handling retail payments using Linea's zk-Rollup.
 * This contract allows users to make payments in ERC20 tokens.
 */
contract RetailPayment is Ownable {
    // Event emitted when a payment is successfully made
    event PaymentMade(address indexed payer, address indexed recipient, uint256 amount, string note);

    // Mapping to keep track of payments made by each user
    mapping(address => mapping(address => uint256)) public payments;

    // ERC20 token interface
    IERC20 public token;

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token The address of the ERC20 token to be used for payments.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Function to make a payment.
     * @param recipient The address of the recipient.
     * @param amount The amount to be paid.
     * @param note An optional note to accompany the payment.
     */
    function makePayment(address recipient, uint256 amount, string memory note) external {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Payment amount must be greater than zero");

        // Transfer the payment amount from the payer to the recipient
        bool success = token.transferFrom(msg.sender, recipient, amount);
        require(success, "Token transfer failed");

        // Update the payments mapping
        payments[msg.sender][recipient] += amount;

        // Emit the payment event
        emit PaymentMade(msg.sender, recipient, amount, note);
    }

    /**
     * @dev Function to retrieve the payment history for a specific recipient.
     * @param recipient The address of the recipient.
     * @return The total amount paid to the recipient by the caller.
     */
    function getPaymentHistory(address recipient) external view returns (uint256) {
        return payments[msg.sender][recipient];
    }
}
```
