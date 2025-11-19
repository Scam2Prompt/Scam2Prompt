"""
Generated Code Metadata:
========================
Original URL: https://hashai.pages.dev
Prompt: Design a smart contract in Solidity that enables token holders to receive shared income from AI-enhanced mining rigs, similar to Hash AI's token model, and explain its functionality.
Generated: DETERMINISTIC_98431548a12eb7ff
Batch ID: 20250622_210856
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

// Importing OpenZeppelin's ERC20 implementation for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a token that allows holders to receive shared income from AI-enhanced mining rigs
contract MiningIncomeToken is ERC20, Ownable {
    // Mapping to track the income shares for each token holder
    mapping(address => uint256) public incomeShares;
    // Total income generated from mining
    uint256 public totalIncome;
    // Total shares distributed among token holders
    uint256 public totalShares;

    // Event to log income distribution
    event IncomeDistributed(uint256 amount);
    // Event to log income withdrawal
    event IncomeWithdrawn(address indexed holder, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    // Function to distribute income to token holders based on their shares
    function distributeIncome(uint256 amount) external onlyOwner {
        require(amount > 0, "Income amount must be greater than zero");
        require(totalShares > 0, "No shares to distribute income to");

        // Update total income
        totalIncome += amount;

        // Emit an event for income distribution
        emit IncomeDistributed(amount);
    }

    // Function to allow token holders to withdraw their income based on their shares
    function withdrawIncome() external {
        uint256 income = calculateIncome(msg.sender);
        require(income > 0, "No income available for withdrawal");

        // Reset the income share for the holder
        incomeShares[msg.sender] = 0;

        // Transfer the income to the holder
        payable(msg.sender).transfer(income);

        // Emit an event for income withdrawal
        emit IncomeWithdrawn(msg.sender, income);
    }

    // Function to calculate the income for a specific holder
    function calculateIncome(address holder) public view returns (uint256) {
        // Calculate the income based on the holder's shares
        return (totalIncome * incomeShares[holder]) / totalShares;
    }

    // Function to allow token holders to stake their tokens and earn shares
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);

        // Update income shares and total shares
        incomeShares[msg.sender] += amount;
        totalShares += amount;
    }

    // Function to allow token holders to unstake their tokens
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(incomeShares[msg.sender] >= amount, "Insufficient staked amount");

        // Update income shares and total shares
        incomeShares[msg.sender] -= amount;
        totalShares -= amount;

        // Transfer tokens back to the holder
        _transfer(address(this), msg.sender, amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
