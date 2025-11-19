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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title Decentralized Voting Contract for Hackathon Project Awards
 * @author [Your Name]
 * @notice This contract facilitates decentralized voting for hackathon project awards.
 */
contract DecentralizedVoting is Ownable {
    using SafeMath for uint256;
    using EnumerableSet for EnumerableSet.AddressSet;

    // Structure to represent a project
    struct Project {
        string name;
        address owner;
        uint256 voteCount;
    }

    // Mapping of project IDs to project details
    mapping(uint256 => Project) public projects;

    // Mapping of voter addresses to their voted project IDs
    mapping(address => uint256) public voterVotes;

    // Set of voters who have already voted
    EnumerableSet.AddressSet private votedAddresses;

    // Total number of projects
    uint256 public projectCount;

    // Event emitted when a new project is added
    event ProjectAdded(uint256 indexed projectId, string name, address owner);

    // Event emitted when a voter casts their vote
    event VoteCast(address indexed voter, uint256 indexed projectId);

    // Event emitted when the owner finalizes the voting
    event VotingFinalized();

    // Error for attempting to vote with an invalid project ID
    error InvalidProjectId();

    // Error for attempting to vote with a project ID that has not been added
    error ProjectNotFound();

    // Error for attempting to vote twice
    error AlreadyVoted();

    /**
     * @notice Adds a new project to the voting list
     * @param _name The name of the project
     */
    function addProject(string memory _name) public onlyOwner {
        projectCount++;
        projects[projectCount] = Project(_name, msg.sender, 0);
        emit ProjectAdded(projectCount, _name, msg.sender);
    }

    /**
     * @notice Casts a vote for a project
     * @param _projectId The ID of the project to vote for
     */
    function castVote(uint256 _projectId) public {
        // Check if the project exists
        if (_projectId == 0 || _projectId > projectCount) {
            revert ProjectNotFound();
        }

        // Check if the voter has already voted
        if (votedAddresses.contains(msg.sender)) {
            revert AlreadyVoted();
        }

        // Update the vote count for the project
        projects[_projectId].voteCount++;

        // Store the voter's vote
        voterVotes[msg.sender] = _projectId;

        // Add the voter to the set of voted addresses
        votedAddresses.add(msg.sender);

        emit VoteCast(msg.sender, _projectId);
    }

    /**
     * @notice Finalizes the voting and returns the winning project ID
     * @return The ID of the winning project
     */
    function finalizeVoting() public onlyOwner returns (uint256) {
        // Find the project with the highest vote count
        uint256 winningProjectId;
        uint256 maxVotes;
        for (uint256 i = 1; i <= projectCount; i++) {
            if (projects[i].voteCount > maxVotes) {
                maxVotes = projects[i].voteCount;
                winningProjectId = i;
            }
        }

        emit VotingFinalized();

        return winningProjectId;
    }

    /**
     * @notice Returns the details of a project
     * @param _projectId The ID of the project to retrieve
     * @return The project's name, owner, and vote count
     */
    function getProject(uint256 _projectId) public view returns (string memory, address, uint256) {
        if (_projectId == 0 || _projectId > projectCount) {
            revert ProjectNotFound();
        }

        Project memory project = projects[_projectId];
        return (project.name, project.owner, project.voteCount);
    }
}
```
