"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quickswap-exchange.github.io
Prompt: Write a Solidity smart contract to enable governance voting using QUICK tokens, allowing holders to participate in QuickSwap's decision-making process.
Generated: DETERMINISTIC_0263349e556a0967
Batch ID: 20250612_154250
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title GovernanceVoting
 * @dev A simple governance voting contract using QUICK tokens for decision-making
 */
contract GovernanceVoting is Ownable {
    // Instance of the QUICK token
    IERC20 public quickToken;

    // Structure to hold proposal details
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
        bool executed;
    }

    // Mapping from proposal ID to Proposal details
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Events to emit on proposal creation and voting
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter);

    /**
     * @param _quickToken Address of the QUICK token contract
     */
    constructor(address _quickToken) {
        require(_quickToken != address(0), "Invalid QUICK token address");
        quickToken = IERC20(_quickToken);
    }

    /**
     * @dev Creates a new proposal for voting
     * @param description A description of the proposal
     */
    function createProposal(string memory description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @dev Allows QUICK token holders to vote on a proposal
     * @param proposalId The ID of the proposal to vote on
     */
    function vote(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        require(proposal.id > 0, "Proposal does not exist");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Check if the voter has enough QUICK tokens to vote (1 token = 1 vote)
        uint256 balance = quickToken.balanceOf(msg.sender);
        require(balance > 0, "You must hold QUICK tokens to vote");

        // Mark the voter as having voted
        proposal.voters[msg.sender] = true;
        proposal.voteCount += balance; // Increment vote count by the voter's balance

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Executes the proposal if certain criteria are met (to be defined)
     * @param proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];

        require(proposal.id > 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");

        // Execute the proposal logic here (to be defined)
        // For demonstration, we simply mark it as executed
        proposal.executed = true;
    }

    /**
     * @dev Fetches the details of a proposal
     * @param proposalId The ID of the proposal
     * @return id The ID of the proposal
     * @return description The description of the proposal
     * @return voteCount The current vote count of the proposal
     * @return executed The execution status of the proposal
     */
    function getProposalDetails(uint256 proposalId) external view returns (uint256 id, string memory description, uint256 voteCount, bool executed) {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id > 0, "Proposal does not exist");

        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
