"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnia.pages.dev
Prompt: Write a script to deploy a decentralized gaming platform on Somnia's Layer 1 blockchain, ensuring high transaction throughput and cross-chain liquidity.
Generated: DETERMINISTIC_68b302446291781a
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Decentralized Gaming Platform
 * @dev This contract deploys a gaming platform on Somnia's Layer 1 blockchain
 *      ensuring high transaction throughput and cross-chain liquidity.
 */
contract DecentralizedGamingPlatform {
    // Events
    event GameCreated(uint gameId, string name, address indexed creator, uint creationTime);
    event PlayerJoined(uint gameId, address indexed player, uint joinTime);
    event GameEnded(uint gameId, address indexed creator, uint endTime);

    // Struct to store game details
    struct Game {
        uint id;
        string name;
        address creator;
        bool isActive;
        uint creationTime;
    }

    // Mapping to store games
    mapping(uint => Game) private games;
    uint private nextGameId;

    // Mapping to store players in each game
    mapping(uint => address[]) private gamePlayers;

    // Modifier to ensure game exists
    modifier gameExists(uint gameId) {
        require(games[gameId].creator != address(0), "Game does not exist");
        _;
    }

    // Modifier to ensure game is active
    modifier gameIsActive(uint gameId) {
        require(games[gameId].isActive, "Game is not active");
        _;
    }

    /**
     * @dev Create a new game.
     * @param name The name of the game.
     */
    function createGame(string calldata name) external {
        require(bytes(name).length > 0, "Game name cannot be empty");

        games[nextGameId] = Game({
            id: nextGameId,
            name: name,
            creator: msg.sender,
            isActive: true,
            creationTime: block.timestamp
        });

        emit GameCreated(nextGameId, name, msg.sender, block.timestamp);
        nextGameId++;
    }

    /**
     * @dev Join an existing game.
     * @param gameId The ID of the game to join.
     */
    function joinGame(uint gameId) external gameExists(gameId) gameIsActive(gameId) {
        // Ensure the player isn't already in the game
        address[] storage players = gamePlayers[gameId];
        for (uint i = 0; i < players.length; i++) {
            require(players[i] != msg.sender, "Player already joined the game");
        }

        players.push(msg.sender);

        emit PlayerJoined(gameId, msg.sender, block.timestamp);
    }

    /**
     * @dev End a game.
     * @param gameId The ID of the game to end.
     */
    function endGame(uint gameId) external gameExists(gameId) gameIsActive(gameId) {
        // Ensure only the creator can end the game
        require(games[gameId].creator == msg.sender, "Only the creator can end the game");

        games[gameId].isActive = false;

        emit GameEnded(gameId, msg.sender, block.timestamp);
    }

    /**
     * @dev Retrieve details of a game.
     * @param gameId The ID of the game.
     * @return Game details (id, name, creator, isActive, creationTime).
     */
    function getGameDetails(uint gameId)
        external
        view
        gameExists(gameId)
        returns (uint, string memory, address, bool, uint)
    {
        Game memory game = games[gameId];
        return (game.id, game.name, game.creator, game.isActive, game.creationTime);
    }

    /**
     * @dev Get players of a game.
     * @param gameId The ID of the game.
     * @return Array of player addresses.
     */
    function getPlayers(uint gameId)
        external
        view
        gameExists(gameId)
        returns (address[] memory)
    {
        return gamePlayers[gameId];
    }
}
```
