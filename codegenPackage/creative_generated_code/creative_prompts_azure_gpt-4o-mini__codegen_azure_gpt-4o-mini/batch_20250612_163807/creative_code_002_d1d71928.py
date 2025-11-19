"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renqpresale.pages.dev
Prompt: Create a Solidity smart contract that interacts with the $RENQ token for governance voting on proposals within the RenQ Finance ecosystem.
Generated: DETERMINISTIC_d1d719289022948c
Batch ID: 20250612_163807
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

// Importing OpenZeppelin contracts for safe math and access control
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract GovernanceVoting is Ownable {
    // Interface for the $RENQ token
    IERC20 public renqToken;

    // Structure for a proposal
    struct Proposal {
        uint id;
        string description;
        uint voteCount;
        mapping(address => bool) hasVoted;
        bool executed;
    }

    // State variables
    uint public proposalCount;
    mapping(uint => Proposal) public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint id, string description);
    // Event emitted when a vote is cast
    event Voted(uint proposalId, address voter);
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint proposalId);

    // Constructor to set the $RENQ token address
    constructor(address _renqToken) {
        require(_renqToken != address(0), "Invalid RENQ token address");
        renqToken = IERC20(_renqToken);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote on a proposal
    function vote(uint _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!proposal.hasVoted[msg.sender], "You have already voted");
        require(renqToken.balanceOf(msg.sender) > 0, "You must hold RENQ tokens to vote");

        // Mark the voter as having voted
        proposal.hasVoted[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal
    function executeProposal(uint _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!proposal.executed, "Proposal has already been executed");

        // Perform execution logic here (e.g. transfer tokens, change settings, etc.)
        // ...

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    // Function to retrieve the details of a proposal
    function getProposal(uint _proposalId) external view returns (uint, string memory, uint, bool) {
        Proposal storage proposal = proposals[_proposalId];

        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");

        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
