"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Generate a Solidity implementation for decentralized governance that allows Bulldogito Coin holders to propose and vote on asset management strategies using their voting power.
Generated: DETERMINISTIC_19815f3a3d0e94e1
Batch ID: 20250612_154239
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The Governance contract for Bulldogito Coin holders
contract BulldogitoGovernance is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        uint256 endTime;    // End time for voting
        mapping(address => bool) voted; // Tracks if an address has voted
    }

    // State variables
    IERC20 public bulldogitoCoin; // Reference to the Bulldogito Coin contract
    Proposal[] public proposals;    // List of proposals
    uint256 public votingDuration;  // Duration for voting in seconds

    // Events to notify about proposal creation and voting
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Modifiers
    modifier onlyDuringVoting(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].endTime, "Voting has ended");
        _;
    }

    modifier onlyAfterVoting(uint256 proposalId) {
        require(block.timestamp >= proposals[proposalId].endTime, "Voting is still ongoing");
        _;
    }

    // Constructor to initialize the contract with the ERC20 token address and voting duration
    constructor(address _bulldogitoCoin, uint256 _votingDuration) {
        bulldogitoCoin = IERC20(_bulldogitoCoin);
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.endTime = block.timestamp + votingDuration;
        
        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external onlyDuringVoting(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        
        // Check if the voter has already voted
        require(!proposal.voted[msg.sender], "You have already voted");

        // Check if the voter has sufficient Bulldogs to vote
        uint256 voterBalance = bulldogitoCoin.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold Bulldogito Coin to vote");

        // Record the vote
        proposal.voted[msg.sender] = true;
        proposal.voteCount += voterBalance;

        emit Voted(proposalId, msg.sender);
    }

    // Function to retrieve the results of a proposal after voting has ended
    function getProposalResults(uint256 proposalId) external view onlyAfterVoting(proposalId) returns (string memory description, uint256 voteCount) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }
    
    // Function to retrieve the proposal count
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
