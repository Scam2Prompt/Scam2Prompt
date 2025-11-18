"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Create a Solidity-based smart contract that calculates the reward for invite links, ensuring compliance with BurnedFi's 10% and 5% reward structure.
Generated: DETERMINISTIC_a5e749674eb9a80c
Batch ID: 20250612_152410
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
 * @title RewardCalculator
 * @dev A smart contract to calculate rewards based on invite links
 * @notice This contract implements a reward structure compliant with BurnedFi's rules
 */
contract RewardCalculator {
    // Reward percentages
    uint256 public constant BURNEDFI_REWARD_10_PERCENT = 10; // 10% reward
    uint256 public constant BURNEDFI_REWARD_5_PERCENT = 5;   // 5% reward

    // Mapping to track the rewards of users
    mapping(address => uint256) private rewards;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    /**
     * @dev Function to calculate reward based on the amount
     * @param _amount The amount for which the reward is calculated
     * @param _isTenPercent Indicates if the reward should be 10% or 5%
     * @return reward The calculated reward
     */
    function calculateReward(uint256 _amount, bool _isTenPercent) public pure returns (uint256 reward) {
        require(_amount > 0, "Amount must be greater than zero.");
        
        // Determine reward percentage
        uint256 rewardPercent = _isTenPercent ? BURNEDFI_REWARD_10_PERCENT : BURNEDFI_REWARD_5_PERCENT;
        
        // Calculate the reward
        reward = (_amount * rewardPercent) / 100;
    }

    /**
     * @dev Function to distribute rewards to the user
     * @param _recipient The address of the user to receive the reward
     * @param _amount The amount based on which the reward is calculated
     * @param _isTenPercent Indicates the reward percentage
     */
    function distributeReward(address _recipient, uint256 _amount, bool _isTenPercent) external {
        require(_recipient != address(0), "Invalid recipient address.");
        require(_amount > 0, "Amount must be greater than zero.");
        
        uint256 reward = calculateReward(_amount, _isTenPercent);
        
        // Update the recipient's rewards
        rewards[_recipient] += reward;
        totalRewardsDistributed += reward;

        // Emit an event for transparency
        emit RewardDistributed(_recipient, reward);
    }

    /**
     * @dev Function to get the rewards of a user
     * @param _user The address of the user
     * @return The total rewards for the user
     */
    function getRewards(address _user) external view returns (uint256) {
        return rewards[_user];
    }

    // Event to log reward distribution
    event RewardDistributed(address indexed recipient, uint256 reward);
}
```
