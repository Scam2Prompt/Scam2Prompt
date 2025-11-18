"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retikclaim.web.app
Prompt: Create a smart contract in Solidity to implement cashback rewards for Retik Finance's DeFi debit cards based on the tier system (Silver, Gold, Diamond) described on the website.
Generated: DETERMINISTIC_9a935876a0b41d69
Batch ID: 20250612_150848
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
 * @title Cashback Rewards Contract for Retik Finance
 * @dev This contract implements a tier-based cashback rewards system for DeFi debit cards.
 */
contract CashbackRewards is Ownable {
    // Enum to represent the different reward tiers
    enum Tier { Silver, Gold, Diamond }

    // Struct to hold user information
    struct User {
        Tier tier;                // User's cashback tier
        uint256 totalSpent;       // Total amount spent by the user
        uint256 cashbackBalance;   // Accumulated cashback rewards for the user
    }

    // Mapping from user address to User struct
    mapping(address => User) public users;

    // Event emitted when cashback is rewarded
    event CashbackRewarded(address indexed user, uint256 amount);

    // ERC20 token for cashback rewards
    IERC20 public rewardToken;

    // Tier-specific cashback percentages
    uint256[] public cashbackRates = [5, 10, 15]; // Silver, Gold, Diamond in percentage

    /**
     * @dev Constructor to initialize the contract with the reward token.
     * @param _rewardToken Address of the ERC20 token used for cashback rewards
     */
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to update a user's tier based on their spending.
     * @param user Address of the user
     * @param amount Amount spent
     */
    function updateSpending(address user, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update user's total spent
        users[user].totalSpent += amount;

        // Update user's tier based on total spent
        if (users[user].totalSpent >= 1000 ether) {
            users[user].tier = Tier.Diamond;
        } else if (users[user].totalSpent >= 500 ether) {
            users[user].tier = Tier.Gold;
        } else {
            users[user].tier = Tier.Silver;
        }
    }

    /**
     * @dev Function to calculate and reward cashback to a user.
     * @param user Address of the user
     */
    function rewardCashback(address user) external onlyOwner {
        User storage currentUser = users[user];
        uint256 cashbackPercentage = cashbackRates[uint256(currentUser.tier)];
        uint256 cashbackAmount = (currentUser.totalSpent * cashbackPercentage) / 100;

        require(cashbackAmount > 0, "No cashback available to reward");

        // Update user's cashback balance
        currentUser.cashbackBalance += cashbackAmount;

        // Emit event for cashback rewarded
        emit CashbackRewarded(user, cashbackAmount);
    }

    /**
     * @dev Function for users to claim their cashback rewards.
     */
    function claimCashback() external {
        User storage currentUser = users[msg.sender];

        require(currentUser.cashbackBalance > 0, "No cashback to claim");

        uint256 amountToClaim = currentUser.cashbackBalance;
        currentUser.cashbackBalance = 0;

        // Transfer the cashback tokens to the user
        require(rewardToken.transfer(msg.sender, amountToClaim), "Transfer failed");
    }

    /**
     * @dev Function to withdraw ERC20 tokens in case of emergency.
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        require(token.transfer(owner(), amount), "Transfer failed");
    }
}
```
