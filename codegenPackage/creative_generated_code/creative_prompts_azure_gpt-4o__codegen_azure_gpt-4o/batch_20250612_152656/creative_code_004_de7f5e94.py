"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notcoin-90l.pages.dev
Prompt: Write a Solidity smart contract that tracks NotCoin mining progress and rewards users with bonuses for inviting friends and advancing through leagues, as described in the NotCoin ecosystem.
Generated: DETERMINISTIC_de7f5e943fad5209
Batch ID: 20250612_152656
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
 * @title NotCoinMiningTracker
 * @dev A contract to track mining progress, reward users for inviting friends,
 * and provide bonuses for progressing through leagues in the NotCoin ecosystem.
 */
contract NotCoinMiningTracker {
    // Struct to store user data
    struct User {
        uint256 miningProgress;   // Tracks mining progress
        uint256 bonusRewards;     // Tracks total bonus rewards
        uint256 league;           // Current league of the user
        address[] invitedFriends; // List of invited friends
    }

    // Mapping to track registered users
    mapping(address => User) private users;

    // Event emitted when a user receives a bonus reward
    event BonusRewarded(address indexed user, uint256 bonusAmount, string reason);

    // Modifier to ensure only registered users can call certain functions
    modifier onlyRegistered() {
        require(users[msg.sender].league > 0, "User not registered");
        _;
    }

    /**
     * @dev Registers a new user and assigns them to the initial league.
     */
    function registerUser() external {
        require(users[msg.sender].league == 0, "User already registered");
        users[msg.sender] = User(0, 0, 1, new address[](0));
    }

    /**
     * @dev Updates the user's mining progress.
     * @param progress The amount of mining progress to add.
     */
    function updateMiningProgress(uint256 progress) external onlyRegistered {
        users[msg.sender].miningProgress += progress;

        // Reward user with a mining bonus if they reach a milestone
        if (users[msg.sender].miningProgress % 1000 == 0) {
            uint256 bonus = 50; // Example bonus amount
            users[msg.sender].bonusRewards += bonus;
            emit BonusRewarded(msg.sender, bonus, "Mining milestone reached");
        }
    }

    /**
     * @dev Allows a user to invite a friend to the platform.
     * @param friend The address of the friend being invited.
     */
    function inviteFriend(address friend) external onlyRegistered {
        require(friend != msg.sender, "Cannot invite yourself");
        require(users[friend].league == 0, "Friend is already registered");

        users[msg.sender].invitedFriends.push(friend);

        // Reward the inviter with a bonus for inviting a friend
        uint256 bonus = 100; // Example bonus amount
        users[msg.sender].bonusRewards += bonus;
        emit BonusRewarded(msg.sender, bonus, "Invited a friend");
    }

    /**
     * @dev Advances the user to the next league if eligible.
     */
    function advanceLeague() external onlyRegistered {
        uint256 currentLeague = users[msg.sender].league;

        // Example league progression logic
        require(currentLeague < 5, "Already in the highest league");
        require(users[msg.sender].miningProgress >= currentLeague * 1000, "Not enough mining progress");

        users[msg.sender].league += 1;

        // Reward user with a bonus for advancing leagues
        uint256 bonus = currentLeague * 200; // Example bonus amount
        users[msg.sender].bonusRewards += bonus;
        emit BonusRewarded(msg.sender, bonus, "Advanced to next league");
    }

    /**
     * @dev Retrieves user data.
     * @return miningProgress The mining progress of the user.
     * @return bonusRewards The total bonus rewards of the user.
     * @return league The current league of the user.
     * @return invitedFriends The list of friends invited by the user.
     */
    function getUserData()
        external
        view
        onlyRegistered
        returns (
            uint256 miningProgress,
            uint256 bonusRewards,
            uint256 league,
            address[] memory invitedFriends
        )
    {
        User memory user = users[msg.sender];
        return (user.miningProgress, user.bonusRewards, user.league, user.invitedFriends);
    }
}
```
