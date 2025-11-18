"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsonlinedapps.weebly.com
Prompt: Provide an example of customizing a ConnectsOnlineDApps template for a specific use case, such as a voting system.
Generated: DETERMINISTIC_b31eb98bbd6af159
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title Voting System
 * @dev A simple voting contract for managing voting on various proposals.
 */
contract VotingSystem is Ownable {
    using Counters for Counters.Counter;

    // Structure representing a single proposal
    struct Proposal {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    // Maps proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    // Counter for proposal IDs
    Counters.Counter private proposalIdCounter;
    // Mapping of voters to their voted proposal
    mapping(address => uint256) public votes;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string name);
    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed proposalId);

    /**
     * @dev Create a new proposal.
     * @param _name The name of the proposal.
     */
    function createProposal(string memory _name) external onlyOwner {
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();
        proposals[newProposalId] = Proposal(newProposalId, _name, 0);

        emit ProposalCreated(newProposalId, _name);
    }

    /**
     * @dev Cast a vote for a proposal.
     * @param _proposalId The ID of the proposal to vote for.
     */
    function vote(uint256 _proposalId) external {
        // Ensure the proposal exists
        require(_proposalId > 0 && _proposalId <= proposalIdCounter.current(), "Invalid proposal ID");
        // Prevent double voting
        require(votes[msg.sender] == 0, "You have already voted");

        votes[msg.sender] = _proposalId;
        proposals[_proposalId].voteCount++;

        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @dev Get the details of a proposal.
     * @param _proposalId The ID of the proposal.
     * @return The proposal details including ID, name, and vote count.
     */
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        require(_proposalId > 0 && _proposalId <= proposalIdCounter.current(), "Invalid proposal ID");
        return proposals[_proposalId];
    }

    /**
     * @dev Get the total number of proposals.
     * @return The total number of proposals created.
     */
    function totalProposals() external view returns (uint256) {
        return proposalIdCounter.current();
    }
}
```
