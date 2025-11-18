"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-everdome-staking.pages.dev
Prompt: Create a function in Solidity to calculate the vesting period for claimed rewards in the Everdome staking protocol, ensuring compliance with the 12-month vesting rule.
Generated: DETERMINISTIC_a10e85632226ec00
Batch ID: 20250612_150552
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

contract EverdomeStaking {

    // Struct to hold information about user rewards and vesting
    struct Reward {
        uint256 claimedAmount; // Amount of rewards claimed
        uint256 vestingStartTime; // Timestamp of when the vesting started
        uint256 vestingPeriod; // Duration of the vesting period in seconds
    }

    // Mapping from user addresses to their reward information
    mapping(address => Reward) public rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constants
    uint256 public constant VESTING_DURATION = 365 days; // 12 months vesting period

    /**
     * @dev Function to claim rewards. This function sets the vesting start time and amount of claimed rewards.
     * @param amount The amount of rewards to claim.
     */
    function claimRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Set the rewards for the user
        rewards[msg.sender] = Reward({
            claimedAmount: amount,
            vestingStartTime: block.timestamp,
            vestingPeriod: VESTING_DURATION
        });

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to check if rewards are fully vested.
     * @param user The address of the user to check.
     * @return bool True if the rewards are fully vested, false otherwise.
     */
    function areRewardsVested(address user) external view returns (bool) {
        Reward memory reward = rewards[user];

        // Check if vesting period has expired
        if (reward.claimedAmount == 0) {
            return false; // No rewards claimed
        }
        
        return (block.timestamp >= reward.vestingStartTime + reward.vestingPeriod);
    }

    /**
     * @dev Function to retrieve the claimed rewards of a user.
     * @param user The address of the user to retrieve the claimed rewards for.
     * @return uint256 The amount of claimed rewards.
     */
    function getClaimedRewards(address user) external view returns (uint256) {
        return rewards[user].claimedAmount;
    }
}
```
