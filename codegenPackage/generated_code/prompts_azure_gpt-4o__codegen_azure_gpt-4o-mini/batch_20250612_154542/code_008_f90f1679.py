"""
Generated Code Metadata:
========================
Original URL: https://rewardusdctoken.com
Prompt: Develop a smart contract audit checklist tailored for the RewardUSDC Token (RUSDC), focusing on its buy/sell tax mechanism, liquidity lock on PinkSale, and reward distribution system.
Generated: DETERMINISTIC_f90f1679117e879a
Batch ID: 20250612_154542
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RewardUSDC Token (RUSDC)
 * @dev ERC20 Token with buy/sell tax mechanism, liquidity lock, and reward distribution system
 */
contract RewardUSDC is ERC20, Ownable {
    // Tax rates
    uint256 public buyTaxRate; // Buy tax rate in basis points (1% = 100)
    uint256 public sellTaxRate; // Sell tax rate in basis points (1% = 100)

    // Liquidity lock status
    bool public liquidityLocked;

    // Reward distribution variables
    mapping(address => uint256) public rewards;
    uint256 public totalRewardsDistributed;

    // Events
    event TaxUpdated(uint256 buyTaxRate, uint256 sellTaxRate);
    event LiquidityLocked();
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        buyTaxRate = 200; // 2% buy tax
        sellTaxRate = 300; // 3% sell tax
        liquidityLocked = false;
    }

    /**
     * @dev Function to update tax rates
     * @param _buyTaxRate New buy tax rate in basis points
     * @param _sellTaxRate New sell tax rate in basis points
     */
    function updateTaxRates(uint256 _buyTaxRate, uint256 _sellTaxRate) external onlyOwner {
        require(_buyTaxRate <= 1000, "Buy tax rate too high"); // Max 10%
        require(_sellTaxRate <= 1000, "Sell tax rate too high"); // Max 10%
        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        emit TaxUpdated(buyTaxRate, sellTaxRate);
    }

    /**
     * @dev Function to lock liquidity
     */
    function lockLiquidity() external onlyOwner {
        require(!liquidityLocked, "Liquidity already locked");
        liquidityLocked = true;
        emit LiquidityLocked();
    }

    /**
     * @dev Internal function to handle tax deduction on buy/sell
     * @param amount Amount of tokens to process
     * @param isBuy Boolean indicating if the transaction is a buy
     * @return netAmount Amount after tax deduction
     */
    function _applyTax(uint256 amount, bool isBuy) internal returns (uint256 netAmount) {
        uint256 taxRate = isBuy ? buyTaxRate : sellTaxRate;
        uint256 taxAmount = (amount * taxRate) / 10000; // Convert basis points to percentage
        netAmount = amount - taxAmount;
        return netAmount;
    }

    /**
     * @dev Function to distribute rewards to users
     * @param user Address of the user to distribute rewards to
     * @param amount Amount of rewards to distribute
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        rewards[user] += amount;
        totalRewardsDistributed += amount;
        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Override the transfer function to include tax mechanism
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 netAmount = _applyTax(amount, false);
        _transfer(_msgSender(), recipient, netAmount);
        return true;
    }

    /**
     * @dev Override the transferFrom function to include tax mechanism
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 netAmount = _applyTax(amount, false);
        _transfer(sender, recipient, netAmount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }
}
```
