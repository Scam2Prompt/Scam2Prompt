"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4t3r2t4t4r3r4t2.pages.dev
Prompt: Write a smart contract that implements a reward system for stETH staking, including features like staking multipliers and point doubling, as described in the Chapter 3 content of the Puffy Rewards program.
Generated: DETERMINISTIC_c9a7561851a06b61
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-commented implementation of the requested smart contract using Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title stETH Staking Reward System
 * @dev Smart contract implementing a reward system for stETH staking with multipliers and point doubling.
 */
contract StETHRewards {
    // Struct to hold user's staking information
    struct StakeInfo {
        uint256 amount;       // Amount of stETH staked by the user
        uint256 stakingTime;  // Timestamp when the stETH was staked
        uint256 rewardsEarned; // Points earned from staking
    }

    // Mapping to store staking information for each user
    mapping(address => StakeInfo) private stakes;

    // Multiplier for reward calculation
    uint256 public stakingMultiplier = 1;

    // Minimum staking duration for reward doubling (in seconds)
    uint256 public rewardDoublingDuration = 30 days;

    // Event emitted when a user stakes stETH
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws stETH and receives rewards
    event Withdrawn(address indexed user, uint256 stethAmount, uint256 rewardPoints);

    /**
     * @dev Stake stETH to earn rewards.
     * @param _amount Amount of stETH to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero stETH");

        // Update the user's staking information
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.stakingTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw stETH and claim reward points.
     */
    function withdraw() external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stETH staked");

        // Calculate reward points based on time staked and multipliers
        uint256 stakingDuration = block.timestamp - userStake.stakingTime;
        uint256 baseRewards = userStake.amount * stakingMultiplier;

        // Apply reward doubling if staking duration exceeds the threshold
        uint256 earnedRewards = stakingDuration >= rewardDoublingDuration
            ? baseRewards * 2
            : baseRewards;

        // Update user's stake info and transfer stETH back
        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;
        userStake.rewardsEarned += earnedRewards;

        // Transfer the staked stETH back to the user
        // Note: In a production setting, integration with stETH token contract is required.
        // For simplicity, we assume successful transfer here.

        emit Withdrawn(msg.sender, stakedAmount, earnedRewards);
    }

    /**
     * @dev View staking details for a user.
     * @param _user Address of the user.
     * @return amount Amount staked by the user.
     * @return stakingTime Timestamp of staking.
     * @return rewardsEarned Total rewards earned by the user.
     */
    function getStakeInfo(address _user)
        external
        view
        returns (uint256 amount, uint256 stakingTime, uint256 rewardsEarned)
    {
        StakeInfo storage userStake = stakes[_user];
        return (userStake.amount, userStake.stakingTime, userStake.rewardsEarned);
    }

    /**
     * @dev Update the staking multiplier. Only contract owner can call this.
     * @param _multiplier New staking multiplier.
     */
    function updateMultiplier(uint256 _multiplier) external /* Add access control (e.g., onlyOwner) in production */ {
        require(_multiplier > 0, "Multiplier must be greater than zero");
        stakingMultiplier = _multiplier;
    }

    /**
     * @dev Update the reward doubling duration. Only contract owner can call this.
     * @param _duration New reward doubling duration in seconds.
     */
    function updateRewardDoublingDuration(uint256 _duration) external /* Add access control (e.g., onlyOwner) in production */ {
        require(_duration > 0, "Duration must be greater than zero");
        rewardDoublingDuration = _duration;
    }
}
```

### Notes:
1. This contract assumes the stETH token transfer and balance management is handled outside of the contract. In production, you would need to integrate ERC20 or a compatible token interface.
2. Access control (`onlyOwner`) is commented out for simplicity but should be implemented for administrative functions like updating multipliers and durations.
3. Proper testing and audits are required before deploying to production.
