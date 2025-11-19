"""
Generated Code Metadata:
========================
Original URL: https://orikod.com
Prompt: Develop a smart contract for a micro-payment app using Arbitrum AnyTrust chains, ensuring maximum speed and minimal cost while maintaining full security guarantees.
Generated: DETERMINISTIC_1a0f96e119995951
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title MicroPaymentApp
 * @dev A smart contract for handling micro-payments on Arbitrum AnyTrust chains.
 *      Designed for maximum speed, minimal cost, and full security guarantees.
 */
contract MicroPaymentApp {
    // Events
    event PaymentSent(address indexed sender, address indexed recipient, uint256 amount);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // Mapping to store balances of users
    mapping(address => uint256) private balances;

    /**
     * @dev Deposit funds into the contract.
     *      Users can deposit funds to their balance for future micro-payments.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
    }

    /**
     * @dev Send a micro-payment to another user.
     * @param recipient The address of the recipient.
     * @param amount The amount to send.
     */
    function sendPayment(address recipient, uint256 amount) external {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Payment amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct the amount from sender's balance
        balances[msg.sender] -= amount;

        // Add the amount to recipient's balance
        balances[recipient] += amount;

        emit PaymentSent(msg.sender, recipient, amount);
    }

    /**
     * @dev Withdraw funds from the contract.
     *      Users can withdraw their balance to their wallet.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct the amount from user's balance
        balances[msg.sender] -= amount;

        // Transfer the amount to the user's wallet
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the balance of a user.
     * @param user The address of the user.
     * @return The balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to handle Ether sent directly to the contract.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
