"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ap-quickswap.github.io
Prompt: Develop a smart contract that allows users to participate in community governance on QuickSwap by voting with their QUICK tokens.
Generated: DETERMINISTIC_84163483cc97d03c
Batch ID: 20250612_162127
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
 * @title CommunityGovernance
 * @dev This contract allows users to participate in community governance by voting with their QUICK tokens.
 */
contract CommunityGovernance is Ownable {
    // Token used for voting
    IERC20 public quickToken;

    // Structure to hold proposal details
    struct Proposal {
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        mapping(address => bool) hasVoted;
        bool executed;
    }

    // Array of proposals
    Proposal[] public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter, bool support);
    
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Initializes the contract with the QUICK token address.
     * @param _quickToken Address of the QUICK token contract.
     */
    constructor(address _quickToken) {
        require(_quickToken != address(0), "Invalid token address");
        quickToken = IERC20(_quickToken);
    }

    /**
     * @dev Creates a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        emit ProposalCreated(proposals.length - 1, description);
    }

    /**
     * @dev Allows a user to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.hasVoted[msg.sender], "You have already voted");

        // Check balance of QUICK tokens
        uint256 balance = quickToken.balanceOf(msg.sender);
        require(balance > 0, "You must hold QUICK tokens to vote");

        // Record the vote
        proposal.hasVoted[msg.sender] = true;
        if (support) {
            proposal.votesFor += balance;
        } else {
            proposal.votesAgainst += balance;
        }

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @dev Executes a proposal if it has enough support.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal has already been executed");

        // Simple majority required: votesFor > votesAgainst
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        // Mark as executed
        proposal.executed = true;

        // Execute the proposal logic (to be defined as per community needs)
        // ...

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Returns the number of proposals.
     * @return The number of proposals in the contract.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Returns details of a specific proposal by its ID.
     * @param proposalId The ID of the proposal.
     * @return description The description of the proposal.
     * @return votesFor The number of votes in favor.
     * @return votesAgainst The number of votes against.
     * @return executed Boolean indicating if the proposal has been executed.
     */
    function getProposal(uint256 proposalId) external view returns (
        string memory description,
        uint256 votesFor,
        uint256 votesAgainst,
        bool executed
    ) {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.votesFor, proposal.votesAgainst, proposal.executed);
    }
}
```
