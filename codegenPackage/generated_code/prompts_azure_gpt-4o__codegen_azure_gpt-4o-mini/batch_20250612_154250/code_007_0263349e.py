"""
Generated Code Metadata:
========================
Original URL: https://quickswap-exchange.github.io
Prompt: Write a Solidity smart contract to enable governance voting using QUICK tokens, allowing holders to participate in QuickSwap's decision-making process.
Generated: DETERMINISTIC_0263349e556a0967
Batch ID: 20250612_154250
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// GovernanceVoting contract allows QUICK token holders to participate in governance voting
contract GovernanceVoting is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        mapping(address => bool) voters; // Track if an address has voted
        bool executed; // Track if the proposal has been executed
    }

    // State variables
    IERC20 public quickToken; // Reference to the QUICK token contract
    Proposal[] public proposals; // Array of proposals
    uint256 public votingEndTime; // End time for the current voting session

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check if voting is active
    modifier votingActive() {
        require(block.timestamp < votingEndTime, "Voting has ended");
        _;
    }

    // Modifier to check if voting has ended
    modifier votingEnded() {
        require(block.timestamp >= votingEndTime, "Voting is still active");
        _;
    }

    // Constructor to initialize the contract with the QUICK token address
    constructor(address _quickToken) {
        quickToken = IERC20(_quickToken);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposals.length - 1, _description);
    }

    // Function to start a voting session
    function startVoting(uint256 duration) external onlyOwner {
        votingEndTime = block.timestamp + duration;
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external votingActive {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Check if the voter has enough QUICK tokens to vote (1 token = 1 vote)
        require(quickToken.balanceOf(msg.sender) > 0, "You must hold QUICK tokens to vote");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount += quickToken.balanceOf(msg.sender);

        emit Voted(proposalId, msg.sender);
    }

    // Function to execute a proposal after voting has ended
    function executeProposal(uint256 proposalId) external votingEnded {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal has already been executed");

        // Logic to execute the proposal can be added here
        // For example, transferring funds, changing state, etc.

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    // Function to get the number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    // Function to get details of a specific proposal
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount, bool executed) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
