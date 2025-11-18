"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meties.pages.dev
Prompt: Create a voting smart contract that implements the Community Ecosystem Governance (CEG) framework described on the Metis platform.
Generated: DETERMINISTIC_f87c8005dc54d8af
Batch ID: 20250612_151636
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
 * @title Community Ecosystem Governance (CEG) Voting Smart Contract
 * @notice This contract allows users to propose and vote on governance decisions in the Metis ecosystem.
 */

contract CEGVoting {
    // Struct to hold information about each proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount; // Number of votes for this proposal
        mapping(address => bool) voters; // Track whether an address has voted
        bool executed; // Track whether the proposal has been executed
    }

    // State variables
    address public chairperson; // The address of the chairperson
    mapping(uint256 => Proposal) public proposals; // Store proposals by ID
    uint256 public proposalCount; // Count of proposals
    mapping(address => bool) public isMember; // Track the members of the community
    uint256 public votingDuration; // Duration of voting in seconds

    // Events
    event ProposalCreated(uint256 indexed id, string description);
    event Voted(uint256 indexed proposalId, address voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to check if the caller is the chairperson
    modifier onlyChairperson() {
        require(msg.sender == chairperson, "Only chairperson can call this function.");
        _;
    }

    // Modifier to check if the caller is a community member
    modifier onlyMember() {
        require(isMember[msg.sender], "Only community members can vote.");
        _;
    }

    // Constructor to initialize the contract
    constructor(address[] memory members, uint256 _votingDuration) {
        chairperson = msg.sender; // Set the deployer as the chairperson
        votingDuration = _votingDuration; // Set the voting duration
        for (uint256 i = 0; i < members.length; i++) {
            isMember[members[i]] = true; // Add members to the community
        }
    }

    /**
     * @notice Create a new proposal
     * @param description The description of the proposal
     */
    function createProposal(string memory description) public onlyChairperson {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @notice Vote for a proposal
     * @param proposalId The ID of the proposal to vote for
     */
    function vote(uint256 proposalId) public onlyMember {
        Proposal storage proposal = proposals[proposalId];

        require(!proposal.voters[msg.sender], "You have already voted.");
        require(!proposal.executed, "Proposal has already been executed.");

        proposal.voters[msg.sender] = true; // Mark voter as having voted
        proposal.voteCount++; // Increment vote count

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @notice Execute a proposal if it has received enough votes
     * @param proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) public onlyChairperson {
        Proposal storage proposal = proposals[proposalId];

        require(!proposal.executed, "Proposal has already been executed.");
        require(proposal.voteCount > 0, "Proposal must have votes to be executed.");

        proposal.executed = true; // Mark proposal as executed

        emit ProposalExecuted(proposalId);
        // Implement proposal execution logic here (e.g., transfer funds, change state, etc.)
    }
}
```
