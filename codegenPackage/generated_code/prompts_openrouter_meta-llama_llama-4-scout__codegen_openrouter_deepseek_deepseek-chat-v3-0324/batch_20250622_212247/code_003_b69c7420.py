"""
Generated Code Metadata:
========================
Original URL: https://op-rf4-voting-ui.vercel.app
Prompt: "How can I implement a badgeholder manual voting system for Retro Funding rounds using web3 technologies?"
Generated: DETERMINISTIC_b69c7420ee1ba526
Batch ID: 20250622_212247
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

contract RetroFundingVoting is Ownable {
    // Struct to store vote information
    struct Vote {
        address voter;
        uint256 projectId;
        uint256 amount;
    }

    // Struct to store project information
    struct Project {
        uint256 id;
        string name;
        uint256 totalVotes;
    }

    // Mapping to track votes by voter address
    mapping(address => Vote[]) public votesByVoter;

    // Mapping to track projects by ID
    mapping(uint256 => Project) public projects;

    // ERC721 badge contract address
    IERC721 public badgeContract;

    // Voting round details
    uint256 public roundId;
    uint256 public votingStartTime;
    uint256 public votingEndTime;
    uint256 public totalVotesCast;

    // Events
    event ProjectAdded(uint256 indexed projectId, string name);
    event VoteCast(address indexed voter, uint256 indexed projectId, uint256 amount);
    event VotingRoundStarted(uint256 indexed roundId, uint256 startTime, uint256 endTime);
    event VotingRoundEnded(uint256 indexed roundId);

    constructor(address _badgeContract) {
        badgeContract = IERC721(_badgeContract);
    }

    /**
     * @dev Start a new voting round
     * @param _duration Duration of the voting round in seconds
     */
    function startVotingRound(uint256 _duration) external onlyOwner {
        require(votingEndTime == 0 || block.timestamp > votingEndTime, "Previous round still active");
        
        roundId++;
        votingStartTime = block.timestamp;
        votingEndTime = block.timestamp + _duration;
        
        emit VotingRoundStarted(roundId, votingStartTime, votingEndTime);
    }

    /**
     * @dev Add a project to the current voting round
     * @param _projectId Unique identifier for the project
     * @param _name Name of the project
     */
    function addProject(uint256 _projectId, string memory _name) external onlyOwner {
        require(votingEndTime == 0 || block.timestamp <= votingEndTime, "Voting round not active");
        require(projects[_projectId].id == 0, "Project already exists");
        
        projects[_projectId] = Project({
            id: _projectId,
            name: _name,
            totalVotes: 0
        });
        
        emit ProjectAdded(_projectId, _name);
    }

    /**
     * @dev Cast a vote for a project
     * @param _projectId ID of the project to vote for
     * @param _amount Voting power to allocate
     */
    function vote(uint256 _projectId, uint256 _amount) external {
        require(badgeContract.balanceOf(msg.sender) > 0, "No voting badge held");
        require(votingEndTime > 0 && block.timestamp <= votingEndTime, "Voting round not active");
        require(projects[_projectId].id != 0, "Invalid project ID");
        require(_amount > 0, "Vote amount must be positive");
        
        // Record the vote
        votesByVoter[msg.sender].push(Vote({
            voter: msg.sender,
            projectId: _projectId,
            amount: _amount
        }));
        
        // Update project totals
        projects[_projectId].totalVotes += _amount;
        totalVotesCast += _amount;
        
        emit VoteCast(msg.sender, _projectId, _amount);
    }

    /**
     * @dev End the current voting round
     */
    function endVotingRound() external onlyOwner {
        require(votingEndTime > 0 && block.timestamp > votingEndTime, "Voting round still active");
        
        emit VotingRoundEnded(roundId);
        
        // Reset round-specific state
        votingStartTime = 0;
        votingEndTime = 0;
    }

    /**
     * @dev Get all votes cast by a specific voter
     * @param _voter Address of the voter
     * @return Array of votes cast by the voter
     */
    function getVotesByVoter(address _voter) external view returns (Vote[] memory) {
        return votesByVoter[_voter];
    }

    /**
     * @dev Get total votes for a specific project
     * @param _projectId ID of the project
     * @return Total votes received by the project
     */
    function getProjectVotes(uint256 _projectId) external view returns (uint256) {
        return projects[_projectId].totalVotes;
    }

    /**
     * @dev Get all projects in the current round
     * @return Array of all projects
     */
    function getAllProjects() external view returns (Project[] memory) {
        uint256 count;
        for (uint256 i = 1; projects[i].id != 0; i++) {
            count++;
        }
        
        Project[] memory allProjects = new Project[](count);
        for (uint256 i = 1; i <= count; i++) {
            allProjects[i-1] = projects[i];
        }
        
        return allProjects;
    }
}
```
