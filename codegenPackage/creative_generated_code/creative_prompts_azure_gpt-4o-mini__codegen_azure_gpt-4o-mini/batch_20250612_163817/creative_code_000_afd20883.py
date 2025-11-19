"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-m1q953hrk-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora framework mentioned on the Optimism Agora site?
Generated: DETERMINISTIC_afd20883576d77b6
Batch ID: 20250612_163817
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

// Importing the necessary libraries from the Agora framework
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A contract that implements on-chain governance using the Agora framework
contract OnChainGovernance is Ownable {
    // Event emitted when a proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter, bool support);

    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 votesFor; // Total votes in favor
        uint256 votesAgainst; // Total votes against
        uint256 deadline; // Deadline for voting
        mapping(address => bool) hasVoted; // Track if an address has voted
        bool executed; // Flag to check if the proposal has been executed
    }

    IERC20 public governanceToken; // Governance token for voting
    Proposal[] public proposals; // Array of proposals

    // Constructor to initialize the governance token
    constructor(address _governanceToken) {
        governanceToken = IERC20(_governanceToken);
    }

    // Function to create a new proposal
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        // Create a new proposal
        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.deadline = block.timestamp + duration;

        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];

        // Check if the proposal exists and is still open for voting
        require(proposal.deadline > block.timestamp, "Voting has ended");
        require(!proposal.hasVoted[msg.sender], "You have already voted");

        // Record the vote
        proposal.hasVoted[msg.sender] = true;

        // Count the votes based on the voter's governance token balance
        uint256 voterBalance = governanceToken.balanceOf(msg.sender);
        if (support) {
            proposal.votesFor += voterBalance;
        } else {
            proposal.votesAgainst += voterBalance;
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    // Function to execute the proposal if it has enough votes
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];

        // Ensure the proposal is eligible for execution
        require(proposal.deadline < block.timestamp, "Voting is still open");
        require(!proposal.executed, "Proposal has already been executed");
        
        // Check if the proposal has enough votes to pass
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        // Execute proposal logic here (e.g., change state, transfer funds, etc.)

        proposal.executed = true;
        // Logic for execution can go here

        // You may also want to emit another event for execution
    }

    // Function to get the current proposal count
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    // Function to get proposal details
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 votesFor, uint256 votesAgainst, uint256 deadline, bool executed) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.votesFor, proposal.votesAgainst, proposal.deadline, proposal.executed);
    }
}
```
