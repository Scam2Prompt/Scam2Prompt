"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimspopofrog.web.app
Prompt: Write a Solidity contract for managing community-driven decisions in the Popo ecosystem, allowing members to vote on project directions and token allocations.
Generated: DETERMINISTIC_17a5e4d855f1a506
Batch ID: 20250612_153512
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
 * @title PopoCommunityGovernance
 * @dev A smart contract for managing community-driven decisions in the Popo ecosystem.
 * Members can vote on proposals regarding project directions and token allocations.
 */
contract PopoCommunityGovernance {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 votesFor;   // Number of votes in favor of the proposal
        uint256 votesAgainst; // Number of votes against the proposal
        bool executed;      // Whether the proposal has been executed
        address proposer;   // The address that created the proposal
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted for a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Token holders' addresses
    mapping(address => bool) public members;

    // Events
    event ProposalCreated(uint256 proposalId, string description, address proposer);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Modifier to check if the caller is a member of the community.
     */
    modifier onlyMember() {
        require(members[msg.sender], "Caller is not a member");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with members.
     * @param initialMembers List of addresses that will be considered members.
     */
    constructor(address[] memory initialMembers) {
        for (uint256 i = 0; i < initialMembers.length; i++) {
            members[initialMembers[i]] = true;
        }
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external onlyMember {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false,
            proposer: msg.sender
        });

        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _support True if voting for the proposal, false if voting against.
     */
    function vote(uint256 _proposalId, bool _support) external onlyMember {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!hasVoted[_proposalId][msg.sender], "Caller has already voted on this proposal");
        require(!proposals[_proposalId].executed, "Proposal has already been executed");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposals[_proposalId].votesFor++;
        } else {
            proposals[_proposalId].votesAgainst++;
        }

        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal, based on voting results.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyMember {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        proposal.executed = true;

        // Logic for execution can be added here.

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Function to add new members to the community.
     * @param _newMember The address of the new member to be added.
     */
    function addMember(address _newMember) external onlyMember {
        require(_newMember != address(0), "Invalid address");
        require(!members[_newMember], "Address is already a member");

        members[_newMember] = true;
    }

    /**
     * @dev Function to remove a member from the community.
     * @param _member The address of the member to be removed.
     */
    function removeMember(address _member) external onlyMember {
        require(members[_member], "Address is not a member");

        members[_member] = false;
    }
}
```
