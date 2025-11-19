"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Create a Solidity smart contract that allows users to vote on governance proposals within the Zushi ecosystem.
Generated: DETERMINISTIC_dd58598547177d8e
Batch ID: 20250612_160853
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

/// @title Zushi Governance Voting Contract
/// @dev This contract allows users to create proposals and vote on them within the Zushi ecosystem.
contract ZushiGovernance {
    // Struct representing a governance proposal
    struct Proposal {
        uint256 id;                  // Unique identifier for the proposal
        string description;          // Proposal description
        uint256 voteCountFor;        // Votes in favor
        uint256 voteCountAgainst;    // Votes against
        address proposer;            // Address of the proposal creator
        bool executed;               // Has the proposal been executed?
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;
    
    // Mapping to track whether a user has voted for a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for generating unique proposal IDs
    uint256 public proposalCount;

    // Events to log activities
    event ProposalCreated(uint256 id, string description, address proposer);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId);

    /// @dev Modifier to ensure the proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    /// @dev Modifier to ensure the proposal has not been executed
    modifier notExecuted(uint256 proposalId) {
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    /// @dev Creates a new governance proposal
    /// @param _description The description of the proposal
    function createProposal(string calldata _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCountFor: 0,
            voteCountAgainst: 0,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    /// @dev Votes on a proposal
    /// @param _proposalId The ID of the proposal
    /// @param _support If true, votes in favor; if false, votes against
    function vote(uint256 _proposalId, bool _support) external proposalExists(_proposalId) notExecuted(_proposalId) {
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal");

        if (_support) {
            proposals[_proposalId].voteCountFor++;
        } else {
            proposals[_proposalId].voteCountAgainst++;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit Voted(_proposalId, msg.sender, _support);
    }

    /// @dev Executes a proposal (only callable by the proposer)
    /// @param _proposalId The ID of the proposal to execute
    /// @notice Execution logic is left for future implementation (e.g., updating governance rules)
    function executeProposal(uint256 _proposalId) external proposalExists(_proposalId) notExecuted(_proposalId) {
        require(msg.sender == proposals[_proposalId].proposer, "Only proposer can execute");
        require(proposals[_proposalId].voteCountFor > proposals[_proposalId].voteCountAgainst, "Proposal failed");

        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);

        // Proposal execution logic goes here
    }
}
```
