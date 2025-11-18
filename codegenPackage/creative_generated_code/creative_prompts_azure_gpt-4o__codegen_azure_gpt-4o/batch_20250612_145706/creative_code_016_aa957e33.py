"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write a Solidity contract for a community-governed meme token like $FROP, allowing token holders to vote on project decisions.
Generated: DETERMINISTIC_aa957e339bf4a545
Batch ID: 20250612_145706
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

/// @title Community-Governed Meme Token: $FROP
/// @dev This contract implements an ERC20 token with governance functionality allowing token holders to vote on proposals.

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeGovernanceToken is ERC20, Ownable {
    // A struct to represent a governance proposal
    struct Proposal {
        string description; // Proposal description
        uint256 yesVotes;   // Number of "yes" votes for the proposal
        uint256 noVotes;    // Number of "no" votes for the proposal
        uint256 deadline;   // Proposal voting deadline
        bool executed;      // Whether this proposal has been executed
        mapping(address => bool) voters; // Tracks addresses that have voted on this proposal
    }

    // Array of all proposals
    Proposal[] public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 proposalId, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId, bool successful);

    /// @dev Constructor to initialize the token with a name and symbol
    /// @param name Name of the token
    /// @param symbol Symbol of the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    /// @dev Create a new proposal
    /// @param description The description of the proposal
    /// @param votingDuration Duration in seconds for which voting will be open
    function createProposal(string memory description, uint256 votingDuration) external onlyOwner {
        require(bytes(description).length > 0, "Proposal description cannot be empty");
        require(votingDuration > 0, "Voting duration must be greater than zero");

        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.deadline = block.timestamp + votingDuration;

        emit ProposalCreated(proposals.length - 1, description, newProposal.deadline);
    }

    /// @dev Cast a vote on a proposal
    /// @param proposalId The ID of the proposal to vote on
    /// @param support Boolean indicating whether to vote "yes" (true) or "no" (false)
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!proposal.voters[msg.sender], "You have already voted on this proposal");
        require(balanceOf(msg.sender) > 0, "Only token holders can vote");

        // Record the vote
        proposal.voters[msg.sender] = true;
        if (support) {
            proposal.yesVotes += balanceOf(msg.sender);
        } else {
            proposal.noVotes += balanceOf(msg.sender);
        }

        emit VoteCast(msg.sender, proposalId, support);
    }

    /// @dev Execute a proposal after the voting period has ended
    /// @param proposalId The ID of the proposal to execute
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;
        bool successful = (proposal.yesVotes > proposal.noVotes);

        emit ProposalExecuted(proposalId, successful);
    }

    /// @dev Get the details of a proposal
    /// @param proposalId The ID of the proposal to retrieve
    /// @return description The description of the proposal
    /// @return yesVotes The number of "yes" votes
    /// @return noVotes The number of "no" votes
    /// @return deadline The voting deadline
    /// @return executed Whether the proposal has been executed
    function getProposal(uint256 proposalId)
        external
        view
        returns (
            string memory description,
            uint256 yesVotes,
            uint256 noVotes,
            uint256 deadline,
            bool executed
        )
    {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.description,
            proposal.yesVotes,
            proposal.noVotes,
            proposal.deadline,
            proposal.executed
        );
    }
}
```
