"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicgame.pages.dev
Prompt: Provide an example of using Sonic's composable gaming primitives and sandbox utilities to build business logic for an on-chain game.
Generated: DETERMINISTIC_aa9056c00c01d3c8
Batch ID: 20250612_145831
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
 * @title OnChainGame
 * @dev Example of using composable gaming primitives and sandbox utilities with Sonic.
 * This contract demonstrates a simple on-chain game logic with player registration,
 * scoring, and reward system.
 */

import "@sonicprotocol/core/Sandbox.sol";
import "@sonicprotocol/core/GamePrimitives.sol";

contract OnChainGame {
    using GamePrimitives for GamePrimitives.Score;
    using Sandbox for Sandbox.Action;

    // State variables
    address public owner;
    uint256 public gameEndTime; // Timestamp when the game ends
    mapping(address => GamePrimitives.Score) public playerScores; // Player scores
    mapping(address => bool) public registeredPlayers; // Track registered players
    uint256 public rewardPool; // Total reward pool

    // Events
    event PlayerRegistered(address indexed player);
    event ActionPerformed(address indexed player, uint256 score);
    event RewardsDistributed(uint256 totalRewards);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    modifier gameActive() {
        require(block.timestamp < gameEndTime, "Game has ended.");
        _;
    }

    modifier onlyRegisteredPlayer() {
        require(registeredPlayers[msg.sender], "Player is not registered.");
        _;
    }

    constructor(uint256 _gameDuration) payable {
        require(msg.value > 0, "Initial reward pool must be greater than 0.");
        owner = msg.sender;
        gameEndTime = block.timestamp + _gameDuration;
        rewardPool = msg.value;
    }

    /**
     * @dev Registers a player for the game.
     */
    function registerPlayer() external gameActive {
        require(!registeredPlayers[msg.sender], "Player is already registered.");
        registeredPlayers[msg.sender] = true;
        playerScores[msg.sender] = GamePrimitives.Score(0); // Initialize score to 0
        emit PlayerRegistered(msg.sender);
    }

    /**
     * @dev Performs an action within the Sonic sandbox. Updates player's score based on the action.
     * @param actionType The type of action performed (e.g., "attack", "defend").
     * @param actionValue A numeric value representing the action's impact.
     */
    function performAction(string memory actionType, uint256 actionValue)
        external
        gameActive
        onlyRegisteredPlayer
    {
        Sandbox.Action memory action = Sandbox.Action(actionType, actionValue);
        GamePrimitives.Score storage score = playerScores[msg.sender];

        // Validate the action using Sonic's sandbox utilities
        require(action.isValid(), "Invalid action!");

        // Update the player's score using Sonic's composable primitives
        score.updateScore(actionValue);

        emit ActionPerformed(msg.sender, score.value);
    }

    /**
     * @dev Distributes rewards based on player scores. Can only be called after the game ends.
     */
    function distributeRewards() external onlyOwner {
        require(block.timestamp >= gameEndTime, "Game is still active.");

        uint256 totalScore = 0;
        uint256 totalRewards = rewardPool;

        // Calculate total score of all players
        for (uint256 i = 0; i < registeredPlayersList.length; i++) {
            totalScore += playerScores[registeredPlayersList[i]].value;
        }

        // Distribute rewards proportionally
        for (uint256 i = 0; i < registeredPlayersList.length; i++) {
            address player = registeredPlayersList[i];
            uint256 playerScore = playerScores[player].value;

            uint256 reward = (playerScore * totalRewards) / totalScore;
            (bool success, ) = player.call{value: reward}("");
            require(success, "Reward transfer failed!");
        }

        emit RewardsDistributed(totalRewards);
    }

    /**
     * @dev Fallback function to receive additional reward pool contributions.
     */
    receive() external payable {
        rewardPool += msg.value;
    }
}
```
