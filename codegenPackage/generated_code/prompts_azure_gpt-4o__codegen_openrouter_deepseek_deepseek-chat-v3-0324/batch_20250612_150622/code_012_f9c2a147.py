"""
Generated Code Metadata:
========================
Original URL: https://to-ousd.pages.dev
Prompt: Generate code to interact with the OGV governance module, allowing users to vote on fund allocation across OUSD strategies.
Generated: DETERMINISTIC_f9c2a1471661eb8c
Batch ID: 20250612_150622
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IOGV {
    function balanceOf(address account) external view returns (uint256);
    function getVotes(address account) external view returns (uint256);
}

contract OGVGovernance is Ownable {
    using SafeMath for uint256;

    // OGV token contract
    IOGV public ogvToken;

    // Voting period in blocks
    uint256 public votingPeriod;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        address[] strategies;
        uint256[] allocations;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Array of all proposals
    Proposal[] public proposals;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        string description,
        address[] strategies,
        uint256[] allocations,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _ogvToken, uint256 _votingPeriod) {
        require(_ogvToken != address(0), "Invalid OGV token address");
        require(_votingPeriod > 0, "Voting period must be > 0");
        
        ogvToken = IOGV(_ogvToken);
        votingPeriod = _votingPeriod;
    }

    /**
     * @dev Create a new proposal for fund allocation across strategies
     * @param description Description of the proposal
     * @param strategies Array of strategy addresses
     * @param allocations Corresponding allocation percentages (sum must be 100)
     */
    function createProposal(
        string memory description,
        address[] memory strategies,
        uint256[] memory allocations
    ) external onlyOwner {
        require(strategies.length == allocations.length, "Arrays length mismatch");
        require(strategies.length > 0, "No strategies provided");
        
        uint256 totalAllocation = 0;
        for (uint256 i = 0; i < allocations.length; i++) {
            totalAllocation = totalAllocation.add(allocations[i]);
        }
        require(totalAllocation == 100, "Total allocation must be 100%");

        uint256 startBlock = block.number;
        uint256 endBlock = startBlock.add(votingPeriod);

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposals.length - 1;
        newProposal.description = description;
        newProposal.strategies = strategies;
        newProposal.allocations = allocations;
        newProposal.startBlock = startBlock;
        newProposal.endBlock = endBlock;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            newProposal.id,
            description,
            strategies,
            allocations,
            startBlock,
            endBlock
        );
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support Whether to support the proposal (true = for, false = against)
     */
    function castVote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        require(block.number >= proposal.startBlock, "Voting not started");
        require(block.number <= proposal.endBlock, "Voting period ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 votes = ogvToken.getVotes(msg.sender);
        require(votes > 0, "No voting power");

        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(votes);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(votes);
        }

        emit VoteCast(msg.sender, proposalId, support, votes);
    }

    /**
     * @dev Execute a proposal if it has passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        require(block.number > proposal.endBlock, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal did not pass");

        // Here you would implement the actual fund allocation logic
        // This is a placeholder for the actual implementation
        // which would interact with the OUSD strategy contracts
        
        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get proposal details
     * @param proposalId ID of the proposal
     * @return id, description, strategies, allocations, startBlock, endBlock, forVotes, againstVotes, executed
     */
    function getProposal(uint256 proposalId) external view returns (
        uint256 id,
        string memory description,
        address[] memory strategies,
        uint256[] memory allocations,
        uint256 startBlock,
        uint256 endBlock,
        uint256 forVotes,
        uint256 againstVotes,
        bool executed
    ) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        return (
            proposal.id,
            proposal.description,
            proposal.strategies,
            proposal.allocations,
            proposal.startBlock,
            proposal.endBlock,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }

    /**
     * @dev Check if an address has voted on a proposal
     * @param proposalId ID of the proposal
     * @param voter Address to check
     * @return True if the address has voted
     */
    function hasVoted(uint256 proposalId, address voter) external view returns (bool) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        return proposals[proposalId].hasVoted[voter];
    }

    /**
     * @dev Update voting period (only owner)
     * @param newVotingPeriod New voting period in blocks
     */
    function setVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        require(newVotingPeriod > 0, "Voting period must be > 0");
        votingPeriod = newVotingPeriod;
    }
}
```
