"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megadrop-bouncebit.pages.dev
Prompt: Write a Solidity contract to distribute rewards based on user rankings in a gamified blockchain system, referencing Points Paradise's leaderboard structure.
Generated: DETERMINISTIC_c6a14f5a2425a713
Batch ID: 20250612_152235
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
 * @title PointsParadiseRewards
 * @dev A smart contract to distribute rewards based on user rankings in a gamified blockchain system.
 */
contract PointsParadiseRewards {
    // Owner of the contract
    address public owner;

    // Mapping to store user rankings and points
    mapping(address => uint256) public userPoints;

    // Array to store leaderboard addresses
    address[] public leaderboard;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 totalReward, uint256 timestamp);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update the leaderboard.
     * @param users Array of user addresses.
     * @param points Array of corresponding user points.
     * Requirements:
     * - Arrays must have the same length.
     * - Only contract owner can call this function.
     */
    function updateLeaderboard(address[] calldata users, uint256[] calldata points) external onlyOwner {
        require(users.length == points.length, "Input arrays must have the same length");
        leaderboard = users;

        for (uint256 i = 0; i < users.length; i++) {
            userPoints[users[i]] = points[i];
        }
    }

    /**
     * @dev Function to distribute rewards to users based on their rankings.
     * @param totalReward Total amount of reward to distribute.
     * Requirements:
     * - The leaderboard should not be empty.
     * - Only contract owner can call this function.
     */
    function distributeRewards(uint256 totalReward) external onlyOwner {
        require(leaderboard.length > 0, "Leaderboard is empty");
        require(totalReward > 0, "Total reward must be greater than zero");

        uint256 totalPoints = 0;

        // Calculate total points on the leaderboard
        for (uint256 i = 0; i < leaderboard.length; i++) {
            totalPoints += userPoints[leaderboard[i]];
        }

        require(totalPoints > 0, "Total points must be greater than zero");

        // Distribute rewards proportionally based on user points
        for (uint256 i = 0; i < leaderboard.length; i++) {
            address user = leaderboard[i];
            uint256 userReward = (totalReward * userPoints[user]) / totalPoints;

            // Transfer reward to the user
            (bool success, ) = user.call{value: userReward}("");
            require(success, "Reward transfer failed");
        }

        emit RewardsDistributed(totalReward, block.timestamp);
    }

    /**
     * @dev Function to receive Ether (if needed for funding rewards).
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw Ether from the contract.
     * Requirements:
     * - Only contract owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
