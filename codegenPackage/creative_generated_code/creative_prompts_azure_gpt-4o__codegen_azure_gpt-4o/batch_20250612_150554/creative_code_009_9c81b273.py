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

/**
 * @title HackathonVoting
 * @dev A decentralized voting system for hackathon project awards.
 * Allows participants to vote on projects and ensures one vote per address.
 */
contract HackathonVoting {
    // Struct to store details of each project
    struct Project {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    // Mapping of project ID to Project details
    mapping(uint256 => Project) public projects;

    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;

    // Array of project IDs (used for listing projects)
    uint256[] public projectIds;

    // Address of the contract owner (admin)
    address public owner;

    // Event emitted when a vote is cast
    event Voted(address indexed voter, uint256 projectId);

    // Event emitted when a new project is added
    event ProjectAdded(uint256 projectId, string projectName);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * The deployer becomes the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new project to the voting system.
     * Can only be called by the owner.
     * @param projectId The unique ID of the project.
     * @param name The name of the project.
     */
    function addProject(uint256 projectId, string memory name) external onlyOwner {
        require(bytes(name).length > 0, "Project name cannot be empty");
        require(projects[projectId].id == 0, "Project ID already exists");

        projects[projectId] = Project(projectId, name, 0);
        projectIds.push(projectId);

        emit ProjectAdded(projectId, name);
    }

    /**
     * @dev Vote for a project by its ID.
     * Each address can vote only once.
     * @param projectId The ID of the project to vote for.
     */
    function vote(uint256 projectId) external {
        require(!hasVoted[msg.sender], "You have already voted");
        require(projects[projectId].id != 0, "Project does not exist");

        hasVoted[msg.sender] = true;
        projects[projectId].voteCount++;

        emit Voted(msg.sender, projectId);
    }

    /**
     * @dev Get a project's details by its ID.
     * @param projectId The ID of the project to retrieve.
     * @return name The name of the project.
     * @return voteCount The number of votes the project has received.
     */
    function getProject(uint256 projectId) external view returns (string memory name, uint256 voteCount) {
        require(projects[projectId].id != 0, "Project does not exist");

        Project memory project = projects[projectId];
        return (project.name, project.voteCount);
    }

    /**
     * @dev Get the total number of projects in the voting system.
     * @return The total number of projects.
     */
    function getTotalProjects() external view returns (uint256) {
        return projectIds.length;
    }
}
```
