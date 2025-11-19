"""
Generated Code Metadata:
========================
Original URL: https://tesneiro-5281.vercel.app
Prompt: Create a Solidity contract that replicates the community-ownership model of Neiro, ensuring all decisions are made via decentralized governance voting.
Generated: DETERMINISTIC_665b943e07530f2c
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title CommunityOwnership
 * @dev A contract that implements a community ownership model with decentralized governance voting.
 */
contract CommunityOwnership is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
        bool executed;
    }

    // State variables
    Counters.Counter private proposalIdCounter;
    mapping(uint256 => Proposal) public proposals;
    uint256 public totalProposals;
    IERC20 public governanceToken;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to check if the caller has already voted
    modifier hasNotVoted(uint256 proposalId) {
        require(!proposals[proposalId].voters[msg.sender], "You have already voted.");
        _;
    }

    // Constructor to initialize the governance token
    constructor(IERC20 _governanceToken) {
        governanceToken = _governanceToken;
    }

    /**
     * @dev Create a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();

        Proposal storage newProposal = proposals[newProposalId];
        newProposal.id = newProposalId;
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        totalProposals++;

        emit ProposalCreated(newProposalId, description);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external hasNotVoted(proposalId {
        require(proposalId > 0 && proposalId <= totalProposals, "Invalid proposal ID.");

        // Ensure the voter holds governance tokens
        require(governanceToken.balanceOf(msg.sender) > 0, "You must hold governance tokens to vote.");

        // Record the vote
        proposals[proposalId].voters[msg.sender] = true;
        proposals[proposalId].voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if it has enough votes.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId > 0 && proposalId <= totalProposals, "Invalid proposal ID.");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal has already been executed.");
        require(proposal.voteCount > (totalProposals / 2), "Not enough votes to execute proposal.");

        // Execute the proposal logic here (to be defined based on the proposal's purpose)
        // ...

        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get the details of a proposal.
     * @param proposalId The ID of the proposal.
     * @return The details of the proposal.
     */
    function getProposal(uint256 proposalId) external view returns (uint256, string memory, uint256, bool) {
        require(proposalId > 0 && proposalId <= totalProposals, "Invalid proposal ID.");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
