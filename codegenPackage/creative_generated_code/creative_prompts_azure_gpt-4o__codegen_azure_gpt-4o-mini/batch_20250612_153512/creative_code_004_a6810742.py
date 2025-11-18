"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimspopofrog.web.app
Prompt: Write a function in Solidity to distribute $FROP tokens according to the tokenomics breakdown (Presale 25%, Staking 25%, Marketing 25%, Rewards 15%, Liquidity 10%).
Generated: DETERMINISTIC_a68107423831a530
Batch ID: 20250612_153512
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FROPTokenDistributor
 * @dev A contract to distribute $FROP tokens based on predefined tokenomics.
 */
contract FROPTokenDistributor is Ownable {
    IERC20 public froptoken; // The $FROP token contract
    uint256 public totalSupply; // Total supply of $FROP tokens to distribute

    // Distribution percentages defined as constants
    uint256 constant PRESALE_PERCENTAGE = 25; // 25%
    uint256 constant STAKING_PERCENTAGE = 25; // 25%
    uint256 constant MARKETING_PERCENTAGE = 25; // 25%
    uint256 constant REWARDS_PERCENTAGE = 15; // 15%
    uint256 constant LIQUIDITY_PERCENTAGE = 10; // 10%

    // Events for tracking distributions
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @param _froptoken The address of the $FROP token contract
     * @param _totalSupply Total supply of $FROP tokens to be distributed
     */
    constructor(IERC20 _froptoken, uint256 _totalSupply) {
        froptoken = _froptoken;
        totalSupply = _totalSupply;
    }

    /**
     * @dev Distributes $FROP tokens according to the specified tokenomics breakdown.
     */
    function distributeTokens() external onlyOwner {
        uint256 presaleAmount = (totalSupply * PRESALE_PERCENTAGE) / 100;
        uint256 stakingAmount = (totalSupply * STAKING_PERCENTAGE) / 100;
        uint256 marketingAmount = (totalSupply * MARKETING_PERCENTAGE) / 100;
        uint256 rewardsAmount = (totalSupply * REWARDS_PERCENTAGE) / 100;
        uint256 liquidityAmount = (totalSupply * LIQUIDITY_PERCENTAGE) / 100;

        _distribute(msg.sender, presaleAmount, "Presale");
        _distribute(msg.sender, stakingAmount, "Staking");
        _distribute(msg.sender, marketingAmount, "Marketing");
        _distribute(msg.sender, rewardsAmount, "Rewards");
        _distribute(msg.sender, liquidityAmount, "Liquidity");
    }

    /**
     * @dev Internal function to handle token distribution.
     * @param recipient The address that will receive the tokens
     * @param amount The amount of tokens to distribute
     * @param category The category of distribution (for logging)
     */
    function _distribute(address recipient, uint256 amount, string memory category) internal {
        require(amount > 0, "Amount must be greater than zero");
        require(froptoken.balanceOf(address(this)) >= amount, "Insufficient token balance in contract");

        // Transfer tokens to the recipient
        froptoken.transfer(recipient, amount);
        
        // Emit event for tracking
        emit TokensDistributed(recipient, amount);
    }
}
```
