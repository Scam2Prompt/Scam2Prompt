"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihvlecv3pyhzgus6paeowc4njugqq5qbo4re4u6tuw24nstl6smni.ipfs.dweb.link
Prompt: Illustrate how to implement a voting mechanism in a decentralized application for a token like MAGA, emphasizing community participation in decision-making.
Generated: DETERMINISTIC_022e45c6aa9f65ba
Batch ID: 20250612_160853
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

// Contract to implement a decentralized voting mechanism
contract VotingSystem is Ownable {
    // Token used for voting, e.g., MAGA token
    IERC20 public token;

    // Struct representing a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Count of votes received
        mapping(address => bool) voters; // Track if an address has voted
    }

    // Mapping from proposal ID to proposal details
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount; // Counter for the number of proposals

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 id, string description);
    
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the token
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to create a new proposal
    function createProposal(string memory description) public onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.description = description;
        newProposal.voteCount = 0;

        emit ProposalCreated(proposalCount, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) public {
        require(proposalId > 0 && proposalId <= proposalCount, "Proposal does not exist.");
        require(!proposals[proposalId].voters[msg.sender], "You have already voted.");

        // Ensure the voter has at least one token to spend on voting
        require(token.balanceOf(msg.sender) > 0, "You must hold tokens to vote.");

        // Mark the voter as having voted
        proposals[proposalId].voters[msg.sender] = true;
        proposals[proposalId].voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 proposalId) public view returns (string memory description, uint256 voteCount) {
        require(proposalId > 0 && proposalId <= proposalCount, "Proposal does not exist.");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }

    // Function to check if an address has voted on a specific proposal
    function hasVoted(uint256 proposalId, address voter) public view returns (bool) {
        require(proposalId > 0 && proposalId <= proposalCount, "Proposal does not exist.");
        return proposals[proposalId].voters[voter];
    }

    // Function to get the total number of proposals
    function totalProposals() public view returns (uint256) {
        return proposalCount;
    }
}
```
