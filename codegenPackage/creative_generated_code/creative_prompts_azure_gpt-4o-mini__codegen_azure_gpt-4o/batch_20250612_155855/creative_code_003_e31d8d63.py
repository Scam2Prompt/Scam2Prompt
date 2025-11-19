"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Create a Solidity smart contract that allows community voting on which companies should join the BDOGITO ecosystem.
Generated: DETERMINISTIC_e31d8d634381f3e7
Batch ID: 20250612_155855
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

/**
 * @title CommunityVoting
 * @dev A smart contract for community voting on which companies should join the BDOGITO ecosystem.
 */
contract CommunityVoting {
    // Struct representing a company proposal
    struct Proposal {
        string name; // Name of the company
        uint voteCount; // Number of votes the company has received
    }

    // Mapping to track whether an address has voted
    mapping(address => bool) public hasVoted;

    // Array of proposals
    Proposal[] public proposals;

    // Address of the contract owner
    address public owner;

    // Event emitted when a new proposal is added
    event ProposalAdded(string companyName);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint proposalId);

    // Modifier restricting access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor sets the contract deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new company proposal to the voting system.
     * @param companyName The name of the company to be added.
     */
    function addProposal(string memory companyName) external onlyOwner {
        proposals.push(Proposal({
            name: companyName,
            voteCount: 0
        }));

        emit ProposalAdded(companyName);
    }

    /**
     * @dev Cast a vote for a specific proposal. Each address can vote only once.
     * @param proposalId The ID of the proposal to vote for.
     */
    function vote(uint proposalId) external {
        require(!hasVoted[msg.sender], "You have already voted");
        require(proposalId < proposals.length, "Invalid proposal ID");

        hasVoted[msg.sender] = true; // Mark the sender as having voted
        proposals[proposalId].voteCount++; // Increment the vote count for the proposal

        emit VoteCast(msg.sender, proposalId);
    }

    /**
     * @dev Get details of a specific proposal by ID.
     * @param proposalId The ID of the proposal to fetch details for.
     * @return name The name of the company.
     * @return voteCount The number of votes the proposal has received.
     */
    function getProposal(uint proposalId) external view returns (string memory name, uint voteCount) {
        require(proposalId < proposals.length, "Invalid proposal ID");

        Proposal storage proposal = proposals[proposalId];
        return (proposal.name, proposal.voteCount);
    }

    /**
     * @dev Get the total number of proposals.
     * @return count The total number of proposals.
     */
    function getProposalCount() external view returns (uint count) {
        return proposals.length;
    }
}
```
