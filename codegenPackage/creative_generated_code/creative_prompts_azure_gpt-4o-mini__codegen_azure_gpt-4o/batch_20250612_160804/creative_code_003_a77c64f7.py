"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.web.app
Prompt: Explain how to implement a referral bonus system for the God Candle NFT project using ERC-20 tokens.
Generated: DETERMINISTIC_a77c64f721d6d1d8
Batch ID: 20250612_160804
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

/**
 * @title Referral Bonus System for God Candle NFT Project
 * @notice This contract implements a referral bonus system using ERC-20 tokens.
 * @dev Tokens are distributed to referrers based on successful referrals.
 */
contract ReferralBonusSystem {
    // Address of the ERC-20 token contract used for bonuses
    IERC20 public bonusToken;

    // Mapping to track the referral bonuses earned by each referrer
    mapping(address => uint256) public referralBonuses;

    // Event emitted when a referral bonus is distributed
    event ReferralBonusDistributed(address indexed referrer, uint256 amount);

    // Constructor to set the ERC-20 token address
    constructor(address _bonusTokenAddress) {
        require(_bonusTokenAddress != address(0), "Invalid token address");
        bonusToken = IERC20(_bonusTokenAddress);
    }

    /**
     * @dev Distributes referral bonuses to referrers.
     * @param referrer The address of the referrer.
     * @param bonusAmount The amount of ERC-20 tokens to be distributed as bonus.
     * @notice Only the contract owner can call this function.
     */
    function distributeReferralBonus(address referrer, uint256 bonusAmount) external onlyOwner {
        require(referrer != address(0), "Invalid referrer address");
        require(bonusAmount > 0, "Bonus amount must be greater than zero");

        // Ensure the contract has sufficient token balance
        require(bonusToken.balanceOf(address(this)) >= bonusAmount, "Insufficient token balance");

        // Transfer tokens to the referrer
        bonusToken.transfer(referrer, bonusAmount);

        // Update the referral bonuses mapping
        referralBonuses[referrer] += bonusAmount;

        // Emit an event for the referral bonus distribution
        emit ReferralBonusDistributed(referrer, bonusAmount);
    }

    /**
     * @dev Allows the owner to withdraw excess tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     * @notice Only the contract owner can call this function.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(bonusToken.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens to the owner
        bonusToken.transfer(msg.sender, amount);
    }

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Address of the contract owner
    address public owner;

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }
}

// IERC20 interface definition for interacting with ERC-20 token contract
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
