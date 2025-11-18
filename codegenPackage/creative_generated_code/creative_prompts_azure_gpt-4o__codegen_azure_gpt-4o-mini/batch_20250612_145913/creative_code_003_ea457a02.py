"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Create a governance voting system in Solidity for a DeFi platform, inspired by Tenderize's TEND token governance model.
Generated: DETERMINISTIC_ea457a0229dd19f6
Batch ID: 20250612_145913
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

// Importing OpenZeppelin's ERC20 contract for token functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

// Governance Token Contract
contract GovernanceToken is ERC20, ERC20Burnable, Ownable {
    // Using Counters for vote tracking
    using Counters for Counters.Counter;
    Counters.Counter private _proposalIdCounter;

    // Proposal struct to hold proposal information
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTime;
        mapping(address => bool) hasVoted;
        bool executed;
    }

    // Mapping of proposal ID to Proposal details
    mapping(uint256 => Proposal) public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description, uint256 endTime);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter, bool support);
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 id);

    // Modifier to check if the proposal is active
    modifier onlyActiveProposal(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].endTime, "Proposal has ended");
        _;
    }

    // Modifier to check if the proposal is already executed
    modifier onlyExecutableProposal(uint256 proposalId) {
        require(block.timestamp >= proposals[proposalId].endTime, "Proposal still active");
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    // Constructor to initialize the token
    constructor() ERC20("GovernanceToken", "GOV") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to contract deployer
    }

    // Function to create a new proposal
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        uint256 proposalId = _proposalIdCounter.current();
        _proposalIdCounter.increment();

        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.description = description;
        newProposal.endTime = block.timestamp + duration;

        emit ProposalCreated(proposalId, description, newProposal.endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external onlyActiveProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Ensure that the voter has not already voted
        require(!proposal.hasVoted[msg.sender], "You have already voted on this proposal");
        
        // Record the vote
        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.votesFor += balanceOf(msg.sender);
        } else {
            proposal.votesAgainst += balanceOf(msg.sender);
        }

        emit Voted(proposalId, msg.sender, support);
    }

    // Function to execute a proposal if passed
    function executeProposal(uint256 proposalId) external onlyExecutableProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        
        // Determine if the proposal is passed
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");
        
        // Execute proposal logic here (e.g., changing state variables, transferring tokens, etc.)
        proposal.executed = true;
        
        emit ProposalExecuted(proposalId);
    }

    // Function to get proposal details
    function getProposal(uint256 proposalId) external view returns (Proposal memory) {
        return proposals[proposalId];
    }
}
```
