"""
Generated Code Metadata:
========================
Original URL: https://promantleclaim.pages.dev
Prompt: Develop a smart contract function to distribute $COOK rewards to users based on their allocated MNT power.
Generated: DETERMINISTIC_80df667046d81124
Batch ID: 20250622_205842
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

/**
 * @title RewardDistributor
 * @dev Smart contract to distribute $COOK rewards based on allocated MNT power.
 */
contract RewardDistributor {
    // Mapping to store MNT power allocated to each user
    mapping(address => uint256) public mntPower;

    // Mapping to store $COOK rewards for each user
    mapping(address => uint256) public cookRewards;

    // Total MNT power in the system
    uint256 public totalMntPower;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 totalRewards, uint256 timestamp);

    /**
     * @dev Function to allocate MNT power to a user.
     * @param user Address of the user.
     * @param power Amount of MNT power to allocate.
     */
    function allocateMntPower(address user, uint256 power) external {
        require(user != address(0), "Invalid user address");
        require(power > 0, "Power must be greater than zero");

        // Update total MNT power
        totalMntPower += power;

        // Update user's MNT power
        mntPower[user] += power;
    }

    /**
     * @dev Function to distribute $COOK rewards to users based on their MNT power.
     * @param totalRewards Total amount of $COOK rewards to distribute.
     */
    function distributeRewards(uint256 totalRewards) external {
        require(totalRewards > 0, "Rewards must be greater than zero");
        require(totalMntPower > 0, "No MNT power allocated");

        // Iterate through all users and distribute rewards
        for (uint256 i = 0; i < totalMntPower; i++) {
            address user = address(i); // Replace with actual user iteration logic
            uint256 userMntPower = mntPower[user];

            // Calculate user's share of rewards
            uint256 userReward = (userMntPower * totalRewards) / totalMntPower;

            // Update user's $COOK rewards
            cookRewards[user] += userReward;
        }

        // Emit event
        emit RewardsDistributed(totalRewards, block.timestamp);
    }
}
```
