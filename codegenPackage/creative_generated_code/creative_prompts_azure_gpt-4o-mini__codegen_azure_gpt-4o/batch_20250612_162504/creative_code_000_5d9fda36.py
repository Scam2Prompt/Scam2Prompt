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

/**
 * @title SportOrganizationSmartContract
 * @dev A smart contract to manage sports organizations using Web3 principles as described by Sportnode.
 */
contract SportOrganization {
    
    // Struct to represent a team within the organization
    struct Team {
        string name;
        uint256 totalWins;
        uint256 totalLosses;
        address teamLeader; // Ethereum address of the team leader
        bool active;
    }

    // State variables
    address public owner; // Owner of the sports organization
    uint256 public teamCount; // Counter to keep track of the total number of teams
    mapping(uint256 => Team) public teams; // Mapping team ID to the Team struct

    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    /**
     * @dev Event emitted when a new team is created.
     * @param teamId ID of the new team.
     * @param name Name of the team.
     * @param teamLeader Ethereum address of the team leader.
     */
    event TeamCreated(uint256 teamId, string name, address teamLeader);

    /**
     * @dev Event emitted when team details are updated.
     * @param teamId ID of the updated team.
     */
    event TeamUpdated(uint256 teamId);

    /**
     * @dev Event emitted when a team is deactivated.
     * @param teamId ID of the deactivated team.
     */
    event TeamDeactivated(uint256 teamId);

    /**
     * @dev Constructor to initialize the smart contract.
     */
    constructor() {
        owner = msg.sender;
        teamCount = 0;
    }

    /**
     * @dev Create a new team in the sports organization.
     * @param name Name of the team.
     * @param teamLeader Ethereum address of the team leader.
     */
    function createTeam(string memory name, address teamLeader) public onlyOwner {
        require(bytes(name).length > 0, "Team name cannot be empty.");
        require(teamLeader != address(0), "Team leader address cannot be zero.");

        teamCount++;
        teams[teamCount] = Team(name, 0, 0, teamLeader, true);

        emit TeamCreated(teamCount, name, teamLeader);
    }

    /**
     * @dev Update team details such as wins and losses.
     * @param teamId ID of the team to update.
     * @param totalWins Updated total wins for the team.
     * @param totalLosses Updated total losses for the team.
     */
    function updateTeam(uint256 teamId, uint256 totalWins, uint256 totalLosses) public onlyOwner {
        require(teamId > 0 && teamId <= teamCount, "Invalid team ID.");
        require(teams[teamId].active, "Cannot update an inactive team.");

        teams[teamId].totalWins = totalWins;
        teams[teamId].totalLosses = totalLosses;

        emit TeamUpdated(teamId);
    }

    /**
     * @dev Deactivate a team within the sports organization.
     * @param teamId ID of the team to deactivate.
     */
    function deactivateTeam(uint256 teamId) public onlyOwner {
        require(teamId > 0 && teamId <= teamCount, "Invalid team ID.");
        require(teams[teamId].active, "Team is already inactive.");

        teams[teamId].active = false;

        emit TeamDeactivated(teamId);
    }

    /**
     * @dev Fetch details of a specific team.
     * @param teamId ID of the team.
     * @return Team details including name, wins, losses, leader, and active status.
     */
    function getTeamDetails(uint256 teamId) public view returns (string memory, uint256, uint256, address, bool) {
        require(teamId > 0 && teamId <= teamCount, "Invalid team ID.");

        Team memory team = teams[teamId];
        return (team.name, team.totalWins, team.totalLosses, team.teamLeader, team.active);
    }
}
```
