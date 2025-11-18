"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Generate code for implementing programmatic rewards on Farcaster using Moxie smart contracts to reward members for referrals, product trials, and on-chain actions.
Generated: DETERMINISTIC_5bbb6f429e9138a3
Batch ID: 20250612_151027
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
 * @title MoxieRewards
 * @dev Smart contract for implementing programmatic rewards
 * for referrals, product trials, and on-chain actions.
 */
contract MoxieRewards is Ownable {
    IERC20 public rewardToken; // The ERC20 token used for rewards

    // Structure to hold user information
    struct User {
        uint256 referrals; // Number of referrals made
        uint256 trials; // Number of product trials completed
        mapping(address => bool) hasReferred; // Track referrals
    }

    mapping(address => User) private users; // Mapping of user addresses to user data

    event RewardIssued(address indexed user, uint256 amount);
    event ReferralRegistered(address indexed referrer, address indexed referee);

    /**
     * @dev Constructor to set the reward token address.
     * @param _rewardToken Address of the ERC20 token to be used for rewards.
     */
    constructor(address _rewardToken) {
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Register a referral.
     * @param referee Address of the user being referred.
     */
    function registerReferral(address referee) external {
        require(referee != msg.sender, "Cannot refer yourself");
        require(!users[msg.sender].hasReferred[referee], "Referral already registered");

        users[msg.sender].referrals++;
        users[msg.sender].hasReferred[referee] = true;

        emit ReferralRegistered(msg.sender, referee);
    }

    /**
     * @dev Reward user for completing product trials.
     * @param user Address of the user to reward.
     * @param trialCount Number of trials completed.
     */
    function rewardForTrials(address user, uint256 trialCount) external onlyOwner {
        require(trialCount > 0, "Trial count must be greater than zero");

        // Calculate reward amount (example: 10 tokens per trial)
        uint256 rewardAmount = trialCount * 10 * 10 ** 18; // Assuming 18 decimals

        // Transfer tokens to the user
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient reward balance");
        rewardToken.transfer(user, rewardAmount);

        users[user].trials += trialCount; // Update trial count
        emit RewardIssued(user, rewardAmount);
    }

    /**
     * @dev Withdraw any tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        rewardToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Get the referral count of a user.
     * @param user Address of the user.
     * @return The number of referrals made by the user.
     */
    function getReferralCount(address user) external view returns (uint256) {
        return users[user].referrals;
    }

    /**
     * @dev Get the trial count of a user.
     * @param user Address of the user.
     * @return The number of product trials completed by the user.
     */
    function getTrialCount(address user) external view returns (uint256) {
        return users[user].trials;
    }
}
```
