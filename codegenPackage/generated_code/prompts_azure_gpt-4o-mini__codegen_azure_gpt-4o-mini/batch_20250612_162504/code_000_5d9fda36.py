"""
Generated Code Metadata:
========================
Original URL: https://sportnode.nl
Prompt: Generate a smart contract for a sports organization using web3 principles as described by Sportnode.
Generated: DETERMINISTIC_5d9fda36e59e8f32
Batch ID: 20250612_162504
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
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for a sports organization
contract SportsOrganization is Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new player is registered
    event PlayerRegistered(uint256 indexed playerId, string name, address indexed playerAddress);
    
    // Event emitted when a match is scheduled
    event MatchScheduled(uint256 indexed matchId, uint256 indexed homeTeamId, uint256 indexed awayTeamId, uint256 date);
    
    // Struct to represent a player
    struct Player {
        uint256 id;
        string name;
        address playerAddress;
        bool isRegistered;
    }

    // Struct to represent a match
    struct Match {
        uint256 id;
        uint256 homeTeamId;
        uint256 awayTeamId;
        uint256 date;
        bool isScheduled;
    }

    // Mappings to store players and matches
    mapping(uint256 => Player) public players;
    mapping(uint256 => Match) public matches;

    // Counters for player and match IDs
    Counters.Counter private playerIdCounter;
    Counters.Counter private matchIdCounter;

    // Function to register a new player
    function registerPlayer(string memory _name) external {
        require(bytes(_name).length > 0, "Player name cannot be empty");
        
        playerIdCounter.increment();
        uint256 newPlayerId = playerIdCounter.current();

        players[newPlayerId] = Player(newPlayerId, _name, msg.sender, true);
        
        emit PlayerRegistered(newPlayerId, _name, msg.sender);
    }

    // Function to schedule a match
    function scheduleMatch(uint256 _homeTeamId, uint256 _awayTeamId, uint256 _date) external onlyOwner {
        require(players[_homeTeamId].isRegistered, "Home team not registered");
        require(players[_awayTeamId].isRegistered, "Away team not registered");
        require(_date > block.timestamp, "Match date must be in the future");

        matchIdCounter.increment();
        uint256 newMatchId = matchIdCounter.current();

        matches[newMatchId] = Match(newMatchId, _homeTeamId, _awayTeamId, _date, true);
        
        emit MatchScheduled(newMatchId, _homeTeamId, _awayTeamId, _date);
    }

    // Function to get player details
    function getPlayer(uint256 _playerId) external view returns (Player memory) {
        require(players[_playerId].isRegistered, "Player not found");
        return players[_playerId];
    }

    // Function to get match details
    function getMatch(uint256 _matchId) external view returns (Match memory) {
        require(matches[_matchId].isScheduled, "Match not found");
        return matches[_matchId];
    }
}
```
