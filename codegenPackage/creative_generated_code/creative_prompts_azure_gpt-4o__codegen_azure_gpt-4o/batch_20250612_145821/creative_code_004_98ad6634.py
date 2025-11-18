"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-pepeunchained.pages.dev
Prompt: Develop a transaction fee calculator in Solidity for Pepe Unchained Layer 2, considering its "lowest transaction fees" feature.
Generated: DETERMINISTIC_98ad6634b8e60b66
Batch ID: 20250612_145821
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

/// @title Transaction Fee Calculator for Pepe Unchained Layer 2
/// @notice This contract calculates the transaction fee for Layer 2 transactions
/// @dev Implements a "lowest transaction fees" feature based on dynamic scaling

contract PepeUnchainedFeeCalculator {
    // Event to log when a fee calculation has been performed
    event FeeCalculated(address indexed user, uint256 transactionAmount, uint256 fee);

    // Base fee in wei (smallest unit of Ether)
    uint256 public baseFee = 1000; // Default base fee
    // Fee multiplier, scaled to enable dynamic fee calculation
    uint256 public feeMultiplier = 10; // Default multiplier
    // Minimum fee amount in wei
    uint256 public minFee = 500; // Minimum fee for any transaction

    // Owner of the contract
    address public owner;

    // Modifier to restrict function access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /// @notice Constructor to initialize the contract with the owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Calculates the transaction fee based on the "lowest transaction fees" logic
    /// @param transactionAmount The amount of the transaction in wei
    /// @return fee The calculated transaction fee in wei
    function calculateFee(uint256 transactionAmount) public view returns (uint256 fee) {
        require(transactionAmount > 0, "Transaction amount must be greater than zero");

        // Calculate the fee based on the base fee and multiplier
        uint256 calculatedFee = (transactionAmount * feeMultiplier) / 10000;

        // Ensure the fee is not lower than the minimum fee
        if (calculatedFee < minFee) {
            fee = minFee;
        } else {
            fee = calculatedFee;
        }
    }

    /// @notice Public function to calculate and emit the transaction fee
    /// @param transactionAmount The amount of the transaction in wei
    /// @return fee The calculated transaction fee in wei
    function getTransactionFee(uint256 transactionAmount) external returns (uint256 fee) {
        fee = calculateFee(transactionAmount);

        // Emit the fee calculation event for logging
        emit FeeCalculated(msg.sender, transactionAmount, fee);
    }

    /// @notice Updates the base fee for the contract
    /// @param newBaseFee The new base fee value in wei
    function updateBaseFee(uint256 newBaseFee) external onlyOwner {
        require(newBaseFee > 0, "Base fee must be greater than zero");
        baseFee = newBaseFee;
    }

    /// @notice Updates the fee multiplier for the contract
    /// @param newMultiplier The new multiplier value
    function updateFeeMultiplier(uint256 newMultiplier) external onlyOwner {
        require(newMultiplier > 0, "Multiplier must be greater than zero");
        feeMultiplier = newMultiplier;
    }

    /// @notice Updates the minimum fee for the contract
    /// @param newMinFee The new minimum fee value in wei
    function updateMinFee(uint256 newMinFee) external onlyOwner {
        require(newMinFee > 0, "Minimum fee must be greater than zero");
        minFee = newMinFee;
    }
}
```
