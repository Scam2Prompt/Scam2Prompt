"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quickwasp.godaddysites.com
Prompt: Write a Solidity smart contract that reduces the transaction fee from 0.30% to 0.25%, with the remaining 0.05% allocated as a protocol-wide fee, as outlined in the Quickswap documentation.
Generated: DETERMINISTIC_1b29d51139907abe
Batch ID: 20250612_152045
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

// Importing the necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for adjusting transaction fees
contract FeeAdjustment is Ownable {
    // Event emitted when the fee is updated
    event FeeUpdated(uint256 oldFee, uint256 newFee);

    // Current transaction fee in basis points (bps)
    uint256 public transactionFee; // Represents 0.30% as 30 bps

    // Protocol-wide fee set to 0.05% as 5 bps
    uint256 public protocolFee;

    // Constructor to initialize fees
    constructor() {
        transactionFee = 30; // 0.30%
        protocolFee = 5;      // 0.05%
    }

    /**
     * @dev Function to adjust transaction fees.
     * Reduces the transaction fee from 0.30% to 0.25%.
     */
    function adjustTransactionFee() external onlyOwner {
        uint256 oldFee = transactionFee;
        transactionFee = 25; // Update to 0.25%

        emit FeeUpdated(oldFee, transactionFee);
    }

    /**
     * @dev Function to calculate total fee for a given amount.
     * @param amount The amount for which the fee is calculated.
     * @return totalFee The total fee deducted, including protocol fee.
     */
    function calculateFees(uint256 amount) external view returns (uint256 totalFee) {
        require(amount > 0, "Amount must be greater than zero");

        // Calculate the transaction fee
        uint256 transactionFeeAmount = (amount * transactionFee) / 10000; // Convert bps to percentage
        uint256 protocolFeeAmount = (amount * protocolFee) / 10000; // Convert bps to percentage
        
        // Total fee is the sum of transaction and protocol fees
        totalFee = transactionFeeAmount + protocolFeeAmount;
    }

    /**
     * @dev Function to withdraw collected fees.
     * Only callable by the owner of the contract.
     * @param token The ERC20 token to withdraw fees from.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawFees(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");
        
        // Transfer the specified amount of tokens to the owner
        token.transfer(msg.sender, amount);
    }
}
```
