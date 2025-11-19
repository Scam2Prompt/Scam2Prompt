"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agix-reward.net
Prompt: Describe how to implement governance and voting mechanisms for AGIX token holders within a decentralized application.
Generated: DETERMINISTIC_71e88d7e08989a79
Batch ID: 20250612_160720
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

/**
 * @title Governance Contract for AGIX Token Holders
 * @dev This contract implements a simple governance and voting mechanism for AGIX token holders.
 */
contract Governance is Ownable {
    IERC20 public agixToken; // Reference to the AGIX token contract

    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        uint256 createdAt;  // Timestamp of proposal creation
        address proposer;    // Address of the proposal creator
        mapping(address => bool) hasVoted; // Track who has voted
    }

    Proposal[] public proposals; // Array to store proposals
    uint256 public votingDuration; // Duration of voting in seconds

    event ProposalCreated(uint256 proposalId, string description, address proposer);
    event Voted(uint256 proposalId, address voter);

    /**
     * @dev Constructor to set the AGIX token address and voting duration.
     * @param _agixToken Address of the AGIX token contract.
     * @param _votingDuration Duration of voting in seconds.
     */
    constructor(address _agixToken, uint256 _votingDuration) {
        agixToken = IERC20(_agixToken);
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        proposals.push();
        uint256 proposalId = proposals.length - 1;
        Proposal storage newProposal = proposals[proposalId];
        
        newProposal.description = _description;
        newProposal.proposer = msg.sender;
        newProposal.createdAt = block.timestamp;

        emit ProposalCreated(proposalId, _description, msg.sender);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Proposal does not exist");
        require(!proposals[_proposalId].hasVoted[msg.sender], "Already voted");
        require(block.timestamp < proposals[_proposalId].createdAt + votingDuration, "Voting period has ended");

        // Check if the voter has enough AGIX tokens
        uint256 voterBalance = agixToken.balanceOf(msg.sender);
        require(voterBalance > 0, "Insufficient AGIX balance to vote");

        proposals[_proposalId].voteCount += voterBalance; // Count votes based on token balance
        proposals[_proposalId].hasVoted[msg.sender] = true; // Mark the voter

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Get the details of a proposal.
     * @param _proposalId ID of the proposal.
     * @return description Description of the proposal.
     * @return voteCount Total votes received.
     * @return createdAt Timestamp of proposal creation.
     * @return proposer Address of the proposal creator.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 createdAt, address proposer) {
        require(_proposalId < proposals.length, "Proposal does not exist");

        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.createdAt, proposal.proposer);
    }

    /**
     * @dev Change the voting duration.
     * @param _votingDuration New voting duration in seconds.
     */
    function setVotingDuration(uint256 _votingDuration) external onlyOwner {
        votingDuration = _votingDuration;
    }
}
```

In this code, we have implemented a simple governance mechanism for AGIX token holders, with functionalities for creating proposals and voting on them. Each proposal can be voted on as long as the voting duration is valid, and votes are counted based on the voter's AGIX balance.
