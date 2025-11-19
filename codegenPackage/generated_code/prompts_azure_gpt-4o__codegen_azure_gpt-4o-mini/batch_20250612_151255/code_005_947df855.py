"""
Generated Code Metadata:
========================
Original URL: https://saitachains.pages.dev
Prompt: Develop a decentralized application (dApp) on SaitaChain that utilizes its on-chain governance system to allow token holders to propose and vote on network upgrades.
Generated: DETERMINISTIC_947df85540cab6de
Batch ID: 20250612_151255
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token management and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Governance contract for managing proposals and voting
contract Governance is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes for the proposal
        uint256 endTime;    // Voting end time
        mapping(address => bool) voters; // Track if an address has voted
    }

    // State variables
    ERC20 public token; // Reference to the ERC20 token contract
    Proposal[] public proposals; // Array of proposals
    uint256 public votingDuration; // Duration for voting in seconds

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the token and voting duration
    constructor(ERC20 _token, uint256 _votingDuration) {
        token = _token;
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.endTime = block.timestamp + votingDuration;
        emit ProposalCreated(proposals.length - 1, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        // Ensure the proposal exists
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];

        // Ensure the voting period is active
        require(block.timestamp < proposal.endTime, "Voting has ended");
        // Ensure the voter has not already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Transfer tokens to the contract as a vote
        uint256 voterBalance = token.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold tokens to vote");
        
        // Mark the voter as having voted
        proposal.voters[msg.sender] = true;
        proposal.voteCount += voterBalance; // Increment vote count by the number of tokens held

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }

    // Function to get the total number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
