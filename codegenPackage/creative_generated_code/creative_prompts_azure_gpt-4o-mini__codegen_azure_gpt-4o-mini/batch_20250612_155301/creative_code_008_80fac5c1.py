"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Describe how to build a decentralized autonomous organization (DAO) on Ethereum and provide a sample code structure.
Generated: DETERMINISTIC_80fac5c158e3fc82
Batch ID: 20250612_155301
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

// Importing OpenZeppelin's ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// DAO contract inherits ERC20 and Ownable
contract DAO is ERC20, Ownable {
    using SafeMath for uint256;

    // Struct to hold proposal information
    struct Proposal {
        string description; // Description of the proposal
        uint256 votesFor; // Votes in favor
        uint256 votesAgainst; // Votes against
        uint256 endTime; // Time until voting ends
        bool executed; // Whether proposal has been executed
        mapping(address => bool) hasVoted; // Tracks if an address has voted
    }

    // Array to store proposals
    Proposal[] public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 endTime);

    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter, bool inFavor);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Constructor to set token name and symbol, and mint initial supply to contract owner
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _mint(msg.sender, 10000 * 10 ** decimals()); // Mint initial tokens
    }

    // Function to create a new proposal
    function createProposal(string calldata description, uint256 duration) external onlyOwner {
        uint256 endTime = block.timestamp + duration;
        Proposal storage newProposal = proposals.push();
        
        newProposal.description = description;
        newProposal.endTime = endTime;

        emit ProposalCreated(proposals.length - 1, description, endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool inFavor) external {
        Proposal storage proposal = proposals[proposalId];

        // Check if proposal exists and is still active
        require(proposal.endTime > block.timestamp, "Voting has ended");
        require(!proposal.hasVoted[msg.sender], "You have already voted");

        // Record the user's vote
        proposal.hasVoted[msg.sender] = true;

        if (inFavor) {
            proposal.votesFor = proposal.votesFor.add(1);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(1);
        }

        emit Voted(proposalId, msg.sender, inFavor);
    }

    // Function to execute a proposal if it has passed
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        // Check if proposal exists, is active, and has not been executed
        require(proposal.endTime < block.timestamp, "Voting still ongoing");
        require(!proposal.executed, "Proposal already executed");

        // Check if proposal passed
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        // Execute the proposal logic here (custom logic can be added based on the proposal)

        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }
}
```
