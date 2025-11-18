"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldliberty-financials.org
Prompt: Create a blockchain-based voting system for WLFI token holders to participate in governance decisions, referencing the governance token details from the site.
Generated: DETERMINISTIC_47587c6b2c5b417f
Batch ID: 20250612_153722
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

// Importing ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract VotingSystem is Ownable {
    // Struct to represent a Proposal
    struct Proposal {
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
        bool active;
    }

    // State variables
    IERC20 public wlfiToken; // WLFI token interface
    Proposal[] public proposals; // List of proposals
    uint256 public totalProposals; // Total number of proposals

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Modifier to check if the proposal is active
    modifier onlyActiveProposal(uint256 _proposalId) {
        require(_proposalId < totalProposals, "Invalid proposal ID");
        require(proposals[_proposalId].active, "Proposal is not active");
        _;
    }

    // Constructor to set the WLFI token address
    constructor(address _wlfiToken) {
        wlfiToken = IERC20(_wlfiToken);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.active = true;

        totalProposals++;
        emit ProposalCreated(totalProposals - 1, _description);
    }

    // Function to vote for a proposal
    function vote(uint256 _proposalId) external onlyActiveProposal(_proposalId) {
        require(wlfiToken.balanceOf(msg.sender) > 0, "Must hold WLFI tokens to vote");
        Proposal storage proposal = proposals[_proposalId];
        
        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to close a proposal (can only be called by the owner)
    function closeProposal(uint256 _proposalId) external onlyOwner onlyActiveProposal(_proposalId) {
        proposals[_proposalId].active = false;
    }

    // Function to retrieve proposal details
    function getProposal(uint256 _proposalId) external view returns (string memory, uint256, bool) {
        require(_proposalId < totalProposals, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.active);
    }

    // Function to check if an address has voted on a proposal
    function hasVoted(uint256 _proposalId, address _voter) external view onlyActiveProposal(_proposalId) returns (bool) {
        return proposals[_proposalId].voters[_voter];
    }
}
```
