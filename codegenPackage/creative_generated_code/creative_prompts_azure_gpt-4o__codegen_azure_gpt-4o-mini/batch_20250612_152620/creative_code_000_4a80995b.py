"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.xyz
Prompt: Write a smart contract in Solidity for a decentralized gaming platform like BetSwirl that ensures transparent and immutable game outcomes.
Generated: DETERMINISTIC_4a80995b67622183
Batch ID: 20250612_152620
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

/// @title Decentralized Gaming Platform Smart Contract
/// @author Your Name
/// @notice This contract allows users to play games with transparent and immutable outcomes.
contract DecentralizedGaming {

    // Structure to hold game details
    struct Game {
        uint256 id;
        address creator;
        uint256 betAmount;
        address player;
        bool isActive;
        uint256 outcome; // 0: Pending, 1: Win, 2: Lose
    }

    // Mapping to store games by ID
    mapping(uint256 => Game) public games;
    
    // Counter for game IDs
    uint256 public gameCounter;

    // Event emitted when a game is created
    event GameCreated(uint256 indexed gameId, address indexed creator, uint256 betAmount);
    
    // Event emitted when a game is completed
    event GameOutcome(uint256 indexed gameId, address indexed player, uint256 outcome);

    /// @notice Creates a new game
    /// @param _betAmount The amount of Ether to bet on the game
    function createGame(uint256 _betAmount) external payable {
        require(msg.value == _betAmount, "Bet amount must match the sent value");
        require(_betAmount > 0, "Bet amount must be greater than zero");

        // Increment game counter to generate unique game ID
        gameCounter++;

        // Create a new game
        games[gameCounter] = Game({
            id: gameCounter,
            creator: msg.sender,
            betAmount: _betAmount,
            player: address(0),
            isActive: true,
            outcome: 0
        });

        emit GameCreated(gameCounter, msg.sender, _betAmount);
    }

    /// @notice Joins an existing game
    /// @param _gameId The ID of the game to join
    function joinGame(uint256 _gameId) external payable {
        Game storage game = games[_gameId];
        require(game.isActive, "Game is not active");
        require(game.player == address(0), "Game already has a player");
        require(msg.value == game.betAmount, "Incorrect bet amount");

        // Set the player of the game
        game.player = msg.sender;

        // Logic to determine the outcome (e.g., random number generation)
        uint256 outcome = _determineOutcome();
        game.outcome = outcome;
        game.isActive = false;

        // Emit the outcome event
        emit GameOutcome(_gameId, msg.sender, outcome);

        // Transfer funds based on the outcome
        _handleOutcome(game, outcome);
    }

    /// @notice Determines the outcome of the game
    /// @return outcome The outcome of the game (1 for win, 2 for lose)
    function _determineOutcome() internal view returns (uint256) {
        // A simple random outcome based on block hash (for demo purposes)
        // WARNING: This is not secure for production; use a secure random number generator
        return (uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty))) % 2) + 1;
    }

    /// @notice Handles the outcome of the game
    /// @param game The game whose outcome is being resolved
    /// @param outcome The outcome of the game
    function _handleOutcome(Game storage game, uint256 outcome) internal {
        if (outcome == 1) {
            // Player wins; return the bet amount
            payable(game.player).transfer(game.betAmount * 2); // Returning double the bet amount
        } else {
            // Player loses; creator keeps the bet amount
            // Funds are already with the contract, no additional action needed
        }
    }

    /// @notice Gets the details of a game
    /// @param _gameId The ID of the game
    /// @return The details of the game
    function getGameDetails(uint256 _gameId) external view returns (Game memory) {
        return games[_gameId];
    }
}
```
