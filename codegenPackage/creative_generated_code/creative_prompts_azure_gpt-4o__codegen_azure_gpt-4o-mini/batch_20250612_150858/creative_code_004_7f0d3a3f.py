"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy-io.github.io
Prompt: Create a governance smart contract in Solidity that allows ORB token holders to vote on proposals within the Zealy platform.
Generated: DETERMINISTIC_7f0d3a3fde25acb2
Batch ID: 20250612_150858
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

// Interface for the ERC20 token (ORB token)
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Governance contract for proposals voting
contract Governance {
    // Structure to represent a proposal
    struct Proposal {
        string description;        // Description of the proposal
        uint256 voteCount;        // Total votes for the proposal
        mapping(address => bool) voters; // Track if an address has voted
        bool executed;            // Indicates if the proposal has been executed
    }

    // State variables
    IERC20 public orbToken;                // Address of the ORB token contract
    Proposal[] public proposals;            // List of proposals
    address public admin;                   // Admin of the contract

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier validProposal(uint256 proposalId) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        _;
    }

    // Constructor to set the ORB token and admin
    constructor(address _orbToken) {
        orbToken = IERC20(_orbToken);
        admin = msg.sender; // Set the contract deployer as admin
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyAdmin {
        proposals.push(Proposal({
            description: description,
            voteCount: 0,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        
        // Ensure the voter has not voted yet
        require(!proposal.voters[msg.sender], "You have already voted");

        // Check if the voter has enough ORB tokens to vote
        require(orbToken.balanceOf(msg.sender) > 0, "You must hold ORB tokens to vote");

        // Mark the voter as having voted and increase the vote count
        proposal.voters[msg.sender] = true;
        proposal.voteCount += 1;

        emit Voted(proposalId, msg.sender);
    }

    // Function to execute a proposal if enough votes are accumulated
    function executeProposal(uint256 proposalId) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Ensure the proposal has not been executed and has enough votes
        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.voteCount > 0, "No votes cast for this proposal");

        // Execute the proposal logic here (for demo purposes, we just mark it as executed)
        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }

    // Function to get proposal details
    function getProposal(uint256 proposalId) external view validProposal(proposalId) returns (string memory description, uint256 voteCount, bool executed) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
