"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bzreards.top
Prompt: Generate code for a decentralized voting system to allow community contributions to anime lore, inspired by Azuki's community-driven model.
Generated: DETERMINISTIC_c310bbc0d5bbb6d1
Batch ID: 20250612_155024
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

// Importing OpenZeppelin's ERC721 implementation for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract represents a decentralized voting system for community contributions to anime lore
contract AnimeLoreVoting is ERC721, Ownable {
    // Structure to hold information about each lore contribution
    struct LoreContribution {
        string description; // Description of the contribution
        address contributor; // Address of the contributor
        uint256 voteCount;  // Number of votes the contribution has received
        bool exists;        // Flag to check if the contribution exists
    }

    // Mapping from contribution ID to its details
    mapping(uint256 => LoreContribution) public contributions;
    // Mapping to track votes for each contribution by voter address
    mapping(address => mapping(uint256 => bool)) public votes;
    
    // Counter for unique contribution IDs
    uint256 public contributionIdCounter;

    // Event emitted when a new contribution is made
    event ContributionAdded(uint256 id, string description, address contributor);

    // Event emitted when a vote is cast
    event VoteCasted(uint256 contributionId, address voter);

    // Constructor to initialize the contract
    constructor() ERC721("AnimeLoreNFT", "ALNFT") {}

    // Function to add a new lore contribution
    function addContribution(string calldata _description) external onlyOwner {
        contributionIdCounter++;
        contributions[contributionIdCounter] = LoreContribution({
            description: _description,
            contributor: msg.sender,
            voteCount: 0,
            exists: true
        });
        
        emit ContributionAdded(contributionIdCounter, _description, msg.sender);
    }

    // Function for users to vote on a contribution
    function vote(uint256 _contributionId) external {
        require(contributions[_contributionId].exists, "Contribution does not exist.");
        require(!votes[msg.sender][_contributionId], "You have already voted for this contribution.");

        // Record the vote and increment the vote count
        votes[msg.sender][_contributionId] = true;
        contributions[_contributionId].voteCount++;

        emit VoteCasted(_contributionId, msg.sender);
    }

    // Function to retrieve details of a specific contribution
    function getContribution(uint256 _contributionId) external view returns (LoreContribution memory) {
        require(contributions[_contributionId].exists, "Contribution does not exist.");
        return contributions[_contributionId];
    }

    // Function to mint an NFT for a contribution which can be used as a reward for top contributors
    function mintContributionNFT(uint256 _contributionId) external onlyOwner {
        require(contributions[_contributionId].exists, "Contribution does not exist.");
        
        // Minting NFT as a reward for the contribution
        _mint(contributions[_contributionId].contributor, _contributionId);
    }

    // Function to get the total contributions made
    function totalContributions() external view returns (uint256) {
        return contributionIdCounter;
    }
}
```
