"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralized-metis.pages.dev
Prompt: Write a script to deploy a decentralized autonomous company (DAC) on Metis Andromeda, utilizing its governance and scalability features.
Generated: DETERMINISTIC_5dfa162357851f5b
Batch ID: 20250612_152422
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
 * @title Decentralized Autonomous Company (DAC) on Metis Andromeda
 * @dev This contract implements a basic DAC with governance features.
 */
contract DAC {
    // State variables
    address public owner; // Owner of the DAC
    uint256 public proposalCount; // Tracks the number of proposals
    uint256 public votingDuration; // Duration for voting on proposals in seconds

    struct Proposal {
        uint256 id;
        string description; // Proposal description
        uint256 votesFor; // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        uint256 deadline; // Voting deadline
        bool executed; // Whether the proposal has been executed
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Keeps track of voting status
    mapping(address => bool) public members; // DAC membership

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool vote);
    event ProposalExecuted(uint256 proposalId, bool success);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier onlyMember() {
        require(members[msg.sender], "Only DAC members can perform this action");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    modifier notVoted(uint256 proposalId) {
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");
        _;
    }

    modifier notExpired(uint256 proposalId) {
        require(block.timestamp <= proposals[proposalId].deadline, "Voting period has expired for this proposal");
        _;
    }

    constructor(uint256 _votingDuration) {
        owner = msg.sender;
        votingDuration = _votingDuration;
        members[msg.sender] = true; // Add contract owner as the first member
    }

    /**
     * @dev Adds a new member to the DAC.
     * @param _member Address of the new member.
     */
    function addMember(address _member) external onlyOwner {
        require(!members[_member], "Address is already a member");
        members[_member] = true;
    }

    /**
     * @dev Creates a new proposal for voting.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external onlyMember {
        proposalCount++;
        uint256 proposalId = proposalCount;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + votingDuration,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, proposals[proposalId].deadline);
    }

    /**
     * @dev Casts a vote for a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool support)
        external
        onlyMember
        proposalExists(proposalId)
        notVoted(proposalId)
        notExpired(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];
        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @dev Executes a proposal after the voting period has ended.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.deadline, "Voting period has not ended yet");
        require(!proposal.executed, "Proposal has already been executed");

        bool success = proposal.votesFor > proposal.votesAgainst;
        proposal.executed = true;

        emit ProposalExecuted(proposalId, success);

        // Proposal execution logic can be implemented here based on the project's requirements
        // This is a placeholder for actual execution logic
    }
}
```
