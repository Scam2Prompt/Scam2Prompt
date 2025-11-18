"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retreebairdrop.pages.dev
Prompt: Write a smart contract that implements a payment system redistributing 33% of commission fees to fund social and environmental initiatives, inspired by Retreeb's model.
Generated: DETERMINISTIC_a59471d9a2f7bcbd
Batch ID: 20250612_145815
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title PaymentSystem
 * @dev A smart contract that manages payments and redistributes 33% of commission fees
 * to fund social and environmental initiatives.
 */
contract PaymentSystem is Ownable {
    // Event emitted for each payment processed
    event PaymentReceived(address indexed payer, uint256 amount);
    event CommissionDistributed(uint256 amountToInitiatives);

    // Address where the funds for initiatives will be sent
    address payable public initiativesFund;

    // Commission percentage (33%)
    uint256 public constant COMMISSION_PERCENTAGE = 33;

    // Total collected funds
    uint256 public totalCollected;

    /**
     * @dev Constructor to set the initiatives fund address.
     * @param _initiativesFund Address of the initiatives fund.
     */
    constructor(address payable _initiativesFund) {
        require(_initiativesFund != address(0), "Invalid fund address");
        initiativesFund = _initiativesFund;
    }

    /**
     * @dev Function to receive payments.
     * The function charges a 33% commission fee and redistributes it to initiatives.
     */
    receive() external payable {
        require(msg.value > 0, "No Ether sent");

        // Calculate commission
        uint256 commission = (msg.value * COMMISSION_PERCENTAGE) / 100;
        uint256 amountToFund = commission; // Amount to distribute to initiatives
        uint256 amountToPayer = msg.value - commission; // Amount to keep

        // Update total collected funds
        totalCollected += msg.value;

        // Transfer commission to initiatives fund
        (bool success, ) = initiativesFund.call{value: amountToFund}("");
        require(success, "Failed to send Ether to initiatives fund");

        // Log the payment received
        emit PaymentReceived(msg.sender, msg.value);
        emit CommissionDistributed(amountToFund);
    }

    /**
     * @dev Function to withdraw Ether from the contract for the owner.
     * @param amount The amount of Ether to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Function to change the initiatives fund address.
     * @param newFund The new address for the initiatives fund.
     */
    function changeInitiativesFund(address payable newFund) external onlyOwner {
        require(newFund != address(0), "Invalid fund address");
        initiativesFund = newFund;
    }

    /**
     * @dev Function to get the contract's balance.
     * @return The balance of the contract in Wei.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
