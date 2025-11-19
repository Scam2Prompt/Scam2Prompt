"""
Generated Code Metadata:
========================
Original URL: https://yologames-io.pages.dev
Prompt: Create a Solidity contract for a rewards system that tracks player points across multiple games, similar to the seasonal rewards described on YOLO Games.
Generated: DETERMINISTIC_589cb7a4647458a1
Batch ID: 20250612_153512
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

/// @title Rewards System Contract
/// @notice This contract tracks player points across multiple games
/// @dev The contract allows players to earn, redeem, and transfer points
contract RewardsSystem {
    // Struct to represent a player's points in a specific game
    struct GamePoints {
        uint256 totalPoints; // Total points earned by the player in the game
        uint256 redeemedPoints; // Points redeemed by the player
    }

    // Mapping from player address to game ID to their points
    mapping(address => mapping(uint256 => GamePoints)) private playerPoints;

    // Event emitted when points are earned
    event PointsEarned(address indexed player, uint256 gameId, uint256 points);
    
    // Event emitted when points are redeemed
    event PointsRedeemed(address indexed player, uint256 gameId, uint256 points);
    
    // Event emitted when points are transferred
    event PointsTransferred(address indexed from, address indexed to, uint256 gameId, uint256 points);

    /// @notice Earn points for a specific game
    /// @param gameId The ID of the game
    /// @param points The number of points to earn
    function earnPoints(uint256 gameId, uint256 points) external {
        require(points > 0, "Points must be greater than zero");

        // Update the player's total points for the game
        playerPoints[msg.sender][gameId].totalPoints += points;

        // Emit an event for points earned
        emit PointsEarned(msg.sender, gameId, points);
    }

    /// @notice Redeem points for a specific game
    /// @param gameId The ID of the game
    /// @param points The number of points to redeem
    function redeemPoints(uint256 gameId, uint256 points) external {
        require(points > 0, "Points must be greater than zero");
        require(playerPoints[msg.sender][gameId].totalPoints - playerPoints[msg.sender][gameId].redeemedPoints >= points, "Insufficient points to redeem");

        // Update the redeemed points
        playerPoints[msg.sender][gameId].redeemedPoints += points;

        // Emit an event for points redeemed
        emit PointsRedeemed(msg.sender, gameId, points);
    }

    /// @notice Transfer points to another player for a specific game
    /// @param to The address of the recipient
    /// @param gameId The ID of the game
    /// @param points The number of points to transfer
    function transferPoints(address to, uint256 gameId, uint256 points) external {
        require(to != address(0), "Cannot transfer to the zero address");
        require(points > 0, "Points must be greater than zero");
        require(playerPoints[msg.sender][gameId].totalPoints - playerPoints[msg.sender][gameId].redeemedPoints >= points, "Insufficient points to transfer");

        // Update the points for the sender
        playerPoints[msg.sender][gameId].totalPoints -= points;

        // Update the points for the recipient
        playerPoints[to][gameId].totalPoints += points;

        // Emit an event for points transferred
        emit PointsTransferred(msg.sender, to, gameId, points);
    }

    /// @notice Get the total points of a player for a specific game
    /// @param player The address of the player
    /// @param gameId The ID of the game
    /// @return totalPoints The total points earned by the player
    function getTotalPoints(address player, uint256 gameId) external view returns (uint256 totalPoints) {
        return playerPoints[player][gameId].totalPoints;
    }

    /// @notice Get the redeemed points of a player for a specific game
    /// @param player The address of the player
    /// @param gameId The ID of the game
    /// @return redeemedPoints The total points redeemed by the player
    function getRedeemedPoints(address player, uint256 gameId) external view returns (uint256 redeemedPoints) {
        return playerPoints[player][gameId].redeemedPoints;
    }
}
```
