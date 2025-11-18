"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: Write a script in Solidity to implement decentralized governance for NFT cities in the EarthMeta metaverse, allowing token holders to vote on city-related decisions.
Generated: DETERMINISTIC_3ae72db9ebee8e34
Batch ID: 20250612_152658
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Governance contract for decentralized NFT city management
contract NFTCityGovernance is Ownable {
    using Counters for Counters.Counter;

    // Structure to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTimestamp;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // State variables
    IERC721 public cityNFT;                                // Reference to the NFT contract
    Counters.Counter private proposalIdCounter;            // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals;         // Mapping of proposals
    uint256 public votingDuration;                          // Duration for voting in seconds

    // Events
    event ProposalCreated(uint256 indexed id, string description, uint256 endTimestamp);
    event Voted(uint256 indexed proposalId, address voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    // Constructor to initialize the contract with NFT address and voting duration
    constructor(IERC721 _cityNFT, uint256 _votingDuration) {
        cityNFT = _cityNFT;
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string calldata _description) external onlyOwner {
        proposalIdCounter.increment();
        uint256 proposalId = proposalIdCounter.current();
        
        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.description = _description;
        newProposal.endTimestamp = block.timestamp + votingDuration;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, _description, newProposal.endTimestamp);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external {
        // Check that the proposal exists and is still active
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp < proposal.endTimestamp, "Voting has ended");
        
        // Ensure the sender holds an NFT to vote
        require(cityNFT.balanceOf(msg.sender) > 0, "Must own an NFT to vote");
        require(!proposal.hasVoted[msg.sender], "You have already voted");

        // Register the vote
        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }
        proposal.hasVoted[msg.sender] = true;

        emit Voted(proposalId, msg.sender, support);
    }

    // Function to execute the proposal if voting has finished
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.endTimestamp, "Voting is still ongoing");
        require(!proposal.executed, "Proposal has already been executed");

        // Simple decision logic: if votes for are greater than votes against, execute
        if (proposal.votesFor > proposal.votesAgainst) {
            // Execute the decision (custom logic can be added here)
        }
        
        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    // Function to update voting duration (only callable by the owner)
    function updateVotingDuration(uint256 newDuration) external onlyOwner {
        votingDuration = newDuration;
    }
}
```
