"""
Generated Code Metadata:
========================
Original URL: https://skytradefinance.com
Prompt: Create a Solidity-based governance contract for the SHE Protocol, allowing $SHE token holders to vote on ecosystem development proposals.
Generated: DETERMINISTIC_f7de83701afc1066
Batch ID: 20250612_152249
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

// Governance contract for the SHE Protocol
contract SHEGovernance is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
        bool executed;
    }

    // State variables
    IERC20 public sheToken; // The SHE token contract
    Proposal[] public proposals; // Array of proposals
    uint256 public proposalCount; // Counter for proposals

    // Events
    event ProposalCreated(uint256 id, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check if the caller has voted on a proposal
    modifier hasNotVoted(uint256 proposalId) {
        require(!proposals[proposalId].voters[msg.sender], "You have already voted.");
        _;
    }

    // Constructor to initialize the contract with the SHE token address
    constructor(address _sheToken) {
        sheToken = IERC20(_sheToken);
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.executed = false;

        emit ProposalCreated(newProposal.id, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external hasNotVoted(proposalId) {
        // Ensure the proposal exists
        require(proposalId < proposalCount, "Proposal does not exist.");

        // Check if the voter has enough SHE tokens to vote (1 token = 1 vote)
        require(sheToken.balanceOf(msg.sender) > 0, "You must hold SHE tokens to vote.");

        // Record the vote
        proposals[proposalId].voters[msg.sender] = true;
        proposals[proposalId].voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    // Function to execute a proposal (only callable by the owner)
    function executeProposal(uint256 proposalId) external onlyOwner {
        // Ensure the proposal exists and has not been executed
        require(proposalId < proposalCount, "Proposal does not exist.");
        require(!proposals[proposalId].executed, "Proposal has already been executed.");

        // Logic to execute the proposal can be added here
        // For example, transferring funds or changing parameters

        proposals[proposalId].executed = true;

        emit ProposalExecuted(proposalId);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 proposalId) external view returns (uint256, string memory, uint256, bool) {
        require(proposalId < proposalCount, "Proposal does not exist.");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
