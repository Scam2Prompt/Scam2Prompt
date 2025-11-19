"""
Generated Code Metadata:
========================
Original URL: https://kaaia.io
Prompt: Generate a smart contract compatible with Kaia's EVM equivalence that supports real-time gaming transactions with 1-second block time and immediate finality.
Generated: DETERMINISTIC_f302740dc12b90a1
Batch ID: 20250612_154029
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

/// @title RealTimeGamingContract
/// @dev A smart contract for handling real-time gaming transactions
contract RealTimeGamingContract {
    // Event emitted when a new game is created
    event GameCreated(uint256 indexed gameId, address indexed creator, uint256 entryFee);
    
    // Event emitted when a player joins a game
    event PlayerJoined(uint256 indexed gameId, address indexed player);
    
    // Event emitted when a game is completed
    event GameCompleted(uint256 indexed gameId, address indexed winner, uint256 prize);

    // Struct to represent a game
    struct Game {
        address creator;
        uint256 entryFee;
        address[] players;
        bool isActive;
    }

    // Mapping to store games by their ID
    mapping(uint256 => Game) public games;
    uint256 public gameCount;

    // Modifier to check if the game is active
    modifier onlyActiveGame(uint256 gameId) {
        require(games[gameId].isActive, "Game is not active");
        _;
    }

    // Function to create a new game
    function createGame(uint256 _entryFee) external {
        require(_entryFee > 0, "Entry fee must be greater than zero");

        gameCount++;
        games[gameCount] = Game({
            creator: msg.sender,
            entryFee: _entryFee,
            players: new address[](0),
            isActive: true
        });

        emit GameCreated(gameCount, msg.sender, _entryFee);
    }

    // Function for a player to join a game
    function joinGame(uint256 gameId) external payable onlyActiveGame(gameId) {
        Game storage game = games[gameId];
        
        require(msg.value == game.entryFee, "Incorrect entry fee");
        require(msg.sender != game.creator, "Creator cannot join their own game");
        
        game.players.push(msg.sender);
        
        emit PlayerJoined(gameId, msg.sender);
    }

    // Function to complete a game and declare a winner
    function completeGame(uint256 gameId, address winner) external onlyActiveGame(gameId) {
        Game storage game = games[gameId];
        
        require(msg.sender == game.creator, "Only the creator can complete the game");
        require(isPlayerInGame(winner, gameId), "Winner must be a player in the game");

        // Transfer the prize to the winner
        uint256 prize = game.entryFee * game.players.length;
        payable(winner).transfer(prize);

        // Mark the game as inactive
        game.isActive = false;

        emit GameCompleted(gameId, winner, prize);
    }

    // Internal function to check if an address is a player in the game
    function isPlayerInGame(address player, uint256 gameId) internal view returns (bool) {
        Game storage game = games[gameId];
        for (uint256 i = 0; i < game.players.length; i++) {
            if (game.players[i] == player) {
                return true;
            }
        }
        return false;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
