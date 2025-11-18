"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Write a smart contract in Solidity to implement a leaderboard system for tracking $AI holders' lock durations and reward multipliers in the Diamond Hands app.
Generated: DETERMINISTIC_f774f3c88f9d1062
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Leaderboard Smart Contract
 * @dev This contract tracks $AI token lock durations and calculates reward multipliers for a leaderboard system.
 */
contract DiamondHandsLeaderboard {
    // Struct to hold user data
    struct UserData {
        uint256 lockDuration; // Lock duration in seconds
        uint256 rewardMultiplier; // Reward multiplier based on lock duration
    }

    // Mapping to store user data
    mapping(address => UserData) private userInfo;

    // Event emitted when a user updates their lock duration
    event LockDurationUpdated(address indexed user, uint256 lockDuration, uint256 rewardMultiplier);

    /**
     * @dev Modifier to ensure valid lock duration.
     * Requires lock duration to be greater than zero.
     */
    modifier validLockDuration(uint256 lockDuration) {
        require(lockDuration > 0, "Lock duration must be greater than zero");
        _;
    }

    /**
     * @dev Function to update user's lock duration and calculate the reward multiplier.
     * Emits a LockDurationUpdated event.
     * @param lockDuration The lock duration in seconds.
     */
    function updateLockDuration(uint256 lockDuration) external validLockDuration(lockDuration) {
        // Calculate reward multiplier (example formula: 1x for 30 days, 2x for 90 days, 3x for 180 days)
        uint256 rewardMultiplier = calculateRewardMultiplier(lockDuration);

        // Update user's data
        userInfo[msg.sender] = UserData({
            lockDuration: lockDuration,
            rewardMultiplier: rewardMultiplier
        });

        // Emit event
        emit LockDurationUpdated(msg.sender, lockDuration, rewardMultiplier);
    }

    /**
     * @dev Function to retrieve user data.
     * @param user Address of the user to retrieve the data for.
     * @return lockDuration The lock duration of the user.
     * @return rewardMultiplier The reward multiplier of the user.
     */
    function getUserData(address user) external view returns (uint256 lockDuration, uint256 rewardMultiplier) {
        UserData memory data = userInfo[user];
        return (data.lockDuration, data.rewardMultiplier);
    }

    /**
     * @dev Internal function to calculate reward multiplier based on lock duration.
     * @param lockDuration The lock duration in seconds.
     * @return rewardMultiplier The calculated reward multiplier.
     */
    function calculateRewardMultiplier(uint256 lockDuration) internal pure returns (uint256 rewardMultiplier) {
        if (lockDuration >= 180 days) {
            return 3; // 3x multiplier for 180 days or more
        } else if (lockDuration >= 90 days) {
            return 2; // 2x multiplier for 90 days or more
        } else if (lockDuration >= 30 days) {
            return 1; // 1x multiplier for 30 days or more
        } else {
            return 0; // No multiplier for less than 30 days
        }
    }
}
```
