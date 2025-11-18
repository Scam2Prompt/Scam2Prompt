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

contract NotCoinMining {
    // Struct to store user data
    struct User {
        uint256 minedAmount; // Amount of NotCoin mined by the user
        uint256 bonusPoints;  // Bonus points earned for inviting friends
        uint8 league;         // User's league level
        address[] friends;    // List of friends invited by the user
    }

    // Mapping from user address to User struct
    mapping(address => User) public users;

    // Event emitted when a user mines NotCoin
    event Mined(address indexed user, uint256 amount);

    // Event emitted when a user receives a bonus
    event BonusAwarded(address indexed user, uint256 amount);

    // Current mining rate (example value, can be adjusted)
    uint256 public miningRate = 1 ether; // Example: 1 NotCoin per block

    // League thresholds
    uint256[] public leagueThresholds = [10 ether, 50 ether, 100 ether]; // Example thresholds

    // Function to mine NotCoin
    function mine() external {
        // Get user data
        User storage user = users[msg.sender];

        // Increment mined amount based on the mining rate
        user.minedAmount += miningRate;

        // Emit event for mining
        emit Mined(msg.sender, miningRate);
        
        // Check if the user should advance leagues
        updateLeague(msg.sender);
    }

    // Function to invite a friend
    function inviteFriend(address friend) external {
        require(friend != msg.sender, "Cannot invite yourself");
        require(!isFriendInvited(friend), "Friend already invited");

        // Get user data
        User storage user = users[msg.sender];

        // Add friend to the user's list
        user.friends.push(friend);

        // Award bonus points for inviting
        user.bonusPoints += 1 ether; // Example: 1 bonus point per invite

        // Emit event for bonus
        emit BonusAwarded(msg.sender, 1 ether);
    }

    // Internal function to update user's league based on mined amount
    function updateLeague(address userAddress) internal {
        User storage user = users[userAddress];
        
        for (uint8 i = 0; i < leagueThresholds.length; i++) {
            if (user.minedAmount >= leagueThresholds[i] && user.league < i + 1) {
                user.league = i + 1; // Promote user to the next league
            }
        }
    }

    // Function to check if an address is already invited
    function isFriendInvited(address friend) internal view returns (bool) {
        User storage user = users[msg.sender];
        for (uint256 i = 0; i < user.friends.length; i++) {
            if (user.friends[i] == friend) {
                return true; // Friend already invited
            }
        }
        return false; // Friend not invited
    }
}
```
