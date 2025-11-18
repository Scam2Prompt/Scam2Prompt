"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quecko.com
Prompt: Write a Solidity-based DAO smart contract that aligns with Quecko's Web3 development expertise and includes governance mechanisms.
Generated: DETERMINISTIC_579a2a2e8da10530
Batch ID: 20250612_154029
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

/// @title A Decentralized Autonomous Organization (DAO) Smart Contract
/// @author Your Name
/// @notice This contract allows users to create proposals and vote on them
/// @dev This is a simplified DAO implementation using ERC20 tokens for voting power

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DAO is Ownable {
    struct Proposal {
        uint id;
        string description;
        uint voteCount;
        mapping(address => bool) voters;
        bool active;
    }

    IERC20 public votingToken; // ERC20 token used for voting
    uint public proposalCount; // Track number of proposals
    mapping(uint => Proposal) public proposals; // Store proposals by their ID

    event ProposalCreated(uint indexed proposalId, string description);
    event Voted(uint indexed proposalId, address indexed voter);
    event ProposalExecuted(uint indexed proposalId);

    /// @param _votingToken The address of the ERC20 token for voting
    constructor(IERC20 _votingToken) {
        votingToken = _votingToken;
    }

    /// @notice Create a new proposal
    /// @param _description The description of the proposal
    /// @dev Only the contract owner can create a proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.active = true;

        emit ProposalCreated(proposalCount, _description);
    }

    /// @notice Vote on a proposal
    /// @param _proposalId The ID of the proposal to vote on
    /// @dev Users must hold tokens to vote and can only vote once
    function vote(uint _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.active, "Proposal is not active");
        require(!proposal.voters[msg.sender], "You have already voted");

        uint256 voterBalance = votingToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold tokens to vote");

        proposal.voters[msg.sender] = true;
        proposal.voteCount += voterBalance;

        emit Voted(_proposalId, msg.sender);
    }

    /// @notice Execute a proposal if it has more than 50% of the total votes
    /// @param _proposalId The ID of the proposal to execute
    /// @dev Only the contract owner can execute a proposal
    function executeProposal(uint _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.active, "Proposal is not active");
        require(proposal.voteCount > (votingToken.totalSupply() / 2), "Not enough votes");

        proposal.active = false;
        // Logic to execute the proposal goes here

        emit ProposalExecuted(_proposalId);
    }

    /// @notice Get information about a proposal
    /// @param _proposalId The ID of the proposal to retrieve
    /// @return id The ID of the proposal
    /// @return description The description of the proposal
    /// @return voteCount The number of votes the proposal has received
    /// @return active Whether the proposal is still active
    function getProposal(uint _proposalId) external view returns (uint id, string memory description, uint voteCount, bool active) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.active);
    }
}
```
