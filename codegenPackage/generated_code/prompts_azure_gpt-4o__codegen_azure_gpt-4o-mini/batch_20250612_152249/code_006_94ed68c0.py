"""
Generated Code Metadata:
========================
Original URL: https://bafybeiem4tdb52jvbigbeutv36wrofdneknubfksjyr2unfvv3q4weh4xu.ipfs.dweb.link
Prompt: Write a smart contract to deploy a prediction game using Azuro's architecture, ensuring compliance with the audit reports provided on their GitHub.
Generated: DETERMINISTIC_94ed68c0ea646389
Batch ID: 20250612_152249
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

import "@azuro-protocol/azuro-core/contracts/interfaces/IAzuro.sol";
import "@azuro-protocol/azuro-core/contracts/interfaces/IAzuroFactory.sol";
import "@azuro-protocol/azuro-core/contracts/interfaces/IAzuroGame.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title PredictionGame
 * @dev A smart contract for a prediction game using Azuro's architecture.
 */
contract PredictionGame is Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private gameIdCounter;
    IAzuro public azuro;
    IAzuroFactory public azuroFactory;

    struct Game {
        uint256 id;
        string description;
        uint256 startTime;
        uint256 endTime;
        address creator;
        bool isActive;
    }

    mapping(uint256 => Game) public games;

    event GameCreated(uint256 indexed gameId, string description, uint256 startTime, uint256 endTime, address indexed creator);
    event GameEnded(uint256 indexed gameId);

    /**
     * @dev Constructor to initialize the Azuro protocol.
     * @param _azuro Address of the Azuro protocol.
     * @param _azuroFactory Address of the Azuro factory.
     */
    constructor(address _azuro, address _azuroFactory) {
        require(_azuro != address(0), "Invalid Azuro address");
        require(_azuroFactory != address(0), "Invalid Azuro Factory address");
        
        azuro = IAzuro(_azuro);
        azuroFactory = IAzuroFactory(_azuroFactory);
    }

    /**
     * @dev Create a new prediction game.
     * @param _description Description of the game.
     * @param _startTime Start time of the game.
     * @param _endTime End time of the game.
     */
    function createGame(string memory _description, uint256 _startTime, uint256 _endTime) external onlyOwner {
        require(_startTime < _endTime, "Start time must be before end time");
        require(_startTime > block.timestamp, "Start time must be in the future");

        gameIdCounter.increment();
        uint256 newGameId = gameIdCounter.current();

        games[newGameId] = Game({
            id: newGameId,
            description: _description,
            startTime: _startTime,
            endTime: _endTime,
            creator: msg.sender,
            isActive: true
        });

        emit GameCreated(newGameId, _description, _startTime, _endTime, msg.sender);
    }

    /**
     * @dev End a prediction game.
     * @param _gameId ID of the game to end.
     */
    function endGame(uint256 _gameId) external onlyOwner {
        Game storage game = games[_gameId];
        require(game.isActive, "Game is not active");
        require(block.timestamp >= game.endTime, "Game cannot be ended before its end time");

        game.isActive = false;

        emit GameEnded(_gameId);
    }

    /**
     * @dev Get game details.
     * @param _gameId ID of the game.
     * @return Game details.
     */
    function getGame(uint256 _gameId) external view returns (Game memory) {
        return games[_gameId];
    }
}
```
