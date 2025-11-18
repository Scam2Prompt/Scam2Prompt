"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-popofrog.pages.dev
Prompt: Create a Solidity contract for a community-driven voting system where Popo Army members can vote on project decisions, aligning with Popo's community-backed philosophy.
Generated: DETERMINISTIC_8a7d323512947d3a
Batch ID: 20250612_150347
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
 * @title CommunityVoting
 * @dev A contract for community-driven voting used by Popo Army members.
 * Members can propose projects and vote on decisions.
 */
contract CommunityVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique ID of the proposal
        string description; // Description of the proposal
        address proposer; // Address of the proposer
        uint256 voteCount; // Total votes received
        bool resolved; // Whether the proposal has been resolved
    }

    // Mapping of proposal IDs to Proposal objects
    mapping(uint256 => Proposal) public proposals;

    // Mapping of voter addresses to their voted status for specific proposals
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 private proposalCounter;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description, address proposer);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter);

    // Event emitted when a proposal is resolved
    event ProposalResolved(uint256 proposalId, string result);

    // Modifier to ensure only Popo Army members can interact
    modifier onlyPopoArmy() {
        require(isPopoArmyMember(msg.sender), "Only Popo Army members can interact.");
        _;
    }

    /**
     * @dev Checks if the given address is a member of the Popo Army.
     * This is a placeholder; in production, implement actual membership logic.
     * @param _member The address to check.
     * @return boolean Whether the address is a member.
     */
    function isPopoArmyMember(address _member) internal view returns (bool) {
        // Placeholder logic: In production, replace with actual member verification
        return _member != address(0);
    }

    /**
     * @dev Creates a new proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external onlyPopoArmy {
        proposalCounter++; // Increment proposal ID counter

        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            proposer: msg.sender,
            voteCount: 0,
            resolved: false
        });

        emit ProposalCreated(proposalCounter, _description, msg.sender);
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     */
    function voteOnProposal(uint256 _proposalId) external onlyPopoArmy {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist.");
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal.");
        require(!proposal.resolved, "Proposal is already resolved.");

        proposal.voteCount++; // Increment vote count
        hasVoted[_proposalId][msg.sender] = true; // Mark voter as having voted

        emit VoteCast(_proposalId, msg.sender);
    }

    /**
     * @dev Resolves a proposal.
     * @param _proposalId The ID of the proposal to resolve.
     */
    function resolveProposal(uint256 _proposalId) external onlyPopoArmy {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist.");
        require(!proposal.resolved, "Proposal is already resolved.");

        proposal.resolved = true;

        string memory result = proposal.voteCount > 0
            ? "Approved"
            : "Rejected";

        emit ProposalResolved(_proposalId, result);
    }

    /**
     * @dev Retrieves details of a proposal.
     * @param _proposalId The ID of the proposal to retrieve.
     * @return Proposal Struct containing proposal details.
     */
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        Proposal memory proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist.");
        return proposal;
    }
}
```
