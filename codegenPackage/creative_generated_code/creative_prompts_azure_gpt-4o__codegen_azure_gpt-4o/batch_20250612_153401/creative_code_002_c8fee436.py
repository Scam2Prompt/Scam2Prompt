"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt.pages.dev
Prompt: Create a function in Solidity to calculate staking rewards for $GIGA tokens, considering the tokenomics described on the GigaChadGPT website.
Generated: DETERMINISTIC_c8fee43624e7a97d
Batch ID: 20250612_153401
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
 * @title StakingRewards
 * @dev A contract for calculating staking rewards for $GIGA tokens.
 */
contract StakingRewards {
    // Struct to store information about a staker
    struct Staker {
        uint256 amountStaked; // The amount of $GIGA tokens staked
        uint256 lastClaimedTime; // The last time rewards were claimed
    }

    // Mapping to store staker data
    mapping(address => Staker) public stakers;

    // Annual Percentage Yield (APY) defined for staking rewards
    uint256 public constant APY = 1000; // Example: 10% APY (1000 basis points)
    
    // Number of seconds in a year
    uint256 private constant SECONDS_IN_YEAR = 31536000;

    // Event emitted when rewards are calculated
    event RewardsCalculated(address indexed staker, uint256 rewards);

    /**
     * @dev Function to stake $GIGA tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        
        // Update staker data
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        if (staker.lastClaimedTime == 0) {
            staker.lastClaimedTime = block.timestamp; // Set the initial staking time
        }
    }

    /**
     * @dev Function to calculate staking rewards for the caller.
     * @return The amount of rewards earned.
     */
    function calculateRewards() external view returns (uint256) {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "You have no staked tokens");

        // Calculate the time difference since last claim
        uint256 timeDifference = block.timestamp - staker.lastClaimedTime;

        // Calculate rewards based on APY, time difference, and staked amount
        uint256 rewards = (staker.amountStaked * APY * timeDifference) / (SECONDS_IN_YEAR * 10000);

        return rewards;
    }

    /**
     * @dev Function to claim staking rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "You have no staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards();

        // Update the last claimed time
        staker.lastClaimedTime = block.timestamp;

        // Emit rewards calculated event
        emit RewardsCalculated(msg.sender, rewards);

        // Transfer rewards to the staker (this requires proper token handling, which is omitted here)
        // Example: token.transfer(msg.sender, rewards);
    }

    /**
     * @dev Function to unstake tokens.
     * @param _amount The amount of tokens to unstake.
     */
    function unstakeTokens(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked balance");

        // Claim pending rewards before unstaking
        claimRewards();

        // Update staker data
        staker.amountStaked -= _amount;

        // Transfer unstaked tokens back to the staker (this requires proper token handling, omitted here)
        // Example: token.transfer(msg.sender, _amount);
    }
}
```
