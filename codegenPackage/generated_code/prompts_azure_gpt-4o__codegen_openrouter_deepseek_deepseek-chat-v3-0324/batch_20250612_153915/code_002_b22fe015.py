"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: Generate code to implement a leaderboard system for a Web3 game, inspired by TON Station's "Storm the Leagues" Season 2 Finale event.
Generated: DETERMINISTIC_b22fe015bd5b8f7d
Batch ID: 20250612_153915
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

contract Leaderboard is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;
    
    struct PlayerScore {
        address player;
        uint256 score;
        uint256 lastUpdated;
    }
    
    // Season configuration
    uint256 public seasonId;
    uint256 public seasonStart;
    uint256 public seasonEnd;
    bool public isSeasonActive;
    
    // Leaderboard data
    mapping(address => uint256) private _scores;
    EnumerableSet.AddressSet private _players;
    
    // Events
    event ScoreUpdated(address indexed player, uint256 newScore, uint256 timestamp);
    event SeasonStarted(uint256 seasonId, uint256 startTime, uint256 endTime);
    event SeasonEnded(uint256 seasonId, uint256 endTime);
    
    constructor() {
        seasonId = 1; // Initial season
    }
    
    /**
     * @dev Start a new season
     * @param duration Duration of the season in seconds
     */
    function startSeason(uint256 duration) external onlyOwner {
        require(!isSeasonActive, "Leaderboard: Season already active");
        
        seasonStart = block.timestamp;
        seasonEnd = seasonStart + duration;
        isSeasonActive = true;
        
        emit SeasonStarted(seasonId, seasonStart, seasonEnd);
    }
    
    /**
     * @dev End the current season
     */
    function endSeason() external onlyOwner {
        require(isSeasonActive, "Leaderboard: No active season");
        
        isSeasonActive = false;
        seasonId++;
        
        emit SeasonEnded(seasonId - 1, block.timestamp);
    }
    
    /**
     * @dev Update player score
     * @param player Address of the player
     * @param scoreDelta Score to add (can be negative to subtract)
     */
    function updateScore(address player, int256 scoreDelta) external onlyOwner {
        require(isSeasonActive, "Leaderboard: Season not active");
        require(player != address(0), "Leaderboard: Invalid player address");
        
        uint256 currentScore = _scores[player];
        uint256 newScore;
        
        if (scoreDelta > 0) {
            newScore = currentScore + uint256(scoreDelta);
        } else {
            // Prevent underflow
            if (uint256(-scoreDelta) > currentScore) {
                newScore = 0;
            } else {
                newScore = currentScore - uint256(-scoreDelta);
            }
        }
        
        _scores[player] = newScore;
        _players.add(player);
        
        emit ScoreUpdated(player, newScore, block.timestamp);
    }
    
    /**
     * @dev Get top N players
     * @param count Number of top players to return
     * @return Array of PlayerScore structs
     */
    function getTopPlayers(uint256 count) external view returns (PlayerScore[] memory) {
        require(count > 0, "Leaderboard: Invalid count");
        
        uint256 totalPlayers = _players.length();
        if (count > totalPlayers) {
            count = totalPlayers;
        }
        
        PlayerScore[] memory topPlayers = new PlayerScore[](count);
        address[] memory players = _players.values();
        
        // Sort players by score (simple bubble sort for small datasets)
        for (uint256 i = 0; i < players.length - 1; i++) {
            for (uint256 j = 0; j < players.length - i - 1; j++) {
                if (_scores[players[j]] < _scores[players[j + 1]]) {
                    (players[j], players[j + 1]) = (players[j + 1], players[j]);
                }
            }
        }
        
        for (uint256 i = 0; i < count; i++) {
            topPlayers[i] = PlayerScore({
                player: players[i],
                score: _scores[players[i]],
                lastUpdated: block.timestamp
            });
        }
        
        return topPlayers;
    }
    
    /**
     * @dev Get player score and rank
     * @param player Address of the player
     * @return score Player's current score
     * @return rank Player's current rank (0 if not in leaderboard)
     */
    function getPlayerStats(address player) external view returns (uint256 score, uint256 rank) {
        score = _scores[player];
        if (score == 0 || !_players.contains(player)) {
            return (score, 0);
        }
        
        address[] memory players = _players.values();
        rank = 1;
        
        for (uint256 i = 0; i < players.length; i++) {
            if (_scores[players[i]] > score) {
                rank++;
            }
        }
        
        return (score, rank);
    }
    
    /**
     * @dev Get current season information
     * @return id Current season ID
     * @return start Season start timestamp
     * @return end Season end timestamp
     * @return active Whether season is active
     */
    function getSeasonInfo() external view returns (
        uint256 id,
        uint256 start,
        uint256 end,
        bool active
    ) {
        return (seasonId, seasonStart, seasonEnd, isSeasonActive);
    }
}
```
