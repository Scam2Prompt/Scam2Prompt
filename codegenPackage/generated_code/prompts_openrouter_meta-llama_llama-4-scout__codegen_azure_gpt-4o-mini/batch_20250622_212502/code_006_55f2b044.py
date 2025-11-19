"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Describe how Polkadot's governance model enables token holders to participate in decision-making, and propose a code implementation for on-chain governance.
Generated: DETERMINISTIC_55f2b044ec60b27d
Batch ID: 20250622_212502
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the governance token
interface IGovernanceToken is IERC20 {
    function delegate(address delegatee) external;
}

// Struct to represent a proposal
struct Proposal {
    uint256 id;
    string description;
    uint256 voteCount;
    mapping(address => bool) voters;
    bool executed;
}

// On-chain governance contract
contract Governance is Ownable {
    // Governance token used for voting
    IGovernanceToken public governanceToken;

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Constructor to set the governance token
    constructor(address _governanceToken) {
        governanceToken = IGovernanceToken(_governanceToken);
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
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists
        require(proposal.id != 0, "Proposal does not exist");
        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount += governanceToken.balanceOf(msg.sender);

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal (only owner can execute)
    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and has not been executed
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");

        // Logic to execute the proposal (to be defined based on proposal type)
        // For example, changing a contract state or transferring funds

        proposal.executed = true;
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256, bool) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
