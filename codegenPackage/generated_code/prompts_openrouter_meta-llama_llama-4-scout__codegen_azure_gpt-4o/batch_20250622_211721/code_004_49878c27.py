"""
Generated Code Metadata:
========================
Original URL: https://sonicgame.pages.dev
Prompt: "Describe the process of building a fully-onchain game using Sonic's RUSH framework, including one-click deployment and ecosystem-friendly integration."
Generated: DETERMINISTIC_49878c275deb071a
Batch ID: 20250622_211721
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
 * @title OnChainGame
 * @dev A fully on-chain game built using Sonic's RUSH framework.
 * This contract demonstrates one-click deployment and ecosystem-friendly integration.
 */
contract OnChainGame {
    // Game state variables
    uint256 public gameStartTime;
    uint256 public gameEndTime;
    address public owner;
    mapping(address => uint256) public playerScores;

    // Events for game lifecycle
    event GameStarted(uint256 startTime);
    event GameEnded(uint256 endTime);
    event PlayerScored(address indexed player, uint256 score);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to ensure the game is active
    modifier gameActive() {
        require(block.timestamp >= gameStartTime, "Game has not started yet");
        require(block.timestamp <= gameEndTime, "Game has already ended");
        _;
    }

    /**
     * @dev Constructor to initialize the game contract.
     * @param _gameDuration Duration of the game in seconds.
     */
    constructor(uint256 _gameDuration) {
        owner = msg.sender;
        gameStartTime = block.timestamp;
        gameEndTime = block.timestamp + _gameDuration;

        emit GameStarted(gameStartTime);
    }

    /**
     * @dev Function to record a player's score.
     * @param _score The score achieved by the player.
     */
    function recordScore(uint256 _score) external gameActive {
        require(_score > 0, "Score must be greater than zero");
        playerScores[msg.sender] += _score;

        emit PlayerScored(msg.sender, _score);
    }

    /**
     * @dev Function to end the game manually (only owner).
     */
    function endGame() external onlyOwner {
        require(block.timestamp <= gameEndTime, "Game has already ended");
        gameEndTime = block.timestamp;

        emit GameEnded(gameEndTime);
    }

    /**
     * @dev Function to retrieve the score of a specific player.
     * @param _player Address of the player.
     * @return The score of the player.
     */
    function getPlayerScore(address _player) external view returns (uint256) {
        return playerScores[_player];
    }

    /**
     * @dev Function to retrieve the top scorer (for ecosystem-friendly integration).
     * @return The address of the top scorer and their score.
     */
    function getTopScorer() external view returns (address, uint256) {
        address topScorer;
        uint256 highestScore = 0;

        for (uint256 i = 0; i < block.number; i++) {
            address player = address(uint160(i));
            if (playerScores[player] > highestScore) {
                highestScore = playerScores[player];
                topScorer = player;
            }
        }

        return (topScorer, highestScore);
    }
}
```
