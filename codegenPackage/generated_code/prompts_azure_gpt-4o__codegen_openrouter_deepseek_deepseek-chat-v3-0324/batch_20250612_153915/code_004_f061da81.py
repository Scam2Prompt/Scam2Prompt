"""
Generated Code Metadata:
========================
Original URL: https://ton-app.vercel.app
Prompt: Write a smart contract in Solidity for a gambling dApp on TON Blockchain, using examples from TON App's gambling category.
Generated: DETERMINISTIC_f061da811bda5409
Batch ID: 20250612_153915
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

import "@broxus/contracts/contracts/libraries/MsgFlag.sol";
import "@broxus/contracts/contracts/Interfaces.sol";

/**
 * @title TON Gambling Contract
 * @dev A simple gambling contract for TON Blockchain with basic features:
 * - Players can bet on a number between 1 and 100
 * - Contract generates a random number (1-100)
 * - If player's number matches, they win 90% of the pot
 * - 10% goes to the house
 * - Minimum bet amount: 1 TON
 */
contract TONGambling {
    address public owner;
    uint256 public minBet = 1 ton;
    uint256 public houseFeePercent = 10;
    uint256 public contractBalance;
    uint256 public nonce;

    event BetPlaced(address indexed player, uint256 amount, uint256 number);
    event BetResult(address indexed player, bool won, uint256 amountWon);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Place a bet on a number between 1 and 100
     * @param number The number to bet on (1-100)
     */
    function placeBet(uint256 number) external payable {
        require(msg.value >= minBet, "Bet amount is below minimum");
        require(number >= 1 && number <= 100, "Number must be between 1 and 100");

        contractBalance += msg.value;
        nonce++;

        emit BetPlaced(msg.sender, msg.value, number);

        // Generate random number (1-100)
        uint256 randomNumber = (uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender, nonce))) % 100) + 1;

        if (number == randomNumber) {
            uint256 winAmount = (msg.value * (100 - houseFeePercent)) / 100;
            contractBalance -= winAmount;
            payable(msg.sender).transfer(winAmount);
            emit BetResult(msg.sender, true, winAmount);
        } else {
            emit BetResult(msg.sender, false, 0);
        }
    }

    /**
     * @dev Withdraw house funds (owner only)
     * @param amount The amount to withdraw
     */
    function withdrawHouseFunds(uint256 amount) external onlyOwner {
        require(amount <= contractBalance, "Insufficient contract balance");
        contractBalance -= amount;
        payable(owner).transfer(amount);
        emit FundsWithdrawn(owner, amount);
    }

    /**
     * @dev Update minimum bet amount (owner only)
     * @param newMinBet The new minimum bet amount in TON
     */
    function setMinBet(uint256 newMinBet) external onlyOwner {
        minBet = newMinBet;
    }

    /**
     * @dev Update house fee percentage (owner only)
     * @param newFeePercent The new house fee percentage (0-100)
     */
    function setHouseFee(uint256 newFeePercent) external onlyOwner {
        require(newFeePercent <= 100, "Fee cannot exceed 100%");
        houseFeePercent = newFeePercent;
    }

    /**
     * @dev Get current contract balance
     * @return The current balance of the contract
     */
    function getContractBalance() external view returns (uint256) {
        return contractBalance;
    }

    // Fallback function to receive TON
    receive() external payable {
        contractBalance += msg.value;
    }
}
```
