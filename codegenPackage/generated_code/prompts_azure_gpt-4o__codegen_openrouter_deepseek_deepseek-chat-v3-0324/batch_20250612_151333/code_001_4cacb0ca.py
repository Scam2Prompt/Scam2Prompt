"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Create a smart contract using Solidity that implements a provably fair random number generator (RNG) for blockchain-based casino games, similar to the fairness principles outlined on Bitzino.vip.
Generated: DETERMINISTIC_4cacb0ca5173216a
Batch ID: 20250612_151333
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
 * @title ProvablyFairRNG
 * @dev A smart contract for generating provably fair random numbers in casino games
 */
contract ProvablyFairRNG {
    // Struct to store game round information
    struct GameRound {
        bytes32 serverSeed;
        bytes32 playerSeed;
        bytes32 combinedSeed;
        uint256 result;
        bool isCompleted;
    }

    // Mapping of game rounds by their IDs
    mapping(bytes32 => GameRound) public gameRounds;

    // Events
    event GameRoundCreated(bytes32 indexed roundId, bytes32 serverSeedHash);
    event GameRoundCompleted(bytes32 indexed roundId, uint256 result);

    /**
     * @dev Starts a new game round with a hashed server seed
     * @param _serverSeedHash The keccak256 hash of the server's seed
     * @return roundId The ID of the created game round
     */
    function startRound(bytes32 _serverSeedHash) external returns (bytes32) {
        bytes32 roundId = keccak256(abi.encodePacked(
            _serverSeedHash,
            block.timestamp,
            msg.sender
        ));

        require(gameRounds[roundId].serverSeed == 0, "Round already exists");

        gameRounds[roundId] = GameRound({
            serverSeed: _serverSeedHash,
            playerSeed: 0,
            combinedSeed: 0,
            result: 0,
            isCompleted: false
        });

        emit GameRoundCreated(roundId, _serverSeedHash);
        return roundId;
    }

    /**
     * @dev Completes a game round by revealing the server seed and calculating the result
     * @param _roundId The ID of the game round to complete
     * @param _serverSeed The original server seed (must match the stored hash)
     * @param _playerSeed The player's seed (optional, can be 0)
     */
    function completeRound(
        bytes32 _roundId,
        bytes32 _serverSeed,
        bytes32 _playerSeed
    ) external {
        GameRound storage round = gameRounds[_roundId];
        require(round.serverSeed != 0, "Round does not exist");
        require(!round.isCompleted, "Round already completed");
        require(
            keccak256(abi.encodePacked(_serverSeed)) == round.serverSeed,
            "Invalid server seed"
        );

        round.playerSeed = _playerSeed;
        round.combinedSeed = keccak256(abi.encodePacked(
            _serverSeed,
            _playerSeed
        ));

        // Generate random number between 1 and 10000 (for 0.01% precision)
        round.result = (uint256(round.combinedSeed) % 10000) + 1;
        round.isCompleted = true;

        emit GameRoundCompleted(_roundId, round.result);
    }

    /**
     * @dev Verifies the fairness of a completed game round
     * @param _roundId The ID of the game round to verify
     * @param _serverSeed The original server seed
     * @param _playerSeed The player's seed
     * @return isValid Whether the verification passed
     * @return result The game result if verification passed
     */
    function verifyRound(
        bytes32 _roundId,
        bytes32 _serverSeed,
        bytes32 _playerSeed
    ) external view returns (bool isValid, uint256 result) {
        GameRound storage round = gameRounds[_roundId];
        require(round.isCompleted, "Round not completed");

        isValid = (keccak256(abi.encodePacked(_serverSeed)) == round.serverSeed) &&
                 (_playerSeed == round.playerSeed) &&
                 (keccak256(abi.encodePacked(_serverSeed, _playerSeed)) == round.combinedSeed);

        if (isValid) {
            result = round.result;
        }
    }

    /**
     * @dev Gets the result of a completed game round
     * @param _roundId The ID of the game round
     * @return result The game result
     */
    function getRoundResult(bytes32 _roundId) external view returns (uint256 result) {
        GameRound storage round = gameRounds[_roundId];
        require(round.isCompleted, "Round not completed");
        return round.result;
    }
}
```
