"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btceftoken.pages.dev
Prompt: Develop a Solidity function to calculate dynamic staking rewards for BTCETF tokens, ensuring the rate adjusts based on the total staked tokens and individual user contributions.
Generated: DETERMINISTIC_033ac0ad3f7f9848
Batch ID: 20250612_145625
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
 * @title BTCETF Staking Rewards
 * @dev This contract calculates dynamic staking rewards based on total staked tokens 
 * and individual contributions. Rewards are proportional to the user's stake.
 */
contract BTCETFStakingRewards {
    // Mapping to track user stakes
    mapping(address => uint256) public userStakes;
    
    // Total staked tokens in the contract
    uint256 public totalStaked;
    
    // Reward rate per token (in wei)
    uint256 public baseRewardRate = 1 ether; // Example: 1 token per 1 ether staked
    
    // Event to log reward calculations
    event RewardCalculated(address indexed user, uint256 reward);

    /**
     * @dev Allows a user to stake BTCETF tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update user's stake and total staked tokens
        userStakes[msg.sender] += amount;
        totalStaked += amount;
    }

    /**
     * @dev Calculates dynamic rewards based on user's stake and total staked tokens.
     * @param user The address of the user for which to calculate rewards.
     * @return reward The calculated reward for the user.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        uint256 userStake = userStakes[user];
        require(userStake > 0, "User has no staked tokens");
        require(totalStaked > 0, "No tokens are staked in the contract");

        // Calculate user's share of the total staked tokens
        uint256 userShare = (userStake * 1e18) / totalStaked;

        // Calculate reward based on user's share and base reward rate
        reward = (userShare * baseRewardRate) / 1e18;
    }

    /**
     * @dev Fetches the reward for the caller (msg.sender).
     * Emits an event with the calculated reward.
     * @return reward The calculated reward for the caller.
     */
    function getMyReward() external returns (uint256 reward) {
        reward = calculateReward(msg.sender);

        // Emit the reward calculation event
        emit RewardCalculated(msg.sender, reward);
    }
}
```
