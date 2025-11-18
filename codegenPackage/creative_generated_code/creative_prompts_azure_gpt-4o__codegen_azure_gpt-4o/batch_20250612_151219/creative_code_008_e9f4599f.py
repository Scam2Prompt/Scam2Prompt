"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Create a Solidity contract for decentralized governance of NFT cities in the EarthMeta metaverse, allowing users to vote on economic policies.
Generated: DETERMINISTIC_e9f4599f9a752700
Batch ID: 20250612_151219
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
 * @title EarthMeta NFT Cities Governance Contract
 * @dev Enables decentralized governance of NFT cities in the EarthMeta metaverse, allowing users to vote on economic policies.
 */
contract NFTCitiesGovernance {
    // Struct representing a policy proposal
    struct Proposal {
        uint256 id;
        string description; // Description of the policy proposal
        uint256 voteCountYes; // Total votes in favor
        uint256 voteCountNo; // Total votes against
        address proposer; // Address of the proposer
        bool executed; // Whether the proposal has been executed
    }

    // Mapping from proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public nextProposalId;

    // Governance events
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed proposer);
    event Voted(uint256 indexed proposalId, address indexed voter, bool votedYes);
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    // Modifier to ensure a proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    /**
     * @dev Create a new policy proposal.
     * @param description The description of the policy proposal.
     */
    function createProposal(string memory description) external {
        require(bytes(description).length > 0, "Description cannot be empty");

        Proposal memory newProposal = Proposal({
            id: nextProposalId,
            description: description,
            voteCountYes: 0,
            voteCountNo: 0,
            proposer: msg.sender,
            executed: false
        });

        proposals[nextProposalId] = newProposal;
        emit ProposalCreated(nextProposalId, description, msg.sender);
        nextProposalId++;
    }

    /**
     * @dev Vote on a policy proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param voteYes True if voting in favor, false if voting against.
     */
    function vote(uint256 proposalId, bool voteYes) external proposalExists(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        Proposal storage proposal = proposals[proposalId];

        if (voteYes) {
            proposal.voteCountYes++;
        } else {
            proposal.voteCountNo++;
        }

        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender, voteYes);
    }

    /**
     * @dev Execute a proposal if voting concludes in favor.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.voteCountYes > proposal.voteCountNo, "Proposal did not pass");

        // Placeholder for policy execution logic
        // Actual implementation would depend on the specifics of the metaverse policies
        proposal.executed = true;

        emit ProposalExecuted(proposalId, true);
    }
}
```
