"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-news.com
Prompt: Provide a code example for managing Ethereum governance tokens, including minting and voting functionalities, as anticipated in Ethereum governance token evolution.
Generated: DETERMINISTIC_bc83d6e211d37855
Batch ID: 20250612_154306
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

// Importing the OpenZeppelin ERC20 token standard and Ownable contract for access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// GovernanceToken contract which inherits from ERC20 and Ownable
contract GovernanceToken is ERC20, Ownable {
    // Mapping of proposals and their respective votes
    struct Proposal {
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
    }

    // Array to hold all proposals
    Proposal[] public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address voter);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    // Function to mint new tokens, callable only by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        _mint(to, amount);
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.voteCount = 0;

        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to vote for a proposal
    function vote(uint256 proposalId) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];

        // Ensure the voter has not already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount += 1;

        emit Voted(proposalId, msg.sender);
    }

    // Function to get the total number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    // Function to get details of a specific proposal
    function getProposal(uint256 proposalId) external view returns (string memory, uint256) {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }

    // Function to withdraw tokens (if applicable)
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= balanceOf(address(this)), "Insufficient balance");
        _transfer(address(this), to, amount);
    }
}
```
