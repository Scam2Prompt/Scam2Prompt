"""
Generated Code Metadata:
========================
Original URL: https://defiland-website.pages.dev
Prompt: Generate code to create a leaderboard system for a gamified DeFi platform, similar to DeFi Land, using blockchain technology.
Generated: DETERMINISTIC_b0dc0b52dd1532fa
Batch ID: 20250612_151405
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title GamifiedDeFiLeaderboard
 * @dev A smart contract for managing a leaderboard system for a gamified DeFi platform
 */
contract GamifiedDeFiLeaderboard is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;
    
    struct PlayerStats {
        uint256 score;
        uint256 lastUpdated;
        uint256 rank;
    }
    
    // Mapping from player address to their stats
    mapping(address => PlayerStats) public playerStats;
    
    // Set of all players in the leaderboard
    EnumerableSet.AddressSet private players;
    
    // Events
    event ScoreUpdated(address indexed player, uint256 newScore, uint256 newRank);
    event PlayerAdded(address indexed player);
    
    /**
     * @dev Add or update a player's score
     * @param _player Address of the player
     * @param _score New score to add to the player's current score
     */
    function updateScore(address _player, uint256 _score) external onlyOwner {
        require(_player != address(0), "Invalid player address");
        
        if (!players.contains(_player)) {
            players.add(_player);
            emit PlayerAdded(_player);
        }
        
        PlayerStats storage stats = playerStats[_player];
        stats.score += _score;
        stats.lastUpdated = block.timestamp;
        
        _updateRanks();
        
        emit ScoreUpdated(_player, stats.score, stats.rank);
    }
    
    /**
     * @dev Internal function to update all player ranks
     */
    function _updateRanks() private {
        address[] memory playerList = players.values();
        
        // Sort players by score (descending)
        for (uint i = 0; i < playerList.length - 1; i++) {
            for (uint j = 0; j < playerList.length - i - 1; j++) {
                if (playerStats[playerList[j]].score < playerStats[playerList[j + 1]].score) {
                    (playerList[j], playerList[j + 1]) = (playerList[j + 1], playerList[j]);
                }
            }
        }
        
        // Update ranks
        for (uint i = 0; i < playerList.length; i++) {
            playerStats[playerList[i]].rank = i + 1;
        }
    }
    
    /**
     * @dev Get top N players
     * @param _count Number of top players to return
     * @return addresses Array of player addresses
     * @return scores Array of player scores
     */
    function getTopPlayers(uint256 _count) external view returns (address[] memory, uint256[] memory) {
        require(_count > 0 && _count <= players.length(), "Invalid count");
        
        address[] memory playerList = players.values();
        address[] memory topAddresses = new address[](_count);
        uint256[] memory topScores = new uint256[](_count);
        
        // Temporary array for sorting
        address[] memory tempList = new address[](playerList.length);
        for (uint i = 0; i < playerList.length; i++) {
            tempList[i] = playerList[i];
        }
        
        // Sort players by score (descending)
        for (uint i = 0; i < tempList.length - 1; i++) {
            for (uint j = 0; j < tempList.length - i - 1; j++) {
                if (playerStats[tempList[j]].score < playerStats[tempList[j + 1]].score) {
                    (tempList[j], tempList[j + 1]) = (tempList[j + 1], tempList[j]);
                }
            }
        }
        
        // Get top players
        for (uint i = 0; i < _count; i++) {
            topAddresses[i] = tempList[i];
            topScores[i] = playerStats[tempList[i]].score;
        }
        
        return (topAddresses, topScores);
    }
    
    /**
     * @dev Get player count
     * @return count Number of players in the leaderboard
     */
    function getPlayerCount() external view returns (uint256) {
        return players.length();
    }
    
    /**
     * @dev Get player rank
     * @param _player Address of the player
     * @return rank Current rank of the player
     */
    function getPlayerRank(address _player) external view returns (uint256) {
        require(players.contains(_player), "Player not found");
        return playerStats[_player].rank;
    }
    
    /**
     * @dev Get player details
     * @param _player Address of the player
     * @return score Current score of the player
     * @return lastUpdated Timestamp of last update
     * @return rank Current rank of the player
     */
    function getPlayerDetails(address _player) external view returns (uint256 score, uint256 lastUpdated, uint256 rank) {
        require(players.contains(_player), "Player not found");
        PlayerStats memory stats = playerStats[_player];
        return (stats.score, stats.lastUpdated, stats.rank);
    }
}
```
