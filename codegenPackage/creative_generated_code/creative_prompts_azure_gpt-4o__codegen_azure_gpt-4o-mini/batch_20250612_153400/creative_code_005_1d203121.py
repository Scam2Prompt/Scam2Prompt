"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-inqubeta-ai.pages.dev
Prompt: Create a governance voting smart contract for QUBE token holders to propose, discuss, and vote on platform decisions, as described in the governance section of InQubeta.
Generated: DETERMINISTIC_1d203121811b046b
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract GovernanceVoting is Ownable {
    using Counters for Counters.Counter;

    // Data structure to hold details of a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 creationTime;
        address proposer;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    IERC20 public token; // QUBE token
    Counters.Counter private proposalCounter;
    mapping(uint256 => Proposal) public proposals;
    
    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed proposer);
    event VoteCast(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to check if the caller has enough tokens to propose
    modifier onlyTokenHolders() {
        require(token.balanceOf(msg.sender) > 0, "Must hold tokens to propose or vote");
        _;
    }

    // Constructor to initialize the contract with token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyTokenHolders {
        proposalCounter.increment();
        uint256 proposalId = proposalCounter.current();
        
        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.description = _description;
        newProposal.creationTime = block.timestamp;
        newProposal.proposer = msg.sender;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, _description, msg.sender);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external onlyTokenHolders {
        Proposal storage proposal = proposals[_proposalId];
        
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.voters[msg.sender], "Already voted on this proposal");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit VoteCast(_proposalId, msg.sender);
    }

    // Function to execute a proposal if conditions are met
    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");
        
        // You can add conditions based on voteCount or time here
        if (proposal.voteCount > 0) { // Example condition
            // Execute the proposal logic here (custom implementation needed)
            proposal.executed = true;
            emit ProposalExecuted(_proposalId);
        }
    }

    // Function to retrieve proposal details
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256, address, bool) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.proposer, proposal.executed);
    }
}
```
