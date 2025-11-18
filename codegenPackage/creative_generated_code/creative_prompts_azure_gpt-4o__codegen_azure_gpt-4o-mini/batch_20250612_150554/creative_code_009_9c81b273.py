"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Write a Solidity smart contract that facilitates decentralized voting for hackathon project awards, inspired by ETHBerlin04's participatory event structure.
Generated: DETERMINISTIC_9c81b27303cbbde8
Batch ID: 20250612_150554
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

/// @title Decentralized Voting for Hackathon Awards
/// @author Your Name
/// @notice This contract facilitates a voting system for hackathon project awards
/// @dev Make sure to follow the rules of the hackathon and local regulations

contract Voting {
    // Structure to hold project information
    struct Project {
        string name; // Name of the project
        address payable creator; // Address of the project creator
        uint256 voteCount; // Number of votes received
        bool exists; // Flag to check if project exists
    }

    // Mapping from project ID to Project structure
    mapping(uint256 => Project) public projects;
    // Mapping to track if an address has voted
    mapping(address => bool) public voters;
    // Count of registered projects
    uint256 public projectCount;
    // Event emitted when a new project is registered
    event ProjectRegistered(uint256 projectId, string name, address creator);
    // Event emitted when a vote is cast
    event Voted(uint256 projectId, address voter);

    /// @notice Register a new project for voting
    /// @param _name The name of the project
    function registerProject(string memory _name) external {
        // Ensure the project name is not empty
        require(bytes(_name).length > 0, "Project name must not be empty");

        // Increment project count to get a unique ID
        projectCount++;
        projects[projectCount] = Project({
            name: _name,
            creator: payable(msg.sender),
            voteCount: 0,
            exists: true
        });

        emit ProjectRegistered(projectCount, _name, msg.sender);
    }

    /// @notice Cast a vote for a project
    /// @param _projectId The ID of the project to vote for
    function vote(uint256 _projectId) external {
        // Ensure the project exists
        require(projects[_projectId].exists, "Project does not exist");
        // Ensure the voter has not voted before
        require(!voters[msg.sender], "You have already voted");

        // Record the vote
        voters[msg.sender] = true;
        projects[_projectId].voteCount++;

        emit Voted(_projectId, msg.sender);
    }

    /// @notice Get the vote count for a specific project
    /// @param _projectId The ID of the project
    /// @return The number of votes received by the project
    function getVoteCount(uint256 _projectId) external view returns (uint256) {
        require(projects[_projectId].exists, "Project does not exist");
        return projects[_projectId].voteCount;
    }

    /// @notice Get project details by ID
    /// @param _projectId The ID of the project
    /// @return name The name of the project
    /// @return creator The address of the project creator
    /// @return voteCount The number of votes the project has received
    function getProject(uint256 _projectId) external view returns (string memory name, address creator, uint256 voteCount) {
        require(projects[_projectId].exists, "Project does not exist");
        Project memory project = projects[_projectId];
        return (project.name, project.creator, project.voteCount);
    }
}
```
