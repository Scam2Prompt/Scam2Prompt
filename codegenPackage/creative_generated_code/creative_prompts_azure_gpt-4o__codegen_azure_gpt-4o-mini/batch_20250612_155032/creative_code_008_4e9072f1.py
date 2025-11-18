"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nbnm.pages.dev
Prompt: Write a smart contract that calculates and distributes rewards based on Sonic Gems rankings (Emrald, Sapphire, Ruby) for participating applications.
Generated: DETERMINISTIC_4e9072f1dc745794
Batch ID: 20250612_155032
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

/// @title Sonic Gems Reward Distribution Contract
/// @dev This contract calculates and distributes rewards based on user rankings (Emerald, Sapphire, Ruby)
contract SonicGemsReward {

    // Enum to represent the rankings
    enum Rank { Emerald, Sapphire, Ruby }

    // Structure to hold user information
    struct User {
        Rank rank;
        uint256 reward;
        bool exists;
    }

    // Mapping of user addresses to their information
    mapping(address => User) private users;

    // Total rewards pool
    uint256 public totalRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 reward);

    // Modifier to check if user exists
    modifier userExists(address _user) {
        require(users[_user].exists, "User does not exist");
        _;
    }

    // Function to add or update a user
    function setUser(address _user, Rank _rank) external {
        require(_user != address(0), "Invalid user address");
        users[_user] = User({
            rank: _rank,
            reward: 0,
            exists: true
        });
    }

    // Function to deposit total rewards into the contract
    function depositRewards() external payable {
        require(msg.value > 0, "Must deposit a positive amount");
        totalRewards += msg.value;
    }

    // Function to calculate rewards based on user rank
    function calculateRewards(address _user) public userExists(_user) {
        uint256 reward;

        // Calculate the reward based on rank
        if (users[_user].rank == Rank.Emerald) {
            reward = totalRewards * 50 / 100; // 50% for Emerald
        } else if (users[_user].rank == Rank.Sapphire) {
            reward = totalRewards * 30 / 100; // 30% for Sapphire
        } else if (users[_user].rank == Rank.Ruby) {
            reward = totalRewards * 20 / 100; // 20% for Ruby
        }

        users[_user].reward += reward;
    }

    // Function to distribute rewards to the user
    function distributeRewards(address _user) external userExists(_user) {
        calculateRewards(_user);

        uint256 rewardToDistribute = users[_user].reward;
        require(rewardToDistribute > 0, "No rewards to distribute");

        // Resetting the user's reward
        users[_user].reward = 0;

        // Transfer the reward to the user
        (bool success, ) = _user.call{value: rewardToDistribute}("");
        require(success, "Reward distribution failed");

        emit RewardsDistributed(_user, rewardToDistribute);
    }

    // Function to withdraw remaining contract balance (only owner can call this)
    function withdrawBalance() external {
        // It is assumed that this function is protected by an access control modifier in a real contract
        require(totalRewards > 0, "No balance to withdraw");

        uint256 balance = totalRewards;
        totalRewards = 0;

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to receive Ether
    receive() external payable {
        depositRewards();
    }
}
```
