"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yologames-io.pages.dev
Prompt: Create a Solidity contract for a rewards system that tracks player points across multiple games, similar to the seasonal rewards described on YOLO Games.
Generated: DETERMINISTIC_589cb7a4647458a1
Batch ID: 20250612_153512
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
 * @title RewardsSystem
 * @dev A smart contract to manage player points across multiple games.
 * Players earn points, and the contract tracks these points per game.
 */
contract RewardsSystem {
    // Struct to hold player data
    struct Player {
        uint256 totalPoints;
        mapping(string => uint256) gamePoints; // Points per game
    }

    // Mapping from player address to their Player struct
    mapping(address => Player) private players;

    // Events
    event PointsAdded(address indexed player, string indexed game, uint256 points);
    event PointsReset(address indexed player, string indexed game);

    /**
     * @dev Modifier to ensure a valid game name is provided.
     * @param game The name of the game.
     */
    modifier validGame(string memory game) {
        require(bytes(game).length > 0, "Game name cannot be empty");
        _;
    }

    /**
     * @dev Add points to a player's total and for a specific game.
     * @param player The address of the player.
     * @param game The name of the game.
     * @param points The number of points to add.
     */
    function addPoints(address player, string memory game, uint256 points) external validGame(game) {
        require(player != address(0), "Invalid player address");
        require(points > 0, "Points must be greater than zero");

        Player storage p = players[player];
        p.totalPoints += points;
        p.gamePoints[game] += points;

        emit PointsAdded(player, game, points);
    }

    /**
     * @dev Get a player's total points across all games.
     * @param player The address of the player.
     * @return The total points of the player.
     */
    function getTotalPoints(address player) external view returns (uint256) {
        require(player != address(0), "Invalid player address");
        return players[player].totalPoints;
    }

    /**
     * @dev Get a player's points for a specific game.
     * @param player The address of the player.
     * @param game The name of the game.
     * @return The points of the player for the specified game.
     */
    function getGamePoints(address player, string memory game) external view validGame(game) returns (uint256) {
        require(player != address(0), "Invalid player address");
        return players[player].gamePoints[game];
    }

    /**
     * @dev Reset a player's points for a specific game.
     * @param player The address of the player.
     * @param game The name of the game.
     */
    function resetGamePoints(address player, string memory game) external validGame(game) {
        require(player != address(0), "Invalid player address");

        Player storage p = players[player];
        uint256 gamePoints = p.gamePoints[game];

        require(gamePoints > 0, "Player has no points for this game");

        p.totalPoints -= gamePoints;
        p.gamePoints[game] = 0;

        emit PointsReset(player, game);
    }
}
```
