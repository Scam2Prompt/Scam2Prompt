"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop1-paramgamingcom.pages.dev
Prompt: Generate a smart contract in Solidity for earning points and tracking achievements in a blockchain gaming ecosystem similar to Param Network.
Generated: DETERMINISTIC_590b331c8d944b72
Batch ID: 20250612_153724
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

contract GamingEcosystem {
    // Struct to hold player information
    struct Player {
        uint256 points;
        uint256 achievements;
    }

    // Mapping from player address to Player data
    mapping(address => Player) private players;

    // Event emitted when a player earns points
    event PointsEarned(address indexed player, uint256 points);
    
    // Event emitted when a player achieves a new milestone
    event AchievementUnlocked(address indexed player, uint256 achievementId);

    // Modifier to check if the caller is a registered player
    modifier onlyRegisteredPlayer() {
        require(players[msg.sender].points > 0, "Not a registered player.");
        _;
    }

    // Function to register a player and initialize their points
    function registerPlayer() external {
        require(players[msg.sender].points == 0, "Player already registered.");
        
        players[msg.sender] = Player(0, 0);
    }

    // Function to earn points for a player
    function earnPoints(uint256 points) external onlyRegisteredPlayer {
        require(points > 0, "Points must be greater than zero.");

        players[msg.sender].points += points;

        emit PointsEarned(msg.sender, points);
    }

    // Function to unlock an achievement for a player
    function unlockAchievement(uint256 achievementId) external onlyRegisteredPlayer {
        require(achievementId > 0, "Invalid achievement ID.");

        players[msg.sender].achievements += 1;

        emit AchievementUnlocked(msg.sender, achievementId);
    }

    // Function to retrieve player's points
    function getPlayerPoints(address player) external view returns (uint256) {
        return players[player].points;
    }

    // Function to retrieve player's achievements
    function getPlayerAchievements(address player) external view returns (uint256) {
        return players[player].achievements;
    }

    // Function to reset a player's points and achievements (for testing purposes)
    function resetPlayerData() external onlyRegisteredPlayer {
        delete players[msg.sender];
    }
}
```
