"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.pages.dev
Prompt: Create a Solidity contract to enable users to vote on upcoming games or features on the BetSwirl platform.
Generated: DETERMINISTIC_6094aaeb5582fa5b
Batch ID: 20250612_150946
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

/// @title BetSwirl Voting Contract
/// @notice This contract allows users to vote on upcoming games or features.
/// @dev It includes functions to create proposals, vote, and view results. 

contract BetSwirlVoting {
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool exists;
    }

    // Mapping from proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    
    // Keep track of the number of proposals
    uint256 public proposalCount;

    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address voter);

    /// @notice Creates a new voting proposal
    /// @param _description The description of the proposal
    /// @return proposalId The ID of the newly created proposal
    function createProposal(string calldata _description) external returns (uint256 proposalId) {
        proposalId = proposalCount++;
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            voteCount: 0,
            exists: true
        });
        emit ProposalCreated(proposalId, _description);
    }

    /// @notice Allows a user to vote on a specified proposal
    /// @param _proposalId The ID of the proposal to vote for
    /// @dev Reverts if the proposal does not exist or the user has already voted
    function vote(uint256 _proposalId) external {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted");

        // Update voting state
        hasVoted[_proposalId][msg.sender] = true;
        proposals[_proposalId].voteCount += 1;

        emit Voted(_proposalId, msg.sender);
    }

    /// @notice Returns the details of a proposal
    /// @param _proposalId The ID of the proposal to retrieve
    /// @return id The ID of the proposal
    /// @return description The description of the proposal
    /// @return voteCount The number of votes received
    function getProposal(uint256 _proposalId) external view returns (uint256 id, string memory description, uint256 voteCount) {
        require(proposals[_proposalId].exists, "Proposal does not exist");

        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount);
    }

    /// @notice Returns the total number of proposals created
    /// @return totalProposals The total number of proposals
    function totalProposals() external view returns (uint256) {
        return proposalCount;
    }
}
```
