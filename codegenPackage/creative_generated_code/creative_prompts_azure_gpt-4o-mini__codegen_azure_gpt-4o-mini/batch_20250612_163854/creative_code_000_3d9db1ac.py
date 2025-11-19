"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-loafqqvg5-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora platform mentioned on the Optimism Agora website?
Generated: DETERMINISTIC_3d9db1ac4582f445
Batch ID: 20250612_163854
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title OnChainGovernance
 * @dev Implements a simple on-chain governance system using the Agora platform.
 * This contract allows users to propose and vote on governance proposals.
 */
contract OnChainGovernance is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold proposal details
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool exists;
        mapping(address => bool) hasVoted;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;
    Counters.Counter private proposalIdCounter;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    /**
     * @dev Create a new proposal
     * @param _description The description of the proposal
     */
    function createProposal(string memory _description) external onlyOwner {
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();

        proposals[newProposalId] = Proposal({
            id: newProposalId,
            description: _description,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(newProposalId, _description);
    }

    /**
     * @dev Cast a vote for a specific proposal
     * @param _proposalId The ID of the proposal to vote for
     */
    function vote(uint256 _proposalId) external {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!proposals[_proposalId].hasVoted[msg.sender], "Already voted");

        proposals[_proposalId].hasVoted[msg.sender] = true;
        proposals[_proposalId].voteCount += 1;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Get details of a proposal
     * @param _proposalId The ID of the proposal
     * @return id The ID of the proposal
     * @return description The description of the proposal
     * @return voteCount The number of votes the proposal has received
     */
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        string memory description,
        uint256 voteCount
    ) {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];

        return (proposal.id, proposal.description, proposal.voteCount);
    }
}
```
   require(proposal.exists, "Proposal does not exist");

        return (proposal.id, proposal.description, proposal.voteCount);
    }
}
```

This code implements a basic on-chain governance contract. The contract allows an owner to create proposals and users to vote on them while ensuring that each user can only vote once per proposal. The contract emits events for proposal creation and voting, providing a clear and auditable record of governance actions.
