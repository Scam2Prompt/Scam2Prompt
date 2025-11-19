"""
Generated Code Metadata:
========================
Original URL: https://buytoken-scapesmania.pages.dev
Prompt: Create a smart contract that enables Web3 players to vote on game development decisions, aligning with ScapesMania's goal of letting players influence project development.
Generated: DETERMINISTIC_ce4d40046e669dd7
Batch ID: 20250612_152511
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
 * @title GameDevelopmentVoting
 * @dev A smart contract that allows Web3 players to vote on game development decisions
 */
contract GameDevelopmentVoting {
    // Struct to represent a voting proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool isActive;
    }

    // Struct to track player votes
    struct Voter {
        bool hasVoted;
        uint256 votedProposalId;
    }

    // Contract owner (ScapesMania team)
    address public owner;

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;

    // Mapping of voter address to Voter
    mapping(address => Voter) public voters;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Voting duration in seconds (default: 7 days)
    uint256 public votingDuration = 604800;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    event VoteCast(address indexed voter, uint256 indexed proposalId);
    event VotingClosed(uint256 indexed proposalId, uint256 totalVotes);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Modifier to check if proposal is active
    modifier onlyActiveProposal(uint256 _proposalId) {
        require(proposals[_proposalId].isActive, "Proposal is not active");
        require(block.timestamp < proposals[_proposalId].endTime, "Voting period has ended");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new voting proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        uint256 endTime = block.timestamp + votingDuration;
        
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            endTime: endTime,
            isActive: true
        });

        emit ProposalCreated(proposalCount, _description, endTime);
    }

    /**
     * @dev Cast a vote for a proposal
     * @param _proposalId ID of the proposal to vote for
     */
    function vote(uint256 _proposalId) external onlyActiveProposal(_proposalId) {
        require(!voters[msg.sender].hasVoted, "Already voted");

        proposals[_proposalId].voteCount++;
        voters[msg.sender] = Voter({
            hasVoted: true,
            votedProposalId: _proposalId
        });

        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @dev Close voting for a proposal manually (can be called by anyone after end time)
     * @param _proposalId ID of the proposal to close
     */
    function closeVoting(uint256 _proposalId) external {
        require(proposals[_proposalId].isActive, "Proposal is already closed");
        require(block.timestamp >= proposals[_proposalId].endTime, "Voting period not ended yet");

        proposals[_proposalId].isActive = false;
        emit VotingClosed(_proposalId, proposals[_proposalId].voteCount);
    }

    /**
     * @dev Get details of a proposal
     * @param _proposalId ID of the proposal
     * @return Proposal details
     */
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }

    /**
     * @dev Check if an address has voted
     * @param _voter Address to check
     * @return True if the address has voted, false otherwise
     */
    function hasVoted(address _voter) external view returns (bool) {
        return voters[_voter].hasVoted;
    }

    /**
     * @dev Change the voting duration (only owner)
     * @param _duration New voting duration in seconds
     */
    function setVotingDuration(uint256 _duration) external onlyOwner {
        require(_duration >= 86400, "Voting duration must be at least 1 day");
        votingDuration = _duration;
    }
}
```
