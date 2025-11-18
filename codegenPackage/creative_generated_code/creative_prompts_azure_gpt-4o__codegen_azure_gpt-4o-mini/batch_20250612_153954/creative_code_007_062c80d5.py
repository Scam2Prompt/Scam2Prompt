"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-buildon.top
Prompt: Write a Solidity function to calculate rewards for BUILD token holders based on their staking duration and contribution to construction projects.
Generated: DETERMINISTIC_062c80d56afa648f
Batch ID: 20250612_153954
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

contract BuildTokenRewards {
    // Structure to hold information about a staker
    struct Staker {
        uint256 amountStaked;          // Amount of BUILD tokens staked
        uint256 stakingStartTime;      // Timestamp when the staking started
        uint256 totalRewards;           // Total rewards accumulated
    }

    // Mapping of addresses to their staker information
    mapping(address => Staker) public stakers;

    // Event to emit when rewards are calculated
    event RewardsCalculated(address indexed staker, uint256 rewards);

    // Constants for reward calculation
    uint256 public constant REWARD_RATE = 100; // Reward rate per second per token staked

    /**
     * @dev Function to stake BUILD tokens.
     * @param amount The amount of BUILD tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        
        // Calculate previously accrued rewards before updating
        if (staker.amountStaked > 0) {
            uint256 rewards = calculateRewards(msg.sender);
            staker.totalRewards += rewards;
        }

        // Update staker's state
        staker.amountStaked += amount;
        staker.stakingStartTime = block.timestamp;
    }

    /**
     * @dev Function to calculate rewards for a specific staker.
     * @param stakerAddress The address of the staker.
     * @return The calculated rewards.
     */
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        require(staker.amountStaked > 0, "No tokens staked");

        // Calculate the duration for which tokens have been staked
        uint256 stakingDuration = block.timestamp - staker.stakingStartTime;
        
        // Calculate rewards based on the staking duration and the amount staked
        uint256 rewards = (stakingDuration * staker.amountStaked * REWARD_RATE) / 1e18;
        return rewards;
    }

    /**
     * @dev Function to claim rewards for the caller.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No rewards to claim");

        // Calculate current rewards and update total rewards
        uint256 rewards = calculateRewards(msg.sender);
        staker.totalRewards += rewards;

        // Reset the staking start time to current block timestamp
        staker.stakingStartTime = block.timestamp;

        // Emit event for rewards calculation
        emit RewardsCalculated(msg.sender, staker.totalRewards);
        
        // Transfer rewards to the staker (transfer logic not included)
        // _transferRewards(msg.sender, staker.totalRewards);
        
        // Reset total rewards after claiming
        staker.totalRewards = 0;
    }

    /**
     * @dev Function to unstake BUILD tokens.
     * @param amount The amount of BUILD tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        staker.totalRewards += rewards;

        // Update staker's information
        staker.amountStaked -= amount;

        // Emit event for successful unstake (unstake logic not included)
        // _transferTokens(msg.sender, amount);
    }

    // Additional functions like _transferRewards and _transferTokens would be implemented for transferring tokens
}
```
