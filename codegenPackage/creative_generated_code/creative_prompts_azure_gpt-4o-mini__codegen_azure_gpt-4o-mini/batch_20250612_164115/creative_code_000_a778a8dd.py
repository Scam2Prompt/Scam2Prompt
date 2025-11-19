"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-3tvf739hr-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora platform for proposal voting?
Generated: DETERMINISTIC_a778a8ddebf1d19f
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's an example implementation of on-chain governance for proposal voting using the Agora platform. This example is written in Solidity, suitable for Ethereum smart contracts.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title OnChainGovernance
 * @dev This contract allows users to create proposals and vote on them using the Agora platform.
 */
contract OnChainGovernance {
    // Struct representing a proposal
    struct Proposal {
        uint id;
        address creator;
        string description;
        uint voteCount;
        mapping(address => bool) voters; // Track if an address has voted
        bool exists;
    }

    // State variables
    uint public proposalCount; // Count of proposals
    mapping(uint => Proposal) public proposals; // Mapping of proposal ID to Proposal

    event ProposalCreated(uint id, address creator, string description);
    event Voted(uint proposalId, address voter);

    /**
     * @dev Creates a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) public {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.creator = msg.sender;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.exists = true;

        emit ProposalCreated(proposalCount, msg.sender, _description);
    }

    /**
     * @dev Allows a user to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint _proposalId) public {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!proposals[_proposalId].voters[msg.sender], "You have already voted on this proposal");

        proposals[_proposalId].voters[msg.sender] = true; // Mark voter as having voted
        proposals[_proposalId].voteCount++; // Increment the vote count

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Returns the details of a specific proposal.
     * @param _proposalId ID of the proposal to retrieve.
     * @return id Proposal ID.
     * @return creator Address of the proposal creator.
     * @return description Description of the proposal.
     * @return voteCount Current vote count.
     */
    function getProposal(uint _proposalId) public view returns (uint id, address creator, string memory description, uint voteCount) {
        require(proposals[_proposalId].exists, "Proposal does not exist");

        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.creator, proposal.description, proposal.voteCount);
    }
}
```

This Solidity contract allows users to create proposals and vote on them, with events emitted for tracking activity. Proper error handling is implemented to ensure the validity of proposals and voting actions.
