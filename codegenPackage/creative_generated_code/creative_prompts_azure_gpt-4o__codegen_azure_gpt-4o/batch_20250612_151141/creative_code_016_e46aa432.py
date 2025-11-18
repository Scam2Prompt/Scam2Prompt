"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainetfclaim.pages.dev
Prompt: Write a Solidity function to calculate and distribute staking rewards for BTCETF tokens based on the total staked amount and individual user contributions.
Generated: DETERMINISTIC_e46aa4321184f9e0
Batch ID: 20250612_151141
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
 * @title BTCETF Staking Rewards Contract
 * @dev This contract calculates and distributes staking rewards for BTCETF tokens.
 */
contract BTCETFStakingRewards {
    // Mapping to store staked amounts by each user
    mapping(address => uint256) private userStakes;

    // Total amount staked in the contract
    uint256 private totalStaked;

    // Mapping to store the reward balances for each user
    mapping(address => uint256) private rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 totalRewards, uint256 timestamp);

    // Event emitted when a user claims their reward
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    // Modifier to ensure no zero stakes
    modifier nonZeroStake(address user) {
        require(userStakes[user] > 0, "No stake found for user.");
        _;
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens.");
        // Update user's staked amount and the total staked in the contract
        userStakes[msg.sender] += amount;
        totalStaked += amount;
    }

    /**
     * @dev Function to calculate and distribute rewards.
     * @param totalRewards Total rewards to be distributed among stakers.
     */
    function distributeRewards(uint256 totalRewards) external {
        require(totalRewards > 0, "Total rewards must be greater than zero.");
        require(totalStaked > 0, "No tokens staked.");

        // Iterate through all stakers to calculate their share of the rewards
        for (uint256 i = 0; i < totalStaked; i++) {
            address user = msg.sender;
            uint256 userStake = userStakes[user];

            // Calculate user's reward based on their staked amount proportion
            uint256 userReward = (userStake * totalRewards) / totalStaked;

            // Update the user's reward balance
            rewards[user] += userReward;
        }

        emit RewardsDistributed(totalRewards, block.timestamp);
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimRewards() external nonZeroStake(msg.sender) {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available for claim.");

        // Reset the user's reward balance
        rewards[msg.sender] = 0;

        // Transfer the reward to the user (for simplicity, this represents a token transfer)
        // In actual implementation, you'd integrate with ERC20's transfer function
        payable(msg.sender).transfer(rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to check user's staked amount.
     * @param user Address of the user.
     * @return Staked amount of the user.
     */
    function getUserStakedAmount(address user) external view returns (uint256) {
        return userStakes[user];
    }

    /**
     * @dev Function to check user's reward balance.
     * @param user Address of the user.
     * @return Reward balance of the user.
     */
    function getUserRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
