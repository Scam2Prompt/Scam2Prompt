"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Create a Solidity smart contract for decentralized governance of the HEHE ecosystem, allowing $HEHE token holders to vote on proposals.
Generated: DETERMINISTIC_db3da271317d9777
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title HEHE Governance Contract
/// @notice This contract allows $HEHE token holders to propose and vote on governance proposals.
contract HEHEGovernance is Ownable {
    // Structure to hold details of each proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voters;
    }

    // Token interface for $HEHE token
    IERC20 public hehetoken;

    // Mapping of proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 id, string description);

    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Constructor to set the HEHE token address
    constructor(IERC20 _hehetoken) {
        hehetoken = _hehetoken;
    }

    /// @notice Creates a new proposal
    /// @param description The description of the proposal
    function createProposal(string memory description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, description);
    }

    /// @notice Allows $HEHE token holders to vote on a proposal
    /// @param proposalId The ID of the proposal to vote on
    function vote(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        // Ensure proposal exists
        require(proposal.id == proposalId, "Proposal does not exist");
        // Ensure the voter has not already voted
        require(!proposal.voters[msg.sender], "Already voted");

        // Ensure the voter holds $HEHE tokens
        uint256 voterBalance = hehetoken.balanceOf(msg.sender);
        require(voterBalance > 0, "Must hold $HEHE tokens to vote");

        // Vote for the proposal
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /// @notice Executes a proposal if it has majority votes
    /// @param proposalId The ID of the proposal to execute
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];

        // Ensure proposal exists
        require(proposal.id == proposalId, "Proposal does not exist");
        // Ensure proposal is not already executed
        require(!proposal.executed, "Proposal already executed");

        // Check if the proposal has enough votes (simple majority)
        uint256 totalVotes = hehetoken.totalSupply();
        require(proposal.voteCount > totalVotes / 2, "Not enough votes to execute");

        // Execute the proposal logic here (to be defined)
        // ...

        // Mark proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }
}
```
