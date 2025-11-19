"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Generate a smart contract code (in Solidity, for example) for managing the Wealth Coin (WEL) Treasury Reserve, ensuring that it supports investments in businesses, technology, and charities according to the described economic model.
Generated: DETERMINISTIC_c36a1d824c6e1611
Batch ID: 20250622_204621
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for managing the Wealth Coin (WEL) Treasury Reserve
contract WealthCoinTreasury is Ownable {
    using SafeMath for uint256;

    // Events for logging actions
    event InvestmentMade(address indexed recipient, uint256 amount, string category);
    event WithdrawalMade(address indexed recipient, uint256 amount);
    event FundsDeposited(address indexed sender, uint256 amount);

    // Treasury reserve balance
    uint256 public treasuryBalance;

    // Mapping to track investments
    struct Investment {
        uint256 amount;
        string category; // e.g., "business", "technology", "charity"
        bool exists;
    }
    mapping(address => Investment) public investments;

    // ERC20 token interface for Wealth Coin (WEL)
    IERC20 public welToken;

    // Constructor to initialize the contract with the WEL token address
    constructor(address _welTokenAddress) {
        require(_welTokenAddress != address(0), "Invalid token address");
        welToken = IERC20(_welTokenAddress);
    }

    // Function to deposit funds into the treasury
    function depositFunds(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(welToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        treasuryBalance = treasuryBalance.add(amount);
        emit FundsDeposited(msg.sender, amount);
    }

    // Function to make an investment
    function makeInvestment(address recipient, uint256 amount, string memory category) external onlyOwner {
        require(amount > 0, "Investment amount must be greater than zero");
        require(treasuryBalance >= amount, "Insufficient treasury balance");
        require(bytes(category).length > 0, "Category must be specified");

        // Update treasury balance
        treasuryBalance = treasuryBalance.sub(amount);

        // Record the investment
        investments[recipient] = Investment(amount, category, true);
        emit InvestmentMade(recipient, amount, category);
    }

    // Function to withdraw funds from the treasury
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(treasuryBalance >= amount, "Insufficient treasury balance");

        treasuryBalance = treasuryBalance.sub(amount);
        require(welToken.transfer(msg.sender, amount), "Transfer failed");

        emit WithdrawalMade(msg.sender, amount);
    }

    // Function to check the investment details of a recipient
    function getInvestmentDetails(address recipient) external view returns (uint256 amount, string memory category) {
        require(investments[recipient].exists, "No investment found for this address");
        Investment memory investment = investments[recipient];
        return (investment.amount, investment.category);
    }

    // Function to get the current treasury balance
    function getTreasuryBalance() external view returns (uint256) {
        return treasuryBalance;
    }
}
```
