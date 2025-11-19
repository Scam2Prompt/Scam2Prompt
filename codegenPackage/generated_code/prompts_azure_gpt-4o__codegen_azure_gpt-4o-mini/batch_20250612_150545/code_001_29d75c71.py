"""
Generated Code Metadata:
========================
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: Create a smart contract that supports proposal creation within a DAO, inspired by the features showcased on the MetaDAO demo page.
Generated: DETERMINISTIC_29d75c711e3dbfa9
Batch ID: 20250612_150545
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

// @title DAO Proposal Smart Contract
// @notice This contract allows members of a DAO to create and vote on proposals.
contract DAOsProposal is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        address proposer;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voters;
    }

    // Events for logging proposal creation and voting
    event ProposalCreated(uint256 id, string description, address proposer);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // State variables
    Counters.Counter private proposalIdCounter;
    mapping(uint256 => Proposal) public proposals;

    // @notice Create a new proposal
    // @param _description The description of the proposal
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();

        Proposal storage newProposal = proposals[newProposalId];
        newProposal.id = newProposalId;
        newProposal.description = _description;
        newProposal.proposer = msg.sender;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(newProposalId, _description, msg.sender);
    }

    // @notice Vote on a proposal
    // @param _proposalId The ID of the proposal to vote on
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.voters[msg.sender], "You have already voted on this proposal");

        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // @notice Execute a proposal if it has enough votes
    // @param _proposalId The ID of the proposal to execute
    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.voteCount > 0, "Proposal has no votes");

        proposal.executed = true;

        // Logic to execute the proposal goes here
        // For example, transferring funds, changing state, etc.

        emit ProposalExecuted(_proposalId);
    }

    // @notice Get the details of a proposal
    // @param _proposalId The ID of the proposal
    // @return id The ID of the proposal
    // @return description The description of the proposal
    // @return proposer The address of the proposer
    // @return voteCount The number of votes the proposal has received
    // @return executed Whether the proposal has been executed
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        string memory description,
        address proposer,
        uint256 voteCount,
        bool executed
    ) {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id != 0, "Proposal does not exist");

        return (
            proposal.id,
            proposal.description,
            proposal.proposer,
            proposal.voteCount,
            proposal.executed
        );
    }
}
```
