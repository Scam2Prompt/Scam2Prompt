"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Write a Solidity smart contract that facilitates decentralized voting for hackathon project awards, inspired by ETHBerlin04's participatory event structure.
Generated: DETERMINISTIC_9c81b27303cbbde8
Batch ID: 20250612_150554
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
 * @title HackathonVoting
 * @dev A decentralized voting system for hackathon project awards
 */
contract HackathonVoting {
    struct Project {
        uint256 id;
        string name;
        string description;
        address submitter;
        uint256 voteCount;
    }

    struct Voter {
        bool hasVoted;
        uint256[] votedProjects;
    }

    address public admin;
    bool public votingOpen;
    uint256 public projectCount;
    uint256 public maxVotesPerVoter;
    uint256 public totalVotesCast;

    mapping(uint256 => Project) public projects;
    mapping(address => Voter) public voters;

    event ProjectAdded(uint256 indexed projectId, string name, address submitter);
    event VoteCast(address indexed voter, uint256 indexed projectId);
    event VotingStatusChanged(bool votingOpen);
    event AdminChanged(address indexed oldAdmin, address indexed newAdmin);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier votingIsOpen() {
        require(votingOpen, "Voting is currently closed");
        _;
    }

    constructor(uint256 _maxVotesPerVoter) {
        admin = msg.sender;
        maxVotesPerVoter = _maxVotesPerVoter;
        votingOpen = false;
        projectCount = 0;
        totalVotesCast = 0;
    }

    /**
     * @dev Add a new project to the voting system
     * @param _name Name of the project
     * @param _description Description of the project
     */
    function addProject(string memory _name, string memory _description) external {
        require(bytes(_name).length > 0, "Project name cannot be empty");
        require(bytes(_description).length > 0, "Project description cannot be empty");

        projectCount++;
        projects[projectCount] = Project({
            id: projectCount,
            name: _name,
            description: _description,
            submitter: msg.sender,
            voteCount: 0
        });

        emit ProjectAdded(projectCount, _name, msg.sender);
    }

    /**
     * @dev Cast a vote for a project
     * @param _projectId ID of the project to vote for
     */
    function vote(uint256 _projectId) external votingIsOpen {
        require(_projectId > 0 && _projectId <= projectCount, "Invalid project ID");
        require(!voters[msg.sender].hasVoted, "You have already voted");
        require(voters[msg.sender].votedProjects.length < maxVotesPerVoter, "Maximum votes reached");

        projects[_projectId].voteCount++;
        voters[msg.sender].votedProjects.push(_projectId);
        voters[msg.sender].hasVoted = voters[msg.sender].votedProjects.length >= maxVotesPerVoter;
        totalVotesCast++;

        emit VoteCast(msg.sender, _projectId);
    }

    /**
     * @dev Toggle voting status (open/close)
     */
    function toggleVoting() external onlyAdmin {
        votingOpen = !votingOpen;
        emit VotingStatusChanged(votingOpen);
    }

    /**
     * @dev Change the admin address
     * @param _newAdmin Address of the new admin
     */
    function changeAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "Invalid admin address");
        emit AdminChanged(admin, _newAdmin);
        admin = _newAdmin;
    }

    /**
     * @dev Get project details by ID
     * @param _projectId ID of the project
     * @return Project details
     */
    function getProject(uint256 _projectId) external view returns (Project memory) {
        require(_projectId > 0 && _projectId <= projectCount, "Invalid project ID");
        return projects[_projectId];
    }

    /**
     * @dev Get voter details
     * @param _voter Address of the voter
     * @return Voter details
     */
    function getVoter(address _voter) external view returns (Voter memory) {
        return voters[_voter];
    }

    /**
     * @dev Get all project IDs
     * @return Array of project IDs
     */
    function getAllProjectIds() external view returns (uint256[] memory) {
        uint256[] memory ids = new uint256[](projectCount);
        for (uint256 i = 0; i < projectCount; i++) {
            ids[i] = i + 1;
        }
        return ids;
    }
}
```
