"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportnode.nl
Prompt: Generate a smart contract for a sports organization using web3 principles as described by Sportnode.
Generated: DETERMINISTIC_5d9fda36e59e8f32
Batch ID: 20250612_162504
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

/// @title Sports Organization Smart Contract
/// @author Your Name
/// @notice This contract manages a sports organization, allowing for the registration of teams and players.
contract SportsOrganization {
    // Struct to hold team information
    struct Team {
        uint256 id;
        string name;
        address owner;
        uint256 playerCount;
    }

    // Struct to hold player information
    struct Player {
        uint256 id;
        string name;
        uint256 teamId;
    }

    // Events for logging actions
    event TeamRegistered(uint256 indexed teamId, string name, address indexed owner);
    event PlayerRegistered(uint256 indexed playerId, string name, uint256 indexed teamId);

    // Mappings to store teams and players
    mapping(uint256 => Team) public teams;
    mapping(uint256 => Player) public players;

    // Counters for team and player IDs
    uint256 private teamCounter;
    uint256 private playerCounter;

    /// @notice Registers a new team
    /// @param _name The name of the team
    /// @return teamId The ID of the newly registered team
    function registerTeam(string calldata _name) external returns (uint256 teamId) {
        require(bytes(_name).length > 0, "Team name cannot be empty");

        teamCounter++;
        teams[teamCounter] = Team({
            id: teamCounter,
            name: _name,
            owner: msg.sender,
            playerCount: 0
        });

        emit TeamRegistered(teamCounter, _name, msg.sender);
        return teamCounter;
    }

    /// @notice Registers a new player to a team
    /// @param _name The name of the player
    /// @param _teamId The ID of the team to which the player will be registered
    /// @return playerId The ID of the newly registered player
    function registerPlayer(string calldata _name, uint256 _teamId) external returns (uint256 playerId) {
        require(bytes(_name).length > 0, "Player name cannot be empty");
        require(teams[_teamId].owner != address(0), "Team does not exist");
        
        // Ensure only the team owner can register players
        require(msg.sender == teams[_teamId].owner, "Only team owner can register players");

        playerCounter++;
        players[playerCounter] = Player({
            id: playerCounter,
            name: _name,
            teamId: _teamId
        });

        teams[_teamId].playerCount++;

        emit PlayerRegistered(playerCounter, _name, _teamId);
        return playerCounter;
    }

    /// @notice Gets team information by ID
    /// @param _teamId The ID of the team
    /// @return team The Team struct containing the team information
    function getTeam(uint256 _teamId) external view returns (Team memory team) {
        require(teams[_teamId].owner != address(0), "Team does not exist");
        return teams[_teamId];
    }

    /// @notice Gets player information by ID
    /// @param _playerId The ID of the player
    /// @return player The Player struct containing the player information
    function getPlayer(uint256 _playerId) external view returns (Player memory player) {
        require(players[_playerId].teamId != 0, "Player does not exist");
        return players[_playerId];
    }
}
```
