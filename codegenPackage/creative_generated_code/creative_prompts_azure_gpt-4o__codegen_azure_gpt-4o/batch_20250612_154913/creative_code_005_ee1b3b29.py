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
pragma solidity ^0.8.17;

/**
 * @title PaymentSystem
 * @notice A smart contract for retail payments using Linea's zk rollup, ensuring low transaction costs and MetaMask compatibility
 */
contract PaymentSystem {
    // Address of the contract owner
    address public owner;

    // Event emitted when a payment is successful
    event PaymentSuccessful(address indexed payer, uint256 amount, uint256 timestamp);

    // Event emitted when funds are withdrawn from the contract
    event FundsWithdrawn(address indexed owner, uint256 amount, uint256 timestamp);

    // Modifier to restrict access to certain functions for the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to set the owner of the contract to the deployer
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Allows users to make a payment to the contract
     * @dev Accepts payments in ETH and emits a PaymentSuccessful event
     */
    function makePayment() external payable {
        require(msg.value > 0, "Payment amount must be greater than 0");
        
        // Emit the payment event
        emit PaymentSuccessful(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @notice Allows the owner to withdraw funds from the contract
     * @dev Only callable by the owner
     * @param _amount The amount to withdraw in wei
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient balance");

        // Transfer the specified amount to the owner
        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Withdrawal failed");

        // Emit the withdrawal event
        emit FundsWithdrawn(owner, _amount, block.timestamp);
    }

    /**
     * @notice Fetches the contract's current balance
     * @return The balance of the contract in wei
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
