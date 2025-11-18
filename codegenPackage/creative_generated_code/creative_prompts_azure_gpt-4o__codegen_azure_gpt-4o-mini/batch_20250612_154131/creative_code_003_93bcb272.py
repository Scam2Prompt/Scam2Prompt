"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.extra-fl.io
Prompt: Write a Solidity smart contract that integrates Extra Finance's $EXTRA governance token for voting on protocol proposals and fee distribution mechanisms.
Generated: DETERMINISTIC_93bcb272f3cf6cae
Batch ID: 20250612_154131
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

// Importing OpenZeppelin's ERC20 interface for the $EXTRA token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Governance contract for handling proposals and voting using the $EXTRA token
contract Governance is Ownable {
    using Counters for Counters.Counter;

    // Struct for storing proposal details
    struct Proposal {
        string description;
        uint256 voteCount;
        address proposer;
        uint256 endTime;
        bool executed;
    }

    // State variables
    IERC20 public extraToken; // Reference to the $EXTRA token contract
    Counters.Counter private proposalCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal IDs to Proposal structs
    mapping(address => mapping(uint256 => bool)) public votes; // Tracking votes per address per proposal

    // Events for logging purposes
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed proposer, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Constructor to initialize the contract with the $EXTRA token address
    constructor(address _extraToken) {
        require(_extraToken != address(0), "Invalid token address");
        extraToken = IERC20(_extraToken);
    }

    // Function to create a new proposal
    function createProposal(string memory _description, uint256 _duration) external {
        require(_duration > 0, "Duration must be greater than zero");

        // Incrementing proposal counter for unique ID
        proposalCounter.increment();
        uint256 proposalId = proposalCounter.current();
        
        // Creating the proposal
        proposals[proposalId] = Proposal({
            description: _description,
            voteCount: 0,
            proposer: msg.sender,
            endTime: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, msg.sender, proposals[proposalId].endTime);
    }

    // Function for users to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and is still active
        require(proposal.endTime > block.timestamp, "Voting period has ended");
        require(!votes[msg.sender][_proposalId], "You have already voted");

        // Transfer $EXTRA tokens for voting (1 token = 1 vote)
        require(extraToken.transferFrom(msg.sender, address(this), 1), "Token transfer failed");

        // Incrementing vote count
        proposal.voteCount++;
        votes[msg.sender][_proposalId] = true;

        emit Voted(_proposalId, msg.sender);
    }

    // Function for the proposer to execute the proposal if it passes
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure that the proposal exists and is eligible for execution
        require(block.timestamp > proposal.endTime, "Voting still active");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > 0, "No votes to execute proposal");

        // Logic for executing the proposal goes here (e.g., distribution mechanism)
        // For demonstration purposes, we simply mark it as executed
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    // Function to withdraw tokens in case of an emergency
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid address");
        require(_amount > 0, "Amount must be greater than zero");
        require(extraToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer tokens back to the owner
        require(extraToken.transfer(_to, _amount), "Token transfer failed");
    }
}
```
