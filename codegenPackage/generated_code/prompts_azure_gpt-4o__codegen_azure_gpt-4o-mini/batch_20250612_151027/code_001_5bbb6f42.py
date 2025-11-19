"""
Generated Code Metadata:
========================
Original URL: https://moxie.credit
Prompt: Generate code for implementing programmatic rewards on Farcaster using Moxie smart contracts to reward members for referrals, product trials, and on-chain actions.
Generated: DETERMINISTIC_5bbb6f429e9138a3
Batch ID: 20250612_151027
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MoxieRewards contract to manage rewards for referrals, product trials, and on-chain actions
contract MoxieRewards is Ownable {
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount, string reason);

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Constructor to initialize the contract with the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Function to reward users for referrals
    function rewardForReferral(address _referrer, uint256 _amount) external onlyOwner {
        require(_referrer != address(0), "Invalid referrer address");
        require(_amount > 0, "Reward amount must be greater than zero");

        rewards[_referrer] += _amount;
        emit RewardsDistributed(_referrer, _amount, "Referral Reward");
    }

    // Function to reward users for product trials
    function rewardForTrial(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Reward amount must be greater than zero");

        rewards[_user] += _amount;
        emit RewardsDistributed(_user, _amount, "Product Trial Reward");
    }

    // Function to reward users for on-chain actions
    function rewardForAction(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Reward amount must be greater than zero");

        rewards[_user] += _amount;
        emit RewardsDistributed(_user, _amount, "On-Chain Action Reward");
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance before transferring tokens
        rewards[msg.sender] = 0;

        // Transfer the reward tokens to the user
        require(rewardToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(rewardToken.transfer(msg.sender, _amount), "Token transfer failed");
    }

    // Function to check the reward balance of a user
    function getRewardBalance(address _user) external view returns (uint256) {
        return rewards[_user];
    }
}
```
