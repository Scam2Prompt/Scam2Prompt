"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Create a step-by-step guide for integrating Metis decentralized governance features into a socialFi platform using Solidity.
Generated: DETERMINISTIC_4194fa939f11c26e
Batch ID: 20250612_152000
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
 * @title SocialFi Governance Integration Contract with Metis
 * @dev This contract demonstrates how to integrate decentralized governance features into a SocialFi platform.
 * It is designed to function within Metis Andromeda Layer 2 blockchain.
 */
contract SocialFiGovernance {
    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);

    // Event emitted when a proposal is voted on
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Proposal structure
    struct Proposal {
        string description;  // Description of the proposal
        uint256 voteCountFor;  // Votes in favor of the proposal
        uint256 voteCountAgainst;  // Votes against the proposal
        bool executed;  // Whether the proposal has been executed
    }

    // Mapping of proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Current proposal ID
    uint256 public currentProposalId;

    // Voting power mapping
    mapping(address => uint256) public votingPower;

    // Modifier to restrict access to voting power holders
    modifier hasVotingPower() {
        require(votingPower[msg.sender] > 0, "You don't have voting power.");
        _;
    }

    /**
     * @dev Initializes the contract with voting power for specified users.
     * @param users The list of users to assign voting power.
     * @param powers The voting power corresponding to each user.
     */
    constructor(address[] memory users, uint256[] memory powers) {
        require(users.length == powers.length, "Users and powers length mismatch.");
        for (uint256 i = 0; i < users.length; i++) {
            votingPower[users[i]] = powers[i];
        }
    }

    /**
     * @dev Creates a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external hasVotingPower {
        currentProposalId++;
        proposals[currentProposalId] = Proposal({
            description: description,
            voteCountFor: 0,
            voteCountAgainst: 0,
            executed: false
        });

        emit ProposalCreated(currentProposalId, description);
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support Whether the vote supports the proposal (true) or opposes it (false).
     */
    function vote(uint256 proposalId, bool support) external hasVotingPower {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed.");
        require(proposalId <= currentProposalId, "Proposal does not exist.");

        if (support) {
            proposal.voteCountFor += votingPower[msg.sender];
        } else {
            proposal.voteCountAgainst += votingPower[msg.sender];
        }

        emit VoteCast(msg.sender, proposalId, support);
    }

    /**
     * @dev Executes a proposal if it has sufficient votes in favor.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external hasVotingPower {
        Proposal storage proposal = proposals[proposalId];
        require(proposalId <= currentProposalId, "Proposal does not exist.");
        require(!proposal.executed, "Proposal already executed.");
        require(proposal.voteCountFor > proposal.voteCountAgainst, "Proposal did not pass.");

        proposal.executed = true;

        emit ProposalExecuted(proposalId);

        // Logic for executing the proposal can be implemented here (e.g., updating SocialFi platform settings)
    }

    /**
     * @dev Allows the owner to update voting power for specific users.
     * @param user The address of the user.
     * @param power The updated voting power for the user.
     */
    function updateVotingPower(address user, uint256 power) external {
        // Placeholder: Implement access control if required
        votingPower[user] = power;
    }
}
```
